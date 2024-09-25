#
# autor: michel
# data: 25/09/2024

# 
class A:
  
  def __init__(self, value):
    self._b = value
  
  #get
  def getB(self):
    return self._b
  
  # set
  def setB(self, algo):
    if algo % 2 == 0:
      self._b = algo
    else:
      print(f"Erro: foi informado {algo}, informe um valor par!")
    

a1 = A(2)
print(f"valor de _b -> {a1._b}")
print(f"get1 de _b -> {a1.getB()}")
a1._b = 5
a1.setB(3)
print(f"get2 de _b -> {a1.getB()}")