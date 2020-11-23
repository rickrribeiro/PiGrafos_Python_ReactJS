import React, {Component} from 'react'
import apis from './api'
import { Redirect } from 'react-router-dom'



class Grafos extends Component{
   
    
    constructor(props){
        super(props)
        this.state={
            count:0,
            statusSerie:[],
            genre:[],
            series:[],
            isLoading:false,
            redirect:false
        }
        this.gerarGrafos = this.gerarGrafos.bind(this);
      }  


      gerarGrafos(){
        const newGraph={
          series: this.state.series,
          statusList: this.state.statusSerie,
          genreList: this.state.genre,
          status: this.refs.status.value,
          genre: this.refs.genre.value,
          referencia: this.refs.referencia.value
        }
        apis.generateGraph(newGraph).then(
  
        //   this.setState({
        //     redirect: '/series/'+this.refs.genre.value
        //   })
  
         )
        
      }

      componentDidMount(){
        this.setState.isLoading = true;

        apis.loadGenres().then((res)=>{
           
            this.setState({
             
              genre:res.data
      
            })
          })

        apis.loadstatusSerie().then((res)=>{
           
            this.setState({
                
               
              statusSerie:res.data
      
            })
          })


          apis.loadSeries().then((res)=>{
           
            this.setState({
                
               
                series:res.data,
                isLoading:false
      
            })
          })
          
      }
    


render(){

    return(

      
      <section className="intro-section">
      { this.state.redirect &&
        <Redirect to={this.state.redirect}/>
      
      }

            <h1>Grafos</h1>
            <form>
                   <br/> <br/>
                    Genero: &nbsp; <select ref='genre'>
                        <option key = "all" value="all">all</option>
                        {this.state.genre.map(element =><option key = {element} value={element}>{element}</option>)}
                </select>
                <br/> <br/>
                Status: &nbsp; 
                <select ref='status'>
                        <option key = "all" value="all">all</option>
                        {this.state.statusSerie.map(element =><option key = {element} value={element}>{element}</option>)}
                </select>
                <br/><br/>
                Gerado por:&nbsp;<select ref='referencia'>
                        <option key = "genero" value="genero">Genero</option>
                        <option key = "statua" value="status">Status</option>
                </select>
                <br/> <br/>
               
                <br/> <br/>
                <button  onClick={this.gerarGrafos}>Gerar</button>
            </form>
        </section> //depois botar imagem e description
    )
}


}



export default Grafos