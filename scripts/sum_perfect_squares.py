def sum_perfect_squares(number):
    # Complete the function definition and place your implementation code here 
    total = 0 # Set total to 0 for accurate value
    for i in range (1, number+1): # Set for loop to go through each number between 1 and number+1
        total += (i ** 2) # Square current number and add it to total
    result = total # Set result = total and return result
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = [4,9,5,7,10,12] # Test list for variable number
    testAnswers = [30,285,55,140,385,650] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = sum_perfect_squares(testList[i])
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