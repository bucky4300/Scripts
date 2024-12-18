def sum_the_digits(number):
    # Complete the function definition and place your implementation code here 
    result = sum(int(digit) for digit in str(number)) # Create sum for each digit in number and return the result
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = [41113,91550,5555,77772,15457,123456789] # Test list for variable number
    testAnswers = [10,20,20,30,22,45] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = sum_the_digits(testList[i])
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