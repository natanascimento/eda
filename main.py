from EstruturasDeDados.ListaLigada.ListaLigada import ListaLigada
from EstruturasDeDados.ListaDuplamenteLigada.ListaDuplamenteLigada import ListaDuplamenteLigada
from EstruturasDeDados.Pilha.Pilha import Pilha
from EstruturasDeDados.Fila.Fila import Fila
from EstruturasDeDados.Arvore.Arvore import Arvore
from Loja.Loja import Loja
from Fase.Fase import Fase
from Pedido.Pedido import Pedido

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
    # Instanciando fases
    self.fase1 = Fase('Floresta', 300, -100)
    self.fase2 = Fase('Castelo', 400, -200)
    self.fase3 = Fase('Caverna', 100, -30)
    self.fase4 = Fase('Guerra', 3000, -400)
    # Instanciando pedidos
    self.pedido1 = Pedido('Pizza de Calabresa')
    self.pedido2 = Pedido('Pizza de Frango')
    self.pedido3 = Pedido('Pizza de Muçarela')
    self.pedido4 = Pedido('Pizza de Rúcula')
    
  def AvaliarLista(self, lista):
    print("\nQuantidade de elementos na lista: {}".format(lista.quantidade))
    print("Elementos da Lista: ")
    lista.imprimir()
    print("")
    
  def ListaLigadaInstance(self):
    print("##### LISTA LIGADA #####")
    # Iniciando a lista ligada
    lista = ListaLigada()
    # Adicionando itens
    lista.inserir_inicio(self.loja1)
    lista.inserir_inicio(self.loja2)
    lista.inserir_inicio(self.loja3)
    lista.inserir(1, self.loja4)
    lista.inserir(0, self.loja5)
    lista.inserir(2, self.loja6)

    #Avaliar Lista
    self.AvaliarLista(lista)
    
    #Remover Itens
    removido = lista.remover_inicio()
    print("Item removido: {}".format(removido))
    removido = lista.remover_inicio()
    print("Item removido: {}".format(removido))
    
    #Avaliar Lista
    self.AvaliarLista(lista)
    
    #Remover Itens
    removido = lista.remover(1)
    print("Item removido da posicao 1: {}".format(removido))
    
    #Avaliar Lista
    self.AvaliarLista(lista)
    removido = lista.remover(lista.quantidade - 1)
    print("Item removido da posicao {}: {}".format(lista.quantidade, removido))
    
    #Avaliar Lista
    self.AvaliarLista(lista)
    print("Elemento da posicao {}: {}".format(0, lista.item(0)))
    
  def ListaDuplamenteLigadaInstance(self):
    print("##### LISTA DUPLAMENTE LIGADA #####")
    #Iniciando a lista duplamente ligada
    lista = ListaDuplamenteLigada()
    #Método para analisar os dados da lista
    self.AvaliarLista(lista)
    #Inserir conteudo na lista
    lista.inserir_no_inicio(self.loja1)
    lista.inserir_no_inicio(self.loja2)
    lista.inserir_no_fim(self.loja3)
    lista.inserir_no_fim(self.loja4)
    #Avaliar Lista
    self.AvaliarLista(lista)
    lista.inserir(2, self.loja10)
    #Avaliar Lista
    self.AvaliarLista(lista)
    
    removido = lista.remover_do_inicio()
    print("Item removido: {}".format(removido))
    #Avaliar Lista
    self.AvaliarLista(lista)
    
    removido = lista.remover_do_fim()
    print("Item removido: {}".format(removido))
    #Avaliar Lista
    self.AvaliarLista(lista)
  
    removido = lista.remover(0)
    print("Item removido da posicao 0: {}".format(removido))
    #Avaliar Lista
    self.AvaliarLista(lista)
    
  def ValidarItensEmRange(self, lista):
    self._min = int(input("Informe o valor minimo do range: "))
    self._max = int(input("Informe o valor maximo do range: "))
    print("Elementos da Lista no range: {}".format([lista.item(i) for i in range(self._min, self._max)]))
    
  def PilhaInstance(self):
    print("##### PILHA #####")
    fases = Pilha()
    fases.empilha(self.fase1)
    fases.empilha(self.fase2)
    fases.empilha(self.fase3)
    fases.empilha(self.fase4)
    falhou = fases.desempilha()
    print("Falhou na fase {}".format(falhou))
    print("Voltou para a fase {}".format(fases.topo))
    falhou = fases.desempilha()
    print("Falhou na fase {}".format(falhou))
    print("Voltou para a fase {}".format(fases.topo))
    
  def FilaInstance(self):
    print("##### FILA #####")
    pedidos = Fila()
    #Iniciar pedidos na fila
    pedidos.entrar(self.pedido1)
    pedidos.entrar(self.pedido2)
    pedidos.entrar(self.pedido3)
    pedidos.entrar(self.pedido4)
    #Realizar finalização dos pedidos
    pedido = pedidos.sair()
    print("Pedido {} finalizado".format(pedido))
    print("Está vazia? {}".format(pedidos.vazia))
    
    pedido = pedidos.sair()
    print("Pedido {} finalizado".format(pedido))
    print("Está vazia? {}".format(pedidos.vazia))
    
    pedido = pedidos.sair()
    print("Pedido {} finalizado".format(pedido))
    print("Está vazia? {}".format(pedidos.vazia))

    pedido = pedidos.sair()
    print("Pedido {} finalizado".format(pedido))
    print("Está vazia? {}".format(pedidos.vazia))
    
  def ArvoreInstance(self):
    print("##### ARVORE #####")
    livraria = Arvore('Livros')
    livraria.raiz.inserir_filho("Gastronomia")
    livraria.raiz.inserir_filho("Informatica")
    livraria.imprimir()
    
    encontrado = livraria.localizar_node("Livros")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_node("Gastronomia")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_node("Informatica")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_node("Turismo")
    print("Encontrado: {}".format(encontrado))
    
    livraria.inserir_node("Informatica", "Linguagem de programacao")
    livraria.inserir_node("Linguagem de programacao", "Python")
    livraria.inserir_node("Gastronomia", "Mexicana")
    livraria.imprimir()
    
    removido = livraria.remover_node("Mexicana")
    print("Removido: {}".format(removido))
    
    removido = livraria.remover_node("Informatica")
    print("Removido: {}".format(removido))
    
    livraria.imprimir()
    
if __name__ == '__main__':
  main = EstruturasDeDados()
  #main.ListaLigadaInstance()
  #main.ListaDuplamenteLigadaInstance()
  #main.PilhaInstance()
  #main.FilaInstance()
  main.ArvoreInstance()