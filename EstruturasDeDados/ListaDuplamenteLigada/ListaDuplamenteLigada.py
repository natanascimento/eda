from ..Node.Node import Node

class ListaDuplamenteLigada:
  
  def __init__(self):
    self._inicio = None
    self._fim = None
    self._quantidade = 0
  
  @property
  def inicio(self):
    return self._inicio
  
  @property
  def fim(self):
    return self._fim

  @property
  def quantidade(self):
    return self._quantidade