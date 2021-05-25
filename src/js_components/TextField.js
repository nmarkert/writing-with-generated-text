import React, {useState, useEffect} from 'react';
import { Word } from './Word'
import '../App.css';

export function TextField(props){
  /*
  function handleClick(index) {
    console.log('Word \'' + sentence[index] + '\' was clicked.');
  }
  */

  const handleTyping = (event) => {
    props.stop()
    props.handle_typing(event.target.value)
  }

  const handleSubmit = (event) => {
    event.preventDefault();
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
        <textarea id='field' type='text' className="TextField" value={s} onChange={handleTyping}></textarea>
        <input type='submit' value='Apply'></input>
      </form>
    </>
  )
}