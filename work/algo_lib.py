from re import split
def word_search(text: str, word: str,num_of_Err:int=0, Ignore_case:bool=True, replacement:str ='', repair:bool=False)->str:#text- текст в котором ищем; word- слово которое ищем; num_of_Err- количество допустимых ошибок; Ignore_case- игнорироватьгнорировать ли регистр (если True то игнорировать); replacement- если его указать, то все найденные слова будут заменены на replacement; Если repair = True то все найденные слова с ошибками юудут заменены на искомое слово (не рекомендуется при допустимом количесте ошибок>30% от длины слова)
    copy_of_word=word
    counter=0 #счётчик правильности слова
    if repair and replacement=='' : #Если включена функция замены слов с ошибкой на правельное и отключена функция замены слова, то замена слова = самому слову
        replacement=word
    if len(text)==0: #Если пользователь передал пустой текст, то текст равен 1 пробелу, во избежания ошибок
        text=' '
    text=text.replace('(',' (')#Исправляем ошибку при которой человек не ставит пробел до или полсе скобок, и те прилипают к внешнему слову
    text=text.replace(')',') ')
    if Ignore_case:#Игнорировать ли регистр
        word=word.upper()
    sub_couter1=0#Вспомогательный счётчик правильности
    sub_couter2=0#Вспомогательный счётчик правильности
    result=[]#Список предложений с искомым словом
    sub_result=''#Вспомогательный str для result
    if text[len(text)-1]!='.': #Добовляет в конец точку, если её нет для работы split
        text+='.'
    len_of_word=len(word)    #Делит текст на предложения
    offers=split(r'[.?!]+', text) #Делит текст на преложения. re надо для того, чтобы не писать 3 split
    for i in offers: #Идёт по всем предложениям
        words=i.split() #Делит предложение на слова
        for u in words:#Идёт по словам в предложениии
            if u[len(u)-1]==',' or u[len(u)-1]=='.' : #Уберает в cловах запятую и точку
                u=u[0:len(u)-1]
            uo=u #вспомогательная переменная копирующая текущие слово
            u=u.replace('(',' ')#Убераем скобки для коректного поска слова
            u=u.replace(')',' ')#Убераем скобки для коректного поска слова
            u=u.replace(' ','')#Убераем пробелы для коректного поска слова
            if Ignore_case:#Игнорировать ли регистр
                u=u.upper() #Если мы игрорируем регистр то все буквы в слове становятся заглавными
            if (len(u) - len_of_word)**2<=0: #Данное условие сравнивает длину искомого слова с длиной конкретного слова, это надо будет для ввода с ошибкой (если пользователь забыл пару букв)
                for o in range(len(u)):
                    if word[o] == u[o]: #Узнаёт количество одинаковых букв
                        counter+=1
                if counter>=len_of_word- num_of_Err: #Это условие указывает подходит ли слово, учитывая количество букв в искомом слове, количесво совпадений и допустимое количесво ошибок
                    #print(u)
                    if replacement=='': #Смотрит есть ли замена
                        result.append(i)
                    elif replacement!='': #замена слова
                        for h in words: #Идёт по словам, для добовления их в result и замены искомого слова
                            if h!=uo and h!=uo+',' and h!=uo+'.': #Проверяет не заменялимое ли это слово
                                #print(h, uo)
                                sub_result+=h+' ' #Создаёт предложенииe из слов
                            elif h==uo or h==uo+',' or h==uo+'.':
                                sub_result+=replacement+' '  #Создаёт предложенииe из слов
                        result.append(sub_result[0:len(sub_result)-1]+'.')#Добовляет предложенииe в result и точку в конец
                counter=0 #Обнуление счётчика
                sub_result='' #Обнуление вспомогательного str
            elif (len(u) - len_of_word)**2<=num_of_Err**2: #Это условие проходит если длинна слова не совподает на количесво ошибок или меньше
                difference=(len(u) - len_of_word)**2 #делает difference положительным
                difference=int(difference**0.5) #делает difference положительным
                u1=u[0:len(u)-difference] #Создаёт вспомогательную переменную содержащию текущиеслово урезанное до размеров искомого слова
                u2=u[difference:len(u)] #Создаёт вспомогательную переменную содержащию текущиеслово урезанное до размеров искомого слова
                for o in range(len(u)-difference):
                    if word[o] == u1[o]:
                        sub_couter1+=1
                    if word[o] == u2[o]:
                        sub_couter2+=1
                if sub_couter2>=sub_couter1:#Поиск наибольшего резулятата и приравнивание его к основному счётчику
                    counter=sub_couter2
                elif sub_couter1>sub_couter2:
                    counter=sub_couter1
                if counter-abs(difference)>=len_of_word- num_of_Err:
                    if replacement=='':
                        #print(u)
                        result.append(i)
                    elif replacement!='': #замена слова
                        for h in words: #идёт по словам в предложении и добовляет их в результат
                            if h!=uo  and h!=uo+',' and h!=uo+'.':#Проверяет не заменялимое ли это слово
                                sub_result+=h+' ' #Вы это читаете?
                            elif h==uo or h==uo+',' or h==uo+'.': # Если это искомое слово, то вместо него вставляется замена
                                sub_result+=replacement+' '
                        result.append(sub_result[0:len(sub_result)-1]+'.')#Добовляет в результат предложение без последнего символа (он всегда пробел) и добовляет в конец точку (ранее мы её удалили для коректного поиска слова)
                elif counter-abs(difference)<len_of_word- num_of_Err: #Очень хитрый алгоритм, который находит cлово с отсутвующей буквой посреди слова
                    counter=0 #Обнуление счётчика
                    # print(u)
                    for j in range(1,len(u)+1): #Идёт по длине слова пропуская 1 букву
                        # print('u')
                        for j2 in range(1,num_of_Err+1): #Идёт от 1 до количесва ошибок
                            u3=u[0:j]+' '*j2+u[j:len(u)] # Добовляет пробелы посреди слова, для того, чтобы прошла проверка если пользователь забыл символ посреди слова ("Солнце", "Сонце")
                            rp=max(len(u3),len_of_word)
                            ml=min(len_of_word, len(u3))# вычисляет минимальное слово, чтобы не выйти за границы
                            for o in range(ml): #идёт от 0 до длины минимального слова
                                if word[o] == u3[o]:#сравнивает буквы в текущем слове и искомом
                                    counter+=1
                            if counter>=rp-num_of_Err:#если это то самое слова то выходим из цыкла
                                break
                            else:
                                counter=0 #Если это слово не подходим то обнуляем счётчик
                        if counter>=rp- num_of_Err:#если это то самое слова то выходим из цыкла
                            break
                    if counter>=rp- num_of_Err:#если это то записываем предложение в котором оно находится
                        if replacement=='':
                            # print(word, u,u3, counter,num_of_Err,len_of_word)
                            result.append(i)
                        elif replacement!='': #замена слова
                            for h in words:
                                if h!=uo  and h!=uo+',' and h!=uo+'.':#Проверяет не заменялимое ли это слово
                                    sub_result+=h+' '
                                elif h==uo or h==uo+',' or h==uo+'.':
                                    sub_result+=replacement+' '
                            result.append(sub_result[0:len(sub_result)-1]+'.')
                counter=0 #Обнуление счётчика
                sub_couter1=0 #Обнуление вспомогательного счётчика
                sub_couter2=0 #Обнуление вспомогательного счётчика
    final_result="Всего найдено "+str(len(result))+' совпадений '+'cо словом "'+ copy_of_word +'" :\n'#Создаю переменную где будет храниться отформатированный вывод
    result.append(1)
    b=0
    for i in range(len(result)-1):#Форматирование вывода
        result[i]=result[i].replace('  ',' ')#Убераем двойные пробелы
        if result[i]!=result[i+1]:
            while result[i][0]=='\n' or result[i][0]==' ' :#Если в начале Enter или пробел то мы его убераем
                result[i]=result[i][1:]
            final_result+=str(i+1-b)+'. '+result[i]+'\n'
        else:
            b+=1
    return final_result #Возврат списка предложений с искомым словом