from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Jorge')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
