
def calculate_percentage(part, total):
    # Calculation for percentage based on part and total, returns percentage
    percentage = (float(part)/ float(total)) * 100
    return percentage

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    l1 = [10,20,30,40,50,60,] # List for variable part
    testTotal = 200 # Total used for testing purposes
    testResult = [] # Actual answers
    testAnswer = [5,10,15,20,25,30] # Expected Answers

    for i in range(0, len(l1)): # For loop to progress through testList 
        percentage = calculate_percentage(l1[i], testTotal)
        if percentage == testAnswer[i]:
            print(testpass)
            testResult.append(percentage)
        else:
            print(testfail)
            quit()
        
    if testResult == testAnswer:
        print(allTestsPass)
if __name__ == "__main__":
    # Your test code for the function goes here
    testCode()