import React, { Component } from 'react';

import './App.css'
import {Ola,Flw} from './Ola'
import axios from 'axios'
import Create from './create'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'
import Home from './home'

import { Series} from  './series'
import { EditSeries } from './edit'
class App extends Component {


 

  render() {
    return (
      <Router>
      <div>
      <nav className="navbar navbar-default navbar-fixed-top" role="navigation">
        <div className="container">
          <div className="navbar-header page-scroll">
            <Link className="navbar-brand page-scroll" to="/">
                <img src="/images/logo.png" height="30" />
            </Link>
          </div>
    
          <div className="collapse navbar-collapse navbar-ex1-collapse">
            <ul className="nav navbar-nav">
              <li>
                <Link to="/create">Create</Link>
              </li>
              <li>
              <Link to="/">Search</Link>
                </li>
            </ul>
          </div>
    
        </div>
      </nav>
    
    <Route exact path ='/' component={Home}/>
    <Route exact path ='/create' component={Create}/>
    <Route exact path ='/edit/:id' component={EditSeries}/>
    <Route exact path ='/series/:genre' component={Series}/>
    
    {/* <Home/> */}

    </div>
    </Router>
    );
  }
}

export default App;
