from build import Graph
from build import Addons
import flask
from flask import jsonify
from flask import request

def main():
    my_graph = Graph()
    
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    @app.route('/', methods=['GET'])
    def home():
       print("aqq")
     #  my_graph.AddMultNodes("1")
      # my_graph.AddNode('1')
       print(my_graph.ShowNodes())
       return jsonify(list(my_graph.ShowNodes()))
       
    @app.route('/add', methods=['POST'])
    def add():
       print("aq")
       data = request.form
       print("data:")
       print(data)
       my_graph.AddNode('1')
       
       return jsonify("adicionado")
       
       
    @app.route('/Clear', methods=['GET'])
    def clear():
        my_graph.ClearGraph()
        return jsonify("Grafo Limpo")
	
	
	
	
	
	
	
    app.run()
  
        
       # print("\nBem vindo ao projeto av2 ! ")
       # print("\n1- Adicionar vertice individualmente.")
      #  print("2- Adicionar varios vertices.") #"spam"  4 nos: 's', 'p', 'a', 'm'
      #  print("3- Adicionar arestas individualmente.")
       # print("4- Salvar json.")
      #  print("5- Exibir vertices.")
      #  print("6- Exibir arestas.")
      #  print("7- Exibir lista de adjacencia.")
      #  print("8- Grau de um vertice especifico.")
       # print("9- Limpar todos os nos e arestas do grafo.")
       # choice = input("\nEscolha uma das opcoes acima: ")
        
    @app.route('/api/v1/resources/books', methods=['GET'])
    def api_id():
        my_graph.AddMultNodes(1)
        return jsonify(my_graph.ShowNodes())
        
'''
        if choice == '1':
            #my_graph.AddNode(input("Digite o vertice: "))
            #my_graph.PlotGraph()
            my_graph.AdjMatrix()
        elif choice == '2':
            my_graph.AddMultNodes(input("Digite os vertices: "))
        elif choice == '3':
            my_graph.AddEdge(input("Digite a aresta inicial: "),input("Digite a aresta final: "))
            #my_graph.CircularGraph()
            #my_graph.RandomGraph()
            #my_graph.KamadaGraph()
            #my_graph.FruchtermanGraph()
            #my_graph.NumberOfComponents()
            #my_graph.AdjMatrix()
        elif choice == '4':
            my_graph.dump_json_graph("grafo_json")
        elif choice == '5':
            my_graph.ShowNodes()
        elif choice == '6':
            my_graph.ShowEdges()
        elif choice == '7':
            my_graph.ShowListAdj()
        elif choice == '8':
            my_graph.ShowDegreeNode(input("Digite o no desejado: "))
        elif choice == '9':
            my_graph.ClearGraph()
        elif choice == '0':
            my_graph.WritePajek()    
    
        print("\n")

'''

if __name__ == "__main__":
    main()
