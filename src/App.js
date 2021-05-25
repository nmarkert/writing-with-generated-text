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
    };
    this.startClock = this.startClock.bind(this);
    this.stopClock = this.stopClock.bind(this);
    this.redoGeneration = this.redoGeneration.bind(this);
    this.fasterGeneration = this.fasterGeneration.bind(this);
    this.slowerGeneration = this.slowerGeneration.bind(this);
    this.generation_started = this.generation_started.bind(this);
    this.generation_finished = this.generation_finished.bind(this);
  }

  tick() {
    this.setState(state => ({
      seconds: state.seconds + 1,
    }));
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
    this.setState({seconds: -1});
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
  

  render() {
    return (
      <div className="App">
        <h1> prototype </h1>
        <div>
          <KeywordInput g_started={this.generation_started} g_finished={this.generation_finished}/>
        </div>
        <div>
          Generated Text:
          <TextField time={this.state.seconds} stop={this.stopClock}/>
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
