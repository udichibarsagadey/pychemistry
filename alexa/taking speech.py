import speech_recognition as speech


while True:
    try:
        #Take the user input to activate reception of Voice Commands
        userInput=input("Press v to start and q to quit")

        if userInput=='v':

            #Take Voice commands from mic
            r=speech.Recognizer()
            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio=r.listen(source)
            #Convert Voice Commands to Text
            command=r.recognize_google(audio)

            print("You said: "+command)
        else:
            break

    #Statements to Handle errors while receiving voice commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
print("Nice interacting with you!!")