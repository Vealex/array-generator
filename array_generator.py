from random import randint

def generator(n):
    #возвращвемый массив
    mainMass = []
    #массив для проверки уникальности размерностей
    sizeNum = []
    
    #заполнение возвращаемого массива
    for i in range(n):
        mainMass.append([])
        size = randint(0, n)
        
        #проверка на уникальность размерности
        while True:
            flag = False
            for k in sizeNum:
                if k == size:
                    flag = True
            if flag:
                size = randint(1, n)
            else:
                sizeNum.append(size)
                break
        
        #Заполнение массивов случайными числами
        for j in range(size):
            mainMass[i].append(randint(-n*10, n*10))
        
        #сортировка массивов    
        if i / 2 == 0:
            mainMass[i].sort()
        else:
            mainMass[i].sort(reverse = True)
    
    #возврат массива
    return mainMass