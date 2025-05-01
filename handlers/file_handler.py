from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import os
from converter import convert_svg_to_dst

router = Router()

# Папка для временных файлов
DOWNLOADS_DIR = "downloads"
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# Обработчик команды /start
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Отправь мне SVG-файл для конвертации в DST.")

# Обработчик файлов
@router.message(lambda message: message.document)
async def handle_file(message: types.Message):
    document = message.document
    file_name = document.file_name

    # Проверяем, что это SVG-файл
    if not file_name.endswith('.svg'):
        await message.answer("Пожалуйста, отправьте файл в формате SVG.")
        return

    # Скачиваем файл
    file_path = os.path.join(DOWNLOADS_DIR, file_name)
    await message.bot.download(document, destination=file_path)

    # Конвертация SVG -> DST
    dst_path = file_path.replace('.svg', '.dst')
    try:
        convert_svg_to_dst(file_path, dst_path)
        await message.answer_document(FSInputFile(dst_path))
    except FileNotFoundError as e:
        await message.answer(f"❌ Ошибка: {e}")
    except RuntimeError as e:
        await message.answer(f"❌ Ошибка при конвертации файла: {e}")
    except Exception as e:
        await message.answer(f"❌ Непредвиденная ошибка: {e}")
    finally:
        # Удаляем файлы после отправки (опционально)
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(dst_path):
            os.remove(dst_path)

# Функция для регистрации хэндлера
def get_handler():
    return router