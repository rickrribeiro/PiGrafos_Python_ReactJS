import React, {Component} from 'react'
import apis from './api'
import { Redirect } from 'react-router-dom'



class Create extends Component{
    saveSeries(){
      const newSerie={
        name: this.refs.name.value,
        status: this.refs.status.value,
        genre: this.refs.genre.value,
        comment: this.refs.comment.value
      }
      apis.saveSerie(newSerie).then(

        this.setState({
          redirect: '/series/'+this.refs.genre.value
        })

      )
      console.log(newSerie)
    }
    
    constructor(props){
        super(props)
          this.state={
            count:0,
            statusSerie:[],
            genre:[],
            isLoading:false,
            redirect:false
          }
        this.saveSeries = this.saveSeries.bind(this)
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
                
                isLoading:false,
              statusSerie:res.data
      
            })
          })


          
      }
    


render(){

    return(

      
      <section className="intro-section">
      { this.state.redirect &&
        <Redirect to={this.state.redirect}/>
      
      }

            <h1>Cadastrar nova série</h1>
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



export default Create