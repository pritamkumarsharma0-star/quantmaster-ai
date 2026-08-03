from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from app.handlers.quiz import simplification_quiz


async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    question = context.user_data.get("current_question")

    if question is None:
        await query.edit_message_text("❌ Question expired.")
        return

    selected = int(query.data.split("_")[1])

    if selected == question["correct"]:
        text = (
            "✅ Correct!\n\n"
            f"{question['explanation']}"
        )
    else:
        correct = question["options"][question["correct"]]

        text = (
            "❌ Wrong!\n\n"
            f"✅ Correct Answer: {correct}\n\n"
            f"{question['explanation']}"
        )

    keyboard = [
        [
            InlineKeyboardButton(
                "➡️ Next Question",
                callback_data="next_question"
            )
        ]
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await simplification_quiz(update, context)