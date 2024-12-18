def is_strong_password(password):
    special = "!@#$%^&*()" # Special characters list
    lengthCorrect = False # Length Check bool
    hasUpper = False # Uppercase check bool
    hasLower = False # Lowercase check bool
    hasDigit = False # Digit check bool
    hasSpecial = False # Special character check bool
    # If statements check each option of the password and sets to true if the element is present. If not no change, returns result
    if len(password) < 8:
        lengthCorrect = False
    else:
        lengthCorrect = True
    for char in password:
        if char.isupper():
            hasUpper = True
        elif char.islower():
            hasLower = True
        elif char.isdigit():
            hasDigit = True
        elif char in special:
            hasSpecial = True
    if hasUpper and hasLower and hasDigit and hasSpecial and lengthCorrect:
        result = True
    else:
        result = False
    return result


def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = ["Prevent&Fun%2", "Cape#Harm(Lend#0", "Earth%Interfere!7", "password", "qwerty27", "HelloWorld-2"] # Test list for password variable
    testResults = [] # Actual Answers
    testAnswers = [True, True, True, False, False, False] # Expected Answers
    for i in range (0, len(testList)): # For loop to progress through testList 
        result = is_strong_password(testList[i])
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
    #result = is_strong_password("Any&Goal2")
    #print(result)
    testCode()