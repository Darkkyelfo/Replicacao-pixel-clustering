'''
Created on 15 de dez de 2017

@author: raul1
'''
import numpy as np
from sklearn.cluster import KMeans
from base import Base
import time
import math

def arredondar(numero):
    if((numero - int(numero))!=0):
        return int(numero+1)
    return int(numero)

def deveIncrementar(numero):
    if((numero - int(numero))!=0):
        return 1
    return 0
#Classe responsavel por criar o vetor de pixel
class CriarVetor(object):
    
    @staticmethod
    def intensidade(baseTreino):
        atr = np.array(baseTreino.atributos).T
        return atr       

class Projetar(object):
    
    @staticmethod
    def comMedia(atrsCluster):
        novosAtr = []
        for matrizes in atrsCluster:
            novosAtr.append([])
            for matriz in matrizes:
                #print("pixels por cluster:%s"%len(matriz))
                media = np.mean(matriz)
                novosAtr[-1].append(media)
        return novosAtr
                 

class TecnicaCluster(object):
    
    @staticmethod
    def kMeans(k,vetorDePixels):
        kmeans = KMeans(n_clusters=k, random_state=0).fit(vetorDePixels)
        return kmeans.labels_

    @staticmethod
    def quadrado(u,base):
        if(u>=max(base.linhas,base.colunas)):
            return base.atributos
        divLinhas = base.linhas/u
        divColunas = base.colunas/u
        qtClusters = arredondar(divLinhas)*arredondar(divColunas)
        imgsClusterizadas = []
        for img in base.matrizImgs:
            clusters = [[] for i in range(qtClusters)]
            cont2 = 0
            indCluster = 0
            ant = indCluster
            for linha in range(img.shape[0]):
                cont = 0
                if(cont2==u):
                    cont2 = 0
                    ant = indCluster + deveIncrementar(divColunas)
                indCluster = ant
                for coluna in range(img.shape[1]):
                    clusters[indCluster].append(img[linha][coluna])
                    cont+=1
                    if(cont == u):
                        indCluster+=1
                        cont = 0
                cont2+=1
            imgsClusterizadas.append(clusters)
        return imgsClusterizadas
                    
        
class IntensityPatches(object):

    def _extrairVetorDePixels(self,baseTreino,tipo="intensidade"):
        self.vPixels = self._escolherTipoVetorPixel(baseTreino, tipo)
    
    def _escolherTipoVetorPixel(self,baseTreino,tipo):
        if(tipo=="intensidade"):
            return CriarVetor.intensidade(baseTreino)
    

    def _clusterizar(self,tecnica="kmeans"):
        labels = self._escolherTecnicaClusterizacao(tecnica)
        clusters = {}
        for i,cluster in enumerate(labels):
            clusters[i] = cluster
        self.clusters = clusters
            
    def _escolherTecnicaClusterizacao(self,tecnica):
        if(tecnica=="kmeans"):
            return TecnicaCluster.kMeans(self.k,self.vPixels)

    def fit(self,baseTreino,k,tecnica="kmeans",tipoVetorPixel="intensidade"):
        self.k = k
        self._extrairVetorDePixels(baseTreino, tipoVetorPixel)
        self._clusterizar(tecnica)
    
    #Separa o valores contidos no vetor de pixel em um array bidimensional
    #onde cada elemento � o vetor com os atributos.
    def _separarAtrClusters(self,base):
        self.atrsCluster = []
        for atr in base.atributos:
            self.atrsCluster.append([])
            for k in range(self.k):
                self.atrsCluster[-1].append([])
            for i,elemento in enumerate(atr):
                self.atrsCluster[-1][self.clusters[i]].append(elemento)
    
    def _projetar(self,tipoProjecao):
        self.novosAtr = self._definirTipoProjecao(tipoProjecao)
    
    def _definirTipoProjecao(self,tipoProjecao):
        if(tipoProjecao=="media"):
            return Projetar.comMedia(self.atrsCluster)
     
    def run(self,base):
        self._separarAtrClusters(base)
        self._projetar("media")
        return Base(base.classes,self.novosAtr)

class RegionPatches(object):
    
    def clusterizar(self,base,u):
        self.base = base
        self.u = u
        self.clusters = TecnicaCluster.quadrado(u, base)
        
    def _projetar(self,tipoProjecao):
        self.novosAtr = self._definirTipoProjecao(tipoProjecao)
    
    def _definirTipoProjecao(self,tipoProjecao):
        if(tipoProjecao=="media"):
            return Projetar.comMedia(self.clusters)
    
    def run(self,tipoProjecao = "media"):
        self._projetar(tipoProjecao)
        return Base(self.base.classes,self.novosAtr)
        
        
    
    
    
        
    
                
                
                
                
                
            
            
        
        
        