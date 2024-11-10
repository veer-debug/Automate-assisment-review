import os
import pathlib
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class GetInputs:
    def __init__(self, dir, solution=False):
        self.dir = dir
        if not os.path.exists(dir):
            logging.error(f"Directory {dir} does not exist.")
            return
        self.questions = dict()
        logging.info("Initializing questions dictionary.")
        self.get_questions()
        
        if solution:
            self.solutions = dict()
            logging.info("Initializing solutions dictionary.")
            self.populate_dict()

    def get_questions(self):
        questions_dir = os.path.join(self.dir, "Questions")
        if not os.path.exists(questions_dir):
            logging.error(f"Questions directory {questions_dir} does not exist.")
            return
        for filename in os.listdir(questions_dir):
            if filename.endswith(".txt"):
                question_id = filename.split(".")[0]
                try:
                    with open(os.path.join(questions_dir, filename), "r") as file:
                        self.questions[question_id] = file.read().strip()
                        logging.debug(f"Loaded question {question_id}.")
                except Exception as e:
                    logging.error(f"Error reading file {filename}: {e}")

    def populate_dict(self):
        for intern_id in os.listdir(self.dir):
            if intern_id == 'Test Cases':
                continue
            if intern_id.lower() != "questions":
                self.solutions[intern_id] = GetInputs.for_student(self.dir, intern_id)
                logging.debug(f"Loaded solutions for intern {intern_id}.")
    
    @staticmethod
    def for_student(dir, student_folder):
        sol_path = pathlib.Path(dir, str(student_folder))
        solutions = {}
        logging.info('Started Getting Solutions')
        if os.path.isdir(sol_path):
            for filename in os.listdir(sol_path):
                if filename.endswith(".py"):
                    solution_id = filename.split(".")[0]
                    try:
                        with open(pathlib.Path(sol_path, filename), "r") as file:
                            solutions[solution_id] = file.read().strip()
                            logging.debug(f"Loaded solution {solution_id} from {student_folder}.")
                    except Exception as e:
                        logging.error(f"Error reading file {filename} in {student_folder}: {e}")
        return solutions


if __name__ == '__main__':
    inputs = GetInputs('Input/AssignmentID', solution=True)
    
    logging.info("Questions loaded:")
    logging.info(inputs.questions)
    
    logging.info("Solutions loaded:")
    logging.info(inputs.solutions)