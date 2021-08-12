import React from 'react';
import '../App.css';
import { WordCount } from '../pages/WritingPage';

class TextField extends React.Component{

  constructor(props) {
    super(props)
    this.state = {
      intervalId: -1,
      amountBack: 0,
    }
  }

  handleTyping(event) {
    event.preventDefault()
    this.props.stop()

    fetch('/api/task/log_input', {
      method: 'POST',
      body: JSON.stringify({
          'sentence': event.target.value
      }),
      headers: {
          "Content-type": "aplication/json; charset=UTF-8"
        }
    })

    // Count Backspaces
    if(this.to_string(this.props.sentence).length > event.target.value.length)
    {
      this.setState({
        amountBack: this.state.amountBack+1
      })
    }
    this.props.handle_typing(event.target.value)

    if(this.state.intervalId !== -1) {
      clearInterval(this.state.intervalId)
    }
    this.setState({intervalId: setInterval(this.apply_changes.bind(this), 3000)})
  }

  handleSubmit(event) {
    event.preventDefault()
    this.apply_changes()
  }

  apply_changes() {
    if(this.state.intervalId !== -1) {
      clearInterval(this.state.intervalId)
      this.setState({intervalId: -1})
    }
    let sentence = document.getElementById('field').value
    this.props.on_submit(sentence)
  }

  to_string(arr) {
    let s = '';
    for (let w of arr) {
      s += w + ' '
    }
    return s.slice(0, -1) // To remove the last whitespace
  }

  componentWillUnmount() {
    clearInterval(this.state.intervalId)

    fetch('/api/task/store_result', {
      method: 'POST',
      body: JSON.stringify({
          'result': this.to_string(this.props.sentence),
          'amount_back': this.state.amountBack
      }),
      headers: {
          "Content-type": "aplication/json; charset=UTF-8"
        }
    })
  }

  
  render() {
    return (
      <>
        <form onSubmit={this.handleSubmit.bind(this)}>
          <textarea id='field' type='text' className="TextField" 
                    value={this.to_string(this.props.sentence)} 
                    onChange={this.handleTyping.bind(this)} 
                    disabled={this.props.disabled}> 
          </textarea>
        </form>
      </>
    );
  }
}

export default TextField;