import telebot
from algo_lib import *
config=[0,True, '', False, False] #Настройки по умолчанию
text=''
word=''
# Создаем экземпляр бота
bot = telebot.TeleBot('7028322889:AAFlpNzeaWNOyVTPYvrIAJ2iWNL9QxYtMsI')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    print(m.from_user)
    bot.send_message(m.chat.id, 'Это бот поисковик, напишите "/search" для поиска, "/setting" для настроек, "/my_setting" чтобы посмотреть мои настройки или "/rules" чтобы посмотреть предостережения при использовании этого бота')
@bot.message_handler(commands=["rules"])
def send_rules(m):
    rules='Предостережения при пользовании этим ботом:\n 1. Не выставлять "Количество ошибок" больше чем 50% от длинны слова \n 2. Не забывайте разделять предложения \n 3. Просьба не включать исправление слова если "Количество ошибок" больше 3-4'
    bot.send_message(m.chat.id,rules)
@bot.message_handler(commands=["search"])
def get_text_messages(m, res=False):
    bot.send_message(m.chat.id,"Введите текст в котором будет проходить поиск:")
    bot.register_next_step_handler(m, get_word_messages)
def get_word_messages(m):
    global text
    print(m.text)
    text=m.text
    bot.send_message(m.chat.id,"Введите слово которое будет искаться:")
    bot.register_next_step_handler(m, search)
def search(m):
    word=m.text
    bot.send_message(m.chat.id, word_search(text,word,config[0],config[1],config[2],config[3],config[4]))
@bot.message_handler(commands=["my_setting"])
def my_setting(m):
    bot.send_message(m.chat.id, f"Количество ошибок задано: {config[0]}")
    if config[1] == True:
        bot.send_message(m.chat.id, "Игнорирование регистра включено")
    else:
        bot.send_message(m.chat.id, "Игнорирование регистра выключено")
    if config[2]!='':
        bot.send_message(m.chat.id, f"Искомое слово заменяется на {config[2]}")
    else:
        bot.send_message(m.chat.id, f"Искомое слово не заменяется")
    if config[3]==False:
        bot.send_message(m.chat.id, "Искомое слово не заменяется на правильное")
    else:
        bot.send_message(m.chat.id, "Искомое слово заменяется на правильное")
    if config[4]==True:
        bot.send_message(m.chat.id, "Бот ищет искомое слово как часть другого")
    else:
        bot.send_message(m.chat.id, "Бот не ищет искомое слово как часть другого")
@bot.message_handler(commands=["setting"])
def setting(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    num_of_err = telebot.types.InlineKeyboardButton(text='Количество ошибок', callback_data='num_of_err')
    keyboard.add(num_of_err)
    Ignore_case = telebot.types.InlineKeyboardButton(text='Игнорировать ли регистр', callback_data='Ignore_case')
    keyboard.add(Ignore_case)
    replacement = telebot.types.InlineKeyboardButton(text='Заменять ли найденное слово', callback_data='replacement')
    keyboard.add(replacement)
    repair = telebot.types.InlineKeyboardButton(text='Заменять ли искомое слово с ошибкой на правильное', callback_data='repair')
    keyboard.add(repair)
    part_of_word = telebot.types.InlineKeyboardButton(text='Искать ли искомое слово как часть другого',callback_data='part_of_word')
    keyboard.add(part_of_word)
    bot.send_message(message.from_user.id, text='Выбери, что ты хочешь настроить:', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data=='num_of_err':
        bot.send_message(call.message.chat.id, "Введите допустимое количество ошибок:")
        bot.register_next_step_handler(call.message, set_num_of_err)
    elif call.data=='part_of_word':
        part=telebot.types.InlineKeyboardMarkup()
        part_yes=telebot.types.InlineKeyboardButton(text='Да', callback_data="part_yes")
        part.add(part_yes)
        part_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data="part_no")
        part.add(part_no)
        bot.send_message(call.message.chat.id, text='Искать ли искомое слово как часть другого?',reply_markup=part)
    # НАЧАЛО БЛОКА part_of_word
    elif call.data=='part_yes':
        config[4]=True
        bot.send_message(call.message.chat.id,'Теперь бот ищет искомое слово как часть другого')
    elif call.data=='part_no':
        config[4] = False
        bot.send_message(call.message.chat.id, 'Теперь бот не ищет искомое слово как часть другого')
    # КОНЕЦ БЛОКА part_of_word
    elif call.data=='repair':
        dsa = telebot.types.InlineKeyboardMarkup()
        DA = telebot.types.InlineKeyboardButton(text='Да', callback_data="True_repair")
        dsa.add(DA)
        NET = telebot.types.InlineKeyboardButton(text='Нет', callback_data="False_repair")
        dsa.add(NET)
        bot.send_message(call.message.chat.id, text='Заменять ли искомое слово с ошибкой на правильное?', reply_markup=dsa)
    # НАЧАЛО БЛОКА repair
    elif call.data=="True_repair":
        config[3]=True
        bot.send_message(call.message.chat.id, "Искомое слово будет заменятся на правильное.")
    elif call.data=="False_repair":
        config[3]=False
        bot.send_message(call.message.chat.id, "Искомое слово будет не заменятся на правильное.")
    # КОНЕЦ БЛОКА repair
    elif call.data=='Ignore_case':
        asd = telebot.types.InlineKeyboardMarkup()
        YES=telebot.types.InlineKeyboardButton(text='Да', callback_data="True")
        asd.add(YES)
        NO = telebot.types.InlineKeyboardButton(text='Нет', callback_data="False")
        asd.add(NO)
        bot.send_message(call.message.chat.id, text='Игнорировать регистр?', reply_markup=asd)
    # НАЧАЛО БЛОКА Ignore_case
    elif call.data == "True":
        config[1] = True
        bot.send_message(call.message.chat.id, "Игнорирование регистра включено.")
    elif call.data == "False":
        config[1] = False
        bot.send_message(call.message.chat.id, "Игнорирование регистра отключено.")
    # КОНЕЦ БЛОКА Ignore_case
    elif call.data=='replacement':
        dsa = telebot.types.InlineKeyboardMarkup()
        YS = telebot.types.InlineKeyboardButton(text='Да', callback_data="YES")
        dsa.add(YS)
        N = telebot.types.InlineKeyboardButton(text='Нет', callback_data="NO")
        dsa.add(N)
        bot.send_message(call.message.chat.id, text='Заменять найденное слово?', reply_markup=dsa)
    # НАЧАЛО БЛОКА replacement
    elif call.data == "NO":
        config[2]=''
        bot.send_message(call.message.chat.id, "Замена отключена")
    elif call.data == 'YES':
        bot.send_message(call.message.chat.id, "Введите на какое слово надо заменять:")
        bot.register_next_step_handler(call.message, set_replacement)
    # КОНЕЦ БЛОКА replacement
def set_num_of_err(m):
    try:
        config[0] = int(m.text)
        bot.send_message(m.chat.id, f"Количество ошибок задано: {config[0]}")
    except ValueError:
        bot.send_message(m.chat.id, "Ошибка! Пожалуйста, введите корректное число.")
        bot.register_next_step_handler(m, set_num_of_err)
def set_replacement(m):
    config[2]=m.text
    bot.send_message(m.chat.id, f"Искомое слово заменяется на: {config[2]}")
bot.polling(none_stop=True, interval=0)#Бот будет работать вечно
