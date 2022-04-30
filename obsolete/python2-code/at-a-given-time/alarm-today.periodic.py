#!/usr/bin/python 

# esli budil'nik stavyat na etot zhe den': (skazhem, posle polunochi na 8 utra)

import os
import time
import sys

period = 40  # every 40 minutes

player = "mplayer" 
# variant: ogg123 -- does not work

# -- getting the arguments
try: alarmHours = int(sys.argv[1]); alarmMinutes = int(sys.argv[2])
except: print 'Usage: %s hours minutes' % sys.argv[0]; sys.exit(1)
#--                         sys.argv[0] = "0'th argument" = filename

print "first alarm will sound at", alarmHours, "hours", alarmMinutes , "minutes"
print "and then every ", period, " minutes"

Time = time.localtime()
print time.asctime()

# --------------------- getting program path ---------
program_name = sys.argv[0]  # this is full path to the program: path/filename
# say, /home/leyenson/code/python/alarm-clock/alarm-proba.py
print "-- program name: ", program_name 

program_path = os.path.dirname(program_name)
# print "   program path: ", program_path 

sounds_path = program_path + "/sounds"
print "   sounds path: ", sounds_path 

soundfile1  = sounds_path + "/28113__HerbertBoland__Kukuklok_1_slag.ogg" 
soundfile11 = sounds_path + "/28114__HerbertBoland__Kukuklok_11_slag.ogg"

print "   soundfile1:  ", soundfile1  
print "   soundfile11: ", soundfile11  

# ------------------------------

print "[checking that sounds are audible...]"
os.system(player + " " +  soundfile1 )  #  1 beat

currentHours   = Time[3]
currentMinutes = Time[4]
currentSeconds = Time[5]

remainingSeconds = (alarmHours - currentHours) * 60 * 60  +  \
                       (alarmMinutes - currentMinutes) * 60   -  \
                       currentSeconds

print "[now sleeping ", remainingSeconds, "seconds]"
time.sleep(remainingSeconds)
print time.asctime()
os.system(player + " " +  soundfile11 )

for i in range(2,8):    # cycle over 2 - (n-1) (sic!) 
    remainingSeconds = period * 60  
    time.sleep(remainingSeconds)
    print "alarm n ", i
    print time.asctime()
    os.system(player + " " +  soundfile11 ) 


