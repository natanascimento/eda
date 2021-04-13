from ..ListaLigada.ListaLigada import ListaLigada

class Pilha:
  
  def __init__(self):
    self.pilha = ListaLigada()
    
  def empilha(self, conteudo):
    self.pilha.inserir_inicio(conteudo)
  
  def desempilha(self):
    return self.pilha.remover_inicio()
  
  @property
  def topo(self):
    return self.pilha.item(0)

  @property
  def validaVazio(self):
    return self.pilha.quantidade == 0