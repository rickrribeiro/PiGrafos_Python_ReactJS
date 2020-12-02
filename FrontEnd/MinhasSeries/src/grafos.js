import React, {Component} from 'react'
import apis from './api'
import { Redirect } from 'react-router-dom'
import simple from './images/grafo_Gerado.png'


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

      async gerarGrafos(){
       
        const newGraph={
          series: this.state.series,
          statusList: this.state.statusSerie,
          genreList: this.state.genre,
          status: this.refs.status.value,
          genre: this.refs.genre.value,
          referencia: this.refs.referencia.value,
          tipo: this.refs.tipo.value
        }
        apis.generateGraph(newGraph).then(
          
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
        const btnStyle ={
       
          width:"115px",
          height: "55px",
          background: "#4E9CAF",
          padding: "10px",
          textAlign: "center",
          borderRadius: "5px",
          color: "white",
          fontWeight: "bold",
          lineHeight: "25px"
      }

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
                        <option key = "status" value="status">Status</option>
                </select>
                <br/> <br/>
                Tipo do grafo:&nbsp;<select ref='tipo'>
                        <option key = "Simple" value= "Simple">Simple</option>
                        <option key = "Fruchterman" value="Fruchterman">Fruchterman</option>
                        <option key = "Kamada" value="Kamada">Kamada</option>
                        <option key = "Random" value="Random">Random</option>
                        <option key = "Circular" value="Circular">Circular</option>
                </select>
                <br/> <br/>
                <br/> <br/>
                <a style= {btnStyle} onClick={this.gerarGrafos}>Gerar</a>
                <br/><br/><br/>
            </form>
            <img src={simple}ref="foto"/>

        </section> //depois botar imagem e description
    )
}


}



export default Grafos