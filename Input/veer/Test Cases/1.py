def test_solution(solution):
    passed = []
    not_passed = []

    # Test case 1: First two Fibonacci numbers
    if solution(0) == 0:
        passed.append("Solution has passed test case with parameter 0 and expected result 0")
    else:
        not_passed.append("Solution has not passed test case with input 0 result 0")

    if solution(1) == 1:
        passed.append("Solution has passed test case with parameter 1 and expected result 1")
    else:
        not_passed.append("Solution has not passed test case with input 1 result 1")

    # Test case 2: Fibonacci number at position 5
    if solution(5) == 5:
        passed.append("Solution has passed test case with parameter 5 and expected result 5")
    else:
        not_passed.append("Solution has not passed test case with input 5 result 5")

    # Test case 3: Fibonacci number at position 10
    if solution(10) == 55:
        passed.append("Solution has passed test case with parameter 10 and expected result 55")
    else:
        not_passed.append("Solution has not passed test case with input 10 result 55")

    # Test case 4: Fibonacci number at position 15
    if solution(15) == 610:
        passed.append("Solution has passed test case with parameter 15 and expected result 610")
    else:
        not_passed.append("Solution has not passed test case with input 15 result 610")

    # Test case 5: Fibonacci number at position 20
    if solution(20) == 6765:
        passed.append("Solution has passed test case with parameter 20 and expected result 6765")
    else:
        not_passed.append("Solution has not passed test case with input 20 result 6765")

    return passed, not_passed