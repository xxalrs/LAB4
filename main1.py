## --------------------- Сєваті Євген КН-31\1
text = ("Whether you're travelling to the islands or the mountains of Thailand, " ## Створення тексту
         "you're likely to spend at least one night in its capital city on the way."
        " Bangkok might be noisy and polluted but it's also an exciting city with plenty of things to see and do. "
         "Why not make it a longer stay?")
print(text, "\n") ## Вивід тексту у консоль
print(text.lower(), "\n") ## Вивід тексту нижнім регістром букв
print("Amount of letter 'a' in text = ", text.count('a') + text.count('A'), "\n") ## Вивід кількість букв "а" у тексті
print("Is our text lowercased? ", text.islower(), "\n") ## Вивід чи написаний вхідний текст нижнім регістром букв

## --------------------- Лобанов Денис КН-33\1
print(text.replace(" ", "-"), "\n") ## Замінити всі пробіли на дефіси
print("Is our text alphabetic? ", text.isalpha(), "\n") ## Перевірка, чи текст складається лише з букв
print("First occurrence of 'city' is at index: ", text.find("city"), "\n") ## Знайти перше слово "city"
