#
# autor: Michel
# data: 25/09/2024

# criando uma classe de exemplo
class B:
  def __init__(self, value): 
    self.__a = value # atributo privado da classe B que só pode ser acessado por 
    # ela mesma e não por outras classes que a herdam ou instanciam
    self._b = 2 # atributo protegido da classe B que pode ser acessado por 
    # outras classes que a herdam ou instanciam    
    
  #get
  @property # decorator que permite acessar o atributo privado da classe B
  def a(self):  
    print("vc uso get") # mensagem de teste para verificar se o get foi chamado
    return self.__a # retorna o valor do atributo privado __a da classe B 
  
  #set
  @a.setter
  def a(self, algo):
    if algo % 2 == 0:
      self.__a = algo # atribui um novo valor ao atributo privado __a da classe B 
    else:
      print(f"Erro: foi informado {algo}, informe um valor par!")
    

b1 = B(2) # instanciando a classe B com o valor 2 para o atributo privado __a da classe B
# print(f"print no a: -> {b1.__a}") # erro, pois o atributo __a é privado e não pode ser acessado 
# diretamente por outras classes que a herdam ou instanciam 

print(f"print no a: -> {b1._B__a}") # acessando o atributo privado __a da classe B de forma indireta  
print(f"print no a: -> {b1.a}") # acessando o atributo privado __a da classe B de forma direta 
b1.a = 3     # chamando o set para alterar o valor do atributo privado __a da classe B
b1.a = 4     # chamando o set para alterar o valor do atributo privado __a da classe B
print(f"print no a: -> {b1.a}") # acessando o atributo privado __a da classe B de forma direta