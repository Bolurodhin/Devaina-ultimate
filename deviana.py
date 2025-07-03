import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "english")
    engine.say(text)
    engine.runAndWait()

print("💫 Deviana: Hey babe, I'm here. What's your wish?")
while True:
    try:
        q = input("💬 You: ")
        if q.lower() in ["exit", "bye"]: break
        speak("Okay love. You said: " + q)
    except KeyboardInterrupt:
        break
print("👋 Deviana: Bye babe!")
