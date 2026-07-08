def assess_yield(number_of_plants, average_weight):
    total_kg = number_of_plants * average_weight / 1000
    message = None
    if total_kg > 100:
        message = 'Ожидается отличный урожай.'
    elif total_kg > 50:
        message = 'Ожидается хороший урожай.'
    elif total_kg > 0:
        message = 'Урожай будет так себе.'
    else:
        message = 'Урожая не будет.'
    return total_kg, message


# Вызываем функцию и распаковываем кортеж:
total_weight, rating = assess_yield(50, 200)

# Печатаем результат:
print(total_weight, 'кг.', rating)
