<task>Goal  Build a small chatbot that responds based on keywords.  What It Should Do  #Ask the user to type something  #Detect keywords like:  "hello"  "help"  "study"  #Respond with fixed pre-written messages  Otherwise say: "I'm still learning!"</task>

Here is the starter code snippet
<starter>msg = input("Say something: ").lower()  if "hello" in msg:     print("Hello! Ready to study?") elif "help" in msg:     print("Sure! What topic do you need help with?") elif "study" in msg:     print("Let's learn something new today!") else:     print("I'm still learning. Try different words!")  Required Output  Keyword detection  Clear responses</starter>

<instructions>1. Use comments 2. Explain what lines of code do 3. Intergrate logging system with print statements </instructions>