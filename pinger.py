import logging
import logging.config
import os
import subprocess


def main():
    if not os.path.isdir("./logs"):
        os.mkdir("./logs")

    log_filename = os.path.join("./logs", "loggy.log")
    logging.config.fileConfig(os.path.join(".", "logging.ini"), defaults={"logfilename": log_filename})

    while True:
        with open("ip.txt") as f:
            IP = [line.rstrip() for line in f]
        if len(IP) != 0:
            for ping in IP:
                res = subprocess.call(["ping", "-c", "3", ping])
                if res == 0:
                    logging.info(f" {ping} is pinging.\n")
                    subprocess.call(["afplay", "./media/Alarm.wav"])
                    subprocess.call(["afplay", "./media/Alarm.wav"])
                    subprocess.call(["afplay", "./media/Alarm.wav"])
                elif res == 2:
                    logging.info(f"{ping} is not responding.\n")
                else:
                    logging.error(f"ping to {ping} failed.\n")
        else:
            logging.info(
                "No IP listed on ip.txt -- Aborting. Please enter at least 1 IP/ URL. Use new line to define each IP.\n"
            )
            break


if __name__ == "__main__":
    main()
