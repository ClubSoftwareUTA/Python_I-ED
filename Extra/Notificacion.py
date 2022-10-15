import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Alerta",
            message="Este es un mesaje de alerta",
            timeout=10
        )
        time.sleep(3600)
