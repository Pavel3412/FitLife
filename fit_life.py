# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
MILLILITERS_IN_LITER = 1000

print("Вас приветствует бот FitLife. Давай знакомиться!")
# Ввод информации о человеке
user_name = input('Как Вас зовут?: ')
# Ввод информации для расчета

while True:
    try:
        user_age = int(input('Введите ваш полный возраст: '))
        break
    except ValueError:
        print('Ошибка! Пожалуйста, введите число')
while True:
    try:
        user_weight = float(input('Введите ваш вес(например 50.5): '))
        break
    except ValueError:
        print('Ошибка! Введите число или поставьте точку вместо запятой')
while True:
    try:
        user_height = float(input('Введите рост (например 1.65): '))
        break
    except ValueError:
        print('Ошибка! Введите число или поставьте точку вместо запятой')


# Расчет ИМТ и кол-ва жидкости
bmi = user_weight / (user_height ** 2)
water_ml = user_weight * WATER_PER_KG
water_liters = water_ml / MILLILITERS_IN_LITER

print(f'Привет, {user_name}!')
print(f'Возраст: {user_age}. Индекс массы тела составляет: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды составляет {water_liters:.1f}л. в день')
print('Расчёт окончен. Будьте здоровы!')
