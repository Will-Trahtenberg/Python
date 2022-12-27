def calc_bmi(weight, height):  # масса в кг, рост в м
    index = weight / (height * height)
    return index
def print_recomendation(weight, height):
    a = weight / (height * height)
    if a <= 18.5:
        print('У вас недостаточный вес, пройдите на консультацию в кабинет 301')
    elif a > 18.5 and a <= 25:
        print('Ваш вес в норме, пройдите на 3 этаж для продолжения осмотра')
    elif a > 25:
        print('У вас избыточный вес, пройдите на консультацию в кабинет 410')
    return a
weight = float(input('Введите вес (кг): '))
height = float(input('Введите рост (м): '))
print_recomendation(weight, height)
calc_bmi(weight, height)