import math
def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


# print(normpdf(7, 4.25, 0.9574))
# print(normpdf(4, 6, 0.81))
# print(normpdf(7, 3.5, 3.11))
# print(normpdf(4, 4.5, 2.645))

def function_2(n):
    return (0.5 * normpdf(n, 2.3, 1.8)) + (0.5 * normpdf(n, 6.8, 2.2))


x = function_2(2.8)
y = function_2(4.2)
z = function_2(5.3)
a = function_2(5.5)
b = function_2(2.1)

print(math.log(x) + math.log(y) + math.log(z) + math.log(a) + math.log(b))