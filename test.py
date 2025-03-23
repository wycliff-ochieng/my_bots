import telegram
import logging
from typing import Final
from  telegram import Update
from telegram.ext import ContextTypes,MessageHandler,CommandHandler,Application, filters

logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)

#with open('token.txt', 'r') as f:
#    TOKEN = f.read()

TOKEN :Final = '7515591655:AAENecAym5xlcfCwB3nk5Qn1ii_JsyMXGPg'
BOT_USERNAME: Final = '@wycliff_ochieng_bot'

#commands

async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yooo, Unadai aje buda ???")

async def help(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Unataka nikusaidie aje")

async def custom(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I can help with swimming workouts")

    #responses
def handle_response(text:str)->str:
    processed:str=text.lower()

    if any(word in processed for word in ["Hello","hi","habari","yoo","hey"]):
        return "hi, how may i assist today BITCH"
    if "how are you doing" in processed:
        return "I am great. how about you"
    if "i love programming" in processed:
        return "Thats great,what do you love about programming"
    if any(word in processed for word in ["goggle","swim cap","flippers","costume","speedo"]):
        return "All swimming materials are availabe will you like to place an order"
    if any(word in processed for word in ["order","deliver","how"]):
        return "Call 0795643487 for more information"
    return "i dont understand you"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME," ").strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)
        
    print(f"Bot:", response)
    await update.message.reply_text(response) 

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} caused the hitch')

if __name__ == "__main__":
    print("Starting bot....")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('custom', custom))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling....")
    app.run_polling(poll_interval=3)
