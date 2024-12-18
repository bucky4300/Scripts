def subtract_two_numbers(m, n):
    # Complete the function definition and place your implementation code here 
    result = m - n # Subtract second value passed from first and return result
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList1 = [10,15,27,-46,500,6432] # Test list for m value
    testList2 = [4,15,17,-45,247,432] # Test list for n value
    testAnswers = [6,0,10,-1,253,6000] # Expected answers
    testResults = [] # Actual results
    for i in range(0, len(testList1)): # For loop to progress through testList 
        result = subtract_two_numbers(testList1[i], testList2[i])
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