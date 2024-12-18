def weather_advice(sunny, rainy, windy, temperature):
    # Complete the function definition and place your implementation code here
    # Set statements equal to variable names for easier scripting
    sunnyStatement = "Wear sun cream."
    sunnyHotStatement = "It's hot and sunny! Eat some ice cream."
    rainyStatement = "Carry an umbrella."
    rainyWindyStatement = "It's windy! Hold onto your umbrella tightly." 
    windyStatement = "Hold on to your hat."
    statement = "" # Empty string for appending statements
    # If checks based on values passed in from function
    if sunny:
        statement += " " + sunnyStatement
        if temperature >= 25.0:
            statement += " " + sunnyHotStatement
    if rainy:
        statement += " " + rainyStatement
        if windy:
            statement += " " + rainyWindyStatement
            windRecorded = True
    if windy:
        statement += " " + windyStatement
    
    result = statement.lstrip() # Sets result, also removes leading whitespace from left side of string
    return result
    
def testCode(): # Test code to handle testing before program starts, if all pass code proceeds to userInput(), if fail, program quits
    testpass : str = "\033[1;32m Test OK \033[0m" # test passed string with colouring
    testfail : str = "\033[1;31m Test Fail \033[0m" # test failed string with colouring
    allTestsPass: str = "\033[1;32m All Tests Passed \033[0m" # All test Passed string with colouring
    testList = [[True, False, False, 25.5], [True, False, True, 21], [False, True, True, 10], [False, False, True, 10]] # Test list for variables in function
    testAnswers = ["Wear sun cream. It's hot and sunny! Eat some ice cream.","Wear sun cream. Hold on to your hat.", "Carry an umbrella. It's windy! Hold onto your umbrella tightly. Hold on to your hat.", "Hold on to your hat." ] # Expected Answers
    testResults = [] # Actual Answers
    for i in range(0, len(testList)): # For loop to progress through testList 
        
        sublist =testList[i] # Set sublist equal to index value of testList
        # Pull values from sublist out to pass into function
        sunny = sublist[0]
        rainy = sublist[1]
        windy = sublist[2]
        temperature = sublist[3]
        result = weather_advice(sunny, rainy, windy, temperature)
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