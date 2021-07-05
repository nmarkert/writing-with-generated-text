import React from 'react';
//import { Word } from './Word'
import '../App.css';

var intervalId = -1

export function TextField(props){
  /*
  function handleClick(index) {
    console.log('Word \'' + sentence[index] + '\' was clicked.');
  }
  */

  const handleTyping = (event) => {
    event.preventDefault()
    props.stop()
    props.handle_typing(event.target.value)

    if(intervalId !== -1) {
      clearInterval(intervalId)
    }
    intervalId = setInterval(apply_changes, 3000)
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    apply_changes()
  }

  const apply_changes = () => {
    if(intervalId !== -1) {
      clearInterval(intervalId)
      intervalId = -1
    }
    let sentence = document.getElementById('field').value
    props.on_submit(sentence)
  }

  var s = '';
  let i = 0;
  for (let w of props.sentence) {
    //s.push(<Word value={w} key={i} index={i} onClick={handleClick}/>);
    s += w
    if(i < props.sentence.length -1) {
      s += ' '
    }
    i = i+1;
  }
  //console.log(s)

  
  return (
    <>
      <form onSubmit={handleSubmit}>
        <textarea id='field' type='text' className="TextField" value={s} onChange={handleTyping} disabled={props.disabled}></textarea>
      </form>
    </>
  )
}