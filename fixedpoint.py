import math
import array as arr
from Equation import Expression
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import re

con1=""
g=""
string=''
it=""
x1=0

error = arr.array('d', [0.0])
xi = arr.array('d', [0.0])
xii = arr.array('d', [0.0])

def ReadFile(fileName,x0, e,N):
 fs = open(fileName,'r')
 global con1
 con1=fs.readline()
 fs.close()
 body(con1, x0, e, N)

def body(exp, x0, e, N):
    global con1
    con1=exp
    count = 0
    for element in con1:
        check = con1[count - 1]
        if element == 'x' and count > 0 and check.isdigit():
            con1 = re.sub(r"\b{}\b".format(check + element), check + '*' + element, con1)
        count += 1
    E = math.exp(1)
    for element in con1:
        if element == 'E':
            con1 = re.sub(r"\b{}\b".format(element), str(E), con1)

    count = 0
    for element in con1:
        check = con1[count - 1]
        if element == 'x' and count > 0 and check == ')':
            con1 = re.sub(r"\b{}\b".format(re.escape(check + element)), check + '*' + element, con1)
        count += 1
    print(con1)
    global g
    g = Expression(con1, ["x"])
    check=validate(x0)
    if check == true:
        CallFixedPoint(x0, e, N)
    else:
        global string
        string="Enter a valid g(x)"


def gdiff(y):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(con1, my_symbols)
    gd = diff(my_func, my_symbols['x'])
    answer = gd.subs(my_symbols['x'], y)
    return answer

def validate(x0):
    if abs(gdiff(x0)) < 1:
        return true
    else:
        return false

def fixedPointIteration(x0, e, N):
    global x1
    global xi
    global xii
    global error
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    error = arr.array('d', [0.0])
    xi = arr.array('d', [0.0])
    xii = arr.array('d', [0.0])
    while condition:
        x1 = g(x0)
        xii.insert(step, x1)
        # print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        xi.insert(step, x0)
        ea = abs((x0 - x1) / x1)
        x0 = x1

        step = step + 1

        if step > N:
            break

        condition = ea > e
        error.insert(step, ea)
    return error, xi, xii, x1




def CallFixedPoint(x0, e, N):

 global xi
 global xii
 global error
 global it
 global x1
 try:
    global string
    if validate(x0):
        error, xi,xii, x1 =fixedPointIteration(x0, e, N)
        it = len(error) - 1
        for i in range(1, len(error)):
            print('ERROR=%0.09f,xi = %0.09f and xii = %0.09f' % (error[i], xi[i],xii[i]))
        print("Root=%0.09f" % x1)

    else:

        string= "Enter a valid g(x)"
 except:

    string = "Enter valid format."
