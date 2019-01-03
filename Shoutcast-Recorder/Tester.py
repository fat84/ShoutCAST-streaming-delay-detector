##import audioop
##import pyaudio
##
##chunk = 1024
##
##p = pyaudio.PyAudio()
##
##stream = p.open(format=pyaudio.paInt16,
##                channels=1,
##                rate=44100,
##                input=True,
##                frames_per_buffer=chunk)
##
##data = stream.read(chunk)
##
##rms = audioop.rms(data, 2)  #width=2 for format=paInt16

#from selenium import webdriver
#x = 0
##from pydub import silence
##x = silence



#! /usr/bin/env python
from Shoutcast.stream_writer import StreamWriter
from pprint import pprint
import array
import http.client,urllib
from pydub.utils import get_array_type

from pydub.playback import play
from pydub.utils import mediainfo
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np
import  audioop
import time
import os
import sys
import subprocess
##poURL = 'api.pushover.net:443'
##apikey = 'xxxxxxxxxxxxxx'

#pushover_alert################################################################
##def Notify(poApiKey, poUserKey, poTitle, poMessage, poPriority,poSound):
##        conn = http.client.HTTPSConnection(poURL)
##        conn.request('POST', '/1/messages',
##        urllib.urlencode({
##        'token': poApiKey,
##        'user': poUserKey,
##        'token': poApiKey,
##        'user': poUserKey,
##        'title': poTitle,
##        'message': poMessage,
##        'priority': poPriority,
##        'sound': poSound,
##        }), { 'Content-type': 'application/x-www-form-urlencoded' })
start = time.time()
time.clock()
i = 0
####subprocess.Popen([r'C:\Program Files (x86)\Winamp\winamp.exe',r'C:\Users\erick\Desktop\Cosas del Escritorio\Canciones\Corazón Delator - Soda Estereo.mp3'])
while True:

        #try:
                ######################Here you need to edit the link of the streaming.#################################
                s = StreamWriter( "https://usa11.fastcast4u.com/proxy/wplpnnir", 0.5, destination="Output/", filename="output.mp3")
                s.record()
                #pprint(s.metadata)
                sound = AudioSegment.from_mp3("Output/output.mp3")


                bit_depth = sound.sample_width * 8
                array_type = get_array_type(bit_depth)
                numeric_array = array.array(array_type, sound._data)
                info = mediainfo("Output/output.mp3")
                #print numeric_array
                if sound.rms <10:
                        i = 0
                else:#############We add an extra delay of 1.26, because is the time that the program takes to begin the detection.
                        i = 1
                        print (i)
                        print((time.time() + 1.26) - start)
                        break

                #if i  == 5:
                        #mesg = 'Qkradio Stream Silence Detected for more than 5seconds'
                        #print ('alert sent', mesg)
                        #Notify('xxxxxxxxxxxx','xxxxxxxxxxxxx','Aquarium controller',mesg,0,'siren')
                print (i)
        #except:
        #        print ("error")
