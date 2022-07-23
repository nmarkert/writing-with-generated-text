import '../App.css';

export function ControllButtons(props) {

    return(
        <>
          <button onClick={props.startClock}  disabled={props.disabled || props.running}  className='cButton'> Continue </button>
          <button onClick={props.stopClock}   disabled={props.disabled || !props.running} className='cButton'> Stop </button>
        </>
    )
}