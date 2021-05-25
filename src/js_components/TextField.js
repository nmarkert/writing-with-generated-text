import React, {useState, useEffect} from 'react';
import { Word } from './Word'
import '../App.css';

var sentence = [];

export function TextField(props){

  function handleClick(index) {
    console.log('Word \'' + sentence[index] + '\' was clicked.');
  }

  if(props.time === -1) {
    sentence = []
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
      if(message.word === "\\eof") {
        console.log('Try to stop')
        props.stop();
      }
      else {
        sentence.push(message.word)
        console.log(sentence)
      }
    })
  },[props.time])
  
  var s = [];
  let i = 0;
  for (let w of sentence) {
    s.push(<Word value={w} key={i} index={i} onClick={handleClick}/>);
    i = i+1;
  }
  
  return (
    <div className="TextField">
       {s}
    </div>
  )
}