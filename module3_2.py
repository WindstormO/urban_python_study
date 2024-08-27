def email_check(sender="university.help@gmail.com", recipient=""):
    if not "@" in sender:
        return(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender[-3:]==".ru":
        return(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender[-4:]==".com":
        return(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender[-4:]==".net":
        return(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        return(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


print(email_check())
