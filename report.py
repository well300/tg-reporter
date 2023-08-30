import requests
from colorama import init, Fore

init(autoreset=True)

def report_to_telegram(bot_token, chat_id, message):
    base_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(base_url, data=data)
    if response.status_code != 200:
        raise Exception("Reporting failed: Failed to transmit report message.")

def main():
    print(Fore.RED + r"""
            _  _  ____  __    __   
 __ __ __ ___ | || ||__ / /  \  /  \  
 \ V  V // -_)| || | |_ \| () || () | 
  \_/\_/ \___||_||_||___/ \__/  \__/                                                                                                                       
                                                                                                                                                                         
    """)
    print(Fore.CYAN + "🕵️‍♂️ Welcome to the Telegram Reporting Script! 🕵️‍♀️")
    print("Use this tool to report suspicious accounts on Telegram.")
    print("We're working to keep the digital world safe and peaceful.")
    print(Fore.MAGENTA + "------------------------------------------------------------")
    
    try:
        bot_token = "5882947325:AAGW5WXZP3qUe0K9vKX65qf2YdTJCXI2oks"  # Replace with your actual bot token

        print(Fore.YELLOW + "Select the type of entity to report (user/channel/group):")
        target_type = input().lower()

        if target_type == 'user':
            print(Fore.YELLOW + "Do you want to report multiple users? (yes/no):")
            report_multiple = input().lower()
            if report_multiple == 'yes':
                print(Fore.MAGENTA + "------------------------------------------------------------")
                print(Fore.YELLOW + "Enter the number of users to report (maximum 3):")
                num_targets = min(int(input()), 3)
            else:
                num_targets = 1

            target_infos = []
            for i in range(num_targets):
                print(f"Enter the user ID or username for user #{i+1}:")
                target_info = input()
                target_infos.append(target_info.split("@")[1] if "@" in target_info else target_info)
        else:
            print(f"Enter the ID or username of the {target_type}:")
            target_infos = [input()]

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Enter the number of times to report each entity:")
        num_reports = int(input())

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Select a reason for reporting:")
        print("1. Harassment\n2. Spam\n3. Impersonation\n4. Hate Speech\n5. Fake Account")
        print("6. Violent Content\n7. Inappropriate Content\n8. Scam\n9. Threatening Behavior\n10. Other")
        print(Fore.YELLOW + "Enter the reason number (1-10) or '10' for a custom reason:")
        reason_choice = input()

        reason_choices = {
            '1': "Harassment",
            '2': "Spam",
            '3': "Impersonation",
            '4': "Hate Speech",
            '5': "Fake Account",
            '6': "Violent Content",
            '7': "Inappropriate Content",
            '8': "Scam",
            '9': "Threatening Behavior",
            '10': "Other"
        }

        if reason_choice == '10':
            print("Enter a custom reason for reporting:")
            custom_reason = input()
            reason = f"Custom Reason: {custom_reason}"
        else:
            reason = reason_choices.get(reason_choice, "Invalid Reason")

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Confirm your reporting details:")
        print(f"Entity Type: {target_type.capitalize()}")
        print(f"Entity IDs: {', '.join(target_infos)}")
        print(f"Reports to Send: {num_reports}")
        print(f"Reason for Reporting: {reason}")

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Do you want to proceed with reporting? (yes/no):")
        confirm = input().lower()
        if confirm != 'yes':
            print(Fore.RED + "Reporting aborted. Be vigilant.")
            return

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Enter your chat/group ID for reporting:")
        chat_id = input()

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Enter your Telegram ID using @:")
        reporter_id = input()

        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(Fore.YELLOW + "Initiating the reporting process...")

        try:
            for target_info in target_infos:
                message = f"@{target_info} has been reported {num_reports} times by User {reporter_id}. Reason: {reason}"
                report_to_telegram(bot_token, chat_id, message)
            print(Fore.GREEN + "Reporting successful. Stay vigilant.")
        except Exception as e:
            print(Fore.RED + f"Reporting failed: {e}")

        print(Fore.CYAN + "\nReporting Summary:")
        print(Fore.MAGENTA + "------------------------------------------------------------")
        print(f"Entity Type: {target_type.capitalize()}")
        print(f"Entity IDs: {', '.join(target_infos)}")
        print(f"Reports Sent: {num_reports * len(target_infos)}")
        print(f"Reports per Entity: {num_reports}")
        print(f"Reason for Reporting: {reason}")
        print(Fore.MAGENTA + "------------------------------------------------------------")

    except KeyboardInterrupt:
        print(Fore.RED + "\nReporting interrupted. Proceed with caution.")
    except Exception as ex:
        print(Fore.RED + f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    main()
