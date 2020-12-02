import React, {Component} from 'react'

class Ola extends Component {

    render(){
        return <span id="cabs">Olá {this.props.name} </span>

    }

}
var clikd =true;
function ChangeName(){
    console.log("as");
    if(clikd){
        document.getElementById('cabs').innerHTML = "O react ta saindo";
        clikd=false;
    }else{
        document.getElementById('cabs').innerHTML = "Uhuu!";
        clikd=true;
    }
}


class Flw extends Component {

    render(){
        return (
            <div>

              <button id="btn" onClick={ChangeName}>Click</button>
           
            </div>
        );

    }

}



export{Flw,Ola}
