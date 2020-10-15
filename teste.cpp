#include<bits/stdc++.h>

using namespace std;

typedef struct teste{
	int a;
}teste;
int main(){
	vector<teste*> a;
	teste *b = (teste*)malloc(sizeof(teste));
	b->a = 10;
	a.push_back(b);
	cout<<a.at(0)->a<<endl;
}
