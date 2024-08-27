def send_email(message="", recipient="", sender="university.help@gmail.com"):
    if (not "@" in sender) or not(sender[-3:]==".ru" or sender[-4:]==".com" or sender[-4:]==".net"):
        return(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient==sender:
        return(f"Нельзя отправить письмо самому себе!")
    elif sender=="university.help@gmail.com":
        return(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


print(
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'),
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'),
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'),
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'),
          )
