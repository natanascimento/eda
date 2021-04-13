from .Node import Node

class Arvore:
  
  def __init__(self, conteudo):
    self.raiz = Node(conteudo)
    
  def imprimir(self):
    self.raiz.imprimir()
    
  def localizar_node(self, conteudo):
    return self.raiz.localizar_node(conteudo)
  
  def inserir_node(self, pai, filho):
    node_pai = self.localizar_node(pai)
    if node_pai:
      node_pai.inserir_filho(filho)
      
  def remover_node(self, conteudo):
    encontrado = self.raiz.localizar_node(conteudo)
    if encontrado:
      if encontrado is self.raiz:
        self.raiz = None
      else:
        encontrado.remover()
    return encontrado
