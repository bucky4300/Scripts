def sum_odd_numbers_in_table(n):
    # Complete the function definition and place your implementation code here 
    total = 0 # Set sum to 0 to ensure accurate value
    for i in range(1, n+1): # Create loop for number value + 1
        for j in range(1, n+1):# Create second loop
            sum = i * j # multiply values
            if (sum % 2) != 0: # Find if they are odd or even
                total += sum # If odd add to total
    result = total # set result = to total for display
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = [3,5,7,9,11,13] # Test list for variable n
    testAnswers = [16,81,256,625,1296,2401] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = sum_odd_numbers_in_table(testList[i])
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