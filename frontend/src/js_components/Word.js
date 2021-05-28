export function Word(props) {
    const handleClick = (event) => {
        event.preventDefault();
        props.onClick(props.index);
    }
    
    return(
        <a onClick={handleClick}> {props.value} </a>
    )
}