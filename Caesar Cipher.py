define_work = input('Шифрование или дешифрование? ')
language_define = input('Русский или английский? ')
LN_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ln_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
LN_ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ln_eng = 'abcdefghijklmnopqrstuvwxyz'
k = int(input('Шаг сдвига (со сдвигом вправо)? '))
s = input('Введите строку ')
s1 = ''

if define_work.lower() == 'шифрование':
    if language_define.lower() == 'русский':
        for char in s:
            if char in LN_RU:
                s1 += LN_RU[(LN_RU.find(char) + k) % 32]
            elif char in ln_ru:
                s1 += ln_ru[(ln_ru.find(char) + k) % 32]
            else:
                s1 += char
    elif language_define.lower() == 'английский':
        for char in s:
            if char in LN_ENG:
                s1 += LN_ENG[(LN_ENG.find(char) + k) % 26]
            elif char in ln_eng:
                s1 += ln_eng[(ln_eng.find(char) + k) % 26]
            else:
                s1 += char
elif define_work.lower() == 'дешеифрование':
    if language_define.lower() == 'русский':
        for char in s:
            if char in LN_RU:
                s1 += LN_RU[(LN_RU.find(char) - k) % 32]
            elif char in ln_ru:
                s1 += ln_ru[(ln_ru.find(char) - k) % 32]
            else:
                s1 += char
    elif language_define.lower() == 'английский':
        for char in s:
            if char in LN_ENG:
                s1 += LN_ENG[(LN_ENG.find(char) - k) % 26]
            elif char in ln_eng:
                s1 += ln_eng[(ln_eng.find(char) - k) % 26]
            else:
                s1 += char
print(s1)