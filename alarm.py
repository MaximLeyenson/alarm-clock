#!/usr/bin/python3
# GPL license, Maxim Leyenson

#  alarm will sound in h hours m minutes
# and then every N minutes

# usage: see below, in the try/except statement

# dependencies:  python3-alsaaudio

import os     # i need to know alarm.py localtion
import time   # see help(time)
import sys
import getopt  # parsing command line options
import alsaaudio # getting and setting audio volume
                 # python3-alsaaudio in not in Mint yet [2020];
                 # installation via pip3:
                    # apt install python3-dev libasound2-dev 
                    # pip3 install pyalsaaudio

# ----------- parsing command line options via getopt-----------

options, args =  getopt.gnu_getopt(sys.argv[1:], 
        't:v:p:m:', 'times=volume=period=message')
#      -t 5    sound 5 times
#      -v 80   volume in percents
#      -m "Morning alarm"  -- message to print;
#      8 30    2 arguments, 8 hours and 30 minutes

# print "options: ", options
# print "args: ",    args

# ----- setting  default values ----------------

period = 30    # every 30 minutes
# period = 40    # every 40 minutes
# period = 0.5 # for testing 
number_of_alarms = 8
# volume = '85'               #should be a string
volume = 85                   #should be an interger for the alsa python module
message = ''                # default message is empty

# air plugs: 80 may be not enough
# weizmann: volume = 76;
# 70 < volume < 85
# in a library: 10 <= volume <= 20

#------- parsing options ------------

for option, value in options:
#  print '(option,value) = ', option, value
   if option in ('-t', '--times'):
      print('[ number_of_alarms = ', value, ' ]')
      number_of_alarms = int(value)
   if option in ('-v', '--volume'):
      print('[ alarm volume=', value, '% ]')
      volume = int(value)       # should be integer for the python alsa module
   if option in ('-p', '--period'):
      print('[ period = ', value, ' minutes ]')
      period = int(value)
   if option in ('-m', '--message'):
      print('[ message = ', value, ' ]')
      message = value


try: 
   alarmHours   = int(args[0]) 
   alarmMinutes = int(args[1])
except: 
   print('Usage: %s \ ' % sys.argv[0])
   print('  [-t | --times  number_of_alarms] \ ')
   print('  [-v | --volume volume] \ ')
   print('  [-p | --period period] \ ')
   print('  [-m | --message message] \ ')
   print(' hours-till-first-alarm minutes-till-first-alarm  \ ')
   sys.exit(1)
#--                         sys.argv[0] = "0'th argument" = filename

# print "[ number_of_alarms = ",  number_of_alarms, ' ]'
#  already printed this
print("[ volume = ", volume, '% ]')
print("[ period = ", period, ' minutes ]')

night_length = (alarmHours * 60  + alarmMinutes) * 60  

print("[ MAKE ME PUBLIC ON GITLAB ] ")
print("[ MAKE ME PUBLIC ON GITLAB ] ")
print("[ MAKE ME PUBLIC ON GITLAB ] ")
print("[ MAKE ME PUBLIC ON GITLAB ] ")

print("[ ---------------------------------------------------- ] ")
print("[ ", time.asctime(), " ]")    # time in 'Wed Aug 12 20:23:04 2009' format
print("[ ALARM WILL SOUND IN", alarmHours, "HOURS", alarmMinutes, "MINUTES ]")
print("  at ", time.ctime(time.time() + night_length )  )
print("  and then every", period, "minutes ]")
# print "[ need to CHANGE to accomodate PLAYNG TIME]"
print("[ ---------------------------------------------------- ] ")

# ---------- location of the local sounds library --

# --------------------- getting program path ---------

program_path_and_name = os.path.realpath(__file__)
#   "Return the canonical path of the specified filename, eliminating
#    any symbolic links "
#   rerurns 'path/alarm.py'

program_path = os.path.dirname(program_path_and_name)
#  strip the filename

   # print("[ program path: ]" )
   # print(program_path )

sounds_path = program_path + "/sounds/"

# print("[sounds location:]")
# print("> " + sounds_path )


# --------------------------------------------------------------------
# ----------- choosing sound file, & setting filename -----------
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# = local paths =
# --------------------------------------------------------------------

cuckoo_local=sounds_path + "28113__HerbertBoland__Kukuklok_1_slag.ogg"

mechanical_alarm_clock1_local= sounds_path + \
    "78562.joedeshon.alarm-clock-ringing-01.3seconds.q2.ogg"

owl_scream = sounds_path + "owl.mono.64kbps.ogg"

office_phone_ring1 = sounds_path + \
    "329781__visualasylum__office-phone-ring.q2.ogg"


office_phone_ring2 = sounds_path + \
     "77723__cs272__phone-ring.q2.ogg"
# Phone ring, by Chris Shamburg 

# --------------------------------------------------------------------
# = remote paths =
# --------------------------------------------------------------------

skype_call="/library/sounds/skype/CallRingingIn.q4.ogg"

moonlight_tomisc="/library/music/beethhoven/moonlight.dubravka-tomsic/01-piano-sonata-no.14-in-c-sharp-minor-op.27.2-moonlight.adagio-sostenuto.mp3"
# also, need to convert to OGG

bwv1044="/library/music/bwv1044/bwv1044.trevor-pinnock.q5.ogg"

# = end of: paths =


# --------------------------------------------------------------------
# --------------------- choosing the sound to play -------------------------
# --------------------------------------------------------------------

print('[ --------------------- ] ' )
print('   please choose the sound file to play: \n ' )

# print('    0: skype_call ' )
#              no public license; not using 

print('    1: Cuckoo' )  
#            by HerbertBoland; see the 'attributions' file

