# twitch-chat-logger

Simple tool for logging chat data from a Twitch stream.

Listens for messages on the Twitch chat's IRC and logs these messages to a file. Once the logging session is ended (or when the user runs the parse_log.py script) it breaks the messages into parts and stores it as a CSV file.

To use, navigate to config.py and supply your 'nickname' (Twitch username), 'token' (OAuth Key from [here](https://twitchapps.com/tmi/)), and 'channel' (name of Twitch channel you want to connect to, prefixed with a "#"). Then run main.py.
