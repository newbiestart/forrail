from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = "AAFFC73WT2REuygaceCxpPAIzTWt4JBjZ1M"

async def start(update, context):
    await update.message.reply_text("Hello! I'm your Telegram bot.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
