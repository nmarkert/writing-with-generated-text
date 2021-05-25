export function KeywordInput(props) {

    const handleSubmit = (event) => {
        event.preventDefault();
        let keyword = document.getElementById('input').value
        document.getElementById('status_lbl').textContent = 'Generating...'
        document.getElementById('generate_btn').disabled = true
        props.g_started()
        
        fetch('/generate', {
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
              document.getElementById('status_lbl').textContent = 'Finished Generation!'
              document.getElementById('generate_btn').disabled = false
              props.g_finished()

          })
    }

    return (
        <>
            <form onSubmit={handleSubmit}>
                <input type='text' required id='input'></input>
                <input type='submit' value='Generate' id='generate_btn'></input>
            </form>
            <label id='status_lbl'></label>
        </>
    )
}