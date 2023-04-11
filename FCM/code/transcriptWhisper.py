#Built based on 
#https://towardsdatascience.com/transcribe-audio-files-with-openais-whisper-e973ae348aa7
#https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/
#https://github.com/zhuzilin/whisper-openvino


import whisper
from pydub import AudioSegment
import os

# define paths
data_path = 'data'
output_path = 'output'

# set parent folder as working directory
os.chdir('..')
os.getcwd()

model = whisper.load_model("small")

source = os.path.join(data_path,"FILE.m4a")

sound = AudioSegment.from_file(source) # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

# Extract a segment 
#extract = sound[600000:] #in miliseconds 1=60000

#save output as wav file
output_path = os.path.splitext(source)[0]+"_extract.wav"

sound.export(output_path, format="wav")

#transcribe wav file
result= model.transcribe(os.path.join(output_path,"FILE.wav")
resultxt=result['text']

#save file 
text_file = open(os.path.join(output_path,"FILE.txt"), "w", encoding="utf-8")
text_file.write(resultxt)
text_file.close()
