import React from 'react';
import '../App.css';

class TextField extends React.Component{

  constructor(props) {
    super(props)
    this.state = {
      intervalId: -1,
    }
  }

  handleTyping(event) {
    event.preventDefault()
    this.props.stop()
    this.props.handle_typing(event.target.value)

    if(this.state.intervalId !== -1) {
      clearInterval(this.state.intervalId)
    }
    this.setState({intervalId: setInterval(this.apply_changes.bind(this), 3000)})
  }

  handleSubmit(event) {
    event.preventDefault()
    apply_changes()
  }

  apply_changes() {
    if(this.state.intervalId !== -1) {
      clearInterval(this.state.intervalId)
      this.setState({intervalId: -1})
    }
    let sentence = document.getElementById('field').value
    this.props.on_submit(sentence)
  }

  componentWillUnmount() {
    clearInterval(this.state.intervalId)
  }

  
  render() {
    let s = '';
    let i = 0;
    for (let w of this.props.sentence) {
      s += w
      if(i < this.props.sentence.length -1) {
        s += ' '
      }
      i = i+1;
    }

    return (
      <>
        <form onSubmit={this.handleSubmit.bind(this)}>
          <textarea id='field' type='text' className="TextField" value={s} onChange={this.handleTyping.bind(this)} disabled={this.props.disabled}></textarea>
        </form>
      </>
    );
  }
}

export default TextField;