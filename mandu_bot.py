from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import logging

# === YOUR BOT TOKEN ===
BOT_TOKEN = "8542028079:AAFNi6Tc_WJOXDrgYSN67e1W_MEbXZjCOdI"  # Replace with your BotFather token

# === Logging ===
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# === Command Handlers ===
def start(update, context):
    update.message.reply_text(
        "👋 Welcome to the MANDU Official Community!\n\n"
        "Type /map to view our roadmap, or visit our website below:\n"
        "🌐 https://www.novalab2023.com"
    )

def roadmap(update, context):
    update.message.reply_text(
        "🗺️ *MANDU Roadmap*\n\n"
        "- Q4 2025: Token Launch\n"
        "- Q1–Q2 2026: Community Expansion\n"
        "- Q4 2026: Mandu Messenger Launch\n"
        "- Q3–Q4 2027: UB Pay Integration\n"
        "- 2028+: DAO Governance",
        parse_mode=ParseMode.MARKDOWN
    )

def whitepaper(update, context):
    update.message.reply_text("📄 Official Whitepaper:\nhttps://www.novalab2023.com/whitepaper.pdf")

def website(update, context):
    update.message.reply_text("🌐 Visit our website:\nhttps://www.novalab2023.com")

def social(update, context):
    update.message.reply_text(
        "🔗 *MANDU Official Links*\n"
        "🌐 Website: https://www.novalab2023.com\n"
        "📄 Whitepaper: https://www.novalab2023.com/whitepaper.pdf\n"
        "🐦 Twitter: https://x.com/MANDUCOINBNB\n"
        "💬 Telegram: https://t.me/MANDUCOIN\n"
        "💻 GitHub: https://github.com/nobalab2023/mandu-website",
        parse_mode=ParseMode.MARKDOWN
    )

# === Welcome message for new members ===
def welcome(update, context):
    for member in update.message.new_chat_members:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"👋 Welcome {member.first_name}! Welcome to the MANDU Community!"
        )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("map", roadmap))
    dp.add_handler(CommandHandler("whitepaper", whitepaper))
    dp.add_handler(CommandHandler("website", website))
    dp.add_handler(CommandHandler("social", social))

    # New member welcome
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    print("🤖 MANDU Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
