import pyttsx3

if __name__ == "__main__":
    print("You are welcome to text to speech")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "q":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