print('    2: Mechanical alarm clock' )
#            by joedeshon; file 78562.joedeshon.alarm-clock-ringing-01;
#            see the 'attributions' file

print('    3: Owl scream. Scary!' )
# By Syed Usama

print('    4: Office phone ring')
#  by VisualAsylum

print('    5: Phone ring \n ')
# by Chris Shamburg


print('   ----------------------  ')
print('   = long compositions = ')
print('   ----------------------  ')
print('   TO LINK / Remote / On Toucan: ')

print('   8: Moonlight, 1st movement, Dubravka Tomsic; on toucan library ' )
            # license: on YouTube and Yandex Music; see the license file here

print('   9: bwv1044, on toucan library ')
              
# reading alarm number
n = sys.stdin.readline()
# print(' [chosen soundfile number = ', n, ' ]')
n = int( n )
# sometimes produces error 'IOError: [Errno 11] Resource temporarily unavailable'


if  n == 0:              
   print('chosen: 0: skype call')
   soundfile = skype_call 
   times_to_play = 2
elif n == 1:
   print('chosen: cuckoo')
   soundfile = cuckoo_local
   times_to_play = 2
elif n == 2:
   print('chosen: mechanical alarm clock')
   soundfile = mechanical_alarm_clock1_local
   times_to_play = 8
elif n == 3:
   print('chosen: Owl scream! scary. ')
   soundfile = owl_scream
   times_to_play = 1    
   #       owl is so scary! playing this sound once is enough!
elif n == 4:
   # print(' office_phone_ring1 :  329781__visualasylum__office-phone-ring   ')
   print(' Office phone ring')
   # by VisualAsylum 
   soundfile = office_phone_ring1   
   times_to_play = 1    
elif n == 5:
   print(' Phone ring, by Chris Shamburg'  )
   # by Chris Shamburg (cs272)
   soundfile = office_phone_ring2   
   times_to_play = 1    
elif n == 6:
   print('   Moonlight, 1st movement; Dubravka Tomsic' )
   soundfile =  moonlight_tomisc
   times_to_play = 1    
elif n == 7:
   # 9: bwv1044
   print(' Bach, bwv1044  ' )
   soundfile =  bwv1044
   times_to_play = 1    
else:                  
   print('choosing cuckoo')
   soundfile = cuckoo
   times_to_play = 2

soundfile_test = soundfile 

# print("        soundfile for testing:  ", soundfile_test )
# print("        main soundfile:  ", soundfile)

print('[ --------------------------------------------- ] ' )

# --------------------- Choosing ogg audio player ---------

Player = "mpv" 

# Player = "mplayer -volume 100 -ao alsa -really-quiet" 
# '-ao alsa' is necessary, since pulse is bad on HP

# Player = "ogg123 -d alsa"

print(' [Using audio player: ', Player , ' ] ')
print(' [You may want to change it for something else if you like] ')

# --------------------------------------------------------------------
# -- function: setting sound volume via alsaaudio module

def set_sound_volume_via_alsaaudio(p): #  p is in percent of maximum (0-100) 
   print('[setting volume ', p, '% via alsaaudio volume ]')
   # using Master channel (not PCM)
   ## print '[checking the type of volume variable p : ', type(p), ' ] '
   # 
   p = int(p)  # in case it is a string
   p = min(p, 100)   
   # since get_sound_volume could return number higher that 100 on Mint!
   #
   m = alsaaudio.Mixer()
   m.setvolume(p) # Set the volume to p %


# --------------------------------------------------------------------
# -- function: checking sound volume via alsaaudio module

def get_sound_volume_via_alsaaudio(): 
   #
   m = alsaaudio.Mixer()
   #
   current_volume = m.getvolume() # Get the current Volume
   # This number is a long integer in a list. to make it into a usable number, we can do int(vol[0])
   current_volume = int(current_volume[0])
   print("current sound volume: ", current_volume, "%")
   return current_volume
   # can return number higher than 100% in Mint! dealing with it elsewhere

# --------------------------------------------------------------------
# -- main code --

# -- Step 1: performing sound test --


print("[checking that sounds are audible...]")
current_volume=get_sound_volume_via_alsaaudio() 
set_sound_volume_via_alsaaudio(volume) # the volume of alarm
os.system(Player + " " +  soundfile_test )   
# now need to restore original sound voulme for programs/music/etc in other shells
# set_sound_volume(70) 
set_sound_volume_via_alsaaudio(current_volume) 

# -- declaring night; sleeping for 'night_length' seconds
time.sleep(night_length)

# -- Step 2 --
# now, sounds the first alarm; and then the next ones
# each 'period' seconds

for i in range(1, number_of_alarms + 1):    # cycle over 1 - (n-1) (sic!)
    # now: alarm # i; explaining this:
    print("[ alarm # ", i, '/', number_of_alarms, ' ]')
    print("[", time.asctime(), "]")
    print("[ Message for this alarm: ]")
    print("[", message, "]")
    # first, need to keep current sound vclume, to return to it later: 
    current_volume=get_sound_volume_via_alsaaudio() 
    # -- alarm sounds --
    # setting sound volume to one requested by user for alarm:
    set_sound_volume_via_alsaaudio(volume) 
    # playing the soundfile a given number of times
    # (i.e., i might want a short sound played N times in a row
    for t in range(1, times_to_play + 1):    # cycle 1- (n-1) (sic!!)
       print(' ( sound #', t, '/',  times_to_play, ')')
       os.system(Player + " " + soundfile)
    # now need to restore original sound voulme for programs/music/etc in other shells
    set_sound_volume_via_alsaaudio(current_volume) 
    # -- sleeping again --
    if i < number_of_alarms: 
       print("[now sleeping ", period , "minutes]")
       time.sleep(period * 60)
       print('------------------------------------------' )

