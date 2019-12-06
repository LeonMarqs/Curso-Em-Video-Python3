try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    div = n/d

except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você colocou.')
except ZeroDivisionError:
    print('Não é possível dividir por 0.')
except KeyboardInterrupt:
    print('O usuário preferiu não inserir dados.')
except Exception as erro:
    print(f'O erro foi {erro.__class__}')
else:
    print(f'O resultado é {div}')
finally:
    print('Muito obrigado, volte sempre!')