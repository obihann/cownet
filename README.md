Cownet
======

> I wanted to view my up to date network usage in a easy to read and friendly way. So I built a tool that pulls the data in from [netstat](http://linux.die.net/man/8/netstat), and displays a cleaned up output in [Cowsay](http://linux.die.net/man/1/cowsay). 

```

 _______________________________
< Received 1.6 GB / Sent 1.8 GB >
 -------------------------------
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
