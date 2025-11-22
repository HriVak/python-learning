print(" === Задача 2 === ")
price = float(input("Колко струва продукта? "))
discount_percent = 20

# Изчисления
price_discount = price * discount_percent / 100
total_price = price - price_discount

# Показване с .2f и хубаво подравняване
print(f"Оригинална цена:  {price:8.2f} лв.")
print(f"Отстъпка: {discount_percent}%    -  {price_discount:7.2f} лв.")
print(f"Крайна цена:  {total_price:8.2f} лв.")
print("Благодаря за покупката!")
print()
