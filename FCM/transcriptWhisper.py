# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Built based on 
#https://towardsdatascience.com/transcribe-audio-files-with-openais-whisper-e973ae348aa7
#https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/
#https://github.com/zhuzilin/whisper-openvino


import whisper
from pydub import AudioSegment
import os

model = whisper.load_model("small")

source = r"C:\Users\isaldiviagonzatti\Downloads\debora1.m4a"

sound = AudioSegment.from_file(source) # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

# Extract a segment 
#extract = sound[600000:] #in miliseconds 1=60000

#save output as wav file
output_path = os.path.splitext(source)[0]+"_extract.wav"

sound.export(output_path, format="wav")

#transcribe wav file

result= model.transcribe(r"C:\Users\isaldiviagonzatti\Downloads\debora1_extract.wav")

resultxt=result['text']

#save file 

text_file = open(r"C:\Users\isaldiviagonzatti\Downloads\debora1.txt", "w", encoding="utf-8")
text_file.write(resultxt)
text_file.close()
