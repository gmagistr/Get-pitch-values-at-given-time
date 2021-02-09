import glob
import numpy as np
import pandas as pd
import parselmouth


from parselmouth.praat import call
def measurePitch(voiceID, f0min, f0max, unit):
    sound = parselmouth.Sound(voiceID)
    pitchObject = call(sound, "To Pitch", 0.0, 25, 350) # we create the pitch object that we will query
    pitch1 = call(pitchObject, "Get value at time", 0.1, "Hertz", "linear")  # here we get the value, the second value is the time we are enquiring
    pitch2 = call(pitchObject, "Get value at time", 0.2, "Hertz", "linear" )
    pitch3 = call(pitchObject, "Get value at time", 0.3, "Hertz", "linear")
    pitch4 = call(pitchObject, "Get value at time", 0.4, "Hertz", "linear")
    pitch5 = call(pitchObject, "Get value at time", 0.55, "Hertz", "linear")
    pitch6 = call(pitchObject, "Get value at time", 0.7, "Hertz", "linear")
    pitch7 = call(pitchObject, "Get value at time", 0.8, "Hertz", "linear")
    pitch8 = call(pitchObject, "Get value at time", 0.9, "Hertz", "linear")
    pitch9 = call(pitchObject, "Get value at time", 1, "Hertz", "linear")
    pitch10 = call(pitchObject, "Get value at time", 1.01, "Hertz", "linear")
# you can add as many points as you want
    return pitch1, pitch2, pitch3, pitch4, pitch5, pitch6, pitch7, pitch8, pitch9, pitch10 # adapt according to the pitch points
file_list = []
f0_1 = []
f0_2 = []
f0_3 = []
f0_4 = []
f0_5 = []
f0_6= []
f0_7 = []
f0_8 = []
f0_9 = []
f0_10 = []
for wave_file in glob.glob("your path\\*.wav"): # insert here the path where your audio files are stored
    sound = parselmouth.Sound(wave_file)
    (pitch1, pitch2, pitch3, pitch4, pitch5, pitch6, pitch7, pitch8, pitch9, pitch10) = measurePitch(sound, 25, 350, "Hertz") # adjust according to the pitch points, the second part 
# sets the floor, ceiling and unit
    file_list.append(wave_file)
    f0_1.append(pitch1)
    f0_2.append(pitch2)
    f0_3.append(pitch3)
    f0_4.append(pitch4)
    f0_5.append(pitch5)
    f0_6.append(pitch6)
    f0_7.append(pitch7)
    f0_8.append(pitch8)
    f0_9.append(pitch9)
    f0_10.append(pitch10) # do not forget to adjust 
df = pd.DataFrame(np.column_stack([file_list, f0_1, f0_2, f0_3, f0_4, f0_5, f0_6, f0_7, f0_8, f0_9, f0_10]), # adjust
                               columns=['voiceID', 'f0_1', 'f0_2', 'f0_3', 'f0_4', 'f0_5', 'f0_6',
                                        'f0_7', 'f0_8', 'f0_9', 'f0_10']) # adjust

df.to_csv("processed_results.csv", index=False) # your .csv is named processed_results .csv

# Have fun!
