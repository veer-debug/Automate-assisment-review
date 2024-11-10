import pathlib
import re


class Make_Files:
    @classmethod
    def make_question(cls, description, directory, file_name):
        """
        Makes txt files with given 'file_name' and description' messages and store it in 'directory'
        """
        destination = pathlib.Path(directory, 'Questions', f'{file_name}.txt')
        test_cases, constrains = cls.extract_test_case(description)
        with open(destination, 'w') as file:
            file.writelines('------------------------DESCRIPTION----------------\n')
            file.writelines(constrains)
        cls.make_test_file(test_cases, directory, file_name=file_name)
    
    @classmethod
    def extract_test_case(cls, description):
        # Pattern to extract test cases
        test_case_pattern = r'--Test Cases Start--\s*.*\s*(def.*?)\s*`{0,3}\s*--Test Cases End--'
        # Extract test cases
        test_cases_match = re.search(test_case_pattern, description, re.DOTALL)
        test_cases = test_cases_match.group(1).strip() if test_cases_match else "Test Cases not found"

        # Extract everything else (constraints)
        constrains = re.sub(test_case_pattern, '', description, flags=re.DOTALL).strip()
        return test_cases, constrains

    @classmethod
    def make_test_file(cls, test_cases, directory, file_name):
        # Ensure the "Test Cases" directory exists
        test_cases_dir = pathlib.Path(directory, 'Test Cases')
        test_cases_dir.mkdir(parents=True, exist_ok=True)

        destination = test_cases_dir / f'{file_name}.py'
        with open(destination, 'w') as file:
            file.writelines(test_cases)        

