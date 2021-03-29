import math
from Equation import Expression
import array as arr
import re
con=""
f=""
string=""
it=""
error = arr.array('d', [0.0])
xi = arr.array('d', [0.0])
xii = arr.array('d', [0.0])
x2=0

def ReadFromFile(fileName,x0, x1, e,N): # It will read the entire file
  fs = open(fileName,'r')
  global con
  con= fs.readline()
  fs.close()
  body(con, x0, x1, e, N)


def body(exp,x0, x1, e,N):
    count = 0
    global con
    con=exp
    print(con)
    for element in con:
        check = con[count - 1]
        if element == 'x' and count > 0 and check.isdigit():
            con = re.sub(r"\b{}\b".format(check + element), check + '*' + element, con)
        count += 1
    count = 0
    for element in con:
        check = con[count - 1]
        if element == 'x' and count > 0 and check == ')':
            con = re.sub(r"\b{}\b".format(re.escape(check + element)), check + '*' + element, con)
        count += 1
    E = math.exp(1)
    for element in con:
        if element == 'E':
            con = re.sub(r"\b{}\b".format(element), str(E), con)
    print(con)
    global f
    f = Expression(con, ["x"])
    print(con)
    CallBisection(x0, x1, e,N)

def bisection(x0, x1, e,N):
 global xi
 global xii
 global error
 global x2
# Implementing Bisection Method

 step = 1

 print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
 condition = True
 while condition:
        global x2
        x2 = (x0 + x1) / 2
       # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:

            xi.insert(step, x1)
            ea=abs((x1 - x2)/x2)
            x1 = x2
            xii.insert(step, x2)
        elif f(x0) * f(x2) > 0:
            xi.insert(step, x0)
            ea = abs((x0 - x2) / x2)
            x0 = x2
            xii.insert(step, x2)
        else:
            string = f'x2 value {x2} is the root'
            break
        step = step + 1
        condition = ea > e
        error.insert(step,ea)
        if step > N:
            break
        #print('\nRequired root is: %0.8f' % x2)
 return error, xi, xii, x2

def CallBisection(x0, x1, e, N):
    global string
    global xi
    global xii
    global error
    global it
    global x2
    try:
     if f(x0) * f(x1) > 0.0:

                string='Given guess values do not bracket the root.Try Again with different guess values.'
     elif  f(x0)==0:
              string = f'x0 value {x0} is the root'
     elif f(x1) == 0:
            string = f'x1 value {x1} is the root'

     else:
                error, xi, xii, x2 = bisection(x0, x1, e, N)
                it = len(error) - 1
                for i in range(1, len(error)):
                    print('ERROR=%0.09f, xi = %0.09f and xi+1 = %0.09f' % (error[i], xi[i], xii[i]))
                    print("Root=%0.09f" % x2)
    except:
                string="Enter valid format."






