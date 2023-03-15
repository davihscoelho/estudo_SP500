from scipy.stats import norm
import numpy as np

def criar_precos(media,desvio,variancia,tamanho,preco_inicial):
  #Media, desvio e varaiancia são baseados em um log returns
  #O tamanho se refere a quantidade de dias passados no caso de um backtesting ou dias futuros
  #Adota-se aqui uma distribuição Normal
  
  #Calcular o Brownian Motion 
  NumIntervals = tamanho
  Iterations = 20

  np.random.seed(7)
  SBMotion = norm.ppf(np.random.rand(NumIntervals, Iterations)) 
  
  #Calcular o Drift
  drift = media - 0.5*variancia
  
  #Retorno Diario
  DailyReturns = np.exp(drift+desvio*SBMotion)
  
  #Serie Preços Construcao
  serie_precos = np.zeros_like(DailyReturns)
  
  #Preço Inicial
  serie_precos[0] = preco_inicial
  
  #Construcao da Serie
  for t in range(1,tamanho):
    serie_precos[t] = serie_precos[t-1]*DailyReturns[t]
  
  return serie_precos

