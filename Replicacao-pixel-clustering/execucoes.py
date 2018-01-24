'''
Created on 30 de dez de 2017

@author: raul1
'''
from classificadores import classicarKNN
from imagemparabase import imgsParaBase
from dividirbase import Holdout
from pixelcluster import IntensityPatches
from numba import jit

def executarIntensity(base,qtCla=15,hold=10,knn=1):
    #Bases
    if(base=="georgia"):
        baseAtual = imgsParaBase("Bases/%s"%base,qtClasses=qtCla,dirClasse = "s",tipoArq = "jpg")
    else:
        baseAtual = imgsParaBase("Bases/%s"%base,qtClasses=qtCla)

    rodarInt(base,baseAtual,hold,knn)

def gerarBases(baseAtual,hold):
    bases = []
    for k in range(hold):
        bTesteOri, bTreinoOri = Holdout.dividirImg(baseAtual)
        bases.append([bTesteOri,bTreinoOri])
    return bases

def criarCSV(nome,valores):
    caminhoArq = "Resultados/%s"%nome+".csv"
    arqSave = open(caminhoArq,"a")
    arqSave.write(valores)
    arqSave.close()

@jit
def rodarInt(nomeBase,baseAtual,hold,k):
    basesHold = gerarBases(baseAtual,hold+1)
    bTreinoOri = basesHold[0][0]
    for j in range(1,12):
        pCluster = IntensityPatches()
        pCluster.fit(bTreinoOri, 2**j)
        erro = 0
        for h in basesHold[1:]:
            bTeste = h[0]
            bTreino = h[1]
            bTreino = pCluster.run(bTreino)
            bTeste = pCluster.run(bTeste)
            erro = classicarKNN(bTreino.atributos, bTreino.classes, bTeste.atributos, bTeste.classes,k) + erro
        criarCSV("IntensityPatches_%s" % nomeBase, "%s,%s\n" % (2**j,1 - (erro / hold)))
        print("IntensityPatches_%s" % nomeBase, "%s,%s\n" % (2**j,1 - (erro / hold)))
