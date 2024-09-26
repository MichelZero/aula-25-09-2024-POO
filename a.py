#
# autor: michel
# data: 25/09/2024

# criando uma classe de exemplo 
class A:
  
  def __init__(self, value):
    self._b = value # atributo protegido da classe A que pode 
    # ser acessado por outras classes que a herdam ou instanciam 
  
  #get
  def getB(self):
    return self._b # retorna o valor do atributo protegido _b da classe A 
  
  # set
  def setB(self, algo):
    if algo % 2 == 0:
      self._b = algo # atribui um novo valor ao atributo protegido _b da classe A
    else:
      print(f"Erro: foi informado {algo}, informe um valor par!")

    

a1 = A(2) # instanciando a classe A com o valor 2 para o atributo protegido _b da classe A
print(f"valor de _b -> {a1._b}") # acessando o atributo protegido _b da classe A de forma direta
print(f"get1 de _b -> {a1.getB()}") # acessando o atributo protegido _b da classe A de forma indireta
a1._b = 5 # alterando o valor do atributo protegido _b da classe A de forma direta 
a1.setB(3) # chamando o set para alterar o valor do atributo protegido _b da classe A
a1.setB(3) # chamando o set para alterar o valor do atributo protegido _b da classe A
print(f"get2 de _b -> {a1.getB()}") # acessando o atributo protegido _b da classe A de forma indireta