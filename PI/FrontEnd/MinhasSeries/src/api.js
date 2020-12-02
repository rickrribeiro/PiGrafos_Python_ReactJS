import axios from 'axios'

//API DB
const api = axios.create({
    baseURL:'http://localhost:3001/'

})

//API Grafos
const apiGraph = axios.create({
    baseURL:'http://localhost:5000/'

})
//export const loadGenres : () => api.get('genres')
const apis = {
    //API DB
    loadGenres : () => api.get('genres'),
    loadSeries : () => api.get('series'),
    loadstatusSerie : () => api.get('status'),
    saveSerie : (newSerie) => api.post('series', newSerie),
    loadSeriesByGenre : (genre) => api.get('series?genre='+genre),
    deleteSeries : (id)=>api.delete('series/'+id),
    loadSeriesById : (id) => api.get('series/'+id),
    updateSeries : (series) =>api.put('series/'+series.id,series),
    deleteall: () => {
        api.get('series').then((val)=>{
            val.data.forEach(element => {
                api.delete('series/'+element.id)
            });
        })
        

    },
    
    //API Graph
    getRecommendation:() =>{
        apiGraph.get('getRecommendation').then((val)=>{
            console.log(val.data)
            alert(val.data);
        })

    },
    generateGraph : (graph) => apiGraph.post('generateGraphs', graph)
}
export default apis