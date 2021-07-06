import speech_recognition as speech
import pyttsx3
import pygame
import time

engine = pyttsx3.init()
engine.setProperty('rate', 200)

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Novelexa')

bg = pygame.image.load("pictures/Listening.jpeg")
image1 = pygame.transform.scale(bg, (600, 600))
screen.blit(image1, (0, 0))
pygame.display.update()

PercyJackson = {"writer": ["imgSpch", "The author of the Percy Jackson series is Rick Riordan.", "writer"],

                "series": ["Spch", "There are a total of 5 books in the PJO series."],

                "genre": ["Spch", "There are three genres in the series, fanatsy, mythology, and young adult fiction."],

                "characters": ["Spch",
                               "The main characters of the series are Percy Jackson, Annabeth Chase, and Grover Underwood.",
                               "characters"],

                "movie": ["Spch", "There are two movies based on the first and second book in the series.", ],

                "fact": ["Spch", "Mostly all demigods have ADHD or Dyslexia."],

                "trivia": ["Spch", "All children of Poseidon can speak and understand horses or equestrial animals,"],

                "Poseidon": ["Spch", "Poseidon is the greek God of the ocean, earthquakes and storms.", "Poseidon"],

                "Hades": ["Spch", "Hades is the Greek God of Death.", "hades"],

                "Zeus": ["Spch", "Zeus is the King of Olympus and is the Greek god of lightning and thunder.", "zeus"],

                "plot": ["Spch",
                         "Theseries revolves around Percy jackson as he faces monsters and Gods with the help of his friends and tells us about his hardships and how he overcomes them."],

                "year": ["Spch", "The series was released over the span of 2005 to 2009."],

                "Quote": ["Spch", "If my life is going to mean anything, I have to live it myself.", "quote"],

                "age": ["Spch", "The age group for the Percy Jackson series is 9+."]}

GeronimoStilton = {"author": ["Spch", "The author of the famous book series Geronimo Stilton is Elisabetta Dami."],

                   "characters": ["Spch",
                                  "The main characters of Geronimo Stilton are Geronimo Stilton,Thea Stilton,Trap Stilton and Benjimin Stilton."],

                   "famous quote": ["Spch",
                                    "The famous quote from Geronimo Stilton is 'Loving means sharing what you have however big or small it may be!'"],

                   "genre": ["Spch", "It's children's literature"],

                   "number": ["Spch", "There are 207 books of Geronimo Stilton in total"],

                   "plot": ["Spch",
                            "In the series, the title character is an anthropomorphic mouse who lives in the fictional New Mouse City on fictional Mouse Island. A best-selling author, Geronimo Stilton works as a journalist and editor for the fictional newspaper The Rodent's Gazette.He has a younger sister named Thea Stilton,a cousin named Trap Stilton,and a favourite nephew, nine-year-old Benjamin Stilton and also Petunina Pretty Paws. Geronimo is a nervous, mild-mannered mouse who would like nothing better than to live a quiet life, but he keeps getting involved in faraway adventures with Thea, Trap, and Benjamin, and sometimes Aunt Sweetfur. The books are written as though they are autobiographical adventure stories."],

                   "best selling": ["Spch",
                                    "The Kingdom of Fantasy which is a special edition is the best selling book of Geronimo Stilton."],

                   "TV series": ["Spch",
                                 "The New Adventures of Geronimo Stilton is the TV seies basedd on Geronimo Stilton."],

                   "year": ["Spch", "In the year 2000 the first book of Geronimo Stilton was published."],

                   "Thea Stilton": ["Spch",
                                    "Thea Stilton is a special correspondent for The Rodent's Gazette, Mouse Island's most famouse newspaper. A graduate of Mouseford Academy, Ms. Stilton loves traveling and adventures."],

                   "Thea Sisters": ["Spch",
                                    "The Thea Sisters are a group of young mouselets who currently attend Mouseford Academy. The group consists of Nicky, Violet, Colette, Paulina, and Pamela. They got their group's name from Thea Stilton, who teaches them in their journalism courses and serves as their mentor."],

                   "Geronimo Stilton": ["Spch",
                                        "Geronimo Stilton is an anthropomorphic mouse who lives in the fictional New Mouse City on fictional Mouse Island. A best-selling author, Geronimo Stilton works as a journalist and editor for the fictional newspaper The Rodent's Gazette."],

                   "first book": ["Spch", "Lost Treasure of the Emerald Eye is the first book published."],

                   "sold": ["Spch",
                            "The series has sold over 180 million copies worldwide, and with 249 editions it is one of the best-selling book series ever written.The books have been translated into 49 languages, with more translations to come."],

                   "publisher": ["Spch",
                                 "Edizioni Piemme Scholastic Corporation is the publisher of Geronimo Stilton."],

                   "language": ["Spch", "Geronimo Stilton was originally written in Italian."],

                   "latest": ["Spch",
                              "The Garbage Thief is the latest book of Geronimo Stilton, it was published on 21 September 2021."],

                   "moral": ["Spch",
                             "Geronimo Stilton's behavior is based on universal ethical values, like being approachable for others, the desire to do good, the commitment to grow and improve oneself.Additionally, Geronimo is brought to life with a healthy optimism: he is never discouraged in negative situations."],

                   "age group": ["Spch",
                                 "The books are intended for readers in the special correspondent for The Rodent's Gazette."],

                   "exit": ["exit", "Good Bye and Keep reading my friend!!"],

                   "close": ["exit", "Have a nice Day!"]}

