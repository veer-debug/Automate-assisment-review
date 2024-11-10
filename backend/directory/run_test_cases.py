import importlib, sys

def dynamic_import_and_test(solution_file, intern_id, assignment, test_case_folder):
    # Construct module paths
    solution_module_name = f"Input.{assignment}.{intern_id}.{solution_file}"
    test_case_module_name = f"Input.{assignment}.{test_case_folder}.{solution_file}"
   
    try:
        # Dynamically import solution and test_case modules
        solution_module = importlib.import_module(solution_module_name)
        test_case_module = importlib.import_module(test_case_module_name)
       
        # Get the solution function and test_solution function
        solution_function = getattr(solution_module, 'solution', None)
        test_solution = getattr(test_case_module, 'test_solution', None)
        
        if not callable(solution_function):
            raise AttributeError(f"'solution' function not found in {solution_module_name}")
        if not callable(test_solution):
            raise AttributeError(f"'test_solution' function not found in {test_case_module_name}")
        
        # Run the tests
        passed, not_passed = test_solution(solution_function)
       
        if len(passed) + len(not_passed) == 0:
            raise ValueError("No test cases were run")
        
        score = len(passed) / (len(passed) + len(not_passed)) * 100
        
    except ModuleNotFoundError as e:
        print(f"Error: Module not found - {e}", file=sys.stderr)
        return 0, []
    except AttributeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 0, []
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 0, []
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 0, []
   
    return score, not_passed

    
if __name__ == '__main__':
    dynamic_import_and_test(1, 1, 'AssignmentID', 'Test Cases')