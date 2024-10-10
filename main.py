import re
def word_search(text: str, word: str,num_of_Err:int=0, Ignore_case:bool=True, replacement:str ='')->list:#text- текст в котором ищем; word- слово которое ищем; num_of_Err- количество допустимых ошибок; Ignore_case- игнорироватьгнорировать ли регистр (если True то игнорировать); replacement- если его указать, то все найденные слова будут заменены на replacement
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
    offers=re.split(r'[.\n?]+', text)
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
                    elif replacement!='': #замена слова
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
                if counter>=len_of_word- num_of_Err:
                    if replacement=='':
                        result.append(i)
                    elif replacement!='': #замена слова
                        for h in words:
                            if h!=uo:
                                sub_result+=h+' '
                            elif h==uo:
                                sub_result+=replacement+' '
                    #print(u, len_of_word, counter, difference)
                        result.append(sub_result[0:len(sub_result)-1]+'.')
                counter=0
                sub_couter1=0
                sub_couter2=0
    return result
# tex=''' For almost any person, there is nothing more important in the world than their family. I love my family too. Today I would like to tell you about them.

# My family is quite big. It consists of my mother, father, my three siblings and our cat Bob. Well, most people would say that a pet is not a family member but no one in our family would agree with that. We all love Bob and consider him a family member.

# My mother’s name is Anna, she is a teacher. She has been working in our local school for a long time. My mom teaches History and Social Studies, the subjects that I really love! She loves reading very much, and her favorite book is “A Street Cat Named Bob” by James Bowen. If you are familiar with the book, you can guess why she named our ginger cat Bob.

# My father’s name is Igor. He is a little older than mom and he used to be a police officer. He retired at a quite young age and has been running his own business ever since. He has a small coffee shop and a candy store. To be honest, I don’t know much about his business, but he says it is doing well.

# As for my siblings, I have a sister, her name is Maria, and she is the oldest one, and two brothers – Viktor and Boris. By the way, I am the youngest child in the family but I am totally happy with that role. My sister Maria is an engineer, she lives in another town but visits us at least once a month. My brothers are still students. Viktor studies history, following in our mother’s footsteps, Boris is going to be a software developer. He is a big fan of videogames, and his dream is to develop his own game.

# In conclusion, I would like to say that I love my family and for me there is nothing more important than them. I think, they all have the same opinion. Even Bob.'''
# print(word_search(tex,'really', 2,True, 'ДААААААААААААААААААААА'))
