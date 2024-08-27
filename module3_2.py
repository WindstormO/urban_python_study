def email_check(sender="university.help@gmail.com"):
    if not "@" in sender:
        return("Не является емейлом")
    elif sender[-3:]==".ru":
        return("RU")
    elif sender[-4:]==".com":
        return("EU")
    elif sender[-4:]==".net":
        return("EU_OLD")
    else:
        return("Не удалось определить домен")


print(email_check())
