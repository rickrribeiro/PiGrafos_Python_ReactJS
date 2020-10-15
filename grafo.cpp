#include "graph.h"

/*


*/


int main(){
	int tamanho;
	cout<<"Digite o tamanho do grafo: ";
	cin>>tamanho;
	matrizAdjacencia matrizAdj=  (int**)malloc(tamanho * sizeof(int*));
	for (int lin = 0; lin < tamanho; lin++) {
       		 matrizAdj[lin] = (int*)malloc(tamanho * sizeof(int*));
 	   }
	preencheListaAdj(matrizAdj, tamanho);
	printarListaAdj(matrizAdj, tamanho);
	grafo gaf = criaGrafo(matrizAdj,tamanho);
	/*for(int i=0;i<gaf.vertices.size();i++){
		cout<<i<<": ";
		cout<<gaf.vertices.at(i).id<<endl;
	} */
	//cout<<gaf.vertices.at(0).arestas.at(0).id;
	int encontrar;
	cout<<"Digite qual no voce quer encontrar: ";
	cin>>encontrar;
	string caminho = buscaProf(&gaf.vertices.at(0), encontrar);
	if(caminho != ""){
	cout<<caminho<<endl;
	}else{
		cout<<"caminho nao encontrado"<<endl;
	}
}

