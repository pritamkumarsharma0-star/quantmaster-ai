from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from app.config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📚 Study Topics", "📝 Practice"],
        ["🎯 Mock Tests", "🔥 Daily Quiz"],
        ["📊 Progress", "👤 Profile"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🎉 Welcome to *QuantMaster AI*\n\n"
        "Your Quantitative Aptitude companion for Competitive Exams.\n\n"
        "Choose an option below 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ QuantMaster AI is running...")

    app.run_polling()


if __name__ == "__main__":
    main()