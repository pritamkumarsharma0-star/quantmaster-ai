from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from app.config import BOT_TOKEN
from app.database import create_tables, SessionLocal
from app.handlers.answer import check_answer, next_question
from app.handlers.quiz import simplification_quiz
from app.handlers.topics import study_topics
from app.services.user_service import get_user, create_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    db = SessionLocal()

    telegram_id = str(update.effective_user.id)
    name = update.effective_user.first_name

    user = get_user(db, telegram_id)

    if user is None:
        create_user(db, telegram_id, name)
        message = f"🎉 Welcome, {name}!\n\nLet's start your Quant preparation."
    else:
        message = f"👋 Welcome back, {user.name}!"

    keyboard = [
        ["📚 Study Topics", "📝 Practice"],
        ["🎯 Mock Tests", "🔥 Daily Quiz"],
        ["📊 Progress", "👤 Profile"],
    ]

    await update.message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
        ),
    )

    db.close()


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    print(f"Menu received: {repr(text)}")

    if text == "📚 Study Topics":
        print("Opening Study Topics")
        await study_topics(update, context)

    elif text == "➗ Simplification":
        print("Opening Simplification Quiz")

        try:
            await simplification_quiz(update, context)
        except Exception as e:
            print("Quiz Error:", e)
            await update.message.reply_text(
                f"❌ Quiz Error:\n{e}"
            )

    else:
        print("Unknown button:", repr(text))
        await update.message.reply_text(
            "🚧 This feature is coming soon."
        )


def main():

    create_tables()

    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Callback handlers
    app.add_handler(
        CallbackQueryHandler(
            next_question,
            pattern="^next_question$"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            check_answer,
            pattern="^answer_"
        )
    )

    # Menu buttons
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu,
        )
    )

    print("✅ QuantMaster AI Started")

    app.run_polling()


if __name__ == "__main__":
    main()