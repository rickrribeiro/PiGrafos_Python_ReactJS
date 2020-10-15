#include "grafo.h"

void salvar_pajek(grafo *g){ 
	ofstream file("grafo.pajek");
	vector<arestas*> arestasNaoDirecionadas; //para nao rodar o vector duas vezes
	file<<"*vertices "<<numVertices<<"\n";
	for (const auto& vertice : g->vertices){  
        	file<<vertice->id<<" \""<<vertice.id<<"\"\n";
  	}
  	
  	file<<"*arcs\n";
	for (const auto& arco : g->arestas){
		if(arco->dirigido){
			file<<arco->saida<<" "<<arco->entrada<<" "<<arco->peso<<"\n";
		}else{
			arestasNaoDirecionadas.push_back(arco);
		}
        	
  	}
  	
  	file<<"*edges\n";
	for (const auto& aresta : arestasNaoDirecionadas){  
        	file<<aresta->saida<<" "<<aresta->entrada<<" "<<aresta->peso<<"\n";
  	}
	file.close();
}
