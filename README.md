
# Discord Verification Bot

## Overview
This bot provides a verification process for users on a Discord server. It offers different levels of difficulty for verification and assigns a role to users who successfully complete the verification process.

## Features
- **Verification Command**: Initiate the verification process using the `/verify` command.
- **Difficulty Levels**: Choose between Easy, Medium, and Hard difficulty levels for the verification process.
- **Captcha Generation**: Generates an image with random text that users need to type to verify themselves.
- **Role Assignment**: Assigns a specific role to users who pass the verification.

## Setup and Configuration

### Prerequisites
- Python 3.8 or higher
- Discord.py library
- Pillow library for image processing

### Installation
1. Clone the repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install discord.py pillow
   ```
3. Create a `config.json` file in the same directory as the bot script and add your bot token and the role ID to be assigned. The `config.json` file should look like this:
   ```json
   {
       "token": "YOUR_BOT_TOKEN",
       "role_id": "ROLE_ID_TO_ASSIGN"
   }
   ```

4. Ensure you have an image named `background.png` in the same directory as the bot script. This image will be used as the background for the captcha.

### Running the Bot
Run the bot using the following command:
```bash
python bot.py
```

## Commands

### `/verify`
Initiates the verification process.

- If the user has administrative permissions, it sends an embed with buttons to select the difficulty level (Easy, Medium, Hard).
- Upon selecting a difficulty, another embed with a verification button is sent.
- When the verification button is clicked, the bot sends an image with random text based on the selected difficulty.
- The user has to enter the text shown in the image.
- If the entered text is correct, the user is assigned the specified role.

## Code Explanation

- **on_ready**: Logs the bot's status and synchronizes commands.
- **verify**: Handles the verification process, including checking user permissions, selecting difficulty levels, and generating the captcha image.
- **generate_random_string**: Generates a random string based on the selected difficulty level.
- **create_image_with_text**: Creates an image with the generated random text.
- **TextModal**: A modal for the user to enter the text shown in the captcha image.

## License
This project is licensed under the MIT License.

---

Replace `"YOUR_BOT_TOKEN"` and `"ROLE_ID_TO_ASSIGN"` in the `config.json` example with your actual bot token and the role ID you want to assign. This README provides a clear overview and setup instructions for your Discord verification bot.
