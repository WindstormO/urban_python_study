def email_check(sender="", recipient=""):
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


def send_email(message="", sender="university.help@gmail.com", recipient=""):
    if bool(email_check(sender, recipient)):
        print(email_check)
    else:
        if recipient==sender:
            return(f"Нельзя отправить письмо самому себе!")
        elif sender=="university.help@gmail.com":
            return(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            return(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email(('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
