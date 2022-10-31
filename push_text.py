#!/usr/bin/env python3
import os
import json
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
pushtext_version = "1.0.5"
pushtext_homepage = "https://gitlab.com/robotmachine/PushText"
pushtext_author = "Bee Carter"
pushtext_email = "robotmachine@pm.me"
pushtext_copyright = "2013-2022"
pushtext_configfile = os.path.expanduser("~/.config/pushtext/settings.json")


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.version:
        print(
            f"""\n
        Pushtext v.{pushtext_version}
        (c){pushtext_copyright} {pushtext_author}
        {pushtext_email}\n
        Project Home: {pushtext_homepage}\n
        """
        )
        quit()

    body = {}
    if args.user_key is not None:
        if length_chk("user_key", args.user_key):
            body["user"] = args.user_key
    else:
        body["user"] = read_config("user_key")

    if args.api_token is not None:
        if length_chk("api_token", args.api_token):
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
        if length_chk("device", args.device):
            body["device"] = str(args.device)

    if length_chk("title", args.title):
        body["title"] = str(args.title)

    if length_chk("message", args.message):
        body["message"] = str(args.message)

    if args.URL is not None:
        if length_chk("url", str(args.URL)):
            body["url"] = str(args.URL)
        if args.URL_title is not None:
            if length_chk("url_title", str(args.URL_title)):
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
    if not os.path.exists(pushtext_configfile):
        set_config()
    else:
        with open(pushtext_configfile, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
    try:
        return config[needful]
    except KeyError:
        set_config()


def set_config():
    user_config = {}

    print("\nHint: Create an app here -> https://pushover.net/apps\n")
    user_config["api_token"] = get_query("api_token", "Application Token: ")

    print("\nHint: User Key will be shown after logging in -> https://pushover.net\n")
    user_config["user_key"] = get_query("user_key", "User Key: ")

    with open(pushtext_configfile, "w") as config_file:
        json.dump(user_config, config_file, indent=4, sort_keys=True)

    print("\nSettings saved!\n")
    quit()


def get_query(key, prompt):
    try:
        user_input = input(prompt)
        if length_chk(key, user_input):
            return user_input
    except KeyboardInterrupt:
        quit("\n\nUser Exited")
    except Exception as e:
        quit(e)


def length_chk(key, value):
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
    elif value.__len__() > lengths[key.lower()]:
        quit(f"{key.title()} must under {lengths[key.lower()]} characters")
    else:
        return True


def setup_argparse():
    parser = argparse.ArgumentParser(
        description="PushText: Command line tool for http://pushover.net", prog="push_text.py"
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
