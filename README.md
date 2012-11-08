Pushover Pipe for Python  
========================  

Command line tool for sending messages using [Pushover](http://pushover.net).  
Current Version: 0.01  

Requires Python3, but could be converted down to python2 easily.  

Installation:
------------

```bash
$> cp pushpipe /usr/local/bin/
```

Configuration:
--------------

If you run `pushpipe` without any setup it will ask for your API token and your user key.  
The user key is on your [user page](http://pushover.net).  
You must create an application with Pushover in order to send messages.  
See [Pushover Apps](https://pushover.net/apps) for more information.  

Examples:
---------

The simplest example would be to let you know when something finishes on your computer.
`$> make ; make install ; pushpipe --title "make" --message "Done compiling."`

You could also use it to let you know if something breaks.
`$> some script ; if [ "$?" -ne "0" ]; then pushpipe -m "Oops, you bwoke it." ; fi`

Or add to cron, or whatever. Use your imagination!
  
RTFM:
-----
```
usage: pushpipe [-h] [-u USER] [-t TOKEN] [-m WORDS] [-d DEV] [--title TITLE]  
                [--url URL] [--urltitle UTITLE] [-p PRIORITY]  
  
Pushover Pipe: Sends mesages to Pushover device from the command line.  
Example: `make ; sudo make install ; pushpipe --title "make" -m "All done  
compiling."`  
  
optional arguments:   
  -h, --help            	show this help message and exit  
  -u USER, --user USER  	User key instead of reading from settings. Requires --token.  
  -t TOKEN, --token TOKEN 	Token key instead of reading from settings. Requires --user.  
  -m WORDS, --message WORDS	 Message to send. Default is "Pushover Pipe"  
  -d DEV, --device DEV  	Device name to receive message. Default sends to all devices.  
  --title TITLE         	Title or application name. Default is Pushover_Pipe  
  --url URL             	Optional URL to accompany your message.  
  --urltitle UTITLE     	Title to go with your URL.  
  -p PRIORITY, --priority	Priority level. "High" ignores quiet hours and "Low" sends as quiet. Default is normal.  
```
