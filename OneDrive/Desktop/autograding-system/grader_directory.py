import os


class DirectoryGrader:
    def __init__(self, grader):
        self.grader = grader

    def grade_assignments_in_directory(self, directory_path, from_email, from_password):
        # Validate the directory path before proceeding
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist.")
            return

        for intern_dir in os.listdir(directory_path):
            intern_path = os.path.join(directory_path, intern_dir)

            if os.path.isdir(intern_path):  # Check if it is a directory
                print(f"Processing assignments for {intern_dir}")

                # Loop through each assignment in the intern's directory
                for assignment_file in os.listdir(intern_path):
                    # checking if it's a python file
                    if assignment_file.endswith(".py"):
                        # Filtering assignment files
                        assignment_path = os.path.join(intern_path, assignment_file)

                        # Read the assignment content
                        with open(assignment_path, "r") as f:
                            answer = f.read()

                        # Grade the assignment
                        grading_response = self.grader.grade_answer(answer)
                        marks, feedback = self.grader.extract_marks_and_feedback(
                            grading_response
                        )

                        # Prepare feedback message
                        feedback_message = f"""
                        Hello {intern_dir},

                        Here is your feedback for {assignment_file}:

                        Score: {marks}/100
                        {feedback}

                        Best regards,
                        Autograding System
                        """

                        # Sending feedback to the intern
                        intern_email = (
                            f"{intern_dir}@example.com"  # Placeholder for intern email
                        )
                        self.grader.send_feedback(
                            intern_email,
                            f"Feedback for {assignment_file}",
                            feedback_message,
                            from_email,
                            from_password,
                        )

                        # Print confirmation
                        print(
                            f"Graded and sent feedback for {assignment_file} of {intern_dir}"
                        )

class GetInputs:
    def __init__(self, dir):
        '''
        dir = assignment_directory with a subdirectory questions, internid, internid2, intern3.. 
        -----------------------------------------------------------------------------------------
        self.questions
        - Initializes questions dictionary that stores questions from text files in questions subdirectory
        self.solutions
        - Initializes a dict to store intern and solutions
        - append format :- {intern_id: {solution_id: 'answer_in_string'} }
        '''
        self.dir = dir
        if not os.path.exists(dir):
            print(f"Directory {dir} does not exist.")
            return
        self.questions = dict()
        self.get_questions()
        self.solutions = dict()
        self.populate_solutions()

    
    def get_questions(self):
        dir = os.path.join(self.dir, 'Questions')
        ...

    def populate_solutions(self):
        ...