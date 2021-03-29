from sympy import *
from Equation import Expression
from sympy.parsing.sympy_parser import parse_expr
import re
import array as arr
import math
f=""
con=""
string=""
it=""
error = arr.array('d', [0.0])
xi = arr.array('d', [0.0])
xii = arr.array('d', [0.0])
x1=0
def ReadFile(fileName,x0, e,N):
  fs = open(fileName,'r')
  global con
  con=fs.readline()
  fs.close()
  body(con, x0, e, N)

def body(exp, x0, e, N):
    global con
    con=exp
    count = 0
    for element in con:
        check = con[count - 1]
        if element == 'x' and count > 0 and check.isdigit():
            con = re.sub(r"\b{}\b".format(check + element), check + '*' + element, con)
        count += 1
    E = math.exp(1)
    for element in con:
        if element == 'E':
            con = re.sub(r"\b{}\b".format(element), str(E), con)
    count = 0
    for element in con:
        check = con[count - 1]
        if element == 'x' and count > 0 and check == ')':
            con = re.sub(r"\b{}\b".format(re.escape(check + element)), check + '*' + element, con)
        count += 1

    print(con)
    global f
    f = Expression(con, ["x"])
    CallNewtonRaphson(x0, e, N)


def g(y):
     my_symbols = {'x': Symbol('x', real=True)}
     my_func = parse_expr(con, my_symbols)
     g = diff(my_func, my_symbols['x'])
     answer = g.subs(my_symbols['x'], y)
     return answer

def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    global xi
    global xii
    global error
    global x1
    step = 1
    flag = 1
    condition = True
    error = arr.array('d', [0.0])
    xi = arr.array('d', [0.0])
    xii = arr.array('d', [0.0])
    while condition:
        if g(x0) == 0.0:
            global string
            string = 'Divide by zero error!'
            break

        x1 = x0 - f(x0) / g(x0)
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
    return error, xi,xii, x1





def CallNewtonRaphson(x0, e, N):
 global string
 global xi
 global xii
 global error
 global it
 global x1
 try:
    error, xi,xii, x1 = newtonRaphson(x0, e, N)
    it = len(error) - 1
    for i in range(1, len(error)):
        print('ERROR=%0.09f,xi = %0.09f and xii = %0.09f' % (error[i], xi[i],xii[i]))
    print("Root=%0.09f" % x1)
 except:
     string = "Enter valid format."