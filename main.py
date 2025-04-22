# main.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
import logging

# Настройка логгера
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Стартовое сообщение с кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Проверить заказы", callback_data='check_orders')],
        [InlineKeyboardButton("Статистика", callback_data='stats')],
        [InlineKeyboardButton("Настройки", callback_data='settings')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Выберите действие:', reply_markup=reply_markup)

# Обработка нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'check_orders':
        await query.edit_message_text(text="🔄 Идёт проверка заказов...")
        # Здесь будет логика получения заказов
    elif query.data == 'stats':
        await query.edit_message_text(text="📊 Показываю статистику...")
        # Здесь будет логика показа статистики
    elif query.data == 'settings':
        await query.edit_message_text(text="⚙️ Настройки пока недоступны.")

# Запуск бота
if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()