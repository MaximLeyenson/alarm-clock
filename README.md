# alarm-clock

A simple alarm clock and/or reminder to do something. Better documentation will be
written later.

**Synopsis**

**Usage**

Simplest usage:

```bash
$ alarm.py 8 20
```
play alarm sound in 8 hours 20 minutes.

The alarm clock prompts to choose between several available alarm sounds. 
A cuckoo striking clock, a mechanical alarm clock, a real owl scream, and a few
more sounds are currently available:

```
   please choose the sound file to play: 
 
    1: Cuckoo
    2: Mechanical alarm clock
    3: Owl scream. Scary!
    4: Office phone ring
    5: Phone ring 
```

Another example:

```bash
$ alarm.py -v 60 -p 15 8 0
```

play an alarm at volume 60% of the maximum your systems allows, and
repeat every 15 minutes until interrupted:

```
[ alarm volume= 60 % ]
[ period =  15  minutes ]
[ volume =  60 % ]
```

More options:

```
alarm.py  
     [-t | --times  number_of_alarms] 
     [-v | --volume volume] 
     [-p | --period period] 
     [-m | --message message] 
 hours-till-the-first-alarm minutes-till-the-first-alarm 
```

**Requirements**

   * python3-alsaaudio

   * mpv, or any OGG audio file player of your choice

**Installation for one user**
```bash
   $ mkdir -pv ~/bin
   $ cd ~/bin/
   $ git clone https://gitlab.com/maxim.leyenson/alarm-clock
```

and then add the lines

   ```bash
   PATH=$PATH:$HOME/bin/alarm-clock
   export PATH
   ```
to your .bashrc file.


**System-wide installation**

```bash
   $ sudo mkdir -pv /opt/alarm-clock
   $ cd /opt/alarm-clock
   $ sudo git clone https://gitlab.com/maxim.leyenson/alarm-clock
```

and then add the lines

   ```bash
        PATH=$PATH:/opt/alarm-clock
        export PATH
   ```
to your .bashrc file.


**Attributions**

See in the sounds/ folder.

