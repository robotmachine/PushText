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
![pt example](http://mltshp.com/r/L2TK.jpg "pt example")

You could also use it to let you know if something breaks.
`$> some script ; if [ "$?" -ne "0" ]; then pt -m "Oops, you bwoke it." ; fi`

Send your [Todo.txt](https://github.com/ginatrapani/todo.txt-cli) list daily:
```bash
$> crontab -l | grep pt
30 10 * * * /usr/local/bin/pt --title "Todo" -m "`/usr/local/bin/todo ls`" -d iphone
```
  
The possibilities are endless! (As long as the possibilities only include sending messages to your phone.)  

#### Manual:  
```
usage: pt [-h] [-u USER_KEY] [-t TOKEN_KEY] [-p PRIORITY] [-m MESSAGE]
          [-d DEVICE] [--title TITLE] [--url URL] [--urltitle URL_TITLE] [-v]

PushText: Command line tool for http://pushover.net

optional arguments:
  -h, --help            show this help message and exit
  -u USER_KEY, --user-key USER_KEY
                        User key instead of reading from settings.
  -t TOKEN_KEY, --token-key TOKEN_KEY
                        Token key instead of reading from settings.
  -p PRIORITY, --priority PRIORITY
                        Set priority of high or low. Default is normal.
  -m MESSAGE, --message MESSAGE
                        Message to send. Default is "PushText"
  -d DEVICE, --device DEVICE
                        Device name to receive message. Default sends to all
                        devices.
  --title TITLE         Title or application name. Default is PushText
  --url URL             Optional URL to accompany your message.
  --urltitle URL_TITLE  Title to go with your URL.
  -v, --version         Print version.
```
