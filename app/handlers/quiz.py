from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes

from app.services.question_service import get_random_question


async def simplification_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = get_random_question()

    context.user_data["current_question"] = question

    keyboard = [
        [
            InlineKeyboardButton(
                option,
                callback_data=f"answer_{i}"
            )
        ]
        for i, option in enumerate(question["options"])
    ]

    if update.callback_query:
        await update.callback_query.answer()

        await update.callback_query.edit_message_text(
            f"📘 *Simplification*\n\n{question['question']}",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
    else:
        await update.message.reply_text(
            f"📘 *Simplification*\n\n{question['question']}",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )