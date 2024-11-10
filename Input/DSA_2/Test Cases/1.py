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
    expected_output1 = ['A', 'B', 'C', 'D', 'E']
    if solution(graph1, 'A') == expected_output1:
        passed.append("Solution has passed test case with parameters graph1, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph1, 'A' result " + str(expected_output1))

    # Test case 2: Graph with cycles
    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['E'],
        'D': ['B'],
        'E': []
    }
    expected_output2 = ['A', 'B', 'C', 'D', 'E']
    if solution(graph2, 'A') == expected_output2:
        passed.append("Solution has passed test case with parameters graph2, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph2, 'A' result " + str(expected_output2))

    # Test case 3: Disconnected graph
    graph3 = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    expected_output3 = ['A', 'B', 'C', 'D']
    if solution(graph3, 'A') == expected_output3:
        passed.append("Solution has passed test case with parameters graph3, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph3, 'A' result " + str(expected_output3))

    # Test case 4: Single node graph
    graph4 = {
        'A': []
    }
    expected_output4 = ['A']
    if solution(graph4, 'A') == expected_output4:
        passed.append("Solution has passed test case with parameters graph4, 'A' and expected result")
    else:
        not_passed.append("Solution has not passed test case with inputs graph4, 'A' result " + str(expected_output4))

    return passed, not_passed