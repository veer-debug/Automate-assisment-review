def test_solution(solution):
    passed = []
    not_passed = []

    # Test Case 1
    test_case_input = [1, 2, 3, 4]
    expected_answer = 24  # 2 * 3 * 4
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input [1, 2, 3, 4] and expected result 24")
    else:
        not_passed.append("Solution has not passed test case with input [1, 2, 3, 4] result 24")

    # Test Case 2
    test_case_input = [-10, -10, 5, 2]
    expected_answer = 500  # -10 * -10 * 5
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input [-10, -10, 5, 2] and expected result 500")
    else:
        not_passed.append("Solution has not passed test case with input [-10, -10, 5, 2] result 500")

    # Test Case 3
    test_case_input = [1, 2, 3]
    expected_answer = 6  # 1 * 2 * 3
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input [1, 2, 3] and expected result 6")
    else:
        not_passed.append("Solution has not passed test case with input [1, 2, 3] result 6")

    # Test Case 4
    test_case_input = [0, -1, -2, -3]
    expected_answer = 0  # 0 * -1 * -2
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input [0, -1, -2, -3] and expected result 0")
    else:
        not_passed.append("Solution has not passed test case with input [0, -1, -2, -3] result 0")

    # Test Case 5
    test_case_input = [5, 6, 2, 3, 1]
    expected_answer = 90  # 5 * 6 * 3
    if solution(test_case_input) == expected_answer:
        passed.append("Solution has passed test case with input [5, 6, 2, 3, 1] and expected result 90")
    else:
        not_passed.append("Solution has not passed test case with input [5, 6, 2, 3, 1] result 90")

    return passed, not_passed