HarryPotter = {"parents": ["imgSpch", "James and Lily Potter are Harry Potter's parents", "HarryPotterperents"],

               "owl": ["imgSpch", "Hedwig is the name of Harry Potter's owl", "Harry Potter's owl"],

               "Draco Malfoy's dad": ["imgSpch", "Lucius Malfoy is Draco Malfoy's dad", "Malfoydad"],

               "Ron Weasley's parents.": ["imgSpch", "Arthur and Molly are the names of Ron Weasley's parents",
                                          "Ron Weasely's parents"],

               "Ron Weasley's brothers and sister.": ["imgSpch", "Name Ron Weasley's brothers and sister.",
                                                      "Ron Weasely's brothers and sister"],

               "Ron Weasley's rat.": ["imgSpch", "Name Ron Weasley's pet rat.", "Ron Weasely's pet rat"],

               "Luna Lovegood's father": ["imgSpch", "Name Luna Lovegood's father is Xenophillius Lovegood",
                                          "Luna Lovegood's father"],

               "Dobby": ["imgSpch", "Dobby is the ex-house elf who used to work for the Malfoys.", "dobby"],

               "goblin": ["Spch", "Griphook was the first goblin Harry ever met"],

               "Aragog": ["imgSpch", "Acromantula is the Aragog creature", "aragog"],

               "Hagrid's pet dog": ["imgSpch", "Hagrid's pet dog is called Fang", "Hagrid's pet dog"],

               "centaur": ["imgSpch", "Professor Firenze is the centaur who taught at Hogwarts.", "centaur"],

               "four founders of Hogwarts": ["imgSpch",
                                             "Godric Gryffindor, Helga Hufflepuff, Rowena Ravenclaw and Salazar Slytherin were the four founders of Hogwarts",
                                             "four founders of Hogwarts"],

               "Peter Pettigrew": ["Spch", "Ron's pet rat, Scabbers animal could Peter Pettigrew turn into"],

               "Lord Voldemort's snake": ["imgSpch", "Nagini was the name of Lord Voldemort's loyal snake",
                                          "Lord Voldemort's snake"],

               "killed Dobby": ["Spch", "Bellatrix Lestrange killed Dobby by throwing a knife at him"],

               "author": ["imgSpch", "J. K. Rowling is the writer of harry potter?", "author2"],

               "Wand": ["imgSpch",
                        "A wand is a thin, light-weight rod that is held with one hand, and is traditionally made of wood, but may also be made of other materials, such as metal or plastic. Wands are distinct from scepters, which have a greater thickness, are held differently, and have a relatively large top ornament on them"],

               "Muggle": ["Spch",
                          "In J. K. Rowling's Harry Potter series, a Muggle is a person who lacks any sort of magical ability and was not born in a magical family."],

               "Galleon": ["imgSpch",
                           "A Galleon or Gold-Galleon (ʛ) is the most valued coin of the wizarding currency used in Britain. One Galleon is equal to 17 Sickles or 493 Knuts. Galleons are made of gold."],

               "Poltergeist.": ["imgSpch",
                                "The name 'poltergeist' is German in origin, and roughly translates as 'noisy ghost', although it is not, strictly speaking, a ghost at all. The poltergeist is an invisible entity that moves objects, slams doors and creates other audible, kinetic disturbances.."],

               "Herbology": ["imgSpch",
                             "Herbology was the study of magical and mundane plants and fungi, making it the wizarding equivalent to botany."],

               "Remembrall": ["imgSpch",
                              "A Remembrall is a magical large marble-sized glass ball that contains smoke which turns red when its owner or user has forgotten something. It turns clear once whatever was forgotten is remembered."],

               "Centaurs": ["Spch",
                            "A Centaur was a magical creature whose head, torso, and arms appeared to be human and were joined to a horse's body. They were, however, their own individual species, and thus were not half-breeds. They also had a rich history and were known for being naturally talented in Healing magic, Divination and Astronomy."],

               "Transfiguration": ["imgSpch",
                                   "Transfiguration is the family of magical spells that are used for changing objects from one type of thing into another. At Hogwarts, Transfiguration is taught by Professor Minerva McGonagall."],

               "Seeker": ["imgSpch",
                          "Seeker is a position in the wizarding sport of Quidditch. ... The goal of the Seeker is to catch the Golden Snitch. They play a crucial role in Quidditch, as a game does not end until the Seeker catches the Snitch. A team whose Seeker catches the Snitch receives 150 points, which almost always wins the match for that team."]}

