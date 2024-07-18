## Keylogger Project

A Python-based keylogger that monitors keystrokes and sends periodic PC vitals reports via email, created for educational purposes as part of the Computer Security and Privacy course.

### Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Features](#features)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Disclaimer](#disclaimer)
7. [Contributing](#contributing)

### Overview

This project implements a keylogger in Python that records keystrokes and periodically sends PC vitals (CPU usage, memory usage, disk usage) reports via email. It is developed as part of a Computer Security and Privacy course to demonstrate security implications and monitoring capabilities.

### Requirements

- Logs keys into a file.
- Operates unobtrusively.
- Sends logged data via email.
- Deletes traces after sending.

### Features

- Monitors keystrokes and logs them into a text file.
- Sends PC vitals report (CPU, memory, disk usage) via email using Gmail SMTP.
- Periodically writes keystrokes to a log file and sends an email with the log file attachment.

### Getting Started

#### Installation

1. Clone the repository:

   ```
   git clone https://github.com/Yohannes90/CompSecAssignment.git
   cd CompSecAssignment/keyLoggerAssignment
   ```

2. Install dependencies from `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```

   This command will install all required Python packages specified in the `requirements.txt` file.

#### Configuration

1. Create a `.env` file in the root directory with the following environment variables:

   ```plaintext
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SENDER_EMAIL=your-email@gmail.com
   SENDER_PASSWORD="your email app password"
   RECIPIENT_EMAIL=recipient-email@example.com
   ```

   Replace `your-email@gmail.com`, `your-email-app-password`, and `recipient-email@example.com` with your own values.

2. Ensure that less secure apps access is enabled in your Gmail account settings to send emails programmatically.

#### Preparation

- Remove any sensitive information such as API keys or personal email credentials from the code.
- Modify the code for educational purposes to enhance readability and understanding (e.g., add comments, remove complex logic).

#### Optimization(For Windows)

- **To ensure the keylogger starts each time the computer boots, you can add it to the system's startup programs. This can be done in different ways depending on the operating system. Below, I'll provide examples for Windows only.**


1. **Create a Batch File**
   Create a batch file (`start_keylogger.bat`) to run your Python script:

   ```batch
   @echo off
   pythonw C:\path\to\your\keylogger.py
   ```

   Make sure to replace `C:\path\to\your\keylogger.py` with the actual path to your Python script. Using `pythonw` runs the script without opening a command prompt window.

2. **Add the Batch File to Startup**
   - Press `Win + R`, type `shell:startup`, and press Enter. This opens the Startup folder.
   - Place the `start_keylogger.bat` file in the Startup folder.

### Usage

1. Run the keylogger:

   ```
   python keylogger.py
   ```

   This will start logging keystrokes and periodically send email reports.

### Disclaimer

This project is intended for educational purposes only. It is designed to demonstrate how keyloggers can be implemented and should not be used for any malicious purposes. Use responsibly and ensure compliance with legal regulations.

### Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
