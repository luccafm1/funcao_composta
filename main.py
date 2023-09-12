import math
print("-----------------")
print("1: f o g")
print("2: g o f")
print("3: f o f")
print("4: g o g")
print("-----------------")
## if funcao = true: f o g. else: g o f
def compor(funcao):
  f = lambda x: eval(input("Digite o valor da função f: "))
  g = lambda x: eval(input("Digite o valor da função g: "))
  
  x = eval(input("Digite o valor de x: "))

  if funcao == 1:
    composicao = f(g(x))
    print(f'(f o g) = {composicao}')

  elif funcao == 2:
    composicao = g(f(x))
    print(f'(g o f) = {composicao}')
    
  elif funcao == 3:
    composicao = f(f(x))
    print(f'(f o f) = {composicao}')

  elif funcao == 4:
    composicao = g(g(x))
    print(f'(g o g) = {composicao}')

funcao = int(input())
if funcao == 1:
  compor(1)
elif funcao == 2:
  compor(2)
elif funcao == 3:
  compor(3)
elif funcao == 4:
  compor(4)
else:
  print('input incorreto!')
