import React, {useState, useEffect} from 'react';
import { TextField } from './js_components/TextField'
import { KeywordInput } from './js_components/KeywordInput'
import { ControllButtons } from './js_components/ControllButtons'
import './App.css';


class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = { 
      seconds: -1,
      running: false,
      speed: 1000,
      sentence: [],
      isGenerating: false,
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

    fetch('/api/get_next', {
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

  generation_started(clearSentence) {
    this.stopClock()
    this.setState({
      seconds: -1,
      isGenerating: true,
    });
    if(clearSentence) {
      this.setState({
        sentence: [], 
      })
    }
  }

  generation_finished() {
    this.setState({
      isGenerating: false,
    });
    this.startClock()
  }

  new_generation(sentence) {
    this.generation_started(false)
    fetch('/api/generate_new', {
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
          sentence: sentence.split(" "),
          seconds : message.index - 1
        })
        this.generation_finished()
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
          <KeywordInput 
            g_started={this.generation_started} 
            g_finished={this.generation_finished} 
            disabled={this.state.isGenerating}
          />
        </div>
        <div>
          Generated Text: 
          <TextField 
            stop={this.stopClock}
            on_submit={this.new_generation} 
            sentence={this.state.sentence} 
            handle_typing={this.handle_typing}
            disabled={this.state.isGenerating}
           />
        </div>
        <div>
          <ControllButtons 
            startClock={this.startClock} 
            stopClock={this.stopClock}
            redoGeneration={this.redoGeneration}
            slowerGeneration={this.slowerGeneration}
            fasterGeneration={this.fasterGeneration}
            disabled={this.state.isGenerating}
          />
        </div>
      </div>
    );
  }
}

export default App;
