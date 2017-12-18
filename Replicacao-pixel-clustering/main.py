'''
Created on 17 de dez de 2017

@author: raul1
'''
from pixelcluster import PixelCluster
from imagemparabase import imgsParaBase
from classificadores import classicarKNN
if __name__ == '__main__':
    bYale = imgsParaBase("Bases/yale")
    subBases = bYale.gerarSubBases(2)
    bTeste = subBases[0]
    bTreino = subBases[1]
    
    pC = PixelCluster()
    pC.fit(bTreino, 10)
    b1 = pC.run(bTeste)
    b2 = pC.run(bTreino)
    print(classicarKNN(b2.atributos,b2.classes,b1.atributos,b1.classes))
    pass