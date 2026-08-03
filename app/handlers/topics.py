from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def study_topics(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["➗ Simplification"],
        ["📊 Percentage"],
        ["⬅ Back"],
    ]

    await update.message.reply_text(
        "📚 Select a topic",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
        ),
    )