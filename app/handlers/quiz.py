from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from app.services.question_service import get_random_question


async def simplification_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = get_random_question()

    # Save question in user session
    context.user_data["current_question"] = question

    keyboard = []

    for index, option in enumerate(question["options"]):
        keyboard.append([
            InlineKeyboardButton(
                option,
                callback_data=f"answer_{index}"
            )
        ])

    await update.message.reply_text(
    f"📘 *Simplification Practice*\n\n"
    f"❓ {question['question']}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )