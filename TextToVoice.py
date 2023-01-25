import pyttsx3


def voice(text, gender='m'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if gender == 'm':
        # changing index, changes voices. o for male
        engine.setPropertyz('voice', voices[0].id)
    else:
        # changing index, changes voices. 1 for female
        engine.setProperty('voice', voices[1].id)
    print("Assistant :- ", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
