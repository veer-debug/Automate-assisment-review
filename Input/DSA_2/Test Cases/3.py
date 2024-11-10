def test_solution(solution):
    passed = []
    not_passed = []

    # Test Case 1: Simple path
    start = (0, 0)
    goal = (1, 1)
    grid = [[0, 0], [0, 0]]
    expected_result = [(0, 0), (1, 1)]
    if solution(start, goal, grid) == expected_result:
        passed.append("Solution has passed test case with parameters (0, 0), (1, 1) and expected result [(0, 0), (1, 1)]")
    else:
        not_passed.append("Solution has not passed test case with inputs (0, 0), (1, 1) result [(0, 0), (1, 1)]")

    # Test Case 2: Blocked path
    start = (0, 0)
    goal = (1, 1)
    grid = [[0, 1], [0, 0]]
    expected_result = None  # No path available
    if solution(start, goal, grid) == expected_result:
        passed.append("Solution has passed test case with parameters (0, 0), (1, 1) and expected result None")
    else:
        not_passed.append("Solution has not passed test case with inputs (0, 0), (1, 1) result None")

    # Test Case 3: Larger grid with a clear path
    start = (0, 0)
    goal = (3, 3)
    grid = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    expected_result = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]
    if solution(start, goal, grid) == expected_result:
        passed.append("Solution has passed test case with parameters (0, 0), (3, 3) and expected result [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]")
    else:
        not_passed.append("Solution has not passed test case with inputs (0, 0), (3, 3) result [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]")

    return passed, not_passed