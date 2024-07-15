from telegram import Bot, Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Путь к фото, которое вы хотите отправить
        photo_path = 'photo_5458464354870617471_w.jpg'

        # Текст сообщения
        text = """
        <b>Мы рады пригласить вас присоединиться к нашей уникальной и динамичной группе, посвященной всему, что связано с веб-разработкой.</b>\n
Это место, где вы можете делиться знаниями, узнавать новое, находить решения для сложных задач и вдохновляться последними тенденциями в мире технологий и веб-разработки.\n
<b>Что вас ждет:</b>\n
- <i>Еженедельные вебинары от ведущих разработчиков.</i>\n
- <i>Обсуждение актуальных тем и трендов в области фронтенда и бэкенда.</i>\n
- <i>Совместная работа над проектами и возможность получить обратную связь от профессионалов.</i>\n
- <i>Эксклюзивный доступ к ресурсам, курсам и мастер-классам.</i>\n
<b>Присоединяйтесь к нам, если вы:</b>\n
- <i>Ищете сообщество единомышленников.</i>\n
- <i>Хотите повысить свои навыки в веб-разработке.</i>\n
- <i>Желаете делиться своим опытом и знаниями.</i>\n
Для вступления в группу, пожалуйста, перейдите по <a href='https://t.me/prodigy_it'>ссылке.</a>\n
Мы с нетерпением ждем возможности приветствовать вас среди нас!
@prodigy_it
        """

        # Отправка фото с текстом
        with open(photo_path, 'rb') as photo:
            await update.message.reply_photo(photo=photo, caption=text, parse_mode=ParseMode.HTML)

def main() -> None:
    # Вставьте сюда токен вашего бота
    token = '6793318770:AAHTBJ1U4mdWdk_01LQ13mMGbnxTr4ztZkY'

    # Создаём экземпляр ApplicationBuilder и передаем ему токен вашего бота
    application = ApplicationBuilder().token(token).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()