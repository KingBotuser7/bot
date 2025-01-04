import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Token of your bot (get it from @BotFather in Telegram)
TOKEN = "7791718203:AAFpxwcw0E4DCkBTf9o_aCA5622pIXofjv4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /start command"""
    await update.message.reply_text(
        "👑 Welcome! I'm King Bot - your GitHub repository analysis assistant.\n\n"
        "Available commands:\n"
        "/check [repo-url] - Security check of repository\n"
        "/analyze [repo-url] - Code analysis\n"
        "/help - Show all commands"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /help command"""
    await update.message.reply_text(
        "🔍 List of available commands:\n\n"
        "/check [repo-url] - Security check\n"
        "/analyze [repo-url] - Code analysis\n"
        "/contributors [repo-url] - Contributors information\n"
        "/compare [repo1] [repo2] - Compare repositories\n"
        "/similarity [repo-url] - Code similarity check\n"
        "/user [username] - User information"
    )

async def check_repo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /check command"""
    await update.message.reply_text(
        "🔒 Sorry, this feature isn't available now.\n"
        "Please stay tuned and try again later!"
    )

async def analyze_repo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /analyze command"""
    await update.message.reply_text(
        "🔒 This feature is currently under development.\n"
        "We're working hard to make it available soon!"
    )

async def check_similarity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /similarity command"""
    await update.message.reply_text(
        "🔒 Sorry, similarity check is not available at the moment.\n"
        "The feature will be implemented in future updates."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for regular messages"""
    await update.message.reply_text(
        "👋 Hi! I only understand commands. Use /help to see the list of commands."
    )

async def contributors_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /contributors command"""
    await update.message.reply_text(
        "🔒 Contributors information is not available at this time.\n"
        "This feature will be available in the next update!"
    )

async def compare_repos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /compare command"""
    await update.message.reply_text(
        "🔒 Repository comparison feature is coming soon.\n"
        "We're working on making it available for you!"
    )

async def user_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /user command"""
    await update.message.reply_text(
        "🔒 User information lookup is temporarily unavailable.\n"
        "Please check back later for updates!"
    )

def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("check", check_repo))
    application.add_handler(CommandHandler("analyze", analyze_repo))
    application.add_handler(CommandHandler("similarity", check_similarity))
    application.add_handler(CommandHandler("contributors", contributors_info))
    application.add_handler(CommandHandler("compare", compare_repos))
    application.add_handler(CommandHandler("user", user_info))
    
    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main() 