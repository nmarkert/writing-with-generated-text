import React from 'react';
//import { Version1 } from './versions/Version1';
import { Version2 } from './versions/Version2';
import './App.css';


class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = { 
      seconds: -1,
      running: false,
      speed: 1000,
      sentence: [],
      full_sen: [],
      sen_options: [],
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
    this.generate_options = this.generate_options.bind(this);
    this.handle_typing = this.handle_typing.bind(this);
    this.option_choosed = this.option_choosed.bind(this);
  }

  tick() {
    this.setState({
      seconds: this.state.seconds + 1,
    });
    if(this.state.seconds >= this.state.full_sen.length) {
      this.stopClock()
      this.setState({
        seconds: this.state.full_sen.length-1
      })
    }
    else {
      this.state.sentence.push(this.state.full_sen[this.state.seconds]);
    }
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
    fetch('/api/generate', {
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
          full_sen: message.sentence,
          seconds : message.index - 1
        })
        this.generation_finished()
    })
  }

  generate_options(pre, new_gen=true) {
    if(new_gen) {
      this.setState({
        sentence: [],
        full_sen: pre.split(" "),
      })
      this.redoGeneration()
    }

    console.log(pre)

    fetch('/api/generate_options', {
      method: 'POST',
      body: JSON.stringify({
          'pre_sentence': pre
      }),
      headers: {
          "Content-type": "aplication/json; charset=UTF-8"
        }
    }).then(response => response.json())
    .then(message => {
        //console.log(message.sentences)
        this.setState({
          sen_options: message.sentences,
        })
    })
  }

  option_choosed(opt_idx) {
    console.log(opt_idx)
    let pre_l = this.state.full_sen.concat(this.state.sen_options[opt_idx])
    this.setState({
      full_sen: pre_l,
      sen_options: []
    })
    let pre_sen = ''
    let i = 0
    for (let w of pre_l) {
      pre_sen += w
      if(i < pre_l.length-1) {
        pre_sen += ' '
      }
      i++
    }
    this.startClock()
    this.generate_options(pre_sen, false)
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
        <Version2
          startClock={this.startClock} 
          stopClock={this.stopClock}
          redoGeneration={this.redoGeneration}
          slowerGeneration={this.slowerGeneration}
          fasterGeneration={this.fasterGeneration}
          disabled={this.state.isGenerating}
          generation_started={this.generation_started} 
          generation_finished={this.generation_finished}
          new_generation={this.new_generation}
          sentence={this.state.sentence} 
          handle_typing={this.handle_typing}
          generate_options={this.generate_options}
          sentence_options={this.state.sen_options}
          option_choosed={this.option_choosed}
        />
      </div>
    );
  }
}

export default App;
