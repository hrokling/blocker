import time
import datetime

path = "/etc/hosts"
local = "127.0.0.1"
hostnamelist = ["www.facebook.com", "facebook.com", "www.vg.no", "vg.no"]

while True:
    now = datetime.datetime.now()  # Get the current time
    # Blocking starts at 09.00
    blocktimestart = now.replace(hour=9, minute=0, second=0, microsecond=0)
    # Blocking ends at 17.00
    blocktimeend = now.replace(hour=17, minute=0, second=0, microsecond=0)

    if now > blocktimestart and now < blocktimeend:
        with open((path), "r+") as file:
            content = file.read()
            for hostname in hostnamelist:
                if hostname in content:
                    pass
                else:
                    file.write(local + " " + hostname + "\n")
    else:
        with open((path), "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(hostname in line for hostname in hostnamelist):
                    file.write(line)
            file.truncate()
    time.sleep(900)
