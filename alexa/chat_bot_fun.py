import pyttsx3 as spch

engine = spch.init()

engine.setProperty('rate',250)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


print("Hello I am your assistant for query related to general knowledge")
engine.say("Hello I am your assistant for query related to general knowledge")
engine.runAndWait()
print(" you can ask me any of the following query ")
engine.say(" you can ask me any of the following query ")
engine.runAndWait()
print("a.It is the Rapid and uncontrolled growth of algae in freshwater or Marine environments. it can be harmful to humans, mammals, birds and fish when the toxins are ingested ??")
engine.say("a.It is the Rapid and uncontrolled growth of algae in freshwater or Marine environments. it can be harmful to humans, mammals, birds and fish when the toxins are ingested ??")
engine.runAndWait()
print("b.It is one of the oldest, prettiest and the most famous aquatic flowers that can take the beauty of any water Garden. These flowers can be grown in and found in or Lake by rooting them in the mud ??")
engine.say("b.It is one of the oldest, prettiest and the most famous aquatic flowers that can take the beauty of any water Garden. These flowers can be grown in and found in or Lake by rooting them in the mud ??")
engine.runAndWait()
print("c.It is a beautiful aquatic fern used as a good source of biofilter. Its value lies in its nitrogen fixing capacity where by the plant is capable of reducing nitrogen demand in the soil. it provides nutrients in the soil ??")
engine.say("c.It is a beautiful aquatic fern used as a good source of biofilter. Its value lies in its nitrogen fixing capacity where by the plant is capable of reducing nitrogen demand in the soil. it provides nutrients in the soil ??")
engine.runAndWait()
print("d.This plant is ideal for containing and water Gardens are like, as it can be grown with its toes  in the water. the beautiful foliage is light green and highlighted with bright yellow stripes, remaining beautiful all season and sometimes through the winter ??")
engine.say("This plant is ideal for containing and water Gardens are like, as it can be grown with its toes  in the water. the beautiful foliage is light green and highlighted with bright yellow stripes, remaining beautiful all season and sometimes through the winter ??")
engine.runAndWait()
print("e.Highest mountain peak of Europe??")
engine.say("e.Highest mountain peak of Europe??")
engine.runAndWait()
print("f. the highest mountain peak of Africa??")
engine.say("f. the highest mountain peak of Africa??")
engine.runAndWait()
print("g. highest mountain peak of North America??")
engine.say("g. highest mountain peak of North America??")
engine.runAndWait()
print("h. highest mountain peak of South America??")
engine.say("h. highest mountain peak of South America??")
engine.runAndWait()
print("i. highest mountain peak of Australia??")
engine.say("i. highest mountain peak of Australia??")
engine.runAndWait()
print("j. highest mountain peak of venezuela??")
engine.say("j. highest mountain peak of venezuela??")
engine.runAndWait()

response="y"
while response=="y":
    engine.say("enter choice of query:")
    choice = input("enter choice of query:")
    engine.runAndWait()
    if choice=="a":
        print("algal bloom")
        engine.say("algal bloom")
        engine.runAndWait()
    elif choice=="b":
        print("lotus")
        engine.say("lotus")
        engine.runAndWait()
    elif choice == "c":
        print("sweet flag")
        engine.say("sweet flag")
        engine.runAndWait()
    elif choice == "d":
        print("azolla pinnata")
        engine.say("azolla pinnata")
        engine.runAndWait()
    elif choice == "e":
        print("mount elbrus")
        engine.say("mount elbrus")
        engine.runAndWait()
    elif choice == "f":
        print("Mount Kilimanjaro")
        engine.say("Mount Kilimanjaro")
        engine.runAndWait()
    elif choice == "g":
        print("Mount McKinley")
        engine.say("Mount McKinley")
        engine.runAndWait()
    elif choice == "h":
        print("Mount Aconcagua")
        engine.say("Mount Aconcagua")
        engine.runAndWait()
    elif choice == "i":
        print("Mount Kosciuszko")
        engine.say("Mount Kosciuszko")
        engine.runAndWait()
    elif choice == "j":
        print("Mount Pico Bolivar")
        engine.say("Mount Pico Bolivar")
        engine.runAndWait()
    else:
        print("I dint know the answer")
        engine.say("I dint know the answer")
        engine.runAndWait()

    engine.say("do u wish to continue? y/n")
    response = input("do u wish to continue? y/n")
    engine.runAndWait()

print("thankyou for interacting with me ")
engine.say("thankyou for interacting with me ")
engine.runAndWait()
    