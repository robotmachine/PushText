# PushText
### Command line tool for [Pushover](http://pushover.net)  
#### Installation:
1. Download [the archive](https://github.com/robotmachine/PushText/tarball/master)  
2. Run `chmod +x pt`
3. Move `pt` to `/usr/local/bin` or somewhere else in `$PATH`

#### Configuration:

If you run `pt` without any setup it will ask for your API token and your user key.  
The user key is on your [user page](http://pushover.net).  
You must create an application with Pushover in order to send messages.  
See [Pushover Apps](https://pushover.net/apps) for more information.  

#### Examples:

The simplest example would be to let you know when something finishes on your computer.
`$> make ; make install ; pt --title "make" --message "Done compiling."`  
The above will result in this on your phone:  
![pt example](http://mlkshk.com/r/L2TK.jpg "pt example")

You could also use it to let you know if something breaks.
`$> some script ; if [ "$?" -ne "0" ]; then pt -m "Oops, you bwoke it." ; fi`

Send your [Todo.txt](https://github.com/ginatrapani/todo.txt-cli) list daily:
```bash
$> crontab -l | grep pt
30 10 * * * /usr/local/bin/pt --title "Todo" -m "`/usr/local/bin/todo ls`" -d iphone
```
  
The possibilities are endless! (As long as the possibilities only include sending messages to your phone.)  

RTFM:
-----
```
usage: pt [-h] [-u USER] [-t TOKEN] [-m WORDS] [-d DEV] [--title TITLE]  
                [--url URL] [--urltitle UTITLE] [-p PRIORITY]  
  
PushText: Command line tool for http://pushover.net
Example: `make ; sudo make install ; pt --title "make" -m "All done  
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
