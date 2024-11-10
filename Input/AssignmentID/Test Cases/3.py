def test_solution(solution):
    passed = []
    not_passed = []

    # Test case 1: Regular string
    parameter1 = "hello"
    expected_answer = "olleh"
    if solution(parameter1) == expected_answer:
        passed.append("Solution has passed test case with parameter 'hello' and expected result 'olleh'")
    else:
        not_passed.append("Solution has not passed test case with input 'hello' result 'olleh'")

    # Test case 2: Empty string
    parameter2 = ""
    expected_answer = ""
    if solution(parameter2) == expected_answer:
        passed.append("Solution has passed test case with parameter '' and expected result ''")
    else:
        not_passed.append("Solution has not passed test case with input '' result ''")

    # Test case 3: String with spaces
    parameter3 = "hello world"
    expected_answer = "dlrow olleh"
    if solution(parameter3) == expected_answer:
        passed.append("Solution has passed test case with parameter 'hello world' and expected result 'dlrow olleh'")
    else:
        not_passed.append("Solution has not passed test case with input 'hello world' result 'dlrow olleh'")

    # Test case 4: Palindrome
    parameter4 = "racecar"
    expected_answer = "racecar"
    if solution(parameter4) == expected_answer:
        passed.append("Solution has passed test case with parameter 'racecar' and expected result 'racecar'")
    else:
        not_passed.append("Solution has not passed test case with input 'racecar' result 'racecar'")

    # Test case 5: Special characters
    parameter5 = "12345!@#$%"
    expected_answer = "%$#@!54321"
    if solution(parameter5) == expected_answer:
        passed.append("Solution has passed test case with parameter '12345!@#$%' and expected result '%$#@!54321'")
    else:
        not_passed.append("Solution has not passed test case with input '12345!@#$%' result '%$#@!54321'")

    return passed, not_passed