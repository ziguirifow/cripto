def cripto(frase):
  
  v = []

  for letra in frase:
    l = ord(letra) + 20
    v.append(l)

  for n in v:
    print(n, end='')

  print()
  descripto(v)

def descripto(v):
  
  final = ""

  for n in v:
    l = int(n)
    l = l - 20
    l = chr(l)
    final = final + l

  print ("Mensagem Descriptografada: ")
  print(final)

def main():
  f = input("Digite: ")
  cripto(f)

if __name__ == '__main__':
  main()
