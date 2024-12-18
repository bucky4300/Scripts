def is_monotonic(string_of_digits):
    #Sort string lowest-highest/highest-lowest, if either match, result exported as true
    if str(string_of_digits) == ''.join(sorted(str(string_of_digits))) or str(string_of_digits) == ''.join(sorted(str(string_of_digits), reverse=True)):
        result = True
    else:
        result = False
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = [123456, 122336, 2465321, 121212, 543210, 675432] #  Test list for string_of_digits variable
    testAnswers = [True, True, False, False, True, False] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = is_monotonic(testList[i])
        if result == testAnswers[i]:
            print(testpass)
            testResults.append(result)
        else:
            print(testfail)
            quit()
    if testResults == testAnswers:
        print(allTestsPass)

if __name__ == "__main__":
    # Your test code for the function goes here
    testCode()