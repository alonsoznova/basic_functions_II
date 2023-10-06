#Función 1
def countdown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list
x = countdown(5)
print(x)

#Función 2
def imprimir_y_devolver(list):
    print(list[0])
    return list[1]
y = imprimir_y_devolver([1,2])
print(y)

#Función 3
def primero_mas_lista(list):
    return len(list) + list[0]
z = primero_mas_lista([1,2,3,4,5])
print(z)

#Función 4
def mayor_que_segundo(list = []):
    new_list = []
    if(len(list) < 2):
        return False
    else:
        for x in range(len(list)):
            if(list[x] > list[1]):
                new_list.append(list[x])
        print(len(new_list))
        return new_list
k = mayor_que_segundo([5,2,3,2,1,4])
print(k)
l = mayor_que_segundo([3])
print(l)

#Función 4
def largo_y_valor(largo, valor):
    list = []
    for x in range(largo):
        list.append(valor)
    return list
m = largo_y_valor(4,7)
n = largo_y_valor(6,2)
print(m)
print(n)