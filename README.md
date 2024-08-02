# Verification Bot

This is a Discord bot designed to handle user verification through a series of interactions. The bot provides different difficulty levels for verification, where users need to enter text from an image to get verified.

## Features

- Provides three levels of verification difficulty: Easy, Medium, and Hard.
- Uses a button interface for users to select the difficulty level.
- Generates a random string based on the selected difficulty level.
- Creates an image with the random string and sends it to the user.
- Allows users to enter the text from the image to verify themselves.
- Grants a specific role upon successful verification.

## Prerequisites

- Python 2.4 or higher
- Discord.py library
- PIL library for image processing

## Setup

1. Clone the repository:

```sh
git clone https://github.com/Boda335/Verification-Bot.git
cd verification-bot
```

2. Install the required libraries:

```sh
pip install discord.py Pillow
```

3. Create a `config.json` file in the root directory of the project and add your bot token and the role ID for the verified role:

```json
{
  "token": "YOUR_BOT_TOKEN",
  "role_id": "ROLE_ID"
}
```

4. Make sure you have an image for the background located at `./src/bg/background.png`.

6. Make sure you have a font for the text located at `./src/font/font.ttf`. 

7. Run the bot:

```sh
python bot.py
```

## Usage

1. Invite the bot to your server with the necessary permissions.
2. Use the `/verify` command to start the verification process.
3. Select the difficulty level by clicking one of the provided buttons.
4. Click the "Verify" button to receive an image with the verification text.
5. Enter the text from the image into the modal that appears.
6. If the text is correct, you will be granted the verified role.

## Verification Difficulties

The bot offers three levels of difficulty for the verification process:

### Easy 🟢
- A string of 6 digits.
- Example: `123456`

### Medium 🟡
- A string of 6 alphanumeric characters (letters and numbers).
- Example: `a1b2c3`

### Hard 🔴
- A string of 8 characters including letters, numbers, and punctuation.
- Example: `a1!b2@c3`

Each level is designed to provide a varying degree of challenge to ensure the authenticity of the user verification process.

<div style="text-align: center;">
  <img src="https://d.top4top.io/p_3136ssht11.png" alt="Easy" >
  <img src="https://e.top4top.io/p_3136v3mvg2.png" alt="Medium" ">
  <img src="https://f.top4top.io/p_3136obvf33.png" alt="Hard" >
</div>

## Bot Commands

- `/verify`: Starts the verification process. This command is only available to users with administrative permissions.
**After typing the command, you will respond with Embed with buttons as in the picture, from which you can choose the difficulty**
<div style="text-align: center;">
  <img src="https://d.top4top.io/p_3136ssht11.png" alt="Easy" >
</div>

## Code Explanation

- The bot uses Discord's slash commands and interactions to provide a seamless verification process.
- The `verify` command sends an embed with buttons for selecting the difficulty level.
- Upon selecting a difficulty level, another embed with a verification button is sent.
- The `verify_button_callback` function generates a random string based on the difficulty and creates an image with this text.
- The image is sent to the user, and they are prompted to enter the text from the image.
- The `TextModal` class handles the text input and verification. If the entered text matches the generated string, the user is given the specified role.

## Dependencies

- `discord.py`: A Python wrapper for the Discord API.
- `Pillow`: A Python Imaging Library to create and manipulate images.

## Contributing

If you want to contribute to the project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [MIT License](LICENSE) file for more details.

## Acknowledgements

- The Discord.py community for their continuous support and development of the library.
- The Pillow library for providing easy-to-use image processing capabilities.
