typedef int** matrizAdjacencia;
void preencheListaAdj(matrizAdjacencia matrizAdj, int tamanho){
	int vIni, vFin;
	while(1){
		cout<<"Digite com espaço os vertices que estão ligados do menor para o maior e 0 0 para parar:";
		cin>>vIni>>vFin;
		if(vIni==0 && vFin == 0){
			return;
		}else if((vIni<0 || vFin<0)||(vIni>tamanho-1 || vFin>tamanho-1)){
			cout<<"Vertice invalida"<<endl;
			continue;
		}else{
			matrizAdj[vIni][vFin]=1;
		}
	}
}
void printarListaAdj(matrizAdjacencia matrizAdj,int tamanho){
	cout<<" ";
	for(int i=0;i<tamanho;i++){
		cout<<" "<<i;
	}
	cout<<endl;
	for(int i=0;i<tamanho;i++){
		cout<<i;
		for(int j=0;j<tamanho;j++){
			cout<<" "<<matrizAdj[i][j];
		}
		cout<<endl;
	}
}

