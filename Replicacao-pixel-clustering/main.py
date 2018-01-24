'''
Created on 17 de dez de 2017

@author: raul1
'''
import threading

from execucoes import executarIntensity

if __name__ == '__main__':
    # pPixel40 = [("yale","resultados yale", 15, 100, 1, 40),("orl","resultados orl", 40, 100, 1, 40),("umist", "resultados umist", 20,100,1,40)]
    # pPixel26 = [("yale","resultados yale126", 15, 100, 1, 126),("orl","resultados orl126", 40, 100, 1, 126),("umist", "resultados umist126", 20,100,1,126)]
    # pPixel10 = [("yale","resultados yale10", 15, 100, 1, 10),("orl","resultados orl10", 40, 100, 1, 10),("umist", "resultados umist10", 20,100,1,10)]
    # pPixel16 = [("yale", "resultados yale10", 15, 100, 1, 16), ("orl", "resultados orl10", 40, 100, 1, 16),("umist", "resultados umist10", 20, 100, 1, 16)]

    def exeYale():
        executarIntensity("yale", 15, 100, 1)

    def exeUmist():
        executarIntensity("umist", 20,100,1)

    def exeOrl():
        executarIntensity("orl", 40, 100, 1)

    t1 = threading.Thread(name='execucaoYale', target=exeYale())
    t2 = threading.Thread(name='execucaoUmist', target=exeUmist())
    t3 = threading.Thread(name='execucaoOrl', target=exeOrl())

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
    pass
