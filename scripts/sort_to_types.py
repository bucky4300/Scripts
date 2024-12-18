def sort_to_types(arbitrary_ordered_types):
    # Complete the function definition and place your implementation code here 
    stringsList = [item for item in arbitrary_ordered_types if isinstance(item, str)]
    integerList = [item for item in arbitrary_ordered_types if isinstance(item, int)]
    floatList = [item for item in arbitrary_ordered_types if isinstance(item, float)]

    result = stringsList + integerList + floatList
    return result

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = [['banana', 5, 3.14, 'apple', 42, 2.71],['crayon','simulation',5,5.1515,3.14159,'colour'],['crab',100,1.00,2.00,14567,'helper'], [120,1.4,5,'test!!',3.14]] # Test list for variable arbitrary_order_types
    testAnswers = [['banana','apple',5,42,3.14,2.71],['crayon','simulation','colour',5,5.1515,3.14159], ['crab', 'helper',100,14567,1.00,2.00],['test!!',120,5,1.4,3.14]] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = sort_to_types(testList[i])
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