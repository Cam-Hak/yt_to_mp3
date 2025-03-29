# **YouTube Audio Downloader & Email Sender**

This Python script downloads audio from a YouTube video, converts it to MP3 using ffmpeg, and sends it to your email as an attachment.
## Requirements
Python Packages

Install required Python packages using pip:

```
pip install pytubefix certifi
```

Note: We use pytubefix instead of pytube due to recent updates and stability improvements.

## External Dependencies
1. ffmpeg

Required for converting downloaded audio to MP3.

Install via:

Linux (Debian/Ubuntu):

```
sudo apt install ffmpeg
```

macOS (Homebrew):

```
brew install ffmpeg
```

Windows: Download and install from https://ffmpeg.org/download.html. Make sure to add it to your system PATH.

## Configuration

Before running the script, update the following fields:

```
email = "<enter your email here>"

send_mail(
    send_from=email,
    send_to=[email],
    ...
    password="gmail password"
)
```

## Gmail Configuration

If you're using Gmail:

```
Use an App Password if 2FA is enabled:
https://myaccount.google.com/apppasswords
```

## Usage

Run the script:

    python your_script.py

Paste the YouTube video URL when prompted.

The script will:
- Download the audio
- Convert it to MP3
- Send it to your configured email

## Disclaimer

This script is intended for personal use and educational purposes only. Downloading copyrighted content without permission may violate YouTube’s terms of service.
