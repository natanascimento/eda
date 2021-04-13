class Fase:
  
  def __init__(self, cenario, pontuacao, punicao):
    self.cenario = cenario
    self.pontuacao = pontuacao
    self.punicao = punicao
  
  def __repr__(self):
      return self.cenario