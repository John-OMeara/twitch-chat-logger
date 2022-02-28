import socket
import logging
import pandas as pd
import twitchchatlogger.config as config
import twitchchatlogger.parse_log as parser

sock = socket.socket()

def main():
    logging.basicConfig(level = logging.DEBUG,
                        format = '%(asctime)s — %(message)s',
                        datefmt = '%Y-%m-%d_%H:%M:%S',
                        handlers = [logging.FileHandler(
                            filename = 'twitchchatlogger\output\chat.log', 
                            encoding ='utf-8')])

    sock.connect((config.server, config.port))
    sock.send(f"PASS {config.token}\n".encode('utf-8'))
    sock.send(f"NICK {config.nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {config.channel}\n".encode('utf-8'))

    print("Scraping messages, press Ctrl-C to stop and parse (alternatively run parse_log.py)")
    try:
        while True:
            check_for_response()

    except KeyboardInterrupt:
            print("Terminating connection...")
            sock.close()

    print("Parsing log into CSV file...")
    df = parser.get_chat_dataframe("twitchchatlogger\output\chat.log")
    df.to_csv("twitchchatlogger\output\parsedLog.csv")
    exit()

def check_for_response():
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
                
        elif len(resp) > 0:
                logging.info(resp)

if __name__ == "__main__":
    main()