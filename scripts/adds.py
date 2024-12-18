
def adds(p1, p2):
    # Function takes list input and performs calculation to output result of p1 + p2
    result = []
    result.clear()
    if len(p1) != len(p2):
        print("None.")
        quit()
    for i in range(0, len(p1)):
        result.append(p1[i] + p2[i])
    return result

def testCode():# Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    #test lists pushed into adds function with known result to test that code works, if expected result returns proceed to next test, if not program quits with testfail
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test passed string with colouring
    testList = [[1,2,3],[2,4,6],[4,8,12],[8,16,24]] # Test list for variables p1,p2, repeated for ease of testing
    testAnswers = [[2,4,6],[4,8,12],[8,16,24],[16,32,48]] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)):
        result = adds(testList[i],testList[i])
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
    