#
# autor: michel
# data: 25/09/2024

# 
class B:
  def __init__(self, value):
    self.__a = value
    
  #get
  @property
  def a(self):
    print("vc uso get")
    return self.__a
  
  #set
  @a.setter
  def a(self, algo):
    if algo % 2 == 0:
      self.__a = algo
    else:
      print(f"Erro: foi informado {algo}, informe um valor par!")
    

b1 = B(2)
#print(f"print no a: -> {b1.__a}")
print(f"print no a: -> {b1.a}")
b1.a = 3    