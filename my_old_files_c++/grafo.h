#include<bits/stdc++.h>
using namespace std;
#include "matrizAdj.h"

typedef struct aresta aresta;
typedef struct vertice vertice;


struct vertice{
	int id;
	int cor; //para a busca 1branco, 2cinza, 3preto
	vector<vertice*> arestas; //todos os vertices ligados
};

struct aresta{
	int id;
	vertice *saida;
	vertice *entrada; //se não for dirigido nao tem diferença
	int peso;
	bool dirigido;
};

typedef struct grafo{
	vector<vertice*> vertices;
	vector<arestas*> arestas;
	int numVertices;
	int numArestas;
}grafo;

vertice* criaVertice(int id){
	vertice *nova = (vertice*)malloc(sizeof(vertice));
	nova->cor = 1;
	nova->id=id;
	return nova;
}

aresta* criaAresta(int id, vertice *entrada, vertice *saida, int peso){ // se não for um digrafo não tem diferença
	aresta *nova = (aresta*)malloc(sizeof(aresta));
	nova->id = id
	nova->peso = peso;
	nova->saida = saida;
	nova->entrada = entrada;
	return nova;
}

grafo* criaGrafo(){
	grafo *novo = (grafo*)malloc(sizeof(grafo));
	novo->numVertices=0;
	novo->numArestas= 0;
	return novo;
}


