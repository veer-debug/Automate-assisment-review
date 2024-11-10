from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.api.get_test_case import ASK_GPT4
from backend.directory.make_test_files import Make_Files
from backend.directory.getinput import GetInputs
from DATABASE.DataBase import Connect_DB
import pathlib
import sys
import json, os

def generate_description(test_case_maker, question, subject):
    return test_case_maker.get_test_cases(question, subject)

def write_description(description, dir, file_name):
    Make_Files.make_question(description=description, directory=dir, file_name=file_name)

def make_assignment(dir, secret_key, endpoint, model_name):
    test_case_maker = ASK_GPT4(secret_key, endpoint=endpoint, model_name=model_name)
    get_questions = GetInputs(dir=dir, solution=False)
    subject = 'Python'
    
    with ThreadPoolExecutor() as executor:
        future_to_filename = {executor.submit(generate_description, test_case_maker, question, subject): file_name
                              for file_name, question in get_questions.questions.items()}
        
        for future in as_completed(future_to_filename):
            file_name = future_to_filename[future]
            try:
                description = future.result()
                write_description(description, dir, file_name)
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(sys.argv)
        sys.exit("Input Assignment_Folder as Argument")
    elif len(sys.argv) > 2:
        new_folder_name = '_'.join(sys.argv[1:])
        sys.argv[1] = new_folder_name

    dir = pathlib.Path('Input', sys.argv[1])

    with open("Keys/tester_config.json") as file:
        config = json.load(file)
        endpoint = config["endpoint"]
        model_name = config["model_name"]

    with open('Keys/key.txt') as file:
        key = file.readline().strip()
        
    make_assignment(dir, key, endpoint, model_name)

    db_path = os.path.join('database', 'data.db')
    db = Connect_DB(db_path)

    # Insert the new assignment in the Database
    with open(f'Input/{sys.argv[1]}/config.json') as file:
        config = json.load(file)
        batch_number = config['batch_number']
        subject_name = config['subject_name']
        assignment_topic = config['assignment_topic']
        total_score = config['total_score']

    subject_id = db.get_subject_id(subject_name, batch_number)
    db.insert_into_assignments(subject_id, assignment_topic, total_score)
    db.close_connection()