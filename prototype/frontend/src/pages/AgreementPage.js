import { useState } from "react";
import { Agreement } from "../js_components/Agreement";

export function AgreementPage(props) {
    const [checked, setChecked] = useState(false)

    const handleChange = () => {
        setChecked(!checked)
    }

    // TODO: Change that link is clickable if checked is true
    let li
    if ( checked ) {
        li = <label> Yes </label>
    }
    else {
        li = <label> No </label>
    }

    return(
        <>
        <h1> Agreement </h1>
        <div className='scrollBox'>
            <Agreement />
        </div>
        <div className='smallSpace'/>
        <div>
            <input 
                type='checkbox' 
                checked={checked}
                onChange={handleChange}
            />
            <label>I have read and agreed to the "Statutory Disclosure Duty for the Collection of Data Act 13 GDPR" above</label>
        </div>
        {li}
        </>
    )
}