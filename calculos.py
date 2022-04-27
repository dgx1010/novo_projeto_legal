def hipotenusa():
  while True:
    print('----------------------') 
    c1= int(input('qual o primeiro cateto?: '))
    c2= int(input('qual o segundo cateto?: '))
    an=int(input('Qual o angulo?: '))
    import math
    ang= math.radians(an)
    angu=math.cos(ang)
    h= c1*2+c2*2-2*c1*c2*angu
    
    print('A hipotenusa é igual a', h**(1/2))
def segundo_grau():
    a = int(input('Qual o valor de a: '))
    b = int(input('Qual o valor de b: '))
    c = int(input('Qual o valor de c: '))
    # Não mexer no código abaixo
    formula1 = b ** 2 - 4 * a * c
    print('O valor de delta é', formula1)
    raiz_delta = (formula1 ** (1 / 2))
    print('A raiz de delta é', raiz_delta)
    x1 = (-b + raiz_delta) / (2 * a)
    print('O primeiro valor de x é igual a', x1)
    x2 = (-b - raiz_delta) / (2 * a)
    print('O segundo valor de x é igual a', x2)
    print ('A soma das raízes é', x1+x2)
    
def lancamento_obliquo():
  a= input('A velocidade está em metros por segundos?:  ')
  if a=='sim':
    vi = float(input('qual a velocidade inicial do objeto (m/s)?:  '))
    angulo = float(input('qual o angulo com o solo (graus)?:  '))
    g = float(input('qual a aceleração da gravidade (m/s2)?:  '))
    solo = float(input('qual a altura do solo (m)?:  '))
    import math

    # O seno e o cosseno estão apresentando valor incorreto.
    # É necessario converter para radianos
    rad = math.radians(angulo)
    # Agora dou prosseguimento
    vy = vi * (math.sin(rad))
    vx = vi * (math.cos(rad))
    altura = (vy ** 2) / (2 * g)
    temposu = (vy / g)
    tempodes = math.sqrt((altura - solo) * 2 / g)
    tempo = temposu + tempodes
    alcance = vx * tempo

    print('1- Velocidade para cima é', vy, 'ms')
    print('2- Velocidade para frente é', vx, 'ms')
    print('3- altura máxima é', altura, 'metros')
    print('4- tempo de subida é', temposu, 'segundos')
    print('5- tempo de descida é', tempodes, 'segundos')
    print('6- O tempo de subida e descida do projétil é', tempo, 'segundos')
    print('7- O alcance do projétil é', alcance, 'metros')
  elif a=='não':
    vi = float(input('qual a velocidade inicial do objeto (k/h)?:  '))
    angulo = float(input('qual o angulo com o solo (graus)?:  '))
    g = float(input('qual a aceleração da gravidade (m/s2)?:  '))
    solo = float(input('qual a altura do solo (m)?:  '))
    import math

    # O seno e o cosseno estão apresentando valor incorreto.
    # É necessario converter para radianos
    rad = math.radians(angulo)
    # Agora dou prosseguimento
    vi=vi/3.6
    vy = vi * (math.sin(rad))
    vx = vi * (math.cos(rad))
    altura = (vy ** 2) / (2 * g)
    temposu = (vy / g)
    tempodes = math.sqrt((altura - solo) * 2 / g)
    tempo = temposu + tempodes
    alcance = vx * tempo

    print('1- Velocidade para cima é', vy, 'ms')
    print('2- Velocidade para frente é', vx, 'ms')
    print('3- altura máxima é', altura, 'metros')
    print('4- tempo de subida é', temposu, 'segundos')
    print('5- tempo de descida é', tempodes, 'segundos')
    print('6- O tempo de subida e descida do projétil é', tempo, 'segundos')
    print('7- O alcance do projétil é', alcance, 'metros')

  else:
    print('insira "sim", ou "não", reinicie o código')

print('-------calculos------') 
print('1- segundo grau')
print('2- lancamento obliquo')
print('3- hipotenusa')
print('---------------------')

#aqui comecam as opcoes

opcao = int(input('Qual conta?:  '))
if opcao==1:
    print(segundo_grau())
elif opcao==2:
    print(lancamento_obliquo())
elif opcao==3:
    print(hipotenusa())