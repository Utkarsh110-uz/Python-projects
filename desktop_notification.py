import time
from plyer import notification

# title = "Hello Utkarsh"
# message = "this is a sample message"
# notification.notify(
#     title = title,
#     message = message,
#     timeout = 10
# )

target_time = "12:00:00"
while True:
    current_time = time.strftime("%H:%M:%S")

    if(current_time == target_time):
        notification.notify(
            title = "Time to sleep",
            message = "Its 12:00 clock its time to sleep please shutdown the computer and go to sleep",
        )
        break
    time.sleep(1)