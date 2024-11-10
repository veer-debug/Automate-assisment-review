def test_solution(solution):
    passed = []
    not_passed = []

    # Test case 1: Square matrix
    parameter1 = [[1, 2], [3, 4]]
    expected_answer = [[1, 3], [2, 4]]
    if solution(parameter1) == expected_answer:
        passed.append("Solution has passed test case with parameters " + str(parameter1) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter1) + " result " + str(expected_answer))

    # Test case 2: Rectangular matrix
    parameter2 = [[1, 2, 3], [4, 5, 6]]
    expected_answer = [[1, 4], [2, 5], [3, 6]]
    if solution(parameter2) == expected_answer:
        passed.append("Solution has passed test case with parameters " + str(parameter2) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter2) + " result " + str(expected_answer))

    # Test case 3: Single row matrix
    parameter3 = [[1, 2, 3]]
    expected_answer = [[1], [2], [3]]
    if solution(parameter3) == expected_answer:
        passed.append("Solution has passed test case with parameters " + str(parameter3) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter3) + " result " + str(expected_answer))

    # Test case 4: Single column matrix
    parameter4 = [[1], [2], [3]]
    expected_answer = [[1, 2, 3]]
    if solution(parameter4) == expected_answer:
        passed.append("Solution has passed test case with parameters " + str(parameter4) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter4) + " result " + str(expected_answer))

    # Test case 5: Empty matrix
    parameter5 = []
    expected_answer = []
    if solution(parameter5) == expected_answer:
        passed.append("Solution has passed test case with parameters " + str(parameter5) + " and expected result " + str(expected_answer))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter5) + " result " + str(expected_answer))

    return passed, not_passed