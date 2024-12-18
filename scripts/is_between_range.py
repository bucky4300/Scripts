
def is_between_range(number, range): # Takes input from user and calculates if number is within range given
    # Complete the function definition and place your implementation code here 
    range.sort() # Sort range to ensure lowest value first
    if int(number) >= int(range[0]) and int(number) <= int(range[1]): # Checks if number is greater/equal than first number in range then second
        result = True
    else:
        result = False
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    # List 1 for variable number, list 2/3 for variable range
    list1 = [1,10,20,25,30,50]
    list2 = [1,11,10,30,25,60]
    list3 = [10,20,30,40,50,100]
    testAnswers = [1,0,1,0,1,0] # Expected results
    testResults = [] # Actual Results
    for i in range(0, len(list1)): # For loop to progress through testList 
        value = list1[i]
        # Declare rangelist, make sure empty, append value from list 2/3 for testing
        rangeList = []
        rangeList.clear
        rangeList.append(list2[i])
        rangeList.append(list3[i])
        result = is_between_range(value, rangeList)
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