import React from "react";
import { Link } from "react-router-dom";

import Version1 from '../versions/Version1';
import Version2 from '../versions/Version2';
import Baseline from '../versions/Baseline';

export function WritingPage(props) {

    let v, vn
    if(props.version === 1) {
        v = <Version1/>
        vn = '1.1'
    }
    else if (props.version === 2) {
        v = <Version2/>
        vn = '2.1'
    }
    else {
        v = <Baseline/>
        vn = '0'
    }

    return(
        <>
        <div>
            <Link to="/"> Back home </Link>
            <h1> prototype v{vn} </h1>
        </div>
        <div>
            { v }
        </div>
        </>
    )
}