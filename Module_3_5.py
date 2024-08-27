def get_multiply_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    #Рекурсия
    if len(str_number)>1:
        return first * get_multiply_digits(int(str_number[1:]))
    #Условие выхода
    if len(str_number)<=1:
        return first

print(get_multiply_digits(40203))