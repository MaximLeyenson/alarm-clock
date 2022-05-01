# alarm-clock

A simple alarm clock and/or reminder. Documentation will be written later.

**Synopsis**

**Usage**

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


