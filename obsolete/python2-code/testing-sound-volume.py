#!/usr/bin/python 

import os
import sys
import commands

print "---- imported commands ---"

# getting current sound volume:

current_volume = commands.getoutput("amixer get Master | tr -d '[]' | grep \"Playback.*%\"  | head -n1 | awk '{print $5}' ")  

print "current sound volume: ", current_volume

