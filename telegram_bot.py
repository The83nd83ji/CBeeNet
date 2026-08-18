# telegram_bot.py
# Telegram bot for CBeeNet Gateway - RVG integration
import asyncio
import os
import json
from datetime import datetime
from main import LINKS, LINKS_LOCK, SUBS, SUBS_LOCK, logger, fmt_bytes, get_host, generate_uuid

try:
    from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
    TELEGRAM_AVAILABLE = True
except ImportError:
    TELEGRAM_AVAILABLE = False
    logger.warning("python-telegram-bot not installed. Telegram bot disabled.")

# Telegram bot token from environment
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

bot_instance = None

async def send_message(chat_id: str, text: str, parse_mode: str = "HTML"):
    """Send a message via Telegram bot"""
    if not TELEGRAM_AVAILABLE or not BOT_TOKEN:
        return False
    try:
        bot = Bot(token=BOT_TOKEN)
        await bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
        return True
    except Exception as e:
        logger.error(f"Telegram send error: {e}")
        return False

async def send_link_to_telegram(uuid: str, link_data: dict, vless_link: str):
    """Send a new link to Telegram"""
    if not CHAT_ID:
        return
    
    label = link_data.get("label", "New Link")
    used = fmt_bytes(link_data.get("used_bytes", 0))
    limit = "∞" if link_data.get("limit_bytes", 0) == 0 else fmt_bytes(link_data.get("limit_bytes", 0))
    host = get_host()
    sub_url = f"https://{host}/sub/{uuid}"
    
    message = f"""🔗 <b>New Config Created</b>

📌 <b>Name:</b> {label}
📊 <b>Usage:</b> {used} / {limit}
📅 <b>Created:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}

🔗 <b>Subscription:</b> <code>{sub_url}</code>

📱 <b>VLESS Link:</b>
<code>{vless_link[:200]}{'...' if len(vless_link) > 200 else ''}</code>

<i>Use /links to see all configs</i>"""
    
    await send_message(CHAT_ID, message)

async def start_bot():
    """Start the Telegram bot"""
    if not TELEGRAM_AVAILABLE or not BOT_TOKEN:
        logger.warning("Telegram bot not available")
        return
    
    try:
        # Simple bot that just responds to commands
        # For production, use python-telegram-bot's Application
        logger.info("Telegram bot started (simple mode)")
        # In a real implementation, you'd set up proper handlers here
    except Exception as e:
        logger.error(f"Telegram bot startup error: {e}")

# Command handlers for a full bot implementation
if TELEGRAM_AVAILABLE:
    async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🐝 <b>CBeeNet Gateway Bot</b>\n\n"
            "Commands:\n"
            "/links - List all configs\n"
            "/create <name> - Create a new config\n"
            "/info <uuid> - Get info about a config\n"
            "/sub <uuid> - Get subscription link\n"
            "/status - Get server status\n\n"
            "Channel: @CBeeNet",
            parse_mode="HTML"
        )

    async def links_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not LINKS:
            await update.message.reply_text("No configs available.")
            return
        
        lines = []
        async with LINKS_LOCK:
            for uid, link in list(LINKS.items())[:10]:  # Limit to 10
                status = "✅" if link.get("active", True) else "❌"
                used = fmt_bytes(link.get("used_bytes", 0))
                limit = "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link.get("limit_bytes", 0))
                lines.append(f"{status} <b>{link.get('label', 'Unknown')}</b> - {used}/{limit} - <code>{uid[:8]}…</code>")
        
        text = "📋 <b>Configs (last 10):</b>\n\n" + "\n".join(lines)
        await update.message.reply_text(text, parse_mode="HTML")

    async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        from main import stats, connections, uptime
        text = f"""📊 <b>Server Status</b>

🔌 Active connections: {len(connections)}
📦 Total traffic: {fmt_bytes(stats.get('total_bytes', 0))}
📈 Total requests: {stats.get('total_requests', 0)}
⏱️ Uptime: {uptime()}
📋 Total configs: {len(LINKS)}
📁 Sub groups: {len(SUBS)}

<i>CBeeNet Gateway v1.0.0</i>
@CBeeNet"""
        await update.message.reply_text(text, parse_mode="HTML")
