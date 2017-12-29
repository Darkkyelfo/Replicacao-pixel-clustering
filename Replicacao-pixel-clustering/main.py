'''
Created on 17 de dez de 2017

@author: raul1
'''
from funcoesexecucao import execucaoPixel,executarRegionPatches
from multiprocessing import Pool

if __name__ == '__main__':
   
    pPixel40 = [("yale","resultados yale", 15, 100, 1, 40),("orl","resultados orl", 40, 100, 1, 40),("umist", "resultados umist", 20,100,1,40)]
    pPixel26 = [("yale","resultados yale126", 15, 100, 1, 126),("orl","resultados orl126", 40, 100, 1, 126),("umist", "resultados umist126", 20,100,1,126)]
    pPixel10 = [("yale","resultados yale10", 15, 100, 1, 10),("orl","resultados orl10", 40, 100, 1, 10),("umist", "resultados umist10", 20,100,1,10)]
   
    def executarPoolPixel(args):
        execucaoPixel(*args)
    
    poolPixel40 = Pool(3)
    poolPixel40.map(executarPoolPixel,pPixel40)

    poolPixel126 = Pool(3)
    poolPixel126.map(executarPoolPixel,pPixel26)
    
    poolPixel126 = Pool(3)
    poolPixel126.map(executarPoolPixel,pPixel10)
   
    executarRegionPatches("orl", "resultadosOrlRegion23",40,100,16,1)
    executarRegionPatches("umist", "resultadosUmistRegion23",20,100,23,1)
    
    pass