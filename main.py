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
    self.loja6 = Loja("Quitanda", "Avenida Natan Nascimento, 22")
    self.loja7 = Loja("Supermercado", "Avenida Oliveira, 21")
    self.loja8 = Loja("Padaria", "Rua Matos, 25")
    self.loja9 = Loja("Mercadinho", "Avenida Rio Branco, 1593")
    self.loja10 = Loja("Hortifruti", "Avenida Olimpia, 759")
    
  def AvaliarLista(self, lista):
    print("\nQuantidade de elementos na lista: {}".format(lista.quantidade))
    print("Elementos da Lista: ")
    lista.imprimir()
    print("")
    
  def ListaLigadaInstance(self):
    print("##### LISTA LIGADA ######")
    # Iniciando a lista
    lista = ListaLigada()
    # Adicionando itens
    lista.inserir_inicio(self.loja1)
    lista.inserir_inicio(self.loja2)
    lista.inserir_inicio(self.loja3)
    lista.inserir(1, self.loja4)
    lista.inserir(0, self.loja5)
    lista.inserir(2, self.loja6)
    
    self.AvaliarLista(lista)
    #Remover Itens
    removido = lista.remover_inicio()
    print("Item removido: {}".format(removido))
    removido = lista.remover_inicio()
    print("Item removido: {}".format(removido))
    self.AvaliarLista(lista)
    removido = lista.remover(1)
    print("Item removido da posicao 1: {}".format(removido))
    self.AvaliarLista(lista)
    removido = lista.remover(lista.quantidade - 1)
    print("Item removido da posicao {}: {}".format(lista.quantidade, removido))
    self.AvaliarLista(lista)
    print("Elemento da posicao {}: {}".format(0, lista.item(0)))
    
  def ListaDuplamenteLigadaInstance(self):
    print("##### LISTA DUPLAMENTE LIGADA ######")
    lista = ListaDuplamenteLigada()
    self.AvaliarLista(lista)
    lista.inserir_no_inicio(self.loja1)
    lista.inserir_no_inicio(self.loja2)
    lista.inserir_no_fim(self.loja3)
    lista.inserir_no_fim(self.loja4)
    self.AvaliarLista(lista)
    lista.inserir(2, self.loja10)
    self.AvaliarLista(lista)
    
    removido = lista.remover_do_inicio()
    print("Item removido: {}".format(removido))
    self.AvaliarLista(lista)
    
    removido = lista.remover_do_fim()
    print("Item removido: {}".format(removido))
    self.AvaliarLista(lista)
  
    removido = lista.remover(0)
    print("Item removido da posicao 0: {}".format(removido))
    self.AvaliarLista(lista)
    
  def ValidarItensEmRange(self, lista):
    self._min = int(input("Informe o valor minimo do range: "))
    self._max = int(input("Informe o valor maximo do range: "))
    print("Elementos da Lista no range: {}".format([lista.item(i) for i in range(self._min, self._max)]))
    
if __name__ == '__main__':
  main = EstruturasDeDados()
  #main.ListaLigadaInstance()
  main.ListaDuplamenteLigadaInstance()