def is_even(number):
    # Complete the function definition and place your implementation code here 
    if (number % 2) == 0: # checks if remainder when divided by two == 0, if so pass true
        result = True
    else:
        result = False
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m"
    testList = [10,23,30,43,55,60] # Test list for variable number
    testAnswers = [True, False, True, False, False, True] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result =is_even(testList[i])
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
    