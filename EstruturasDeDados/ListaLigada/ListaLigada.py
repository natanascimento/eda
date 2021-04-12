from ..Node.Node import Node

class ListaLigada:
  
  def __init__(self):
    self._inicio = None
    self._quantidade = 0
    
  @property
  def inicio(self):
    return self._inicio
  
  @property
  def quantidade(self):
    return self._quantidade
  
  def inserir_inicio(self, conteudo):
    node = Node(conteudo)
    node.proximo = self._inicio
    self._inicio = node
    self._quantidade += 1
    
  def inserir(self, posicao, conteudo):
    if posicao == 0:
      self.inserir_inicio(conteudo)
      return
    node = Node(conteudo)
    esquerda = self._node(posicao-1)
    node.proximo = esquerda.proximo
    esquerda.proximo = node
    self._quantidade += 1
    
  def _node(self, posicao):
    self._validar_posicao(posicao)
    atual = self.inicio
    for i in range(0, posicao):
      atual = atual.proximo
    return atual
    
  def _validar_posicao(self, posicao):
      if 0<= posicao < self.quantidade:
        return True
      raise IndexError("Posição Inválida {}".formart(posicao))
      
  def imprimir(self):
    atual = self.inicio
    for i in range(0, self.quantidade):
      print(atual.conteudo) 
      atual = atual.proximo
  
  def remover_inicio(self):
    removido = self.inicio
    self._inicio = removido.proximo
    removido.proximo = None
    self._quantidade -= 1
    return removido.conteudo
  
  def remover(self, posicao):
    if posicao == 0:
      return self.remover_inicio()
    esquerda = self._node(posicao - 1)
    removido = esquerda.proximo
    esquerda.proximo = removido.proximo
    removido.proximo = None
    self._quantidade -= 1
    return removido.conteudo
  
  def item(self, posicao):
    self._validar_posicao(posicao)
    node = self._node(posicao)
    return node.conteudo