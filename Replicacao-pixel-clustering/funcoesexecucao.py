'''
Created on 25 de nov de 2017

@author: raul
'''
from classificadores import classicarKNN
from imagemparabase import imgsParaBase
from pixelcluster import PixelCluster
from base import Base
from sklearn.model_selection import train_test_split

  
def execucaoPixel(base,arq,qtCla=15,hold=10,k=1,clusters=40):
    caminhoArq = "Resultados/%s"%arq
    arqSave = open(caminhoArq,"w")
    baseAtual = imgsParaBase("Bases/%s"%base,qtClasses=qtCla)
    baseAtual.embaralharBase()
    erro = 0
    for i in range(hold):
        train_atr, test_atr, train_classes, test_classes = train_test_split(baseAtual.atributos, baseAtual.classes, test_size=0.5, random_state=i) 
        bTreino = Base(train_classes,train_atr)
        bTeste = Base(test_classes,test_atr)
        pCluster = PixelCluster()
        pCluster.fit(bTreino,clusters)
        bTreino = pCluster.run(bTreino)
        bTeste = pCluster.run(bTeste)
        erro = classicarKNN(bTreino.atributos, bTreino.classes, bTeste.atributos, bTeste.classes,k) + erro
    resultados = "Acerto: %s\n"%(1 - (erro/hold))
    print(resultados)
    arqSave.write(resultados)
    arqSave.close()
    
    