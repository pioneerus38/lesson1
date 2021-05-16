def format_price(price):
    try:
        val = abs(int(price))
    except ValueError:
        print("Неверное значение")
        val = 0
    finally:
        return f'Цена: {val} руб.' 

a = format_price(56.24)
print(a)