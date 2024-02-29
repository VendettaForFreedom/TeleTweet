# Teletweet Project

## Introduction
Teletweet seamlessly connects Telegram with Twitter, empowering users to manage their Twitter feed, post tweets, and interact with their audience directly through Telegram. This integration is facilitated by a sophisticated Telegram bot, built on Python, which handles Twitter operations securely and efficiently.

## Features
- **Direct Twitter Integration**: Link your Twitter account with Telegram for direct tweeting, retweeting, and more.
- **Media Tweeting**: Supports tweeting text, images, videos, and GIFs directly from Telegram.
- **Secure Authentication**: Ensures a secure sign-in process to connect your Twitter account with the Telegram bot.
- **Interactive Bot Commands**: Use simple bot commands to control your Twitter account functionalities.

## Installation
1. Clone the project repository to your local machine.
2. Install Python 3.x, if not already installed.
3. Install necessary Python dependencies by executing `pip install -r requirements.txt`.

## Configuration (`config.py`)
Before running the Teletweet bot, you must configure it with your own API keys and settings in `config.py`. Here's what needs to be configured:

- `APP_ID` and `APP_HASH`: These are your Telegram application ID and hash, obtainable from [my.telegram.org](https://my.telegram.org).
- `BOT_TOKEN`: Your Telegram bot token, provided by @BotFather on Telegram after creating a new bot.
- `CHANNEL_ID` and `CONFIG_CHANNEL_ID`: IDs of Telegram channels for specific bot functionalities, if needed.
- `ALLOW_USERS`: A list of Telegram user IDs allowed to use this bot. Leave empty (`[""]`) to allow everyone.
- `FEEDBACK`: Optional; set a Telegram username or channel ID to receive feedback.
- `TODAY_CONFIG`, `SIGN`, and `LAST_MESSAGE`: Configuration settings for bot operation details.
- `tweet_format`: The URL format for tweets, used to generate links to posted tweets.

Ensure you replace placeholder values in `config.py` with your actual API keys and settings.

## Usage
After configuring `config.py`, run `tweetbot.py` to start the bot. Interact with the bot on Telegram using the commands provided above.

## Contributing
Contributions are welcome! If you have suggestions or want to add features, please fork the repository, commit your changes, and submit a pull request.

- We have deployment on feature-* branches that has an open pull request with build tag
- Production deployment when there is a merge on deployment branch

## License
GPL 2.0__
