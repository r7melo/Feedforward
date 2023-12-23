from functools import partial

# Defina uma função
def minha_funcao(arg1, arg2):
    print(arg1, arg2)

# Crie uma instância parcial da função com argumentos específicos
funcao_parcial = partial(minha_funcao, "Hello", "World")

# Execute a função parcial
#funcao_parcial()
