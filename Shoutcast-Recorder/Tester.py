
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

start = time.time()
time.clock()
i = 0

while True:

        #try:#######You can use this option, if you want to use the code before activing the server.
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