NancyDrew = {"Nancy Drew": ["Spch","Nancy Drew is a fictional character, a sleuth in an American mystery series. The character first appeared in 1930. The books are ghostwritten by a number of authors and published under the collective pseudonym Carolyn Keene."],

             "Publisher": ["Spch", "Nancy Drew is a mystery series created by publisher Edward Stratemeyer"],

             "character": ["Spch", "The character first appeared in 1930."],

             "first": ["Spch", "The Secret of the Old Clock was the first Nancy Drew mystery."],

             "wrote": ["Spch",
                       "The Secret of the Old Clock is the first volume in the Nancy Drew Mystery Stories series written under the pseudonym Carolyn Keene."],

             "Who Nancy Drew?": ["Spch",
                                 "Nancy Drew is a 16-year-old high school graduate (her age was changed to 18 in the 1959 rewrite)."],

             "series": ["Spch",
                        "It was first published on April 28, 1930, and rewritten in 1959 by Harriet Stratemeyer Adams."],

             "father": ["Spch", " Her father, Carson Drew, is a well-known criminal defense lawyer."],

             "live": ["Spch", "The Drews reside in River Heights"],

             "Hannah Gruen": ["Spch",
                              "Hannah Gruen was the housekeeper of Drew's family. In early editions, she is depicted as a mere servant; later in the series, she becomes more of a family member."],

             "Ranking": ["Spch",
                         "In 2001, the novel ranked 53rd on Publishers Weekly's list of the all-time best-selling hardcover children's books in English, having sold about 2.7 million copies."],

             "Summary of the 1930 edition": ["Spch",
                                             "Sixteen-year-old Nancy Drew wishes to help the Turners, who are struggling relatives of the recently deceased Josiah Crowley, by finding a missing will that can give them claim to Crowely's estate. Aided along the way by chum Helen Corning, she becomes interested in the case because she dislikes Crowley's snobbish nouveau-riche social-climbing heirs presumptive, the Tophams."],

             "Nationality of Nancy Drew": ["Spch", "American"],

             "exit": ["exit", "Thanks for Interaction"]}

blank = {"exit": ["exit", "Thanks for Interaction"]}

activate = "none"
exitstatus = "no"
state = blank

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("C pressed")

        if activate == 'c':
            listenImg = pygame.image.load("pictures/listening2.jpeg").convert_alpha()
            image1 = pygame.transform.scale(listenImg, (600, 600))
            screen.blit(image1, (0, 0))
            pygame.display.update()

            r = speech.Recognizer()

            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio = r.listen(source, )
                # print("ok1")
            command = r.recognize_google(audio).lower()
            # print("ok2")

            print("You said: " + command)

            if "harry potter" in command:
                state = HarryPotter

            elif "percy jackson" in command:
                state = PercyJackson

            elif "nancy drew" in command:
                state = NancyDrew

            elif "geronimo stilton" in command:
                state = GeronimoStilton

            if state != blank:
                listenImg = pygame.image.load("pictures/listening2.jpeg").convert_alpha()
                image1 = pygame.transform.scale(listenImg, (600, 600))
                screen.blit(image1, (0, 0))
                pygame.display.update()

                r = speech.Recognizer()

                with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak again:")
                    audio = r.listen(source)

                command = r.recognize_google(audio).lower()

                print("You said: " + command)

            for keyword in state:

                if keyword in command:
                    if state[keyword][0] == "Spch":
                        engine.say(state[keyword][1])
                        engine.runAndWait()
                        state = blank

                    elif state[keyword][0] == "consoleText":
                        print(state[keyword][1])
                        state = blank

                    elif state[keyword][0] == "Img":
                        image = pygame.image.load("pictures/" + state[keyword][1] + ".jpeg").convert_alpha()
                        image1 = pygame.transform.scale(image, (813, 375))
                        screen.blit(image1, (45, 145))

                        pygame.display.update()
                        time.sleep(15)
                        state = blank

                    elif state[keyword][0] == "imgSpch":
                        # print("pictures/"+state[keyword][1]+".jpeg")
                        image = pygame.image.load("pictures/" + state[keyword][2] + ".jpeg").convert_alpha()
                        image1 = pygame.transform.scale(image, (600, 600))
                        screen.blit(image1, (0, 0))

                        pygame.display.update()
                        time.sleep(2)

                        engine.say(state[keyword][1])
                        engine.runAndWait()
                        state = blank


                    elif state[keyword][0] == "exit":
                        engine.say(state[keyword][1])
                        engine.runAndWait()
                        exitstatus = "yes"
                        break

            if exitstatus == "yes":
                pygame.quit()
                break

            activate = "none"
            bg = pygame.image.load("pictures/Listening.jpeg").convert_alpha()
            image1 = pygame.transform.scale(bg, (600, 600))
            screen.blit(image1, (0, 0))

    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break