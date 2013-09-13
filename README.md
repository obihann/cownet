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

##Table of Contents
* [Download](#download)
* [Setup](#setup)
* [Instructions](#instructions)
* [License](#license)

##Setup
This is a Python tool that is presently only built for OSX. To render the output as seen above we use [figlet](http://www.figlet.org/) and [cowsay](http://en.wikipedia.org/wiki/Cowsay).
To get started you will need [homebrew](http://brew.sh/) to manage packages such as Python, figlet, and cowsay. To install please run the following command:
```
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

Once homebrew is installed (or if you already have it) you can run the following command:
```
brew install cownet
```

##Instructions
> cownet

By default this refreshes every 30 seconds while measuring data from the eth1 interface


> cownet -d 5

Specify a delay of your choice


> cownet -i wlan0

Specify a interface of your choice


> cownet -h

Get help

##License
This tool is protected by the [GNU General Public License v2](http://www.gnu.org/licenses/gpl-2.0.html).

Copyright [Jeffrey Hann](http://jeffreyhann.ca/) 2013
