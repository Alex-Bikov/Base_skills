alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = ['v', 'u', 'j', 'g', 'v', 'm', 'c', 'f', 'b']
step = 1
for i in range(len(text)):
    x = (alphabet.index(text[i]) - step) % len(alphabet)
    text[i] = alphabet[x]
print(''.join(text), step)
step += 1

