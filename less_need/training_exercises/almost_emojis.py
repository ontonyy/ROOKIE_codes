inp = input("Some greeting: ")
message = inp.split(" ")

changes = {
    ':)': 'RUSSIA!',
    ':(': 'OMERIKA'
}
output =''
for word in message:
    output += changes.get(word, word) + " "

print(output)