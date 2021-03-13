import pandas as pd
import datetime
import csv
import speech_recognition as sr
import os
from gtts import gTTS
import sys
import time
from matplotlib import pyplot as plt


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en', slow=False)
    tts.save("/Users/rishabh/desktop/audiojain.mp3")
    os.system("mpg321 /Users/rishabh/desktop/audiojain.mp3")


def recordaudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    global data
    # Speech recognition using Google Speech Recognition
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)

    except sr.UnknownValueError:
        speak("your voice is not cleared  please write the given input")
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


while 1:

    print("[1] customer")
    print("[2] restaurant account")
    print("[3] exit")
    choice = int(input("enter your choice"))

    if choice == 1:
        df = pd.DataFrame(columns=['menu', 'price'])
        list1 = ["samosa", "omlette", "veg garlic bread", "upma", "parantha", "veg thali", " non veg thali",
                 "makhan kadi", "roti", "naan", "shahi panner", "gulab zamun", "barfi", "dal makhni", "non veg chicken"]
        list2 = [27.6, 28.0, 28.3, 27.85, 29.95, 28.0, 27.4, 28.0, 28.0, 28.5, 28.9, 28.45, 29.6, 27.85, 27.1]
        if len(list1) == len(list2):
            for i in range(len(list1)):
                row = [list1[i], list2[i]]
                df.loc[i] = row

        now = datetime.datetime.now()
        t = time.localtime()
        x = pd.read_csv("/Users/rishabh/desktop/500770.csv")
        l = []
        data = x.iloc[:21, 1:2]
        breakfast = data.iloc[0:5, :]
        breakfast = breakfast.reset_index(drop=True)
        lunch = data.iloc[5:10, :]
        lunch = lunch.reset_index(drop=True)
        dinner = data.iloc[10:15, :]
        dinner = dinner.reset_index(drop=True)
        # x=data.iloc[:20,1]
        y = data.iloc[:20, -1]


        # plt.plot(range(0,10),range(20,30))




        class Table2:
            def menu(self, data):
                self.data1 = data  # change the values
                print("open menu")
                print(self.data1)
                speak("what do you like ")
                speak("breakfast")
                speak("lunch")
                speak("dinner")
                print("what do you like ")
                print("[1]=breakfast")
                print("[2]=lunch")
                print("[3]=dinner")
                speak("please tell me your choice ")
                data2=recordaudio()

                if (data2 in "breakfast"):

                    if now.hour<12:
                        print("breakfast menu")
                        print(df.head(5))
                        y = breakfast['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humein bahut khushi milegi")
                        print("please give ratings")
                        speak("please enter reviews")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()

                        print("please give ratings")
                        speak("please enter the  reviews")

                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")

                        speak("dhanyavad apka din mangal mei ho")
                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])


                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])



                    else:
                        speak("breakfast not available")
                        print("breakfast not available")
                        two = Table2()
                        two.menu(data1)


                elif (data2 in "lunch" or "lun" or "ch"):

                    if(now.hour>12 or now.hour<17):
                        print("lunch")
                        print(df.iloc[5:10,:])
                        y = lunch['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak(str(pay))
                        speak("sir your payable amount is")
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()

                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")

                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])


                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])



                    else:
                        speak("lunch  is not available")
                        print("lunch  is not available")
                        two = Table2()
                        two.menu(data1)


                elif(data2 in "dinner" or "dine" or "dine"):

                    if(now.hour>20):

                        print("dinner")
                        print(df.iloc[10:15,:])
                        y = dinner['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()

                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")

                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])

                        z = pd.read_csv('/Users/rishabh/desktop/eggsjain122.csv', header=None)
                        q = pd.read_csv("/Users/rishabh/desktop/ratingsjain22.csv", header=None)
                        q = q.rename(columns={0: "ratings"})
                        z = z.rename(columns={0: "time"})

                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])


                    else:
                        speak("dinner is over now")
                        print("dinner is over now")

                        two=Table2()
                        two.menu(data1)


                else:
                    speak("sorry sir this item not have in our restaurant")
                    print("sorry sir this item not have in our restaurant")
                    print("sir what will be yours orders")


        class table4:
            def menu(self, data1):
                self.data1 = data
                print("open menu"
                      "***********"
                      "***********"
                      "***********"
                      "***********"
                      "***********"
                      "***********")
                print(self.data1)
                speak("what do you like ")
                speak("breakfast")
                speak("lunch")
                speak("dinner")
                print("what do you like ")
                print("[1]=breakfast")
                print("[2]=lunch")
                print("[3]=dinner")

                speak("sir what will be your orders")

                data2=recordaudio()

                if (data2 in "breakfast" or "break" or "fast"):
                    if now.hour<12:

                        print("breakfast menu")
                        print(breakfast)
                        y = breakfast['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()


                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")


                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])



                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])


                    else:

                        speak("sorry sir breakfast not available")
                        print("sorry sir breakfast not available")
                        four=table4()
                        four.menu(data1)


                elif (data2 in "lunch" or "lun" or "ch"):

                    if now.hour>12 or now.hour<17:

                        print("lunch")
                        print(lunch)
                        y = lunch['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()

                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")

                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])



                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])


                    else:
                        speak("sir , lunch is not available")
                        print("lunch is not available")
                        four = table4()
                        four.menu(data1)

                elif (data2 in "dinner" or "dine" or "er"):

                    if now.hour>17:
                        print("dinner")

                        print(dinner)
                        y = dinner['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()

                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")


                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])



                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])



                    else:
                        speak("sir , dinner is not available for you")
                        print("dinner is not available")
                        four = table4()
                        four.menu(data1)

                else:
                    speak("sorry sir this item not have in our restaurant")
                    print("sorry sir this item not have in our restaurant")


        class table5:
            def menu(self, data1):
                self.data1 = data
                print("open menu"
                      "***********"
                      "***********"
                      "***********"
                      "***********"
                      "***********"
                      "***********")
                print(self.data1)
                speak("what do you like ")
                speak("[1]=breakfast")
                speak("[2]=lunch")
                speak("[3]=dinner")
                print("what do you like ")
                print("[1]=breakfast")
                print("[2]=lunch")
                print("[3]=dinner")
                speak("sir please give your choice")
                data2=recordaudio()
                if data2 in "breakfast" or "break" or "fast":
                    if now.hour<12:
                        print("breakfast menu")
                        print(breakfast)
                        y = breakfast['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)
                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            print(i)
                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()


                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")

                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])

                        z = pd.read_csv('/Users/rishabh/desktop/eggsjain122.csv', header=None)

                        q = pd.read_csv("/Users/rishabh/desktop/ratingsjain22.csv", header=None)

                        q = q.rename(columns={0: "ratings"})

                        z = z.rename(columns={0: "time"})

                        #plt.plot(z, q)
                        ##plt.show()

                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

                            spamwriter.writerow([pay])

                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:

                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])

                    else:
                        print("breakfast is not available")
                        five=table5()
                        five.menu(data1)



                elif data2 in "lunch" or "lun" or "ch":
                    if now.hour>12 or now.hour<17:
                        print("lunch")
                        print(lunch)
                        y = lunch['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)

                        speak("sir your payable amount is")
                        speak(str(pay))
                        speak("sir please give the ratings of food")
                        speak("humei bhut khushi milegi")

                        for i in list:
                            speak("sir please give the ratings of %d" % (i))
                            print(i)



                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])
                        y = x['ratings'].mean()


                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")

                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])

                        z = pd.read_csv('/Users/rishabh/desktop/eggsjain122.csv', header=None)
                        q = pd.read_csv("/Users/rishabh/desktop/ratingsjain22.csv", header=None)
                        q = q.rename(columns={0: "ratings"})
                        z = z.rename(columns={0: "time"})

                        #plt.plot(z, q)
                        ##plt.show()

                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([datetime.datetime.now()])


                    else:
                        print("lunch is not available")
                        five = table5()
                        five.menu(data1)

                elif (data2 in "dinner" or "dine" ):

                    if now.hour>17:
                        print("dinner")
                        print(dinner)
                        y = dinner['Open Price'].tolist()
                        sum = 0
                        z = 1
                        list = []
                        while (z == 1):

                            if z == 1:
                                x = int(input("product key"))
                                list.append(y[x])
                                sum = sum + y[x]
                                print("anything else sir")
                                z = int(input("answer by customer"))

                            if z == 0:
                                break

                        pay = sum + (2 * (sum * 0.25))
                        print("total bill is ")
                        print("actual price %d" % (sum))
                        print("cgst on bill %d" % (sum * 0.25))
                        print("sgst on bill %d" % (sum * 0.25))
                        print(pay)

                        speak("sir your payable amount is")

                        speak(str(pay))

                        speak("sir please give the ratings of food")

                        speak("humein bhut khushi milegi")

                        for i in list:
                            speak("sir please give the ratings of %d"%(i))
                            print(i)

                        l = [(list[i], int(input("enter a ratings"))) for i in range(len(list))]
                        x = pd.DataFrame(l, columns=["food", "ratings"])

                        y = x['ratings'].mean()


                        with open("/Users/rishabh/desktop/re.txt", "a") as f1:
                            rev = input("enter the reviews")
                            name = input("enter  your  name")
                            q = str(datetime.datetime.now())
                            f1.writelines("'{0}' --------- '{1}'  ----- '{2}'----- ".format(name, q, rev))
                            f1.writelines("\n")


                        with open('/Users/rishabh/desktop/ratingsjain22.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([y])

                        with open('/Users/rishabh/desktop/eggsjain122.csv', 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile)
                            spamwriter.writerow([datetime.datetime.now()])

                        z = pd.read_csv('/Users/rishabh/desktop/eggsjain122.csv', header=None)
                        q = pd.read_csv("/Users/rishabh/desktop/ratingsjain22.csv", header=None)

                        q = q.rename(columns={0: "ratings"})
                        z = z.rename(columns={0: "time"})

                        #plt.plot(z, q)
                        ##plt.show()

                        with open('/Users/rishabh/desktop/eggs124567890.csv', 'a', newline='') as csvfile:

                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

                            spamwriter.writerow([pay])
                        with open('/Users/rishabh/desktop/eggs123456789.csv', 'a', newline='') as csvfile:

                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

                            spamwriter.writerow([datetime.datetime.now()])


                    else:
                        print("dinner is not available ")
                        five = table5()
                        five.menu(data1)

                else:
                    print("sorry sir this item not have in our restaurant")

        speak("hi sir , what can i do for you")
        print("**********"
              "**********"
              "**********"
              "**********")

        print("**********"
              "**********"
              "**********"
              "**********")
        if (now.hour>=9):
            print("OPEN")

            speak("how can i help you")

            print("///*****************///")
            time.sleep(1)

        else:
            speak("sorry sir , restaurant will be open after 11 o clock ")
            sys.exit()
        #tableno = int(input(
        speak("sir , how many people are you")          # that is main program shuru and we have second object data 2 in above code


        data1=recordaudio()




        if data1 in str(2) or "to" or "two" or "too":
            speak("yes sir table for 2 is available")

            speak("sir please give the orders")

            table = Table2()

            table.menu(data)

        elif data1 in str(4) or "for" or "four":
            speak("yes sir table for 4 is available")

            speak("sir please give the orders")

            four = table4()

            four.menu(data)

        elif data1 in str(5) or "five" or "fiv":
            speak("yes sir table for 5 is available")
            speak("sir please give the orders")
            five = table5()
            five.menu(data)

        else:
           speak("sorry we don't have a table for  %s" % (data1))


    elif choice==2:

        x_train = pd.read_csv('/Users/rishabh/desktop/500770.csv', header=None)

        x_train = x_train.rename(columns={0: "data"})

        x_data = x_train['data']
        y_train = pd.read_csv('/Users/rishabh/desktop/eggs123456789.csv', header=None)
        y_train = y_train.rename(columns={0: "time"})
        y_data = y_train['time']

        z = pd.read_csv('/Users/rishabh/desktop/eggsjain122.csv', header=None)

        q = pd.read_csv("/Users/rishabh/desktop/ratingsjain22.csv", header=None)

        q = q.rename(columns={0: "ratings"})

        z = z.rename(columns={0: "time"})

        q_data = q['ratings']
        z_data = z['time']
        print("enter the password")
        pas=input()
        i=0
        z=0
        while i <= 2 and z == 0:
            z=1
            if(pas=="******"):
                speak("password authorized")
                time.sleep(1)
                speak("do you want to see strategy")
                print("[1] show ratings of customer graph")
                print("[2] show total cost graph")
                print("[3] show ratings with time graph")
                print("[4] show total amount graph with time")
                print("[5] reviews")
                frame=int(input("do you want to see strategy"))
                if frame==1:
                    plt.plot(q_data)
                    plt.title("show ratings of customer graph")
                    plt.ylabel("ratings")
                    plt.show()

                if frame==2:
                    plt.plot(y_data)
                    plt.title("show total cost graph")
                    plt.ylabel("profit")
                    plt.show()
                if frame==3:

                    plt.plot(z_data,q_data)
                    plt.title("[3] show ratings with time graph")
                    plt.xlabel("time")
                    plt.ylabel("ratings")
                    plt.show()

                if frame==4:
                    plt.plot(y_data,x_data)
                    plt.title("show total amount graph with time")
                    plt.xlabel("time")
                    plt.ylabel("amount of bill")

                if frame==5:

                    print("thanks")
                    with open("/Users/rishabh/desktop/re.txt", "r") as f1:
                        s = f1.readlines()
                        for i in s:
                            print(i)

                if frame==6:
                    print("thanks")
                    speak("bye bye")


            else:
                print("please re enter your password")
                speak("please re enter your password")
                i+=1
        if (i > 2 ):
            print("sorry too many attempts")
            speak("sorry too many attempts")
            sys.exit()

    elif choice==3:
        print("bye bye")
        speak("bye bye")
        sys.exit()
