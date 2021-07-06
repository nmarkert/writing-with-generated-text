import React from "react";
import { Link } from "react-router-dom";

export function StartingPage(props) {

    return(
        <>
        <h2> Choose your version </h2>
        <li> <Link to='/version0'> Standard input </Link> </li>
        <li> <Link to='/version1'> Version1 </Link> </li>
        <li> <Link to='/version2'> Version2 </Link> </li>
        </>
    )
}