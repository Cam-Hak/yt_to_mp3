import ssl
import certifi
from send_email import send_mail
from pytubefix import YouTube
import os
import subprocess

# Fix SSL cert issue
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Get YouTube URL
yt_url = input("Paste url here: ")

# Download the audio stream
yt_video = YouTube(yt_url)
audio_stream = yt_video.streams.filter(only_audio=True).first()
out_file = audio_stream.download(output_path=".")

# Convert downloaded file to proper MP3 using ffmpeg
base, ext = os.path.splitext(out_file)
mp3_file = base + ".mp3"

subprocess.run([
    "ffmpeg", "-i", out_file, "-vn", "-ab", "192k", "-ar", "44100", "-y", mp3_file
])

# Optionally remove the original .webm file
os.remove(out_file)

email = "<enter your email here>"

# Send email with the actual MP3
send_mail(
    send_from=email,
    send_to=[email],
    subject="Downloaded Song",
    text="Here is your song!",
    file=mp3_file,
    username=email,
    password="gmail password"
)

print(f"{yt_video.title} has been successfully downloaded and emailed.")
