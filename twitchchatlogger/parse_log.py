import pandas as pd
from datetime import datetime
import re

def get_chat_dataframe(file):
    data = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n\n\n')

        for line in lines:
            try:
                time_logged = line.split('—')[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                username_message = line.split('—')[1:]
                username_message = '—'.join(username_message).strip()

                username, channel, message = re.search(
                        ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
                ).groups()

                data.append({
                    'timestamp': time_logged,
                    'channel': channel,
                    'username': username,
                    'message': message
                })

            except Exception:
                pass

    return pd.DataFrame().from_records(data)

def main():
    df = get_chat_dataframe("output\chat.log")
    df.to_csv("output\parsedLog.csv")

if __name__ == "__main__":
    main()