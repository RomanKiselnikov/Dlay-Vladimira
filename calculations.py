def main():
    print('Это калькулятор')
    operator=input('Введите операцию:\n- - вычитание\n+ - сложение\n* - умножение\
        \n** - возведение в степень\n/ -деление\n//-целочисленное деление\n%-показать остаток от деления\n')
    a=float(input('Введите первое число:'))
    b=float(input('Введите второе число:'))
    while (operator=='/' or operator=='//' or operator=='%') and b==0:
        b=float(input('На ноль делить нельзя, введите другое значение для делителя:'))
    result=0
    if operator=='-':
        result=a-b
    elif operator=='+':
        result=a+b
    elif operator=='*':
        result=a*b   
    elif operator=='**':
        result=a**b
    elif operator=='/':
        result=a/b
    elif operator=='//':
        result=a//b
    elif operator=='%':
        result=a%b
    print(f'Результат операции {operator} равен {result:.2f}')
    input()
    
if __name__=='__main__':
    main()