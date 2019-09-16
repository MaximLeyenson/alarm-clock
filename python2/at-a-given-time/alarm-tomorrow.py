#!/usr/bin/python 

import os
import time
import sys

# -- getting the arguments
try: alarmHours   = int(sys.argv[1]); \
     alarmMinutes = int(sys.argv[2])
except: print 'Usage: %s hours minutes' % sys.argv[0]; sys.exit(1)
#--  sys.argv[0] = filename

# alarmHours = 8
# alarmMinutes = 30

print "[checking that sounds are audible...]"
os.system("ogg123 sounds/28113__HerbertBoland__Kukuklok_1_slag.ogg")

Time = time.localtime()
print time.asctime()

currentHours   = Time[3]
currentMinutes = Time[4]
currentSeconds = Time[5]

secondsUntilMidnight = (24 - currentHours) * 60 * 60 - currentMinutes * 60 - currentSeconds
remainingSeconds = secondsUntilMidnight + alarmHours * 60 * 60 + alarmMinutes * 60

print "[secondsUntilMidnight =", secondsUntilMidnight, "]"

print "[minutes until midnight =", secondsUntilMidnight / 60 , "]"

print "[now sleeping ", remainingSeconds, "seconds]"
time.sleep(remainingSeconds)
os.system("ogg123 sounds/28114__HerbertBoland__Kukuklok_11_slag.ogg")

