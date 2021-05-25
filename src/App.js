import React, {useState, useEffect} from 'react';
import { TextField } from './js_components/TextField'
import { KeywordInput } from './js_components/KeywordInput'
import './App.css';



class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = { 
      seconds: -1,
      running: false,
      speed: 1000,
      sentence: [],
    };
    this.startClock = this.startClock.bind(this);
    this.stopClock = this.stopClock.bind(this);
    this.redoGeneration = this.redoGeneration.bind(this);
    this.fasterGeneration = this.fasterGeneration.bind(this);
    this.slowerGeneration = this.slowerGeneration.bind(this);
    this.generation_started = this.generation_started.bind(this);
    this.generation_finished = this.generation_finished.bind(this);
    this.new_generation = this.new_generation.bind(this);
    this.handle_typing = this.handle_typing.bind(this);
  }

  tick() {
    this.setState(state => ({
      seconds: state.seconds + 1,
    }));

    fetch('/api', {
      method: 'POST',
      body: JSON.stringify({
        'id': this.state.seconds
      }),
      headers: {
        "Content-type": "aplication/json; charset=UTF-8"
      }
    }).then(response => response.json())
    .then(message => {
      if(message.word === "\\eof") {
        console.log('Try to stop')
        this.stopClock();
      }
      else {
        this.state.sentence.push(message.word)
        console.log(this.state.sentence)
      }
    })
  }

  startClock() {
    console.log('Starting')
    if(!this.state.running) {
      let intervalId = setInterval(() => this.tick(), this.state.speed);
      this.setState({
        interval: intervalId,
        running: true,
      });
    }
  }

  stopClock() {
    if(this.state.running) {
      clearInterval(this.state.interval);
      this.setState({running: false})
    }
  }

  redoGeneration() {
    //this.stopClock()
    this.setState({
      seconds: -1,
      sentence: [],
    });
    if(!this.state.running) {
      this.startClock()
    }
  }

  componentWillUnmount() {
    clearInterval(this.state.interval);
  }

  fasterGeneration() {
    if(this.state.running) {
      clearInterval(this.state.interval);
      this.setState({speed: this.state.speed / 4})
      let intervalId = setInterval(() => this.tick(), this.state.speed);
      this.setState({
        interval: intervalId,
      })
    }
  }

  slowerGeneration() {
    if(this.state.running) {
      clearInterval(this.state.interval);
      this.setState({speed: this.state.speed * 4})
      let intervalId = setInterval(() => this.tick(), this.state.speed);
      this.setState({
        interval: intervalId,
      })
    }
  }

  generation_started() {
    this.stopClock()
    this.setState({seconds: -1});
    for(let btn of document.getElementsByTagName('button')) {
      btn.disabled = true
    }
  }

  generation_finished() {
    for(let btn of document.getElementsByTagName('button')) {
      btn.disabled = false
    }
    this.startClock()
  }

  new_generation(sentence) {
    this.generation_started()
    fetch('/generate_new', {
      method: 'POST',
      body: JSON.stringify({
          'content': sentence
      }),
      headers: {
          "Content-type": "aplication/json; charset=UTF-8"
        }
    }).then(response => response.json())
    .then(message => {
        console.log(message.index)
        this.setState({
          seconds : message.index - 1
        })
        this.generation_finished()
        this.startClock()
    })

  }

  handle_typing(s) {
    let new_sentence = s.split(" ")
    this.setState({
      sentence: new_sentence,
    })
  }
  

  render() {
    return (
      <div className="App">
        <h1> prototype </h1>
        <div>
          <KeywordInput g_started={this.generation_started} g_finished={this.generation_finished}/>
        </div>
        <div>
          Generated Text:
          <TextField stop={this.stopClock} on_submit={this.new_generation} sentence={this.state.sentence} handle_typing={this.handle_typing}/>
        </div>
        <div>
          <button onClick={this.startClock} > Start </button>
          <button onClick={this.stopClock}> Stop </button>
          <button onClick={this.redoGeneration}> Redo </button>
          <button onClick={this.slowerGeneration}> {'<<'} </button>
          <button onClick={this.fasterGeneration}> {'>>'} </button>
        </div>
      </div>
    );
  }
}

export default App;
