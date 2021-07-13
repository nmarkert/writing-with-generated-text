import React from "react";
import { Link } from "react-router-dom";

export function StartingPage(props) {

    const handleSubmit = (event) => {
        event.preventDefault()
        let uid = document.getElementById('uid_input').value
        fetch(`/api/user/${uid}`)
    }

    return(
        <>
        <div>
            <h2> Enter your UserId </h2>
            <form onSubmit={handleSubmit}>
                <label>UserId</label> <br/>
                <input type="text" id="uid_input"/> <br/>
                <input type="submit" value="Submit"></input>
            </form>
        </div>

        <h2> Choose your version </h2>
        <li> <Link to='/version0'> Standard input </Link> </li>
        <li> <Link to='/version1'> Version1 </Link> </li>
        <li> <Link to='/version2'> Version2 </Link> </li>

        <h2> Start with tasks </h2>
        <Link to='/task0'> Tasks </Link>
        </>
    )
}