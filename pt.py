#!/usr/bin/env python3
import os
import configparser
import argparse
import requests

#  ____            _   _____         _
# |  _ \ _   _ ___| |_|_   _|____  _| |_
# | |_) | | | / __| '_ \| |/ _ \ \/ / __|
# |  __/| |_| \__ \ | | | |  __/>  <| |_
# |_|    \__,_|___/_| |_|_|\___/_/\_\\__|
#
# Command line tool for [Pushover](http://pushover.net)
#
pushtext_version = "1.0.4"
pushtext_homepage = "https://gitlab.com/robotmachine/PushText"
pushtext_author = "Brian A. Carter"
pushtext_email = "robotmachine@pm.me"
pushtext_copyright = "2013-2022"
pushtext_configfile = os.path.expanduser("~/.ptrc")


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.version:
        quit(
            f"\nPushtext v.{pushtext_version}\n \
            (c){pushtext_copyright} {pushtext_author}\n \
            {pushtext_email}\nProject Home: {pushtext_homepage}"
        )

    body = {}
    if args.user_key is not None:
        if length_tool("user_key", args.user_key):
            body["user"] = args.user_key
    else:
        body["user"] = read_config("user_key")

    if args.api_token is not None:
        if length_tool("api_token", args.api_token):
            body["token"] = str(args.api_token)
    else:
        body["token"] = read_config("api_token")

    if args.priority is None:
        body["priority"] = 0
    elif args.priority.lower() in ["high", "hi", "h"]:
        body["priority"] = 1
    elif args.priority.lower() in ["low", "lo", "l"]:
        body["priority"] = -1
    else:
        body["priority"] = 0

    if args.device is not None:
        if length_tool("device", args.device):
            body["device"] = str(args.device)

    if length_tool("title", args.title):
        body["title"] = str(args.title)

    if length_tool("message", args.message):
        body["message"] = str(args.message)

    if args.URL is not None:
        if length_tool("url", str(args.URL)):
            body["url"] = str(args.URL)
        if args.URL_title is not None:
            if length_tool("url_title", str(args.URL_title)):
                body["url_title"] = str(args.URL_title)
        else:
            body["url_title"] = "PushText URL"

    send_message(body)


def send_message(body):
    base_url = "api.pushover.net"
    send_url = f"https://{base_url}/1/messages.json"
    try:
        request = requests.post(send_url, body)
        if int(str(request.status_code)[:1]) != 2:
            quit(f"{request.status_code}: {request.reason}\n{request.content}")
        else:
            return True
    except requests.exceptions.ConnectionError as e:
        quit(e)


def read_config(needful):
    config = configparser.ConfigParser()
    if not os.path.exists(pushtext_configfile):
        set_config()
    if needful == "user_key":
        config.read(pushtext_configfile)
        return config["PushText"]["user"]
    elif needful == "api_token":
        config.read(pushtext_configfile)
        return config["PushText"]["token"]
    else:
        quit("How did you even do that?")


def set_config():
    print("\nHint: Create an app here -> https://pushover.net/apps\n")
    api_token = query_tool("api_token", "Application Token: ")

    print("\nHint: User Key will be shown after logging in -> https://pushover.net\n")
    user_key = query_tool("user_key", "User Key: ")

    config = configparser.ConfigParser()
    config["PushText"] = {"token": api_token, "user": user_key}
    with open(pushtext_configfile, "w") as configfile:
        config.write(configfile)
    quit("\nSettings saved!\n")


def query_tool(key, prompt):
    try:
        user_input = input(prompt)
        if length_tool(key, user_input):
            return user_input
    except KeyboardInterrupt:
        quit("\n\nUser Exited")
    except Exception as e:
        quit(e)


def length_tool(key, value):
    lengths = {
        "message": 1024,
        "title": 250,
        "url": 512,
        "url_title": 100,
        "api_token": 30,
        "user_key": 30,
        "device": 25,
    }
    if value == "":
        quit(f"{key.title()} cannot be empty")
    elif value.__len__() >= lengths[key.lower()]:
        quit(f"{key.title()} must under {lengths[key.lower()]} characters")
    else:
        return True


def setup_argparse():
    parser = argparse.ArgumentParser(
        description="PushText: Command line tool for http://pushover.net", prog="pt"
    )
    parser.add_argument(
        "-u",
        "--user_key",
        action="store",
        dest="user_key",
        default=None,
        help="User key instead of reading from settings.",
    )
    parser.add_argument(
        "-t",
        "--api_token",
        action="store",
        dest="api_token",
        default=None,
        help="Token key instead of reading from settings.",
    )
    parser.add_argument(
        "-p",
        "--priority",
        action="store",
        dest="priority",
        default=None,
        help="Set priority of high or low. Default is normal.",
    )
    parser.add_argument(
        "-m",
        "--message",
        action="store",
        dest="message",
        default="PushText",
        help='Message to send. Default is "PushText"',
    )
    parser.add_argument(
        "-d",
        "--device",
        action="store",
        dest="device",
        default=None,
        help="Device name to receive message. Default sends to all devices.",
    )
    parser.add_argument(
        "--title",
        action="store",
        dest="title",
        default="PushText",
        help="Title or application name. Default is PushText",
    )
    parser.add_argument(
        "--url",
        action="store",
        dest="URL",
        default=None,
        help="Optional URL to accompany your message.",
    )
    parser.add_argument(
        "--urltitle",
        action="store",
        dest="URL_title",
        default="None",
        help="Title to go with your URL.",
    )
    parser.add_argument(
        "-v", "--version", action="store_true", dest="version", help="Print version."
    )
    return parser


if __name__ == "__main__":
    main()
