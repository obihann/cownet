Cownet
======

> I wanted to view my up to date network usage in a easy to read and friendly way. So I built a tool that pulls the data in from [netstat](http://linux.die.net/man/8/netstat), and displays a cleaned up output in [Cowsay](http://linux.die.net/man/1/cowsay). 

```

                              _
  ___ _____      ___ __   ___| |_
 / __/ _ \ \ /\ / / '_ \ / _ \ __|
| (_| (_) \ V  V /| | | |  __/ |_
 \___\___/ \_/\_/ |_| |_|\___|\__|

 ___________________________________
< Received 173.9 MB / Sent 337.7 MB >
 -----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```

##Instructions
> cownet.py

By default this refreshes every 30 seconds while measuring data from the eth1 interface


> cownet.py -d 5

Specify a delay of your choice


> cownet.py -i wlan0

Specify a interface of your choice


> cownet.py -h

Get help
