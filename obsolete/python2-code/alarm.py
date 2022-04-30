#!/usr/bin/python 

#  alarm will sound in h hours m minutes
# and then every 40 minutes

# usage: see below, in the try/except statement

# dependencies:  python-alsaaudio

import os  # i need this program localtion, f.e.
import time   # see help(time)
import sys
import getopt  # parsing command line options
import commands  # getting output of a command
import alsaaudio # getting and setting audio volume


# ----------- parsing command line options -----------

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
      print '[ number_of_alarms = ', value, ' ]'
      number_of_alarms = int(value)
   if option in ('-v', '--volume'):
      print '[ alarm volume=', value, '% ]'
      volume = int(value)       # should be integer for the python alsa module
   if option in ('-p', '--period'):
      print '[ period = ', value, ' minutes ]'
      period = int(value)
   if option in ('-m', '--message'):
      print '[ message = ', value, ' ]'
      message = value


try: 
   alarmHours   = int(args[0]) 
   alarmMinutes = int(args[1])
except: 
   print 'Usage: %s \ ' % sys.argv[0]
   print '  [-t | --times  number_of_alarms] \ '
   print '  [-v | --volume volume] \ '
   print '  [-p | --period period] \ '
   print '  [-m | --message message] \ '
   print ' hours-till-first-alarm minutes-till-first-alarm  \ '
   sys.exit(1)
#--                         sys.argv[0] = "0'th argument" = filename

# print "[ number_of_alarms = ",  number_of_alarms, ' ]'
#  already printed this
print "[ volume = ", volume, '% ]'
print "[ period = ", period, ' minutes ]'

night_length = (alarmHours * 60  + alarmMinutes) * 60  

print "[ ---------------------------------------------------- ] "
print "[ ", time.asctime(), " ]"    # time in 'Wed Aug 12 20:23:04 2009' format
print "[ ALARM WILL SOUND IN", alarmHours, "HOURS", alarmMinutes, "MINUTES ]"
print "  at ", time.ctime(time.time() + night_length )  
print "  and then every", period, "minutes ]"
# print "[ need to CHANGE to accomodate PLAYNG TIME]"
print "[ ---------------------------------------------------- ] "

# ---------- location of the local sounds library --

# --------------------- getting program path ---------
program_name = sys.argv[0]  # this is full path to the program: path/filename
# print program_name 

program_path = os.path.dirname(program_name)

sounds_path = program_path + "./sounds/"
print "[sounds location:]"
print "> " + sounds_path 

#------------------------ ---------------------------------------

# ----------- choosing sound file, & setting filename -----------

# todo: 
# asking about sound file to play
# !! asking whether to play once or twice

# = local paths =
cuckoo_local=sounds_path + "28113__HerbertBoland__Kukuklok_1_slag.ogg"


mechanical_alarm_clock1_local= sounds_path + \
    "78562.joedeshon.alarm-clock-ringing-01.3seconds.q2.ogg"

owl_scream = sounds_path + "owl.mono.64kbps.ogg"


# = remote paths =

skype_call="/library/sounds/skype/CallRingingIn.q4.ogg"


moonlight_tomisc="/library/music/beethhoven/moonlight.dubravka-tomsic/01-piano-sonata-no.14-in-c-sharp-minor-op.27.2-moonlight.adagio-sostenuto.mp3"

bwv1044="/library/music/bwv1044/bwv1044.trevor-pinnock.q5.ogg"

# = end of: paths =


# --------------------- choosing sound to play -------------------------

print '[ --------------------- ] ' 
print '   please choose sound file to play' 
print '    1: skype_call ' 
print '    2: moonlight_tomisc' 

print '    3: cuckoo, local sound library' 
print '    4: mechanical alarm clock, local sound library' 
print '    5: Owl scream! Scary. local sound library' 

n = int( sys.stdin.readline() )
# sometimes produces error 'IOError: [Errno 11] Resource temporarily # unavailable'

# print ' [ soundfile number = ', n, ' ] '

if  n == 1:              
   print 'chosen: 1: skype call'
   soundfile = skype_call 
   times_to_play = 2
elif n == 3:
   print 'chosen: 3: cuckoo'
   soundfile = cuckoo_local
   times_to_play = 2
elif n == 4:
   print 'chosen: 4: mechanical alarm clock'
   soundfile = mechanical_alarm_clock1_local
   times_to_play = 8
elif n == 5:
   print 'chosen: 5: Owl scream! scary. '
   soundfile = owl_scream
   times_to_play = 1    
   #       owl is so scary! playing this sound once is enough!
else:                  
   print 'choosing cuckoo'
   soundfile = cuckoo
   times_to_play = 2

soundfile_test = soundfile 

# soundfile_test = skype_call                # cocoo   

# print "   testing soundfile:  ", soundfile_test 
print "        soundfile:  ", soundfile

print '[ --------------------------------------------- ] ' 

# --------------------- getting program path ---------

