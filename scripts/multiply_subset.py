def multiply_subset(numbers, indices):
    # Complete the function definition and place your implementation code here

    indexList = [numbers[i] for i in indices if 0 <= i <len(numbers)] # Create a new list with the selected values from indices
    result = 1 # Set value to 1 so that the first value multiplied in the for loop is accurate
    for value in indexList: # For loop to process the multiplication for each value present
        result *= value
    return result




def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testnumbers = [2,3,4,5,6,7,8] # Standard list for testing purpose
    testList = [[0,2,4],[1,3,4],[3,4,5],[0,1,2,3,4,5,6]] # Test values for Indices
    testAnswers = [48,90,210,40320] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = multiply_subset(testnumbers, testList[i])
        if result == testAnswers[i]:
            testResults.append(result)
            print(testpass)
        else:
            print(testfail)
            quit()
    if testResults == testAnswers:
        print(allTestsPass)

if __name__ == "__main__":
    # Your test code for the function goes here
    testCode()
    #testnumbers = [2,3,4,5,6,7,8]
    #result = multiply_subset(testnumbers, [0,2,4])
    #print(result)