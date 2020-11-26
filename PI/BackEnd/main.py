from build import Graph
from build import Addons
from build import Recommendations
import flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin

def main():
    my_graph = Graph()
    
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'application/json'


    ##################          ALL GET DATA ENDPOINTS           ###########################
    @app.route('/', methods=['GET'])
    @cross_origin()
    def home():
       return jsonify("Grafos")
    
    @app.route('/getNodes', methods=['GET'])
    @cross_origin()
    def getNodes():
       print(my_graph.ShowNodes())
       return jsonify(list(my_graph.ShowNodes()))
       
       
       
    @app.route('/getEdges', methods=['GET'])
    @cross_origin()
    def getEdges():    
       return jsonify(list(my_graph.ShowEdges()))
       
       
    @app.route('/getList', methods=['GET'])
    @cross_origin()
    def getAdjacencia():    
       print(my_graph.ShowListAdj())
       return jsonify(str(my_graph.ShowListAdj()))   
       
    @app.route('/getMatrix', methods=['GET'])
    @cross_origin()
    def getMatrix():    
       print(my_graph.AdjMatrix())
       return jsonify(str(my_graph.AdjMatrix())) 
        
    @app.route('/getNNodes', methods=['GET'])
    @cross_origin()
    def getNVertice():    
       return jsonify(str(my_graph.NumberOfNodes()))
       
       
    @app.route('/getNEdges', methods=['GET'])
    @cross_origin()
    def getNEdges():    
       return jsonify(str(my_graph.NumberOfEdges()))
    
    
    
    @app.route('/getNComponents', methods=['GET'])
    @cross_origin()
    def getNComponents():    
       return jsonify(str(my_graph.NumberOfComponents()))
       
       
    @app.route('/getDensity', methods=['GET'])
    @cross_origin()
    def getDensity():    
       return jsonify(str(my_graph.GraphDensity()))
       
       
    @app.route('/getClustering', methods=['GET'])
    @cross_origin()
    def getClustering():    
       return jsonify(str(my_graph.AverageClustering()))
        
       
       
       
    @app.route('/getDegree', methods=['POST'])
    @cross_origin()
    def getDegree():    
       
       node = request.get_json()
       print(my_graph.ShowDegreeNode(node))
       return jsonify(my_graph.ShowDegreeNode(node))   
       
       
       
       
    @app.route('/getPath', methods=['POST'])
    @cross_origin()
    def getPath():
       data = str(request.json)
      # data.replace("b","'")
       #data = request.args.get('body')
       data = data.split(".")
       print(data[1])
       result = my_graph.ShortestPath(int(data[0]) , int(data[1]))
       
       return jsonify(str(result))   
       
       
          
    @app.route('/Clear', methods=['GET'])
    @cross_origin()
    def clear():
        my_graph.ClearGraph()
        return jsonify("Grafo Limpo")   
      
    ###################            Generate files ENDPOINTS          ######################
    @app.route('/generateJSON', methods=['GET'])
    @cross_origin()
    def generateJson():    
       return jsonify(my_graph.dump_json_graph("graph")) 
    
    @app.route('/getKamada', methods=['GET'])
    @cross_origin()
    def getKamada():    
       my_graph.KamadaGraph()
       return jsonify("teste") 
       
       
    @app.route('/getSimple', methods=['GET'])
    @cross_origin()
    def getSimple():    
       my_graph.PlotGraph()
       return jsonify("teste")
       
       
    @app.route('/getCircular', methods=['GET'])
    @cross_origin()
    def getCircular():    
       my_graph.CircularGraph()
       return jsonify("teste")  
       
       
    @app.route('/getRandom', methods=['GET'])
    @cross_origin()
    def getRandom():    
       my_graph.RandomGraph()
       return jsonify("teste") 
      
      
    @app.route('/getFruchterman', methods=['GET'])
    @cross_origin()
    def getFruchterman():    
       my_graph.FruchtermanGraph()
       return jsonify("teste") 
      
    ###################            ALL POST DATA ENDPOINTS           ######################
       
    @app.route('/addNode', methods=['POST'])
    @cross_origin()
    def addNode():
       print("aq")
       data = request.get_json()
       print("data:")
       print(data)
       my_graph.AddNode(data)
       
       return jsonify("adicionado")
       
       
    @app.route('/addEdge', methods=['POST'])
    @cross_origin()
    def addEdge():
       print("aq")
       data = str(request.json)
      # data.replace("b","'")
       #data = request.args.get('body')
       data = data.split(".")
       print(data[1])
       my_graph.AddEdge(int(data[0]) , int(data[1]))
       
       return jsonify("adicionado")   
       
       
    
	 
	
	###################            ALL PI NEW ENDPOINTS           ######################
	
    @app.route('/generateGraphs', methods=['POST'])
    @cross_origin()
    def generateGraphs():
        print(request.get_json())
        my_graph.ClearGraph()
        if request.json['referencia'] == 'status':
            for val in request.json['statusList']: #adiciona todos os status
                my_graph.AddNode(val)
            for val in request.json['series']: #adiciona as series
                if request.json['status'] == 'all' or request.json['status'] == val['status']:
                    if request.json['genre'] == 'all' or val['genre'] == request.json['genre']:   
                        my_graph.AddEdge(val['name'],val['status'])
                                          

        else:
            for val in request.json['genreList']: #adiciona todos os generos
                my_graph.AddNode(val)
            for val in request.json['series']: #adiciona todas as series
                if request.json['status'] == 'all' or request.json['status'] == val['status']:
                    if request.json['genre'] == 'all' or val['genre'] == request.json['genre']:  
                        my_graph.AddEdge(val['name'],val['genre'])    

        my_graph.PlotGraph()
        my_graph.FruchtermanGraph()
        my_graph.RandomGraph()
        my_graph.CircularGraph()
        my_graph.KamadaGraph()            
        
      
        return jsonify("adicionado")   
	
	
    app.run()
  
        
       # print("\nBem vindo ao projeto av2 ! ")
       # print("\n1- Adicionar vertice individualmente.") DONE
      #  print("2- Adicionar varios vertices.") #"spam"  4 nos: 's', 'p', 'a', 'm' DONE
      #  print("3- Adicionar arestas individualmente.") DONE
       # print("4- Salvar json.") DONE
      #  print("5- Exibir vertices.") DONE
      #  print("6- Exibir arestas.") DONE
      #  print("7- Exibir lista de adjacencia.") DONE
      #  print("8- Grau de um vertice especifico.") DONE
       # print("9- Limpar todos os nos e arestas do grafo.") DONE
       # choice = input("\nEscolha uma das opcoes acima: ")
        
    @app.route('/api/v1/resources/books', methods=['GET'])
    @cross_origin()
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
