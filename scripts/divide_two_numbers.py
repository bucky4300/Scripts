

def divide_two_numbers(m, n):
    # Complete the function definition and place your implementation code here 
    if n == 0: # If number equals 0 return NAN as cannot divide by 0
        print("NAN")
        quit()
    else:
        result = m / n # Divide m by n and return result 
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testNo1 = [10,20,30,40,50] # List for variable m
    testNo2 = [2,4,6,8,10] # List for variable n
    testAnswers = [5,5,5,5,5] # Expected Answers
    testResults = [] # Actual Answers

    for i in range(0, len(testNo1)): # For loop to progress through testList 
        result = divide_two_numbers(testNo1[i], testNo2[i])
        if result == testAnswers[i]:
            print(testpass)
            testResults.append(result)
        else:
            print(testfail)
            quit()
    if testResults == testAnswers:
        print(allTestsPass)

if __name__ == "__main__":
    testCode()