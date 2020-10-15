//incompoleto

string buscaProf(vertice *cabeca, int encontrar){
	//cout<<"id: "<<cabeca->id<<endl;
	string aux="";
	cabeca->cor = 2;
	for(int i=0;i<cabeca->arestas.size();i++){
	//cout<<"arestas size: "<<cabeca->arestas.size()<<endl;
		if(cabeca->arestas.at(i).id == encontrar){
	//		cout<<"entrou aq"<<endl;
			aux = to_string(encontrar);
		}else{
	//		cout<<"entrou aq2"<<endl;
			if(cabeca->arestas.at(i).cor==1){
	//		cout<<"entrou if"<<endl;
				aux = buscaProf(&cabeca->arestas.at(i), encontrar);
				cabeca->cor = 3;
			}
			
		}
	}
	if(aux!=""){
		return to_string(cabeca->id)+"->"+aux;
	}else{
		return "";
	}
}


