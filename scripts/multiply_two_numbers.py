def multiply_two_numbers(m, n):
    # Complete the function definition and place your implementation code here 
    result = (int(m)*int(n)) # Multiply value 1 by value 2, transform both to int to ensure function can proceed
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList1 = [1,2,3,4,5,6] # Value 1 test list
    testList2 = [7,8,9,10,11,12] # Value 2 test list
    testAnswers = [7,16,27,40,55,72] # Expected Answers
    testResults = [] # List for actual answers
    for i in range(0, len(testList1)): # For loop to progress through testList 
        result = multiply_two_numbers(testList1[i], testList2[i])
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