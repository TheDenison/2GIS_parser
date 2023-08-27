import asyncio
import logging

import aiofiles

from aiogram.utils.markdown import hbold
from telegram.error import TimedOut, RetryAfter
from card_finder import *
from tg_bot.auth_tg import *
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import filters, Application, CallbackQueryHandler, CommandHandler, ContextTypes, CallbackContext, \
    MessageHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    user = update.message.from_user
    logger.info("Пользователь %s начал использовать бота.", user.first_name)

    # Создание клавиатуры
    keyboard = [
        ["/start", "/help", "/run"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Выберите команду:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    msg = ""
    for key, value in type_org_mapping.items():
        if value != "":
            msg += f"<code>{key}</code>: {value}\n"
    await update.message.reply_text("Введите одно ключевое слово из списка (например: flowers)", parse_mode='HTML')
    await update.message.reply_text(msg, parse_mode='HTML')


async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправить сообщение с просьбой ввести строку и установить состояние ожидания"""
    await update.message.reply_text("Пожалуйста, введите ключевое слово из списка (/help)")
    text = update.message.from_user
    print(text)
    return text


async def handle_user_input(update: Update, context: CallbackContext) -> None:
    """Получить слово от пользователя и передать его в другую функцию."""
    user_input = update.message.text
    print(f'[Сообщение] {update.message.from_user["first_name"]}: {user_input}')
    user_input = user_input.lower().split()
    valid_inputs = [key for key in type_org_mapping.keys()]

    for word in user_input:
        if word in valid_inputs:
            await process_user_input(update, context, word)
        else:
            await update.message.reply_text(f"Неверный ввод. '{word}' отсутсвует в списке. Пожалуйста, попробуйте снова.")
            await run(update, context)


async def process_user_input(update: Update, context: CallbackContext, input_word: str) -> None:
    """Обработка слова, введенного пользователем."""
    # Здесь вы можете добавить логику обработки слова
    print(f"Запрос: {input_word}")
    await update.message.reply_text(f"Поиск по запросу {[input_word]} запущен...", parse_mode='HTML')
    try:
        update_list(input_word)
        await update.message.reply_text(f"Идет сбор данных...", parse_mode='HTML')
        parse_info(update.message.chat_id)
        await json_print(update, context, input_word)
    except Exception as ex:
        # Отправка ошибки пользователю
        print(ex)
        await update.message.reply_text(f"Произошла ошибка, поиск прерван")


async def json_print(update: Update, context: ContextTypes.DEFAULT_TYPE, input_word):
    # Загрузка данных из JSON-файла
    async with aiofiles.open("Excels/data.json", mode="r", encoding="utf-8") as f:
        content = await f.read()
        data = json.loads(content)
        if not data:
            msg = "Новых точек не найдено"
            await update.message.reply_text(msg, parse_mode='HTML')
    # Форматируем и отправляем каждую запись как отдельное сообщение
    for entry in data:
        msg = ""
        for key, value in entry.items():
            if value != "":
                msg += f"{hbold(key)}: {value}\n"
        max_retries = 10  # максимальное количество попыток
        for _ in range(max_retries):
            try:
                await update.message.reply_text(msg, parse_mode='HTML')
                break  # если сообщение отправлено успешно, выходим из цикла
            except RetryAfter as e:
                print(e)
                print("Превышен лимит отправки сообщений. Ожидание: 12 сек.")
                await asyncio.sleep(10 + 2)
            except TimedOut:
                print("Время ожидания истекло. Повторная попытка отправить сообщение...")
                await asyncio.sleep(5)  # небольшая задержка перед следующей попыткой
        else:
            # Этот блок будет выполнен, если цикл завершился без "break", т.е. после всех попыток
            print(f"Не удалось отправить сообщение после {max_retries} попыток.")
            await update.message.reply_text("Ошибка при отправке данных. Попробуйте позже.", parse_mode='HTML')
            return
    # Отправка exel таблицы пользователю
    try:
        async with aiofiles.open(f'Excels/Table_{update.message.chat_id}.xlsx', 'rb') as excel_file:
            data = await excel_file.read()
            await update.message.reply_text("Найденные точки в виде Excel таблицы:", parse_mode='HTML')
            await context.bot.send_document(update.message.chat_id, document=data, filename=f"Таблица_{update.message.chat_id}.xlsx")
    except Exception as ex:
        print(ex)
    await update.message.reply_text(f"Поиск по {input_word} завершен", parse_mode='HTML')
    print(f"Поиск по {input_word} закончился")


def main(tkn):
    application = Application.builder().token(tkn).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler('run', run))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_input))

    # executor.start_polling(dp, skip_updates=True)
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main(token)
