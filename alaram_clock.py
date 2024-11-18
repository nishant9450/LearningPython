import os
import datetime
import time


def set_alarm():
    # Get the date and time input from the user
    day, month, year = input("Enter the date (DD/MM/YYYY): ").split("/")
    hour, minute, second = input("Enter the time in 24 hours clock (HH:MM:SS): ").split(":")

    # Parse date and time
    alarm_date = datetime.date(int(year), int(month), int(day))
    alarm_hour = int(hour)
    alarm_minute = int(minute)
    alarm_second = int(second)

    # Loop to check the current time against the alarm time
    while True:
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()

        if current_date == alarm_date and current_time.hour == alarm_hour \
                and current_time.minute == alarm_minute and current_time.second == alarm_second:
            # Play the alarm sound
            os.startfile(r'C:\Users\Nishu\betabikaringtone-8153.mp3')
            break

        # Sleep for a short time to avoid excessive CPU usage
        time.sleep(1)


# Run the alarm
set_alarm()