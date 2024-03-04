# Discord-to-Spotify Volume Manager

The Discord-to-Spotify Volume Manager is a Python script that dynamically adjusts the volume of the Spotify application based on the volume level of Discord. This ensures a balanced audio experience, preventing interference during voice chats or other activities in Discord.

## Features

-   Monitors the volume level of Discord in real-time
-   Automatically adjusts the volume of the Spotify application

## How It Works

The script continuously monitors the volume level of Discord using the Windows Audio Session API (WASAPI). When significant activity is detected in Discord, such as during voice chats, the script lowers the volume of the Spotify application to prevent interference. The Spotify volume is dynamically adjusted to maintain a balanced audio experience.

## Requirements

-   Python 3.x
-   pycaw library

## Usage

1. Install the required dependencies using `pip install pycaw`
2. Run the script using `python discord_to_spotify_volume_manager.py`

## Configuration

-   Adjust volume thresholds and increments in the script as needed

## Acknowledgements

-   This script utilizes the pycaw library for interacting with the Windows Audio Session API

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.