#program_name = sys.argv[0]  # this is full path to the program: path/filename
# print "-- program name: ", program_name 

#program_path = os.path.dirname(program_name)
# print "   program path: ", program_path 

# sounds_path = program_path + "/sounds"
# print "   sounds path: ", sounds_path 


# -- player 

# Player = "mplayer -volume 100 -ao alsa -really-quiet " # do not forget the space in the end!
# alsa is necessary, since pulse is very bad on HP

Player = "ogg123 -d alsa "

# ----------------------------------------------------------------
# -- function: setting sound volume via command line/amixer

# def set_sound_volume(p): #  p is in percent of maximum (0-100) 
#    print '[setting volume ', p, '% via amixer ]'
#    # example: $ amixer -q sset Master,0    85%,85% 
#    # first, Master:
#    cmd='amixer -q   sset Master,0 ' + str(p) + '%,'+ str(p)  + '%'
#    print '[', cmd, ']'
#    os.system(cmd)
# 
#    # second, PCM:
#    #   cmd='amixer -q sset PCM ' + str(p) + '%,'+ volume + '%'
#    # print '[', cmd, ']'
#    # os.system(cmd)

# --------------------------------------------------------------------
# -- function: checking sound volume via command line/amixer

# def get_sound_volume(): #  p is in percent of maximum (0-100) 
#    # cmd="amixer get Master | tr -d '[]' | grep \"Playback.*%\"  | head -n1 | awk '{print $5}' "   
#    # here:  'tr' -- delete characters
#    # i would rather try:
#    cmd=" amixer get Master | grep Playback.*% | head -1 | awk '{print $4}' | tr -d '[]%' "
# 
#    #  me: $ amixer get Master | grep Playback.*% | head -1 | awk '{print $5}' | tr -d '[]%'
#    #  after 'grep', it keeps lines with  Placyback ... 70%
#    # then it keeps just one line, which looks like
#    #       Front Left: Playback 45876 [70%] [on]
#    # then it takes word # 5, and then removes xtra characters
# 
#    # However, on Mint/Findling, it gives  '-25.50dB' instead of value in percent...
#    #  Step 1:    $ amixer get Master | grep Playback.*% | head -1 
#    #   Gives    'Mono: Playback 53 [61%] [-25.50dB] [on]'
#    #  Step 2:   $ amixer get Master | grep Playback.*% | head -1 | awk '{print $5}'    
#    #   Gives  '[-25.50dB]'
#    #   and what I need instead is  awk '{print $4}'...
#    # how to fix???
# 
# 
#    current_volume = commands.getoutput(cmd)
#    print "current sound volume: ", current_volume, "%"
#    return current_volume
# 
# 
# # usage: current_volume=get_sound_volume() 

# --------------------------------------------------------------------
# -- function: setting sound volume via alsaaudio module

def set_sound_volume_via_alsaaudio(p): #  p is in percent of maximum (0-100) 
   print '[setting volume ', p, '% via alsaaudio volume ]'
   # using Master channel (not PCM)
   ## print '[checking the type of volume variable p : ', type(p), ' ] '

   p = int(p)  # just in case it is a string
   ## print '[checking the type of volume variable p : ', type(p), ' ] '

   m = alsaaudio.Mixer()
   m.setvolume(p) # Set the volume to p %


# --------------------------------------------------------------------
# -- function: checking sound volume via alsaaudio module

def get_sound_volume_via_alsaaudio(): 

   m = alsaaudio.Mixer()

   current_volume = m.getvolume() # Get the current Volume
   # This number is a long integer in a list. So to make it into a usable number, we can do int(vol[0])
   current_volume = int(current_volume[0])
   print "current sound volume: ", current_volume, "%"
   return current_volume

# --------------------------------------------------------------------
# -- main code --

# -- Step 1: performing sound test --


print "[checking that sounds are audible...]"
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
    print "[ alarm # ", i, '/', number_of_alarms, ' ]'
    print "[", time.asctime(), "]"
    print "[ Message for this alarm: ]"
    print "[", message, "]"
    # first, need to keep current sound vclume, to return to it later: 
    current_volume=get_sound_volume_via_alsaaudio() 
    # -- alarm sounds --
    # setting sound volume to one requested by user for alarm:
    set_sound_volume_via_alsaaudio(volume) 
    # playing the soundfile a given number of times
    # (i.e., i might want a short sound played N times in a row
    for t in range(1, times_to_play + 1):    # cycle 1- (n-1) (sic!!)
       print ' ( sound #', t, '/',  times_to_play, ')'
       os.system(Player + " " + soundfile)
    # now need to restore original sound voulme for programs/music/etc in other shells
    set_sound_volume_via_alsaaudio(current_volume) 
    # -- sleeping again --
    if i < number_of_alarms: 
       print "[now sleeping ", period , "minutes]"
       time.sleep(period * 60)
       print '------------------------------------------' 

