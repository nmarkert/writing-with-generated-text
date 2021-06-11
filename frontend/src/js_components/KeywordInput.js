export function KeywordInput(props) {

    const handleSubmit = (event) => {
        event.preventDefault();
        let keyword = document.getElementById('input').value
        props.generate(keyword)
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