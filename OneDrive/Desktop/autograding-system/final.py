import re
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI


class HomeworkGrader:
    def __init__(self, token, endpoint, model_name, assignment):
        self.client = OpenAI(
            base_url=endpoint,
            api_key=token,
        )
        self.model_name = model_name
        self.assignment = assignment

    def grade_answer(self, answer):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a master at python algorithms and data structures.",
                },
                {
                    "role": "user",
                    "content": f"Here is My Homework for assignment {self.assignment}. Answer: {answer}. Please Grade it from 1 to 100 and provide short but valuable feedback while telling when and where marks are deducted in a section called Feedback.",
                },
            ],
            model=self.model_name,
            temperature=1.0,
            max_tokens=1000,
            top_p=1.0,
        )
        return response.choices[0].message.content

    def extract_marks_and_feedback(self, grading_response):
        # Regular expression to extract marks
        marks_pattern = r"(\d+)\s*/\s*100"
        marks = re.search(marks_pattern, grading_response)
        marks = marks.group(1) if marks else "Marks not found"

        # Regular expression to extract feedback
        feedback_pattern = r"Feedback:\s*(.*)"
        feedback = re.search(feedback_pattern, grading_response, re.DOTALL)
        feedback = feedback.group(1).strip() if feedback else "Feedback not found"

        return marks, feedback

    def send_feedback(
        self, to_email, subject, feedback_message, from_email, from_password
    ):
        try:
            # Creating the email headers and message
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject

            # Attaching the feedback message as the email body
            msg.attach(MIMEText(feedback_message, "plain"))

            # Setting up the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Logging into the sender's email account
            server.login(from_email, from_password)

            # Sending the email
            server.send_message(msg)
            server.quit()
            print(f"Feedback sent successfully to {to_email}.")

        except Exception as e:
            print(f"Error sending email to {to_email}: {str(e)}")

    # Function to grade assignments from intern directories
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
                if assignment_file.endswith(".py"):
                    # Filtering assignment files
                    assignment_path = os.path.join(intern_path, assignment_file)

                    # Read the assignment content
                    with open(assignment_path, "r") as f:
                        answer = f.read()

                    # Grade the assignment
                    grading_response = self.grade_answer(answer)
                    marks, feedback = self.extract_marks_and_feedback(grading_response)

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
                    self.send_feedback(
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


# Example usage
if __name__ == "__main__":
    # Reading the API token
    with open("git_hub_key.txt") as file:
        token = file.readline().strip()

    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o-mini"
    assignment = (
        "You are given a list of numbers. Make a function for finding unique elements"
    )

    grader = HomeworkGrader(token, endpoint, model_name, assignment)

    # Email details
    student_email = "student@gmail.com"  # Replace with actual student email
    from_email = "ritwickamajumder2021@uem.edu.in"  # Replace with your email
    from_password = "xxxxxx"  # Replace with your email password

    # Define the directory path where intern directories are located
    directory_path = "/path/to/interns_directory"  # Replace with actual path

    # Grade assignments for all interns
    grader.grade_assignments_in_directory(directory_path, from_email, from_password)
