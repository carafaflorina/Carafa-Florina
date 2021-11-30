import math
class Fractie:

    def __init__(self, numarator, numitor):
        self.__numarator = numarator
        self.__numitor = numitor

    def __str__(self):
        return "{}/{}".format(self.__numarator, self.__numitor)

    def __add__(self, other):
        num = int(math.lcm(self.__numitor, other.__numitor))
        if self.__numitor != other.__numitor:
             num1 = int(num/self.__numitor*self.__numarator)
             num2 = int(num/other.__numitor*other.__numarator)
             return "{}/{}".format(num1 + num2, num)
        else:
            return "{}/{}".format(self.__numarator + other.__numarator, num)

    def __sub__(self, other):
        num = int(math.lcm(self.__numitor, other.__numitor))
        if self.__numitor != other.__numitor:
            num1 = int(num / self.__numitor*self.__numarator)
            num2 = int(num / other.__numitor*other.__numarator)
            return "{}/{}".format(num1 - num2, num)
        else:
            return "{}/{}".format(self.__numarator - other.__numarator, num)

    def __str2__(self):
        return "{}/{}".format(self.__numitor, self.__numarator)

my_fraction1 = Fractie(1,3)
my_fraction2= Fractie(1,2)
print("Fractia 1: ",my_fraction1.__str__() )
print("Fractia 2: ",my_fraction2.__str__() )
print("Suma fractiilor: ", Fractie.__add__(my_fraction1,my_fraction2))
print("Diferenta fractiilor: ", Fractie.__sub__(my_fraction1,my_fraction2))
print(" Inversa fractiei 1 : ", Fractie.__str2__(my_fraction1))