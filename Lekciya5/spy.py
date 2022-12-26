from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

#сделаем метод  – обертку, над командами
async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
#  создадим файл
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}')
    file.close()