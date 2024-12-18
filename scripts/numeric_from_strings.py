def numeric_from_strings(list_of_strings):
    # Complete the function definition and place your implementation code here 
    numbers = { # Create number map to convert string to numeric value
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    result = [str(numbers[word]) for word in list_of_strings] # check through each value in number map to match the string from input and attach to a string
    return int("".join(result)) # Return result as a single line converted to int

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    # TestList with values for testing, testing edge cases of repeated numbers as well to ensure each is added individually
    testList = [['one','two','three','zero'], ['one','zero','two','nine','zero'], ['nine','nine','nine','nine'],['nine','eight','seven','six','five','four','three','two','one','zero']] 
    testAnswers = [1230, 10290, 9999, 9876543210] # Expected results
    testResults = [] # Actual results
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = numeric_from_strings(testList[i])
        if result == testAnswers[i]:
            testResults.append(result)
            print(testpass)
        else:
            print(testfail)
            quit()
    if testAnswers == testResults:
        print(allTestsPass)

if __name__ == "__main__":
    # Your test code for the function goes here
    testCode()