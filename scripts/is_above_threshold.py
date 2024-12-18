

def is_above_threshold(number, threshold): # Takes input from userInput() and performs function returning result
    # Complete the function definition and place your implementation code here 
    if number > threshold: # Check if number is above threshold
        result = 1
    elif number < threshold: # Check if number is below threshold
        result = 0
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    
    list1 = [1,25,26,50,49,61] # List for variable number
    list2= [10,20,30,40,50,60] # List for variable threshold
    testAnswers = [0,1,0,1,0,1] # Expected Answers
    testResult = [] # Actual Answers
    for i in range(0, len(list1)): # For loop to progress through testList 
        result =is_above_threshold(list1[i], list2[i])
        if result == testAnswers[i]:
            print(testpass)
            testResult.append(result)
        else:
            print(testfail)
            quit()
    if testResult == testAnswers:
        print(allTestsPass)

if __name__ == "__main__":
    # Your test code for the function goes here
    testCode()