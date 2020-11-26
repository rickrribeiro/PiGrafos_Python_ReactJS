import pandas as pd
import json

class Recommendations(object):

 
   def recommended():
      with open('../FrontEnd/MinhasSeries/db.json') as json_data:
         data = json.load(json_data)
        
         df = pd.DataFrame(data['series']) ###Cria o data frame com todas as series
         ####cria o data frame por genero
         dfDrama = df[df['genre']=='Drama']
         dfComedia = df[df['genre']=='Comédia']
         dfAcao = df[df['genre']=='Ação']
         ####calcula a % dos filmes salvos de cada genero que a pessoa assistiu ----- !!!!!!lembrar de pensar em uma forma de botar um peso pra quantidade de filmes para não ter:(10 comedias sendo que 9 assistindos e 1 ação que foi assistido e recomendar ação ) exemplo: 0.5*qtTotal * %assistido!!!!!!
         mediaComedia = (dfComedia['status'].value_counts())['watched']/dfComedia.shape[0]
         mediaAcao = (dfAcao['status'].value_counts())['watched']/dfAcao.shape[0]
        # mediaDrama = (dfDrama['status'].value_counts())['watched']/dfDrama.shape[0]
         print(mediaComedia)
         print(mediaAcao)
        # print(mediaDrama)
        ### ve qual é a maior media e printa os filmes -- !!botar pra verificar se tem algum toWatch, se não tiver retornar o segundo maior(ou terceiro ou nenhum)!!!!!
         if mediaComedia > mediaAcao:
            print(dfComedia[dfComedia['status']=='toWatch']['name'].to_string(index=False)) 
         if mediaAcao > mediaComedia:
            print(dfAcao[dfAcao['status']=='toWatch']['name'].to_string(index=False))
        
        
       