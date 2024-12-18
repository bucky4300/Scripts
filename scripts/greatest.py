
def greatest(a, b, c):
    # Complete the function definition and place your implementation code here 
    list = [a, b, c] # Place values into a list to use the max function to check highest value
    result = max(list)
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList1 = [1,2,3,4,5] # List for variable a
    testList2 = [6,7,8,9,10] # List for variable b
    testList3 = [11,12,13,14,15] # List for variable c
    testResults = [] # Actual Answers
    testAnswers = [11,12,13,14,15] # Expected Answers
    for i in range(0, len(testList1)): # For loop to progress through testList 
        result = greatest(testList1[i], testList2[i], testList3[i])
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