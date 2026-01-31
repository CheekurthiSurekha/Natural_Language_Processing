def is_spam(message):
    spam_words = ["win", "cash", "free", "prize"]

    message = message.lower()

    for word in spam_words:
        if word in message:
            return True

    return False


text = "you are WINNING a free prize now!"

if is_spam(text):
    print("Spam detected")
else:
    print("Not spam")