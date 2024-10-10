def word_search(text: str, word: str,num_of_Err:int=0, Ignore_case:bool=True, replacement:str ='')->list:#text- текст в котором ищем; word- слово которое ищем; num_of_Err- количество допустимых ошибок; Ignore_case- игнорироватьгнорировать ли регистр (если True то игнорировать)
    counter=0
    if Ignore_case:#Игнорировать ли регистр
        word=word.upper()
    sub_couter1=0
    sub_couter2=0
    result=[]
    sub_result=''
    if text[len(text)-1]!='.': #Добовляет в конец точку, если её нет для работы split
        text+='.'
    len_of_word=len(word)    #Делит текст на предложения
    offers=text.split('.')
    for i in offers: #Идёт по всем предложениям
        words=i.split()
        for u in words:#Идёт по словам в предложениии
            uo=u
            if Ignore_case:#Игнорировать ли регистр
                u=u.upper()
            if (len(u) - len_of_word)**2<=0: #Данное условие сравнивает длину искомого слова с длиной конкретного слова, это надо будет для ввода с ошибкой (если пользователь забыл пару букв)
                for o in range(len(u)):
                    if word[o] == u[o]: #Узнаёт количество одинаковых букв
                        counter+=1
                if counter>=len_of_word- num_of_Err: #Это условие указывает подходит ли слово, учитывая количество букв в искомом слове, количесво совпадений и допустимое количесво ошибок
                    if replacement=='':
                        result.append(i)
                    elif replacement!='':
                        for h in words:
                            if h!=uo:
                                sub_result+=h+' '
                            elif h==uo:
                                sub_result+=replacement+' '
                        #print(u)
                        
                        result.append(sub_result[0:len(sub_result)-1]+'.')
                counter=0
                sub_result=''
            elif (len(u) - len_of_word)**2<=num_of_Err**2:
                difference=(len(u) - len_of_word)**2
                difference=int(difference**0.5)
                u1=u[0:len(u)-difference]
                u2=u[difference:len(u)]
                for o in range(len(u)-difference):
                    if word[o] == u1[o]:
                        sub_couter1+=1
                    if word[o] == u2[o]:
                        sub_couter2+=1
                if sub_couter2>=sub_couter1:
                    counter=sub_couter2
                elif sub_couter1>sub_couter2:
                    counter=sub_couter1
                if len_of_word- counter- num_of_Err<=0:
                    result.append(i)
                    #print(u, len_of_word, counter, difference)
                counter=0
                sub_couter1=0
                sub_couter2=0
    return result
# tex=''' Hello fa. Ja. asd. 34. 42. hello hghg.kello uiui'''
# print(word_search(tex,'Hello', 1,True))
