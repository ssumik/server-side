def meu_random(seed):
    return (seed * 1664525 + 1013904223) % (2 ** 32)  # Gerador congruencial linear


def randomizar_tupla(tupla):
    lista = list(tupla)
    seed = 123456789  # Semente fixa para aleatoriedade

    i = 0
    while i < len(lista):
        seed = meu_random(seed)
        j = seed % len(lista)
        lista[i], lista[j] = lista[j], lista[i]
        i += 1

    return tuple(lista)


# Definição da tupla estática
tupla_original = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Chama a função para randomizar a tupla
tupla_embaralhada = randomizar_tupla(tupla_original)

# Exibe o resultado
print("Tupla original:", tupla_original)
print("Tupla embaralhada:", tupla_embaralhada)


def show_even_nums():
    x = 0
    while x < 20:
        if x % 2 == 0:
            print(x)
        x += 1


def show_names_upper(names):
    i = 0
    while i < len(names):
        print(names[i].upper())
        i += 1


def sum_nums(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    print(total)


def vowels(word):
    vowel_sum = 0
    i = 0
    while i < len(word):
        if word[i] in 'aeiou':
            vowel_sum += 1
        i += 1
    print(vowel_sum)


def fibonacci():
    n1, n2 = 0, 1
    count = 0
    while count < 10:
        n = n1 + n2
        print(n)
        n2 = n1
        n1 = n
        count += 1


def bigger_num(nums):
    i = len(nums) - 1
    while i > 0:
        j = 0
        while j < i:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j += 1
        i -= 1
    print(nums.pop())


def invert_str(word):
    word_formatted = ""
    i = len(word) - 1
    while i >= 0:
        word_formatted += word[i]
        i -= 1
    print(word_formatted)


def remove_duplicated(elements):
    i = 0
    while i < len(elements):
        while elements.count(elements[i]) > 1:
            elements.remove(elements[i])
        i += 1
    print(elements)


def val_crescent(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            return False
        i += 1
    return True
