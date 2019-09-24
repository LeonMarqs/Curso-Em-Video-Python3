from time import sleep
import emoji

print('-=-'* 10)
print('FOGOS DE ARTIFICIO')
print('-=-'* 10)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('Boom :collision:'))
