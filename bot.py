async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_info = f"{user.first_name or ''} {user.last_name or ''}".strip()
    if user.username:
        user_info += f" (@{user.username})"
    user_info = user_info or "No name"
    
    text = (
        f"New message:\n\n"
        f"From: {user_info}\n"
        f"User ID: {user.id}\n\n"
        f"Message:\n{update.message.text}"
    )
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)

    # Reply to user with confirmation and unique link
    link = f"https://t.me/questianonbot?start={user.id}"
    response = (
        "✅ Question sent!\n\n"
        "Your link for questions:\n"
        f"{link}\n\n"
        "Share this link with friends and followers to receive anonymous questions and answer them!"
    )
    await update.message.reply_text(response)