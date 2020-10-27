const addNode = async () => {
  const response = await fetch('http://127.0.0.1:5000/addNode', {
    method: 'POST',
    body: document.getElementById("nodeText").value, // string or object
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}

const addEdge = async () => {
  const response = await fetch('http://127.0.0.1:5000/addEdge', {
    method: 'POST',
    body: document.getElementById("edgeText1").value+"."+document.getElementById("edgeText2").value,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}


const getNodes = async () => {
  const response = await fetch('http://127.0.0.1:5000/getNodes', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': "GET, PUT, POST, DELETE, HEAD, OPTIONS"
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}







const clearGraph = async () => {
  const response = await fetch('http://127.0.0.1:5000/Clear');
  const myJson = await response.json(); //extract JSON from the http response
  console.log(myJson);
  // do something with myJson
}

