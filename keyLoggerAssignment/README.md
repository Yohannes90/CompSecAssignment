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

#### Optimization

- **Batch file (optional)**: Create a batch file (`run_keylogger.bat`) to simplify execution in a Windows environment. Example content for `run_keylogger.bat`:

  ```plaintext
  @echo off
  cd /d %~dp0
  python keylogger.py
  ```

  Double-clicking `run_keylogger.bat` will start the keylogger.

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
