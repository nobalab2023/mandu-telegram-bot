# main.py
import os, time, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
from telegram.utils.request import Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("MANDU-BOT")

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Render 환경변수에서 주입
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN env var is missing")

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

def welcome(update, context):
    for m in update.message.new_chat_members:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"👋 Welcome {m.first_name}! Welcome to the MANDU Community!"
        )

def run():
    # 네트워크 끊김 대비 타임아웃 설정
    req = Request(connect_timeout=20, read_timeout=30)
    updater = Updater(BOT_TOKEN, request_kwargs={'con_pool_size': 8}, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("map", roadmap))
    dp.add_handler(CommandHandler("whitepaper", whitepaper))
    dp.add_handler(CommandHandler("website", website))
    dp.add_handler(CommandHandler("social", social))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    logger.info("🤖 MANDU Bot is starting polling...")
    updater.start_polling(clean=True)   # clean=True: 이전 업데이트 비움
    updater.idle()

if __name__ == "__main__":
    # 예외 발생해도 Render가 재시작하지만, 짧게 재시도 루프 한 번 더.
    while True:
        try:
            run()
        except Exception as e:
            logging.exception("Bot crashed, restarting in 5s: %s", e)
            time.sleep(5)
