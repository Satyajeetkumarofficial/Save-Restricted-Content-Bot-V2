from config import LOG_GROUP, EXTRA_LOG_CHANNEL

async def send_log_message(client, message):
    try:
        if LOG_GROUP:
            await message.copy(LOG_GROUP)
        if EXTRA_LOG_CHANNEL and EXTRA_LOG_CHANNEL != LOG_GROUP:
            await message.copy(EXTRA_LOG_CHANNEL)
    except Exception as e:
        print(f"Log Error: {e}")
