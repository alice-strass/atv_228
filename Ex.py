#oi
def Soma1aN(N):
#if N==1: 
    return(1)
#else: return (N+Soma1aN(N-1)) # note-se a ativação recursiva

# Uso da função
N=int(input('Entre com o valor de N: '))
print('A soma de 1 a', N, 'é', Soma1aN(N))