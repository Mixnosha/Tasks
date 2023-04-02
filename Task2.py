def coin_baskets(n: int, w: int, d: int, p: int) -> int | None:
    if w <= d: return # Деление на ноль, вес монеты отрицательный 
    sum = ((w + w * (n - 1)) / 2) * (n - 1) # Сумма арифметической прогрессии
    if sum == p: return n
    num_basket = int((sum - p) / (w - d))
    return num_basket if num_basket > 0 and num_basket < n else print("Условие задачи не верно")


print(coin_baskets(5, 4, 2, 38)) # -> 1
print(coin_baskets(5, 4, 3, 38)) # -> 2
print(coin_baskets(5, 4, 3, 40)) # -> 5
print(coin_baskets(5, 4, 4, 40)) # -> None // Деление на ноль
print(coin_baskets(5, 4, 5, 40)) # -> None // Вес монеты -1
print(coin_baskets(5, 4, 1, 10)) # -> None print: Условие задачи не верно
