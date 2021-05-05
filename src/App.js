import React, {useState, useEffect} from 'react';
import './App.css';

var sentence = ' ';

function TextField(props){

  if(props.time === -1) {
    sentence = ' ';
  }

  useEffect(()=> {
    fetch('/api', {
      method: 'POST',
      body: JSON.stringify({
        'id': props.time
      }),
      headers: {
        "Content-type": "aplication/json; charset=UTF-8"
      }
    }).then(response => response.json())
    .then(message => {
      sentence = sentence + ' ' + message.word
      console.log(sentence)
    })
  },[props.time]);

  return (
    <div>
      <p> Generated Text: </p>
      <p> {sentence}</p>
    </div>
    
  )
}

class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = { 
      seconds: -1,
    };

    this.startClock = this.startClock.bind(this);
    this.stopClock = this.stopClock.bind(this);
    this.redoGeneration = this.redoGeneration.bind(this);
  }

  tick() {
    this.setState(state => ({
      seconds: state.seconds + 1,
    }));
  }

  startClock() {
    let intervalId = setInterval(() => this.tick(), 1000);
    this.setState({interval: intervalId});
  }

  stopClock() {
    clearInterval(this.state.interval);
  }

  redoGeneration() {
    this.stopClock()
    this.setState({seconds: -1});
    this.startClock()
  }

  componentWillUnmount() {
    clearInterval(this.state.interval);
  }

  render() {
    return (
      <div className="App">
        <h1> prototype </h1>
        <TextField time={this.state.seconds}/>

        <div>
          <button onClick={this.startClock}> Start </button>
          <button onClick={this.stopClock}> Stop </button>
          <button onClick={this.redoGeneration}> Redo </button>
        </div>
      </div>
    );
  }
}

export default App;
