import webbrowser as wb

text = str(input('Enter your query: '))
link = f'https://www.google.com/search?q={text}'

wb.open(link)