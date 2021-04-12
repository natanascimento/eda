from EstruturasDeDados.ListaLigada.ListaLigada import ListaLigada
from EstruturasDeDados.ListaDuplamenteLigada.ListaDuplamenteLigada import ListaDuplamenteLigada
from Loja.Loja import Loja

class EstruturasDeDados:
  
  def __init__(self):
    # Instanciando Lojas
    self.loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 10")
    self.loja2 = Loja("Padaria", "Rua Japaratuba, 60")
    self.loja3 = Loja("Hortifruti", "Rua das Aroeiras, 1900")
    self.loja4 = Loja("Supermercado", "Avenida A, 1900")
    self.loja5 = Loja("Mini mercado", "Avenida B, 564")
    self.loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")
    
  def ListaLigadaInstance(self):
    # Iniciando a lista
    lista = ListaLigada()
    # Adicionando itens
    lista.inserir_inicio(self.loja1)
    lista.inserir_inicio(self.loja2)
    lista.inserir_inicio(self.loja3)
    lista.inserir(1, self.loja4)
    lista.inserir(0, self.loja5)
    lista.inserir(2, self.loja6)
    
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
  
if __name__ == '__main__':
  main = EstruturasDeDados()
  main.ListaLigadaInstance()