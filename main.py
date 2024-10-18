
import os

a = os.path.dirname(os.path.abspath(__file__))
b = os.path.join(a, "main.py")
print(f'aqui esta o a: {a}')
print('===========')
print(f'aqui esta o b : {b}')



class passeio:
    
    def __init__(self):
        print(' esse é o init >>> 1')

    def ponto1(self):
        print('ponto 1>>>>>> 3')
        return self

    def __enter__(self):
        print('enter >>>>> 2')
        return self

    def __exit__(self, exc_type, exec_val, exec_tb):
        print('exit >>>>> 5')

# Função de teste corrigida
def teste():
    try:
        with passeio() as volta:
            volta.ponto1()
            print('função de fora >>>>> 4')
    except Exception as e:
        print(f'erro >>>>> {e}')

# Chama a função de teste
teste()