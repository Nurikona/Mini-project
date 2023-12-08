import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cntpw = int(input('Укажите количество паролей для генерации: '))
lenpw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n) ').strip()
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ').strip()
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ').strip()
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ').strip()
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ').strip()

if digOn.lower() == '+':
    chars += digits
if ABCon.lower() == '+':
    chars += uppercase_letters
if abcOn.lower() == '+':
    chars += lowercase_letters
if chOn.lower() == '+':
    chars += punctuation
if excOn.lower() == '+':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_passwords(lenpw, chars):
    passwords = ''
    for k in range(lenpw):
        passwords += random.choice(chars)
    print(passwords)

for _ in range(cntpw):
    generate_passwords(lenpw, chars)

