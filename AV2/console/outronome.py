import networkx as nx

class Addons(object):
    
    def CreateLog(self,action):
        print("--> Arquivo log atualizado: log.txt")
        with open('log.txt', 'w') as fp:
            fp.write(action)
        print("--> Log atualizado")
        fp.close()
        
    def Log(self,action):
        print("--> Arquivo log atualizado: log.txt")
        with open('log.txt', 'a') as fp:
            fp.write(action)
        print("--> Log atualizado")
        fp.close()
        
    def CreateCalculusLog(self,action):
        print("--> Arquivo log atualizado: logCalculus.txt")
        with open('logCalculus.txt', 'w') as fp:
            fp.write(action)
        print("--> Log de Calculo atualizado")
        fp.close()
        
    def CalculusLog(self,action):
        print("--> Arquivo log atualizado: logCalculus.txt")
        with open('logCalculus.txt', 'a') as fp:
            fp.write(action)
        print("--> Log de Calculo atualizado")
        fp.close()
