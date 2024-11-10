def test_solution(solution):
    passed = []
    not_passed = []

    # Test case 1: 2x2 matrix
    parameter1 = [[4, 7], [2, 6]]
    expected_answer1 = [[0.6, -0.7], [-0.2, 0.4]]
    if solution(parameter1) == expected_answer1:
        passed.append("Solution has passed test case with parameters " + str(parameter1) + " and expected result " + str(expected_answer1))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter1) + " result " + str(expected_answer1))

    # Test case 2: 3x3 matrix
    parameter2 = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    expected_answer2 = [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]
    if solution(parameter2) == expected_answer2:
        passed.append("Solution has passed test case with parameters " + str(parameter2) + " and expected result " + str(expected_answer2))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter2) + " result " + str(expected_answer2))

    # Test case 3: Singular matrix (should raise an error)
    parameter3 = [[1, 2], [2, 4]]
    try:
        solution(parameter3)
        not_passed.append("Solution has not raised an error for singular matrix " + str(parameter3))
    except Exception:
        passed.append("Solution has correctly raised an error for singular matrix " + str(parameter3))

    # Test case 4: Identity matrix
    parameter4 = [[1, 0], [0, 1]]
    expected_answer4 = [[1, 0], [0, 1]]
    if solution(parameter4) == expected_answer4:
        passed.append("Solution has passed test case with parameters " + str(parameter4) + " and expected result " + str(expected_answer4))
    else:
        not_passed.append("Solution has not passed test case with inputs " + str(parameter4) + " result " + str(expected_answer4))

    return passed, not_passed