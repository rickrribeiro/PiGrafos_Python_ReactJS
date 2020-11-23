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
                
                isLoading:false,
                series:res.data
      
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
                Nome: &nbsp; <input type="text" ref='name' class-Name="form-control" /> 
                <br/> <br/>
                    Genero: &nbsp; <select ref='genre'>
                        {this.state.genre.map(element =><option key = {element} value={element}>{element}</option>)}
                </select>
                <br/> <br/>
                Status: &nbsp; 
                <select ref='status'>
                        {this.state.statusSerie.map(element =><option key = {element} value={element}>{element}</option>)}
                </select>
                <br/> <br/>
                Comentários: &nbsp; <input ref='comment' type="text" class-Name="form-control" />
                <br/> <br/>
                <button  onClick={this.saveSeries}>Salvar</button>
            </form>
        </section> //depois botar imagem e description
    )
}


}



export default Grafos