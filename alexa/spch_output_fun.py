import pyttsx3 as spch

engine = spch.init()

engine.setProperty('rate',150)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

print("hello my name is alexa. i am ur virtual friend. you can ask me any questions ")
engine.say("hello my name is alexa. i am ur virtual friend. you can ask me any questions ")
engine.runAndWait()

engine.say("what should i say?")
engine.runAndWait()
userinput=input("what should i say?")
engine.say(userinput)
engine.runAndWait()