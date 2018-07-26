import time
import speech_recognition as sr
import os

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        print ("  Recorded a phrase...")
        output_folder = str(time.strftime('%d%m%Y'))
        if os.path.exists(output_folder) == False:
            os.mkdir(output_folder)
        filename = time.strftime('%H%M%S')
        data = audio.get_wav_data(convert_rate = 8000, convert_width = 2)
        with open(output_folder + "/" + filename + ".wav", "wb") as o:
            o.write(data)
            print ("  Wrote " + filename + ".wav")
    except sr.UnknownValueError:
        print("Wit could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.dynamic_energy_threshold = True
    r.pause_threshold = 2
    r.adjust_for_ambient_noise(source, duration=3)  # we only need to calibrate once, before we start listening
    print (r.energy_threshold)

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback, phrase_time_limit=40)
# `stop_listening` is now a function that, when called, stops background listening

# calling this function requests that the background listener stop listening
# stop_listening(wait_for_stop=False)
while True: time.sleep(0.1)