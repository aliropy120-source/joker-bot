import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
USERNAME = "@alsacr1"
LINK = "https://t.me/alsacr1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = f"""مرحبا بيك في إمبراطورية الصقور - مملكة الزعيم لبيع حسابات eFootball 👑🔥

لبيع وشراء حسابات eFootball بيس بأمان وضمان 🔥
تواصل مع الزعيم مباشرة: {USERNAME}
"""
    keyboard = [
        [InlineKeyboardButton("👑 تواصل مع الزعيم", url=LINK)],
        [InlineKeyboardButton("🎮 عروض eFootball بيس", callback_data="offers")],
        [InlineKeyboardButton("📜 الشروط", url=LINK)]
    ]
    await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "offers":
        text = f"""🔥 باقات eFootball بيس المتاحة:

1- حسابات قوية - تواصل لمعرفة السعر
2- حسابات نجوم - تواصل لمعرفة السعر  
3- حسابات أسطورية - تواصل لمعرفة السعر

للطلب تواصل: {USERNAME}
الرابط: {LINK}
"""
        keyboard = [[InlineKeyboardButton("تواصل الآن 👑", url=LINK)]]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    print(f"Bot Running with {USERNAME}")
    app.run_polling()

if __name__ == "__main__":
    main()
