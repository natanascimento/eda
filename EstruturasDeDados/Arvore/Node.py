from ..ListaDuplamenteLigada.ListaDuplamenteLigada import ListaDuplamenteLigada

class ListaDeNodes(ListaDuplamenteLigada):
  
  def __init__(self):
    super().__init__()
  
  def imprimir(self, nivel):
    atual = self.inicio
    for i in range(0, self.quantidade):
      atual.conteudo.imprimir(nivel)
      atual = atual.proximo
    
  def localizar_node(self, conteudo):
    atual = self.inicio
    for i in range(0, self.quantidade):
      encontrado = atual.conteudo.localizar_node(conteudo)
      if encontrado:
        return encontrado
      atual = atual.proximo
  
  def posicao(self, conteudo):
    atual = self.inicio
    for i in range(0, self.quantidade):
      if atual.conteudo.conteudo == conteudo:
        return i
      atual = atual.proximo

class Node:
  
  def __init__(self, conteudo):
    self.conteudo = conteudo
    self.pai = None
    self.filhos = None
    
  def __repr__(self):
      return self.conteudo
    
  def imprimir (self, nivel=0):
    print("{} - {}".format(" "*nivel, self.conteudo))
    if self.filhos:
      self.filhos.imprimir(nivel + 1)
    
  def inserir_filho(self, filho):
    if self.filhos is None:
      self.filhos = ListaDeNodes()
    node = Node(filho)
    node.pai = self
    self.filhos.inserir_no_fim(node)
    
  def localizar_node(self, conteudo):
    if conteudo == self.conteudo:
      return self
    if self.filhos:
      return self.filhos.localizar_node(conteudo)
  
  def remover(self):
    if self.pai:
      posicao = self.pai.filhos.posicao(self.conteudo)
      return self.pai.filhos.remover(posicao)
    return self