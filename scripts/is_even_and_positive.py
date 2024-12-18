def is_even_and_positive(number):
    # Complete the function definition and place your implementation code here 
    if number > 0 and (number % 2) == 0: # Checks if number is greater than 0 and if remainder after dividing by two == 0
        result = True
    else:
        result = False
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m"
    testList = [1,3,-10,10,6,250] # Test list for variable number
    testAnswers = [False, False, False, True, True, True] # Expected Answers
    testResults = [] # Actual answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = is_even_and_positive(testList[i])
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