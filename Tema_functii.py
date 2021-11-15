#ex1
def function(*args,**kwargs):
    sum=0
    for arg in args:
        if (type(arg) == int or type(arg) == float):
            sum=sum+arg
    return sum

print(function(1, 5, -3,'abc', [12, 56, 'cad']))
print(function())
print(function(2, 4, 'abc', param_1=2))


#ex2

def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)
print('Suma tuturor numerelor: ',recursive_sum(3))

def recursive_sum_par(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + recursive_sum_par(n - 1)
    else:
        return recursive_sum_par(n - 1)
print('Suma numerelor pare:',recursive_sum_par(3))

def recursive_sum_impar(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + recursive_sum_impar(n - 1)
    else:
        return recursive_sum_impar(n - 1)
print('Suma numerelor impare:',recursive_sum_impar(3))

#ex3
def read_input():
    input_value = input("Enter a value: ")
    # try converting the value into integer; if it works it means is a an integer
    try:
        value = int(input_value)
        print("Value introduced is an integer: ", value)
    #if it doesn't wrok it means is something else
    except ValueError:
            print("Value introduced is NOT an integer: 0")

read_input()





