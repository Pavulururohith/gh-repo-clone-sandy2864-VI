# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
import datetime


# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Please say that again")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query


# creating Speak() function to giving Speaking power
# to our voice assistant
def Speak(audio):
    converter = pyttsx3.init() 
    converter.setProperty('rate', 150) 
    # Set volume 0-1 
    converter.setProperty('volume', 0.7) 

    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
    current_time = datetime.datetime.now()
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "ok bye" in command:
            Speak("bai sir! have a good day")
            break
        if "Instagram" in command:
            Speak("Your instagram account is currently deleted")
        if "name" in command:
            Speak("My name is Alex")
        if "how are you" in command:
            Speak("I am good. How are you sir?")
        if "Corona" in command:
            Speak(
                "the only way is by singing corona go, corona go go corona corona, go go corona go corona corona go go, corona")
        if "Ronaldo" in command:
            Speak("obviously Ronaldo")
        if "cricketer" in command:
            Speak("Mahendra singh Dhoni. but I will call him Maahee From now onwards")
        if "ok Vinod" in command:
            Speak("who??? it's Alex here")
        if "sorry" in command:
            Speak("It's alright sir!")
        if "time" in command:
            Speak(current_time)
        if "Who are you" in command:
            Speak("I am Binod. The influencer")
        if "YouTube channel" in command:
            Speak("free code hub")
        if "promote" in command:
            Speak("okay. hello guys if you are new to our channel please consider subscribing.")
        if "Wikipedia" in command:
            Speak(
                "Mahendra Singh Dhoni, is a former Indian international cricketer who captained the Indian national team in limited-overs formats from 2007 to 2016 and in Test cricket from 2008 to 2014.")
        if "everything" in command:
            Speak("Okay. I will not speak a single word now")
        if "can I" in command:
            Speak("Sad to say, but no because everyone knows about help center reality of instagram")
        if "good Alex" in command:
            Speak("Thank you so much sir!")
        if "thank you" in command:
            Speak("My pleasure Sir!")
        if "you just" in command:
            Speak("i sing better than you sir")
        if "Diwali" in command:
            Speak("Happy Diwali to all of you guys. stay safe!")