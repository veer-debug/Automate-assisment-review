from backend.api.chatgpt_api import HomeworkGrader
from database.DataBase import Connect_DB
from backend.api.mail import send_feedback, extract_marks_and_feedback
from backend.directory.getinput import GetInputs
from backend.directory.run_test_cases import dynamic_import_and_test
import sys, json, os

def main():
    # ------------- Config files------------------------------ #
    config_path = os.path.join('Keys', 'autograder_config.json')
    with open(config_path) as file:
         config = json.load(file)
         if config is None:
           sys.exit("AutoGrader Not Configured")
         from_email_address = config['email']
         password = config['password']
         smtp_address = config['smtp']
         
    # Assignment Directory
    assignment_directory = os.path.join('Input', sys.argv[1])

    config_path = os.path.join(assignment_directory, 'config.json')
    with open(config_path) as file:
        config = json.load(file)
        if config is None:
           sys.exit("No Config File For Assignment Directory")
        assignment_topic = config['assignment_topic']
        total_score = int(config['total_score'])
        subject_name = config['subject_name']
        batch_number = int(config['batch_number'])
            
    #----------------------- Taking Input --------------------------- #
    inputs = GetInputs(assignment_directory, solution=True)
    
    #------------- Connect with database ---------------------- #
    db_path = os.path.join('database', 'data.db')
    db = Connect_DB(db_path)

    # Get Assignment ID for storing scores
    assignment_id = db.get_assignment_id(assignment_topic=assignment_topic, subject_name=subject_name, batch_number=batch_number)

    #------------------ Grading --------------------------------- #
    with open('Keys/key.txt') as file:
        token = file.readline().strip()
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o-mini"
    output_tokens = 500
    
    # Initialize Grader
    autograder = HomeworkGrader(token, endpoint, model_name, output_tokens)
    # Dict for storing grades
    grades_by_intern_id = {}
    feedback_by_email = {}
    per_score = 0
    for question_id in inputs.questions:
             # question_score = inputs.questions[question_id]['full_score']
             question_score = 10
             per_score += question_score
             question = inputs.questions[question_id]
             # for each question, select corresponding solution by interns
             for intern_id in inputs.solutions:
                 feedback = f'\nFEEDBACK FOR QUESTION:\n{question}\n'

                 try:
                    test_score, not_passed = dynamic_import_and_test(solution_file=question_id, intern_id=intern_id, assignment=sys.argv[1], test_case_folder='Test Cases')
                    
                    answer = inputs.solutions[intern_id][question_id]

                    if not_passed:
                        for tc in not_passed:
                            answer += '\n'
                            answer += tc
                    
                    feedback += f"ANSWER:\n\n{answer}"

                    response = autograder.grade_answer(question, answer, question_score)

                    result = extract_marks_and_feedback(response)

                    grades = result[0]
                    feedback += result[1]

                    grades_by_intern_id[intern_id] = grades_by_intern_id.get(intern_id, 0) + int(grades)

                    intern_email = db.get_intern_email(intern_id)
                    feedback_by_email[intern_email] = feedback_by_email.get(intern_email, '') + '\n- - - - - - - - - - - - - - - - - -\n\n' + feedback
                 
                 except Exception as e:
                     
                     print('FOR INTERN: ' + intern_id, 'QUESTION_ID: ' + question_id)
                     print(e)

    #--------------------- Storing Grades in Database ------------------ #
    # Normalizing Grades
    factor = total_score/per_score
    for intern_id in grades_by_intern_id:
        grades_by_intern_id[intern_id] *= factor
        grades_by_intern_id[intern_id] = (grades_by_intern_id[intern_id] + test_score)/2
    
    for intern_id in grades_by_intern_id:
        score = grades_by_intern_id[intern_id]
        db.insert_into_grades(score, intern_id=intern_id, assignment_id=assignment_id)
    db.close_connection()


    #---------------------- Send Feedback ------------------------------ #
    subject = f'Assessment Feedback For Assignment {assignment_topic}.'

    for email in feedback_by_email:
        feedback = feedback_by_email[email]
        send_feedback(smtp_address=smtp_address, to_email=email, subject=subject, feedback_message=feedback, from_email=from_email_address, from_password=password)


if __name__ == "__main__":
    main()