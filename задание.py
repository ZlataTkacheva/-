from collections import namedtuple
s1=int(input("Введите кол-во студентов: "))
k1=int(input("Введите кол-во предметов: "))
s=[]*s1
k=[]*k1
Jour=[]#тут будет список всех студентов с предметов и оценкой
wh=1
zz4=0 #Для 4 задания
zz5=0 #6 задание, для подсчета кол-во 4
zzz5=0#6 задание, для подсчета кол-во 4
kk1=0#для задания 5
nnp=[]#список неуспевающих студентов задание 6
pp2=0 #кол-во хорошистов студентов для 5 задания
pp1=0 #Для задания 5
pp=0 #По скольким предметам выставили оценки-нужно для 4 задания
sz=0 #для 2 задания-складываем оценки ученика по всем предметам
sz1=0 #для 2 задания-узнаем колв оценок
ssz=[] #Массив для 2 задания, чтобы записать кортеж
szp=0 #для 3 задания-складываем оценки группы по предмету
szp1=0 #для 3 задания-складываем кол-ов оценок группы
ssp=[] #Массив для 3 задания, чтобы записать кортеж
sf=[] #Для задания 4, тут будут фамилии
Journal=namedtuple('Journal', ['FIO',  'predmet', 'ocenka'])
SO=namedtuple('SO',['FIO1','srbl']) #для 2 задания 1)ФИО, 2)Среднее значение
SOP=namedtuple('SOP',['predmet1','sbl']) #для 3 задания 1)Предмет 3)Сренее значение
for i in range(s1):
    s2=str(input("Введите ФИО студента: "))
    s.append(s2)
for i in range (k1):
    k2=str(input("Введите название предмета: "))
    k.append(k2)
def ocenk(v):
        for i in range(s1):
            print("Введите оценку",s[i],"по ", k[v])
            st=Journal(s[i],k[v],int(input("Введите оценку: ")))
            Jour.append(st)
while wh!=0:
    oc=int(input("Задание 1-введите 1 если хотите выставить оценки или любое число, чтобы пропустить этот пункт: "))
    while oc!=0 and pp!=k1:
        for i in range(k1):
            print (k[i])
        nm=int(input("Введите номер предмета, по которому хотите ввести оценку: "))
        x=ocenk(nm-1)
        pp+=1
        oc=int(input("Если больше не будете вводить оценки, нажмите 0 "))
    print ("PP=",pp)
    z1=int(input("Введите 1, если хотите увидеть весь список группы с оценками или любое число, чтобы пропустить этот пункт: "))
    if z1==1:
        for i in range(len(Jour)):
          print(Jour[i].FIO,"Оценка по предмету ",Jour[i].predmet,":", Jour[i].ocenka)
    z2=int(input("Введите 1 если хотите узнать средний балл каждого студента или любое число, чтобы пропустить этот пункт: "))
    if z2==1:
            for i in range (s1):
             for j in range (len(Jour)):
                if Jour[i].FIO==Jour[j].FIO:
                    sz+=Jour[j].ocenka
                    sz1+=1
             sz=sz/sz1
             st=SO(Jour[i].FIO,sz)
             ssz.append(st)
             sz=0
             sz1=0
            for i in range (len(ssz)):
              print(ssz[i].FIO1, ssz[i].srbl)
    z3=int(input("Dведите 1 если хотите узнать средний бал группы по предмету или любое число, чтобы пропустить этот пункт: "))
    if z3==1:
     for i in range (k1):
        for j in range (len(Jour)):
            if k[i]==Jour[j].predmet:
                szp+=Jour[j].ocenka
                szp1+=1
        szp=szp/szp1
        st=SOP(k[i],szp)
        ssp.append(st)
        szp=0
        szp1=0
     for i in range (len(ssp)):
        print(ssp[i].predmet1,ssp[i].sbl)
    z4=int(input("Dведите 1, чтобы получить списки фамилий назначеных на повышенную степендию или любое число, чтобы пропустить этот пункт: "))
    if z4==1:
        for i in range(s1):
            for j in range(len(Jour)):
                if s[i]==Jour[j].FIO:
                    if Jour[j].ocenka==5:
                        zz4+=1
            if zz4==pp:
                sf.append(s[i])
            zz4=0
        print(sf)
    z5=int(input("Введите 1, чтобы получить списки фамилий назначеных на обычную степендию или любое число, чтобы пропустить этот пункт: "))
    if z5==1:
        for i in range (s1):
            for j in range(len(Jour)):
                if s[i]==Jour[j].FIO:
                    if Jour[j].ocenka==4:
                        zz5+=1  
                    else: 
                        if Jour[j].ocenka==5:
                          zzz5+=1
            if zz5>0 and zzz5+zz5==pp:
                pp2+=1
            zz5=0
            zzz5=0
        print("Студентов назначенных на повышенную степендию: ", pp2)
    z6=int(input("Введите 1,чтобы вывести список неуспевающих студентов или любое число, чтобы пропустить этот пункт:"))
    if z6==1:
         for i in range (s1):
             for j in range (len(Jour)):
                 if s[i]==Jour[j].FIO:
                     if Jour[j].ocenka==2:
                         kk1+=1
             if kk1>0:
                 nnp.append(s[i])
             kk1=0
         print(nnp)
    wh=int(input("Напишите 0 для завершения программы или другое число для продолжения работы: "))
    
                     
 