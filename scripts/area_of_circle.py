
def area_of_circle(radius): # Calculation function for area of circle
    PI : float = 3.142 # Constant for PI
    area = PI * (float(radius) ** 2) # Calculation for area of a circle, returns area
    return area

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList : list = [1,2,3,4,5,6] # List for testing function
    testResults : list = [] # Actual Answers
    testAnswers : list = [3.142, 12.568, 28.278, 50.272, 78.55, 113.112] # Expected answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        area = area_of_circle(testList[i])
        if area == testAnswers[i]:
            print(testpass)
        else:
            print(testfail)
            quit()
        testResults.append(area)
    if testResults == testAnswers:
        print(allTestsPass)

if __name__ == "__main__":
    testCode()
    