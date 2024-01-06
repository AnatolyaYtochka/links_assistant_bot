import telebot
bot = telebot.TeleBot('6676962160:AAFyBONqDjXXkTnuGGuPusFsQJCIVX-6HrU')
start_txt = 'Здорова, бандиты 😘 \n \n ✏ Че, ссылки редачить не умеете? Хэлпану!  \n \n  Пж, пришли хреновую ссылку 🥱'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def createCorrectLink(message):
  badLink = message.text
  number = ''
  badLink = badLink.replace('%2', '')
  for i in badLink:
    if i.isdigit():
      number += i
  if number.isdigit() and len(number) == 9:
    if 'umschool' in badLink:
        bot.send_message(message.from_user.id, '👉 Корректная ссылка: https://old.umschool.net/homework/submissions/' + number + '/')
    elif 'vk' in badLink:
        bot.send_message(message.from_user.id, '👉 Корректная ссылка: https://vk.com/id' + number)
  else:
    bot.send_message(message.from_user.id, 'Это не ссылка, а туфта, я такое не ем 😖')
  bot.send_message(message.from_user.id,'Внимание: спасибо за внимание! Жду еще ссылок 😍')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')
