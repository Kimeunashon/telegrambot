from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace with your actual token
TOKEN = '7783768250:AAGHU7Q6w2UJFMInXuHfznC9_FSWJg8T0xo'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot. Type something and I will echo it back!')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('Available commands: /start, /help')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"You said: {update.message.text}")

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))  # This will catch all text messages

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
