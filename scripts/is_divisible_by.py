def is_divisible_by(number, denominators):
    # Complete the function definition and place your implementation code here 
    for i in range(0, len(denominators)): # Sets loop and checks if number is divisible by denominator one at a time, if any return false, code escapes and returns false
        if (int(number)%int(denominators[i])) == 0:
            result = True
        else: 
            result = False
            break
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    #List 1 for variable number, list 2/3 for variable denominator
    list1 = [10,20,30,40,50,60]
    list2 = [2,4,6,8,10,12]
    list3 = [10,20,30,40,50,60]
    testAnswers = [True, True, True, True, True, True] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(list1)): # For loop to progress through testList 
        # Declare rangelist, clear to make sure empty, append value from list 2/3 for testing
        rangeList = []
        rangeList.clear
        rangeList.append(int(list2[i]))
        rangeList.append(int(list3[i]))
        result = is_divisible_by(int(list1[i]), rangeList)
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