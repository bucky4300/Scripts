def is_vowel(character):
    # Complete the function definition and place your implementation code here
    vowels = ["a","e","i","o","u"] # List of vowels to check against
    containsVowel = False # Flag changes when vowel is found below
    for i in character:
        for j in vowels:
            if i==j:
                containsVowel = True
    if containsVowel == True:
        result = True
    else:
        result = False
    return result # Exports result to global

def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = ["a","b","l","i","r","o"] # List of letters to test code with
    testAnswers = [True, False, False, True, False, True] # Expected results for above tests
    testResults = [] # Empty list to append actual result to
    for i in range(0, len(testList)): # For loop to progress through testList 
        result = is_vowel(testList[i])
        if result == testAnswers[i]:
            print(testpass)
            testResults.append(result)
        else:
            print(testfail)
    if testResults == testAnswers:
        print(allTestsPass)

if __name__ == "__main__":
    # Your test code for the function goes here
    testCode()