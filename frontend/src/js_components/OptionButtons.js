export function OptionButtons(props) {

    var buttons = []
    for (let i=0; i<props.sentence_options.length; i++) {
        let opt = ''
        for (let w of props.sentence_options[i]) {
            opt += w + ' '
        }
        
        buttons.push(
        <div key={i}>
            <button onClick={() => props.on_choose(i)}>{opt}</button>
        </div>
        )
    }
    if (props.sentence_options.length > 0) {
        buttons.push(
            <div className='smallSpace'/>
        )
        buttons.push(
            <button onClick={props.generate_new}> New Options </button>
        )
    }

    return(
        <>
        {buttons}
        </>
    )
}