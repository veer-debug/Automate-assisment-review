import os


class GetInputs:
    def __init__(self, dir):
        """
        dir = assignment_directory with a subdirectory questions, internid, internid2, intern3..
        -----------------------------------------------------------------------------------------
        self.questions
        - Initializes questions dictionary that stores questions from text files in questions subdirectory
        self.solutions
        - Initializes a dict to store intern and solutions
        - append format :- {intern_id: {solution_id: 'answer_in_string'} }
        """
        self.dir = dir
        if not os.path.exists(dir):
            print(f"Directory {dir} does not exist.")
            return
        self.questions = dict()
        self.get_questions()
        self.solutions = dict()
        self.populate_dict()

    def get_questions(self):
        """
        Reads the questions from the 'Questions' subdirectory and stores them in self.questions.
        """
        questions_dir = os.path.join(self.dir, "Questions")
        if not os.path.exists(questions_dir):
            print(f"Questions directory {questions_dir} does not exist.")
            return
        for filename in os.listdir(questions_dir):
            if filename.endswith(".txt"):
                question_id = filename.split(".")[0]
                with open(os.path.join(questions_dir, filename), "r") as file:
                    self.questions[question_id] = file.read().strip()

    def populate_dict(self):
        """
        Populates self.solutions with intern IDs as keys and their corresponding answers as values.
        """
        for intern_id in os.listdir(self.dir):
            intern_dir = os.path.join(self.dir, intern_id)
            if os.path.isdir(intern_dir) and intern_id.lower() != "questions":
                self.solutions[intern_id] = {}
                # Loop through each solution file in the intern's directory
                for filename in os.listdir(intern_dir):
                    if filename.endswith(".py"):
                        solution_id = filename.split(".")[0]
                        with open(os.path.join(intern_dir, filename), "r") as file:
                            self.solutions[intern_id][solution_id] = file.read().strip()
