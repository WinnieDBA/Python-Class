#function defination
def function_name():
    print('hello world')

function_name()#calling a function

#Adding a parameter to a function


def payment(salary,commission,allowance,deduction,helb):
    additional = salary+commission+allowance
    deduction_main =helb+deduction
    net_salary=additional-deduction_main
    return net_salary
final_salary = payment(20000,2000,5000,5500,1500)
print(final_salary)


def amount_obtained(amount_sold,feed,labour,commission):
    gotten_money = amount_sold +commission
    deduction = feed+labour
    last_amoount = gotten_money-deduction
    return last_amoount
expected_amount = amount_obtained(14000,6000,2000,5000,)
print(expected_amount)



def add(x,y):
    ongeza =x+y
    return ongeza
total =add(3,5)
print(total)


def division(parent,children):
    divide = parent/children
    return divide
each_obtain =division(10,2)
print(each_obtain)


def final_amount(expenses,selling):
    cal = expenses-selling
    return cal
profit =final_amount(1500,500)
print(profit)


def output(bags,amount):
    price_bags = bags*amount
    return price_bags
final_output =output(5,1200)
print(final_output)

def mat_biz(amount,insuarance,dividends,sacco):
    expectations = amount-(insuarance+dividends+sacco)
    return expectations
what_gotten =mat_biz(70000,5000,5000,15000)
print(what_gotten)

def multiplication(c,d):
    multiply = c*d
    return multiply
final_multi = multiplication(2,6)
print(final_multi)


def greetings():
  print('hello')
greetings()


def wheat_check(mystring):
    if 'wheat' in mystring:
        return True
    else:
        return False
offer = wheat_check('they have planted Wheat')
print(offer)


def multiply(x,y):
    return x*y
final_ans =multiply(2,8)
print(final_ans)


def myfunc():
    print('Hello World')
myfunc()



def myfunc(a):
    if a <= 10:
        return True
    elif a >= 20:
        return False
ans = myfunc(5)
print(ans)



def system(t):
    if t <= 12:
        return 'open'
    elif  t >= 12:

        return 'close'
hrs = system(55)
print(hrs)

def myfunc(a,b,c):
    if a == c:
        return 'yes'
    else:
        return 'untrue'

ans = myfunc(5,10,5)
print(ans)




def even_num(n):
    if n%2 == 0:
       return 'even'

    else:
        return 'not even'


ans =even_num(5)
print(ans)