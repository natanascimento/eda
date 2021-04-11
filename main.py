from ed.ListaLigada.ListaLigada import ListaLigada

class Loja:
  
  def __init__(self, nome, endereco):
    self._nome = nome
    self._endereco = endereco
  
  def __repr__(self):
      return "{} \n {}".format(self._nome, self._endereco)
    
def main():
  
  loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 10")
  loja2 = Loja("Padaria", "Rua Japaratuba, 60")
  loja3 = Loja("Hortifruti", "Rua das Aroeiras, 1900")
  loja4 = Loja("Supermercado", "Avenida A, 1900")
  loja5 = Loja("Mini mercado", "Avenida B, 564")
  loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")
  
  lista = ListaLigada()
  #Adicionar itens
  lista.inserir_inicio(loja1)
  lista.inserir_inicio(loja2)
  lista.inserir_inicio(loja3)
  lista.inserir(1, loja4)
  lista.inserir(0, loja5)
  lista.inserir(2, loja6)
  
  print("Quantidade de elementos na lista: {}".format(lista.quantidade))
  print("Elementos da Lista: ")
  lista.imprimir()
  print("")
  #Remover Itens
  removido = lista.remover_inicio()
  print("Item removido: {}".format(removido))
  removido = lista.remover_inicio()
  print("Item removido: {}".format(removido))
  print("")
  print("Quantidade de elementos na lista: {}".format(lista.quantidade))
  print("Elementos da Lista: ")
  lista.imprimir()
  print("")
  removido = lista.remover(1)
  print("Item removido da posicao 1: {}".format(removido))
  print("")
  print("Quantidade de elementos na lista: {}".format(lista.quantidade))
  print("Elementos da Lista: ")
  lista.imprimir()
  print("")
  removido = lista.remover(lista.quantidade - 1)
  print("Item removido da posicao {}: {}".format(lista.quantidade, removido))
  print("")
  print("Quantidade de elementos na lista: {}".format(lista.quantidade))
  print("Elementos da Lista: ")
  lista.imprimir()
  print("")
  print("Elemento da posicao {}: {}".format(0, lista.item(0)))
  
  
  
main()