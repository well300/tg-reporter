# Telegram Reporting Script

## Introduction

The Telegram Reporting Script is a tool designed to help users report suspicious accounts, channels, or groups on Telegram. It allows users to send reports to a specified chat or group, providing information about the reported entity and the reason for reporting.

## Features

- Easy-to-use script to report suspicious Telegram entities.
- Reports can be sent to a designated chat or group.
- Multiple reporting reasons to choose from, including a custom reason option.
- Supports reporting multiple entities in a single run.
- Provides reporting statistics for each entity.

## Usage

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/well300/tg-reporter.git
   cd tg-reporter
   ```

2. **Install Dependencies**

   Install the required dependencies by running:

   ```
   pip install -r requirements.txt
   ```

3. **Set Up Your Bot Token**

   Open the `report.py` script in a text editor of your choice and replace `"YOUR_BOT_TOKEN_HERE"` with your actual Telegram bot token.

4. **Run the Script**

   Open a terminal and navigate to the script directory. Then run the script using:

   ```
   python report.py
   ```

5. **Follow the Prompts**

   The script will guide you through the reporting process. You'll be asked to provide information such as the type of entity you want to report (user, channel, or group), the target ID or username, the number of reports to send, the reason for reporting, and more.

6. **Review the Reporting Summary**

   After completing the reporting process, the script will display a summary of the reports sent, including entity type, IDs, number of reports sent, reason for reporting, and more.

## Platform-specific Instructions

### Running on Windows

- Make sure you have Python installed. You can download it from the official Python website.
- Open the Command Prompt and navigate to the script directory.
- Follow the general usage instructions above.

### Running on Linux

- Open a terminal and navigate to the script directory.
- Follow the general usage instructions above.

### Running on Termux (Android)

- Install the Termux app from the Google Play Store.
- Open Termux and install necessary packages:

  ```
  pkg install python git
  ```
  
- Follow the general usage instructions above.

## Note

- Use this script responsibly and only report entities that violate Telegram's terms of service.
- Be cautious when providing your bot token. Keep it private and do not share it with others.
- This script is for educational purposes only and should not be used for malicious activities.


