from time import sleep

def linha():
    print('=='*22)


def maior(*nums):
    linha()
    print('Analisando os valores passados...')
    tamanho = len(nums)
    if tamanho == 0:
        nums = []
        maior = 0
    else:
        maior = max(nums)
    for c in nums:
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {tamanho} números ao todo.')
    print(f'O maior número foi {maior}')



maior(1, 2, 3, 4)
maior(2, 3)
maior(4, 5, 6)
maior(6)
maior()