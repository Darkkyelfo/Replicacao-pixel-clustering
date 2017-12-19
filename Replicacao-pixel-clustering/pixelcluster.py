'''
Created on 15 de dez de 2017

@author: raul1
'''
import numpy as np
from sklearn.cluster import KMeans
from base import Base
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
                media = np.mean(matriz)
                novosAtr[-1].append(media)
        return novosAtr
                

class TecnicaCluster(object):
    
    @staticmethod
    def kMeans(k,vetorDePixels):
        kmeans = KMeans(n_clusters=k, random_state=0).fit(vetorDePixels)
        return kmeans.labels_
        
class PixelCluster(object):

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

    def fit(self,baseTreino,k,tipoVetorPixel="intensidade",tecnica="kmeans"):
        self.k = k
        self._extrairVetorDePixels(baseTreino, tipoVetorPixel)
        self._clusterizar(tecnica)
    
    #Separa o valores contidos no vetor de pixel em um array bidimensional
    #onde cada elemento é o vetor com os atributos.
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
        return Base(base.classes,self.novosAtr,base.posicoes)
        
        
    
                
                
                
                
                
            
            
        
        
        