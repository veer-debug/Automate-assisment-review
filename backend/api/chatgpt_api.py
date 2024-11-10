from openai import OpenAI
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='api_usage.log', level=logging.INFO)

class HomeworkGrader:
    def __init__(self, token, endpoint, model_name, output_limit):
        self.client = OpenAI(
            base_url=endpoint,
            api_key=token,
        )
        self.model_name = model_name
        self.output_words = output_limit  

    def grade_answer(self, question, answer, full_score):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in Python algorithms and data structures. Your task is to evaluate student answers and provide a score along with detailed feedback. Always start with 'Score: X/{full_score}'. If the answer is irrelevant, give a score of 0/{full_score}.",
                },
                {
                    "role": "user",
                    "content": f"""""Evaluate the following assignment for total score{full_score}:

    Question: {question}
    Answer: {answer}

Scoring Criteria:

    Correctness (40%): Is the solution logically correct and does it solve the problem?
    Efficiency (30%): Is the solution optimized in terms of time and space complexity?
    Code Quality (20%): Is the code well-organized, readable, and properly commented?
    Creativity (10%): Does the solution demonstrate innovative thinking or unique approaches?

Feedback Guidelines:

    Provide a breakdown of the score based on the criteria.
    Highlight strengths and suggest specific improvements.
    Use bullet points for clarity.

Example Output:

Score: 8.5/{full_score}({full_score} total score)

Feedback:

    Well done on solving the problem correctly.
    Consider optimizing the loop to reduce time complexity.
    Add comments to improve code readability.

Best regards, Sabudh Foundation""",
                }
            ],
            model=self.model_name,
            temperature=1.,
            max_tokens=self.output_words,
            top_p=1.
        )
        logging.info(f"API request made.")

        return response.choices[0].message.content

# Example usage:
# grader = HomeworkGrader(token, endpoint, model_name, assignment)
# feedback = grader.grade_answer(answer)
# print(feedback)

if __name__ == '__main__':
    import json
    with open('Keys/key.txt') as file:
        token = file.readline().strip()
    with open('Keys/autograder_config.json') as file:
        config = json.load(file)
        endpoint = config['endpoint']
        model_name = config['model_name']
    q = 'You are given a list of number. Make a function for finding unique elements'
    grader = HomeworkGrader(token, endpoint, model_name, 200)
    grade = grader.grade_answer(question=q,answer= 'def unique(arr):\n\treturn set(arr)',full_score=100)
    print(grade)
