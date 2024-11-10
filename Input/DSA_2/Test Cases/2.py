def test_solution(solution):
    passed = []
    not_passed = []

    # Test case 1: Simple graph
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    expected1 = ['A', 'B', 'D', 'C', 'E']  # DFS starting from A
    if solution(graph1, 'A') == expected1:
        passed.append("Solution has passed test case with parameters graph1, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph1, 'A' result " + str(expected1))

    # Test case 2: Graph with cycles
    graph2 = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['A'],
        'D': ['E'],
        'E': []
    }
    expected2 = ['A', 'B', 'C', 'D', 'E']  # DFS starting from A
    if solution(graph2, 'A') == expected2:
        passed.append("Solution has passed test case with parameters graph2, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph2, 'A' result " + str(expected2))

    # Test case 3: Empty graph
    graph3 = {}
    expected3 = []  # DFS starting from any node in an empty graph
    if solution(graph3, 'A') == expected3:
        passed.append("Solution has passed test case with parameters graph3, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph3, 'A' result " + str(expected3))

    # Test case 4: Single node graph
    graph4 = {
        'A': []
    }
    expected4 = ['A']  # DFS starting from A
    if solution(graph4, 'A') == expected4:
        passed.append("Solution has passed test case with parameters graph4, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph4, 'A' result " + str(expected4))

    return passed, not_passed