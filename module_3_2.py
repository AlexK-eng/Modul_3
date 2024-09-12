# This is a Task 3_2.
def send_email(message, recipient, sender="university.help@gmail.com"):
    if recipient.count('@') != 1 or sender.count('@') != 1:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if recipient == sender:
        return print(f'Нельзя отправить письмо самому себе!')

    if recipient[-4:] == '.com' or recipient[-4:] == '.net' or recipient[-3:] == '.ru':
        if sender[-4:] == '.com' or sender[-4:] == '.net' or sender[-3:] == '.ru':
            if 'university.help@gmail.com' == sender:
                return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            return print(
                f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')  # Проверку не прошел отправитель
    else:
        return print(
            f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')  # Проверку не прошел получатель


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
