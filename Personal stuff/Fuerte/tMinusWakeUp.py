import time
from datetime import datetime, timedelta

def calculate_sleep_time(wake_hour, wake_minute=0):
    now = datetime.now()
    
    # Set the target wake-up time for today
    wake_time = now.replace(hour=wake_hour, minute=wake_minute, second=0, microsecond=0)
    
    # If the target time is earlier than the current time, 
    # it means the wake-up time is tomorrow.
    if wake_time < now:
        wake_time += timedelta(days=1)
        
    # Calculate the difference
    time_left = wake_time - now
    
    # Convert timedelta into hours, minutes, and seconds
    total_seconds = int(time_left.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return hours, minutes, seconds

if __name__ == "__main__":
    # --- CONFIGURATION ---
    WAKE_UP_HOUR = 3  # 24-hour format (3 = 3:00 AM, 15 = 3:00 PM)
    WAKE_UP_MINUTE = 0
    # ---------------------
    
    print(f"Tracking sleep until {WAKE_UP_HOUR:02d}:{WAKE_UP_MINUTE:02d}. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            hours, minutes, seconds = calculate_sleep_time(WAKE_UP_HOUR, WAKE_UP_MINUTE)
            
            # \r moves the cursor back to the start of the line to overwrite it
            # flush=True forces the terminal to update immediately
            print(f"\rIf you sleep now, you will get: {hours}h {minutes}m {seconds}s of sleep", end="", flush=True)
            
            # Wait exactly 1 second before recalculating
            time.sleep(1)
            
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C
        print("\n\nTracker stopped. Have a good night!")