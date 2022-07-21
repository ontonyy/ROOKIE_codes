text = '  hello    world --==++_+_?'
t = text.strip('-_=+?')
print(t.strip().replace(' ', ''))