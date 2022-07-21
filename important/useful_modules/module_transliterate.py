from transliterate import translit, detect_language

text = 'Здравствуйте, дамы и господа'
# С любого языка интерпритация на английский
mu_text = translit(text, reversed=True)

print(mu_text)

text = 'Я конечно не понимаю, господа, что вы имеете в виду!'
# Определение языка текста
print('\nText language - ' + detect_language(text))