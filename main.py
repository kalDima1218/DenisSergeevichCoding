from random import randint

# Исходное сообщение
s = "Здравствуйте Денис Сергеевич! Могу вас заверить, что новый год буду встречать в маске и перчатках."

# Расстановка символов в вершинах дерева
chars = list(set(s))
eq = 1
while eq == 1:
    ways = [[randint(0, 2) for i in range(10)] for j in range(len(chars))]
    ways.sort()
    eq = 0
    for i in range(len(ways) - 1):
        if ways[i] == ways[i + 1]:
            eq = 1

# Генерация ключей
char_num = {}
num_char = {}
for i in range(len(chars)):
    char_num[chars[i]] = ""
    for j in ways[i]:
        char_num[chars[i]] += str(j)
    num_char[char_num[chars[i]]] = chars[i]

# Шифрование
encrypted = ""
for i in s:
    encrypted += char_num[i]

encrypted = encrypted.replace("0", "Д")
encrypted = encrypted.replace("1", "С")
encrypted = encrypted.replace("2", "П")

print(encrypted)

# Расшифровка
encrypted = encrypted.replace("Д", "0")
encrypted = encrypted.replace("С", "1")
encrypted = encrypted.replace("П", "2")

decrypted = ""
l = 0
r = 1

while r <= len(encrypted):
    try:
        decrypted += num_char[encrypted[l:r]]
        l = r
    except:
        pass
    r += 1

print(decrypted)
