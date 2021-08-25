export function ControllButtons(props) {

    return(
        <>
          <button onClick={props.startClock}  disabled={props.disabled || props.running}  style={{ margin: 3 }}> Continue </button>
          <button onClick={props.stopClock}   disabled={props.disabled || !props.running} style={{ margin: 3 }}> Stop </button>
        </>
    )
    /*
      <button onClick={props.redoGeneration}    disabled={props.disabled}> Redo </button>
      <button onClick={props.slowerGeneration}  disabled={props.disabled}> {'<<'} </button>
      <button onClick={props.fasterGeneration}  disabled={props.disabled}> {'>>'} </button>
    */
}