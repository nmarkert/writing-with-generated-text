export function KeywordInput(props) {

    const handleSubmit = (event) => {
        event.preventDefault();
        let keyword = document.getElementById('input').value
        props.g_started(true)
        
        fetch('/api/generate', {
            method: 'POST',
            body: JSON.stringify({
                'content': keyword
            }),
            headers: {
                "Content-type": "aplication/json; charset=UTF-8"
              }
          }).then(response => response.json())
          .then(message => {
              console.log(message.ready)
              props.g_finished()
          })
    }

    var lbl
    if(props.disabled) {
        lbl = 'Generating...'
    }
    else {
        lbl = '. . .'
    }

    return (
        <>
            <form onSubmit={handleSubmit}>
                <input type='text' id='input' disabled={props.disabled}></input>
                <input type='submit' value='Generate' disabled={props.disabled}></input>
            </form>
            <label id='status_lbl'> {lbl} </label>
        </>
    )
}