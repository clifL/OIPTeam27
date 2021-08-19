# Tutorial link: https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot
# Getting telegram channel id url: https://api.telegram.org/bot(botToken)/getUpdates

import telepot


def send_telegram_message(msg):
    try:
        # Telegram bot api token for connection to telegram
        bot = telepot.Bot('1933396949:AAFYdLAiyHG-Ro85YNLJ1sPl8h191D0fy1Y')
        # Left parameter, chat ID that represent the Telegram channel.
        # Right parameter for the message
        bot.sendMessage("-1001563822154", msg)
        return True
    except:
        return False


send_telegram_message("Drying process done. Syringes are ready to collect.")