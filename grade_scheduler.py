import sys
import json
import datetime
import heapq
import pathlib
import os
import logging

# Configure logging
logging.basicConfig(
    filename='grader_scheduler.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GradeScheduler:
    """
    Schedules Requests for Grading Assignments as per request limits and requests left for API
    """
    def __init__(self, file_path=pathlib.Path('Keys', 'grading_schedules.json')):
        logging.info('Loading grading request queue from json')
        with open(file_path) as file:
            self.data = json.load(file)
        self.priority_queue = []
        self.make_priority_queue()

        with open(pathlib.Path('Keys', 'autograder_config.json')) as file:
            config = json.load(file)
            if config['last_used'] != str(datetime.datetime.now().date()):
                config['requests_left'] = config['requests_limit']
                config['last_used'] = str(datetime.datetime.now().date())
                with open(pathlib.Path('Keys', 'autograder_config.json'), 'w') as config_file:
                    json.dump(config, config_file, indent=4)
        self.requests_left = config['requests_left']
        
        self.start()

    def make_priority_queue(self):
        for assignment_folder, students in self.data.items():
            for student_email, question_numbers in students.items():
                heapq.heappush(self.priority_queue, (int(question_numbers), assignment_folder, student_email))
        logging.debug(f"Priority queue created with {len(self.priority_queue)} items.")

    def start(self):
        done = []  # tuples ("Assignment_Folder", "Student_email")
        while self.priority_queue:
            req = self.pop_min_request()
            if req[0] > self.requests_left:
                self.add_to_queue(assignment_folder=req[1], student_email=req[2])
                logging.warning(f"Grading stopped due to insufficient requests left: {self.requests_left}.")
                break
            else:
                self.requests_left -= int(req[0])
                logging.info(f"Grading {req[1]} for {req[2]} with {req[0]} requests.")
                os.system(f'python grade_once.py {req[1]} {req[2]}')
                done.append((req[1], req[2]))
        self.stop(done)

    def add_to_queue(self, student_email, assignment_folder):
        question_numbers = self.how_many_requests_for(assignment_folder)
        if assignment_folder in self.data:
            if student_email in self.data[assignment_folder]:
                logging.debug(f"Resuming grading for {assignment_folder} {student_email}.")
                self.start()
            else:
                self.data[assignment_folder][student_email] = question_numbers
                heapq.heappush(self.priority_queue, (question_numbers, assignment_folder, student_email))
                logging.debug(f"Added to queue: {assignment_folder} {student_email}.")
                self.start()
        else:
            self.data[assignment_folder] = {student_email: question_numbers}
            heapq.heappush(self.priority_queue, (question_numbers, assignment_folder, student_email))
            logging.debug(f"New Assignment task added to queue: {assignment_folder} {student_email}.")
            self.start()

    def stop(self, done):
        logging.debug('Stopping Grader!!')
        for assignment_folder, student_email in done:
            del self.data[assignment_folder][student_email]
        with open(pathlib.Path('Keys','grading_schedules.json'), "w") as file:
            json.dump(self.data, file, indent=4)
        with open(pathlib.Path('Keys', 'autograder_config.json')) as file:
            config = json.load(file)
            config['requests_left'] = self.requests_left
            with open(pathlib.Path('Keys', 'autograder_config.json'), "w") as file:
                json.dump(config, file, indent=4)
        logging.info(f"Grading stopped! Assignments remaining in queue: {len(self.priority_queue)}.")

    def pop_min_request(self):
        if self.priority_queue:
            return heapq.heappop(self.priority_queue)
        else:
            logging.error("Attempted to pop from an empty priority queue.")
            return None

    @staticmethod
    def how_many_requests_for(folder):
        with open(pathlib.Path('Input', folder, 'config.json')) as file:
            requests = int(json.load(file)['n'])
            logging.debug(f"Requests needed for {folder}: {requests}")
            return requests

if __name__ == '__main__':

    scheduler = GradeScheduler()
    if len(sys.argv) == 3:
        scheduler.add_to_queue(assignment_folder=sys.argv[1], student_email=sys.argv[2])