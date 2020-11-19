import React, {Component} from 'react'
import './App.css'
import apis from './api'
import {
    BrowserRouter as Router,
    Route,
    Link
  } from 'react-router-dom'

import axios from 'axios'



class Home extends Component{
    constructor(props){
        super(props)
          this.state={
            count:0,
            series:[],
            genres:[],
            isLoading:false
          }
        
      }  

      componentDidMount(){
        this.setState.isLoading = true;
        setInterval(()=> this.setState({count: this.state.count+1}),1000)

        apis.loadGenres().then((res)=>{
         
          this.setState({
          
           genres:res.data
    
          })
        })

        apis.loadSeries().then((res)=>{
          console.log(res)
          this.setState({
            isLoading:false,
            series:res.data
    
          })
        })
      }
    
    renderSerieLink(serie){
       
    return(
      <span>
        &nbsp;
        <Link to={'/'+serie} >{serie}</Link>
        &nbsp;
        </span>
    
    )
    }

    renderGenreLink(genre){
       
        return(
          <span>
            &nbsp;
            <Link to={'/series/'+genre} >{genre}</Link>
            &nbsp;
            </span>
        
        )
        }

    render(){

            return(
                <div>
                <section id="intro" className="intro-section">
                <div className="container">
                  <div className="row">
                    <div className="col-lg-12">
                      <h1><img src="images/logo.png" /></h1>
                      <p>Nunca mais esqueça uma série que você assistiu ou que alguém lhe indicou.</p>
                    </div>
                  </div>
                </div>
              </section>
              <br/><br/><br/><br/>
              <section>
              {
                  this.state.isLoading &&
                    <span>Aguarde, carregando...</span>
        
              }{
                !this.state.isLoading &&
                // <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lista de séries: {this.state.series.map((element)=>this.renderSerieLink(element.name))}</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lista de generos: {this.state.genres.map((element)=>this.renderGenreLink(element))}</div>
              }
        
              </section>
              </div>
            )

    }


}

export default Home