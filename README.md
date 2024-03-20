# Discord Bot README

## Overview
This Discord bot is built using Python and the discord.py library. It provides several functionalities including responding to specific messages, handling member joins, and allowing users to change their nicknames.

## Features
- **Message Handling**: The bot responds to specific messages sent in the channels it has access to.
- **Member Join Handling**: It sends a welcome message to new members and prompts them to enter their in-game names (IGN) as their nickname.
- **Nickname Change**: Users can initiate a process to change their nickname using the `!name_change` command.

## Usage
1. **Running the Bot**:
   - Make sure you have Python installed on your system.
   - Install the discord.py library using `pip install discord.py`.
   - Set up a Discord application and obtain the bot token.
   - Set the `DISCORD_TOKEN` environment variable with the obtained token.
   - Run the script.

2. **Message Handling**:
   - The bot responds to messages containing the text 'hello' with a greeting.

3. **Member Join Handling**:
   - Upon joining the server, new members receive a greeting message in their DMs and are prompted to enter their IGN.

4. **Nickname Change**:
   - Users can use the `!name_change` command to initiate the nickname change process.
   - They will be prompted to enter their new IGN and confirm it.

## Dependencies
- [discord.py](https://github.com/Rapptz/discord.py): An API wrapper for Discord written in Python.

## Environment Variables
- `DISCORD_TOKEN`: The token required for the bot to authenticate with Discord.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
