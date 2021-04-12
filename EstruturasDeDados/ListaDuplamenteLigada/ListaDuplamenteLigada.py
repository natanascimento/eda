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
  
  def _inserir_lista_vazia(self, conteudo):
    node = Node(conteudo)
    self._inicio = node
    self._fim = node
    self._quantidade += 1
  
  def inserir_no_inicio(self, conteudo):
    if self.quantidade == 0:
      return self._inserir_lista_vazia(conteudo)
    node = Node(conteudo)
    node.proximo = self.inicio
    self._inicio.anterior = node
    self._inicio = node
    self._quantidade += 1    
    
  def inserir_no_fim(self, conteudo):
    if self.quantidade == 0:
      return self._inserir_lista_vazia(conteudo)
    node = Node(conteudo)
    node.anterior = self.fim
    self.fim.proximo = node
    self._fim = node
    self._quantidade += 1
    
  def inserir(self, posicao, conteudo):
    if posicao == 0:
      return self.inserir_no_inicio(conteudo)
    if posicao == self.quantidade:
      return self.inserir_no_fim(conteudo)
    esquerda = self._node(posicao-1)
    direita = esquerda.proximo
    node = Node(conteudo)
    node.proximo = direita
    node.anterior = esquerda
    esquerda.proximo = node
    direita.anterior = node
    self._quantidade += 1
      
  def item(self, posicao):
    node = self._node(posicao)
    return node.conteudo
    
  def _valida_posicao(self, posicao):
    if 0 <= posicao < self.quantidade:
      return True
    raise IndexError("Posição Inválida {}".format(posicao))
  
  def _node(self, posicao):
    self._valida_posicao(posicao)
    metade = self.quantidade // 2
    if posicao < metade:
      atual = self.inicio
      for i in range(0, posicao):
        atual = atual.proximo
      return atual
    atual = self.fim
    for i in range(posicao + 1, self.quantidade)[::1]:
      atual = atual.anterior
    return atual
  
  def imprimir(self):
    atual = self.inicio
    for i in range(0, self.quantidade):
      print(atual.conteudo)
      atual = atual.proximo
  