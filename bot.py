import constant as keys

from telegram.ext import  *
import response as R
import requests
import json

print("bot started")
def start_command(update,context):
    update.message.reply_text("hi1234")

def handle_message(update,context):
     text=str(update.message.text).lower()
     response=R.Response(text)
     for x in response:
       update.message.reply_text(x)

def main():
    updater=Updater(keys.API_KEY,use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler((MessageHandler(Filters.text,handle_message)))
    updater.start_polling();
    updater.idle();

main()