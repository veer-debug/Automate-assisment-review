def test_solution(solution):
    passed = []
    not_passed = []

    # Test case 1: Basic case with duplicates
    test_case_input = [1, 2, 2, 3, 4, 4, 5]
    expected_answer = [1, 2, 3, 4, 5]
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input " + str(test_case_input) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with input " + str(test_case_input) + " result " + str(expected_answer))

    # Test case 2: All unique elements
    test_case_input = [1, 2, 3, 4, 5]
    expected_answer = [1, 2, 3, 4, 5]
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input " + str(test_case_input) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with input " + str(test_case_input) + " result " + str(expected_answer))

    # Test case 3: Empty array
    test_case_input = []
    expected_answer = []
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input " + str(test_case_input) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with input " + str(test_case_input) + " result " + str(expected_answer))

    # Test case 4: All elements are the same
    test_case_input = [7, 7, 7, 7]
    expected_answer = [7]
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input " + str(test_case_input) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with input " + str(test_case_input) + " result " + str(expected_answer))

    # Test case 5: Mixed types (if applicable)
    test_case_input = [1, 'a', 2, 'a', 3, 1]
    expected_answer = [1, 'a', 2, 3]
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input " + str(test_case_input) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with input " + str(test_case_input) + " result " + str(expected_answer))

    return passed, not_passed