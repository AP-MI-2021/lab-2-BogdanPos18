#Problema 1
def get_largest_prime_below(n):
    if n <= 2:
        return -1
    found = 0
    largest = n-1
    while found == 0:
        ok = 1
        for i in range(2, largest//2+1):
            if n % i  == 0:
                ok = 0
        if ok == 1:
            found = 1
        else:
            largest -= 1
    return largest

def test_get_largest_prime_below():
    assert (get_largest_prime_below(3) == 2) is True
    assert (get_largest_prime_below(12) == 7) is False


#Problema 13
def get_temp(temp, from_, to):
    if from_ == 'K':
        if to == 'K':
            temp += 0
        if to == 'F':
            temp = (temp - 273.15) * 1.8 + 32
        if to == 'C':
            temp -= 273.15
    if from_ == 'F':
        if to == 'K':
            temp = (temp - 32) * 5/9 + 273.15
        if to == 'F':
            temp += 0
        if to == 'C':
            temp = (temp - 32) / 1.8
    if from_ == 'C':
        if to == 'K':
            temp += 273.15
        if to == 'F':
            temp = temp * 1.8 + 32
        if to == 'C':
            temp += 0
    return temp

def test_get_temp():
    assert (get_temp(34, 'C', 'K') == 309.15) is False
    assert (get_temp(32, 'F', 'C') == 1.00) is False

#Problema 14
def get_cmmmc(numbers):
    #Functia calculeaza cmmdc-ul a cate doua numere consecutive folosind algoritmul lui Euclid, apoi
    #se foloseste de formula cmmdc(a,b)*cmmmc(a,b)=a*b pentru a calcula cmmmc-ul a cate doua numere consecutive
    x = numbers[0]
    i = 1
    while i < len(numbers):
        y = numbers[i]
        a = x
        b = y
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        m = a*b / x
        x = m
        i += 1
    return m

def test_get_cmmmc():
    v = [3, 5, 7, 9]
    assert (get_cmmmc(v) == 315) is True
    a = [5, 9, 4, 13]
    assert (get_cmmmc(a) == 2341) is False

#Programul principal
def program():
    print("Pentru a folosi functia get_largest_prime_below(), apasati tasta 1\n")
    print("Pentru a folosi functia get_temp(), apasati tasta 2\n")
    print("Pentru a folosi functia get_cmmmc(), apasati tasta 3\n")
    a = str(input())
    if a == '1':
        test_get_largest_prime_below()
        n = int(input("Introduceti un numar: "))
        if get_largest_prime_below(n)==-1:
            print("Nu exista!")
        else:
            print(get_largest_prime_below(n))
    if a == '2':
        test_get_temp()
        print("Pentru a citi date, apasati tasta Y. Pentru a opri programul, apasati tasta N \n")
        c = str(input())
        while c == 'y':
            temp = float(input())
            from_ = str(input())
            to = str(input())
            print("Temperatura din grade ", from_, " in grade ", to, " este ", get_temp(temp, from_, to), '\n')
            c = str(input())
    if a == '3':
        test_get_cmmmc()
        numbers = []
        n = int(input("Introdu lungimea sirului: "))
        for i in range(0,n):
            x = int(input("Introdu o valoare: "))
            numbers.append(x)
        print(get_cmmmc(numbers))

program()



