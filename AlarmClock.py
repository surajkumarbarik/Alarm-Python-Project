from datetime import datetime,time
from playsound import playsound

alarm_time= input("Enter the time of alarm to be set : HH:MM:SS AM/PM\n")
alrmhr = alarm_time[0:2]
alrmmnt = alarm_time[3:5]
alrmsec = alarm_time[6:8]
alrmprd = alarm_time[9:12].upper()

print("Setting up alarm...")

while True:
    now=datetime.now()
    crnthr=now.strftime("%I")
    crntmin = now.strftime("%M")
    crntsec = now.strftime("%S")
    crntprd = now.strftime("%p")

    if alrmprd==crntprd:
        if alrmhr==crnthr:
            if alrmmnt==crntmin:
                if alrmsec==crntsec:
                    print("<<<<WAKE UP>>>>")
                    playsound('Most_Romantic_Ringtone_2017-5.mp3')
                    break

