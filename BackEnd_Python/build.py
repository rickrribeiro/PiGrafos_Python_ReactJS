import networkx as nx
from networkx.readwrite import json_graph
import json
from outronome import Addons
import matplotlib.pyplot as plt
import scipy
from networkx.drawing.nx_agraph import graphviz_layout
import pylab
import numpy as np

class Graph(object):
    def __init__(self):
        self.G = nx.Graph()
        Addons.CreateLog(self,"Grafo criado!\n")
        Addons.CreateCalculusLog(self,"Log de calculos criado!\n")
    
    def AddNode(self,node):
        self.G.add_node(node)
       
    
    def AddMultNodes(self,nodes):
        self.G.add_nodes_from(nodes)
        Addons.Log(self,"Nos "+nodes+" adicionados com sucesso!\n")
    
    def AddEdge(self,init_node,end_node):
        edge = (init_node,end_node)
        self.G.add_edge(*edge)
        Addons.Log(self,"Aresta "+str(edge)+" adicionada com sucesso!\n")
    
    def AddMultEdges(self,edges):
        self.G.add_edges_from(edges)
    
    def ShowNodes(self):
        Addons.Log(self,"Visualizacao de Nos !\n")
        return self.G.nodes()
        
        
    def ShowEdges(self):
        Addons.Log(self,"Visualizacao de arestas !\n")
        return self.G.edges()
        
        
    def ShowListAdj(self):
        Addons.Log(self,"Lista de adjacencia gerada !\n")
        return self.G.adj
        
    
    def ShowDegreeNode(self,node):
        Addons.Log(self,"Visualizacao do grau do no "+str(node)+" !\n")
        return self.G.degree(node)
        
    
    def ClearGraph(self):
        self.G.clear()
        Addons.Log(self,"Limpeza do grafo concluida !\n")
        
    def dump_json_graph(self,name):
       # print("--> Gerando grafo no arquivo: " + name + ".json")
        jsondata = json_graph.node_link_data(self.G)
        with open(name + '.json', 'w') as fp:
            json.dump(jsondata, fp)
       #print("--> Completo")
        Addons.Log(self,"Json gerado com sucesso !\n")
        return "--> Gerando grafo no arquivo: " + name + ".json"

    def WritePajek(self):
        nx.write_pajek(self.G,"grafo.net")
        Addons.Log(self,"Arquivo Pajek gerado com sucesso !\n")
        
    def ReadPajek(self):
        nx.read_pajek("grafo.net")
        Addons.Log(self,"Arquivo Pajek carregado com sucesso !\n")
        
    def PlotGraph(self):
        nx.draw(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_Simple.png")
        plt.clf()
        
    def CircularGraph(self):
        nx.draw_circular(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_Circular.png")
        plt.clf()
        
    def RandomGraph(self):
        nx.draw_random(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_Random.png")
        plt.clf()
    
    def KamadaGraph(self):
        nx.draw_kamada_kawai(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_Kamada.png")
        plt.clf()
        
    def FruchtermanGraph(self):
        pos=nx.spring_layout(self.G)
        nx.draw_spring(self.G,with_labels=True,font_weight='bold')
        plt.savefig("grafo_Fruchterman.png")
        plt.clf()
        
    def NumberOfNodes(self):
        Addons.CalculusLog(self,"Numero de nos: " + str(len(self.G)))
        return len(self.G)
        
    def NumberOfEdges(self):
        Addons.CalculusLog(self,"Numero de arestas: " + str(self.G.number_of_edges()))
        return self.G.number_of_edges()
        
    def NumberOfComponents(self):
        Addons.CalculusLog(self,"Numero de componentes: " + str(self.G.number_of_edges()+len(self.G)))
        return self.G.number_of_edges()+len(self.G)
        
    def ShortestPath(self,init,end):
        return nx.shortest_path(self.G,source=init,target=end)
        
    def GraphDensity(self):
        return nx.density(self.G)
        
    def AverageClustering(self):
        return nx.average_clustering(self.G)
    
    def ReadCSV(self):
        self.G = nx.read_adjlist('AdjGraph.csv',delimiter=',')
    
    def ReadCSVDirectedGraph(self):
        self.G = nx.read_adjlist('AdjGraph.csv',delimiter=',',create_using=nx.DiGraph())
    
    def AdjMatrix(self):
        #A = nx.adjacency_matrix(self.G)
        A = nx.to_numpy_matrix(self.G)
        return A
        
    
    
    """def HierarchyGraph(self,root):
        pos = nx.flow_hierarchy(self.G,root)
        nx.draw(self.G, pos=pos, with_labels=True)
        plt.savefig("grafo_arvore.png")
        
    def plot_tree(self):
        # this plot requires pygraphviz package
        pos = nx.nx_agraph.graphviz_layout(self.G, prog='dot')
        nx.draw(self.G, pos, with_labels=False, node_size=10,
                node_color=[[.5, .5, .5]], arrowsize=4)
        plt.savefig("grafo_arvore.png")"""
