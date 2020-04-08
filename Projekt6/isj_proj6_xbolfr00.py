#!/usr/bin/env python3
class Polynomial():
    """ Class for basic mathematical operations with polynomials
    Operations : Add, Pow, derivative, at_value """

    def __init__(self, *args, **kwargs):
        """ There are several ways to create class instances
        pol1 = Polynomial([1,-3,0,2])
        pol2 = Polynomial(1,-3,0,2)
        pol3 = Polynomial(x0=1,x3=2,x1=-3)
        """
        self.polynom = list()
        if args and isinstance(args[0], list):
            self.polynom = args[0]
        elif args:
            self.polynom = list(args)
        else:
            for key, value in kwargs.items():
                numbers = int(key.split("x")[1]) # get index for exmaple x7=1 => 7
                for i in range(1 + numbers - len(self.polynom)): #
                    self.polynom.append(0) # append 0 to get to the right index
                self.polynom[numbers] = value #set value to the index

        for i in range(len(self.polynom) - 1, 0, -1): #delete excess 0 in the highest powers
            if self.polynom[i] == 0: #if item is 0
                del self.polynom[i] #delete it
            else:
                break # else break if item is not 0

    def __str__(self):
        """
        Method for print polynom in correct way

        Input: pol1 = Polynomial([1,-3,0,2])
        Input: pol2 = Polynomial(1,-3,0,2)
        Input: pol3 = Polynomial(x0=1,x3=2,x1=-3)

        Output: 2x^3 - 3x + 1
        """
        temp_string = ""
        length_of_polynom = len(self.polynom)
        if length_of_polynom != 1: # if len of polynomial is not 1
            for i in reversed(range(len(self.polynom))): # reverse the list [1,-3,0,2] into [2,0,-3,1] because 2 is 2x^3
                if self.polynom[i] == 0: # if some item is 0 then continue
                    continue
                if temp_string: # sign treatment
                    if self.polynom[i] > 0:
                        temp_string += " + "
                    else:
                        temp_string += " - "
                if i == 1: #if x^1
                    if abs(self.polynom[1]) != 1: #if koeficinet is not 1 -> 2x
                        temp_string += "{0}x".format(str(abs(self.polynom[1]))) # 2x^1 -> 2x
                    else:
                        temp_string += "x" # if koeficient is 1 -  1x^1 -> x
                elif i > 1: # if x^2 or more
                    if abs(self.polynom[i]) != 1: #if koeficinet is not 1
                        temp_string += "{0}x^{1}".format(str(abs(self.polynom[i])), i) # 2x^2
                    else: # if koeficinet is 1
                        temp_string += "x^{0}".format(i) # 1x^2 => x^2
                else: # if x^0
                    temp_string += "{0}".format(str(abs(self.polynom[0]))) # if 2x^0 -> 2
                    return temp_string
        else:# if len of polynom is 1, this is not polynom just number
            temp_string += str(self.polynom[0]) # set this number
            return temp_string # example: Polynomial(2) return 2
        return temp_string

    def __eq__(self, other):
        """Overrides default implementation of __eq__
        pol1 = Polynomial([1,-3,0,2])
        pol2 = Polynomial(1,-3,0,2)
        Input: pol1 == pol2
        Output: True
        """
        if isinstance(self, other.__class__):
            return self.polynom == other.polynom
        return False

    def __add__(self, other):
        """ Method for sum two polynomials
        Input: Polynomial(1,-3,0,2) + Polynomial(0, 2, 1)
        Output: 2x^3 + x^2 - x + 1
        """
        temp_list = []
        length_of_self_polynom = len(self.polynom)
        length_of_other_polynom = len(other.polynom)
        if length_of_self_polynom > length_of_other_polynom:
            temp_list = self.polynom.copy() # make a copy
            for i in range(length_of_other_polynom):
                temp_list[i] += other.polynom[i]
        else:
            temp_list = other.polynom.copy()
            for i in range(length_of_self_polynom):
                temp_list[i] += self.polynom[i]
        return Polynomial(temp_list)

    def __mul__(self, other):
        """ Method for mul two polynomials
            Overrides default implementation of __mul__
            auxiliary function for pow function
        """
        polynom_mul = [0] * (len(self.polynom) + len(other.polynom) + 1)
        for i in range(len(self.polynom)):
            for j in range(len(other.polynom)):
                polynom_mul[i + j] += self.polynom[i] * other.polynom[j]
        return Polynomial(polynom_mul)

    def __pow__(self, power):
        """
            Methods for pow polynom and number
            Input: Polynomial(-1, 1) ** 2
            Output: x^2 - 2x  + 1
        """
        if power < 0: # if power is negative then return error
            raise ValueError("ERRO: Negative power")
        elif power == 1: #if power is 1 then return original polynom (1,-3,0,2)**1 => 2x^3 - 3x + 1
            return self
        elif power == 0: #if power is 0 then return 1 because everything powered by 0 is 1 example : 2^0 => 1 , (1,-3,0,2)**0 => 1
            return 1
        else: # if power is more than 1
            temp = self
            for i in range(1,power):
                temp *= self
            return temp

    def derivative(self):
        """
        Methods for polynomial derivation
        pol1 = Polynomial([1,-3,0,2])
        Input: pol1.derivative()
        Output: 6x^2 - 3
        """
        temp = self.polynom.copy()
        if len(self.polynom) != 1:
            for i in range(len(self.polynom)):
                temp[i] *= i
            temp.pop(0) #pop first item from list because is equal 0
            return Polynomial(temp)
        else: # devrivation constants is 0 y = 2x + 1 ==> y´ = 2 , y = 3 => y´ = 0
            return 0

    def at_value(self, x, y=None):
        """
        Method return value of polynomial for given x
        pol1 = Polynomial([1,-3,0,2]) => 2x^3 -3x + 1
        Just x set:
        Input: pol1.at_value(2) => 2*2^3 - 3*2 + 1
        Output: 11
        If x,y set:
        Input: pol1.at_value(2,3) => 2*3^3 - 3*3 + 1 => 46  (46 - 11) = 35
        Output: 35
        """
        x_result = 0
        y_result = 0
        for i in range(len(self.polynom)):
            x_result += self.polynom[i] * (x ** i)# 2*2^3 - 3*2 + 1 ==> 11
        if y is None:
            return x_result # 11
        else: # if y is set
            for i in range(len(self.polynom)):
                y_result += self.polynom[i] * (y ** i) #2*3^3 - 3*3 + 1 ==> 46
            return y_result - x_result # (46 - 11) = 35

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
