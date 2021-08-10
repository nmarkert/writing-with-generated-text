import React, {useState, useEffect} from "react";

export function FinishPage() {
    
    const [link, setLink] = useState('')

    useEffect(() => {
        fetch('/api/survey_link')
        .then(response => response.json())
        .then(data => setLink(data.link))
    }, [])
    
    return(
        <>
        <h2> Finished Part 1 </h2>
        <p>
        You finished the first part of this study. Now please follow the link below 
        to take part at the final survey.
        </p>
        <a href={link}> Link </a>
        </>
    )
}