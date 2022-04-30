#!/usr/bin/python 


import alsaaudio


m = alsaaudio.Mixer()

current_volume = m.getvolume() # Get the current Volume
# This number is a long integer in a list. So to make it into a usable number, we can do int(vol[0])
current_volume = int(current_volume[0])
print 'current volume:', current_volume, '%'


m.setvolume(55) # Set the volume to 70%.

current_volume = m.getvolume() # Get the current Volume
# This number is a long integer in a list. So to make it into a usable number, we can do int(vol[0])
current_volume = int(current_volume[0])
print 'current volume:', current_volume, '%'


# If the line m = alsaaudio.Mixer() throws an error, then try:
# m = alsaaudio.Mixer('PCM')
# this might happen because the Pi uses PCM rather than a Master channel.



