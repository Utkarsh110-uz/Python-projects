import time
from plyer import notification

# Below code will send a notification to our system on anytime when we run the python script and we can change the content of the message also. 
title = "Hello Utkarsh"
message = "this is a sample message"
notification.notify(
    title = title,
    message = message,
    timeout = 10
)

# Below code will send the notification at the specific time given by us and we can change the content of the message.
target_time = "20:08:00"
while True:
    current_time = time.strftime("%H:%M:%S")

    if(current_time == target_time):
        notification.notify(
            title = "Time to sleep",
            message = "Its 12:00 clock its time to sleep please shutdown the computer and go to sleep",
        )
        break
    time.sleep(1)