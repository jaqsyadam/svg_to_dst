from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает команду /start и отправляет приветственное сообщение."""
    welcome_message = (
        "👋 Привет! Я бот для конвертации SVG-файлов в DST.\n\n"
        "📂 Просто отправь мне SVG-файл, и я пришлю тебе готовый DST-файл.\n"
        "❓ Для справки отправь команду /help."
    )
    await update.message.reply_text(welcome_message)

def get_handler():
    return CommandHandler("start", start_handler)