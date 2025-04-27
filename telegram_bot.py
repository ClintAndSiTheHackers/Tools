# Import necessary modules from python-telegram-bot library
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import subprocess  # For executing system commands

# Your bot's unique token from BotFather
TOKEN = ""

# Handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send a welcome message when user starts the bot
    await update.message.reply_text("Pi Bot Active. Commands: /cmd [command]")

# Handler for the /cmd command
async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract the command from the message (remove "/cmd " prefix)
    command = update.message.text.replace("/cmd ", "")
    # Execute the command using subprocess and get the output
    result = subprocess.getoutput(command)
    # Send the command output back to the user
    await update.message.reply_text(f"Output:\n{result}")

# Main function to set up and run the bot
def main():
    # Create a new application instance with your bot token
    app = Application.builder().token(TOKEN).build()
    
    # Register command handlers
    # When user types /start, call the start function
    app.add_handler(CommandHandler("start", start))
    # When user types /cmd, call the execute_command function
    app.add_handler(CommandHandler("cmd", execute_command))
    
    # Start the bot and begin polling for updates
    print("Starting bot...")
    # allowed_updates=Update.ALL_TYPES means we want to receive all types of updates
    app.run_polling(allowed_updates=Update.ALL_TYPES)

# Standard Python idiom to run the main function when script is executed directly
if __name__ == "__main__":
    main()