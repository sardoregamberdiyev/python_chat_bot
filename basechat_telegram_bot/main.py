import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Replace YOUR_API_TOKEN with the API token you received from BotFather
bot = telegram.Bot(token='6268136991:AAE5n2hDCbmbl8Kt_Gqz-1vynZVdW-hZZRM')


def handle_message(update, context):
    # Get the text message from the user
    text = update.message.text

    # Define some predefined responses
    responses = {
        'Salom': 'Assalomu Alaykum 😊!',
        'salom': 'Assalomu Alaykum 😊!',
        'Qalesan': 'Men yaxshi ishlayapman, rahmat!\nSiz kuningiz qanday o`tayapti',
        'What is your name': 'My name is ChatGPT, and I am an AI language model.',
        # Add more responses here
    }

    # Check if the user's message matches any of the predefined responses
    if text in responses:
        # Send the predefined response back to the user
        update.message.reply_text(responses[text])
    else:
        # If the user's message doesn't match any predefined responses, send a default message
        update.message.reply_text("Kechirasiz, men tushunmayapman 😕.Siz bot tanimaydiga savol berdingiz. Iltimos,"
                                  "qayta urinib ko'ring?")


# Create an updater and attach the message handler
updater = Updater(token='6268136991:AAE5n2hDCbmbl8Kt_Gqz-1vynZVdW-hZZRM', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C to stop it
updater.idle()
