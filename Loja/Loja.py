class Loja:
  
  def __init__(self, nome, endereco):
    self._nome = nome
    self._endereco = endereco
  
  def __repr__(self):
      return "{} \n {}".format(self._nome, self._endereco)