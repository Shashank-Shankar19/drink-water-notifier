import time
import plyer
from plyer import notification
import subprocess


if __name__ == "__main__":
    subprocess.run("pythonw .\main.py")
    while True:
        notification.notify(title="It's Water Time!!!!!!",
                            message="Drink Water right now or else die. Drink atleast 3.5 litres of water per day", app_icon="icon.ico",
                            timeout=5
                            )
        time.sleep(60*60)
