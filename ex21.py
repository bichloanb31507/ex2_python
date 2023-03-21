with open('D:\input.txt', 'r') as file:
    arr = []
    for line in file:
        row = [int(x) for x in line.split()]
        arr.append(row)  
  
def check_prime_number(n):
    flag = 1;
    if (n <2):
        flag = 0
        return flag
    
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag
      

def ex1a():
    countChan = 0
    countLe = 0
    for row in arr:
        for element in row:
            if (element % 2 == 0):
                countChan += 1
            else:
                countLe += 1                
    print(f"Có {countChan} số chẵn và {countLe} số lẻ")


def ex1b():
    count = 0
    for row in arr:
        for element in row:
            if (check_prime_number(element) != 0):
                count += 1     
    print(f"Có {count} số nguyên tố") 
    

def ex1c():
    countMax = 0
    save = None
    for row in arr:
        for element in row:
            count = row.count(element)
            if count > countMax:
                countMax = count
                save = element
    print(f"Số {save} xuất hiện {countMax}") 