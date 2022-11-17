import pyttsx3		#pip install pyttsx3
import pyaudio
import wave
import sys

#Инициализация голосового "движка" при старте программы
#
#Голос берется из системы, первый попавшийся
#
#Доп материал:
#https://pypi.org/project/pyttsx3/
#https://pyttsx3.readthedocs.io/en/latest/
#https://github.com/nateshmbhat/pyttsx3
#На Linux-ax, скорее всего нужно еще:
#sudo apt update && sudo apt install espeak ffmpeg libespeak1

# engine = pyttsx3.init()
# engine.setProperty('rate', 180)				#скорость речи


def speaker(text):

	CHUNK = 1024
	wf = wave.open(text.strip(), 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)
	data = wf.readframes(CHUNK)
	while len(data) > 0:  # на сайте в примере указано с ошибкой while data != '':
		stream.write(data)
		data = wf.readframes(CHUNK)
	stream.stop_stream()
	stream.close()
	p.terminate()
	'''Озвучка текста'''
	# engine.say(text)
	# engine.runAndWait()