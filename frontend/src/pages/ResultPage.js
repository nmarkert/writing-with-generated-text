import React, {useState, useEffect} from "react";
import { Link } from "react-router-dom";
import { useParams } from "react-router";

import { TaskDisplay } from "../js_components/TaskDisplay";

export function ResultPage() {

    const { tid } = useParams()
    const [task, setTask] = useState([])

    useEffect(() => {
        fetch(`/api/task/${tid}`)
        .then(response => response.json())
        .then(data => setTask(data))

        return () => {
            fetch(`/api/task/${tid}/store`)
        }
    }, [tid])

    const handle_change = (event) => {
        const rbs = document.getElementsByName('rating');
        let selectedValue = 0;
        for (const rb of rbs) {
            if (rb.checked) {
                selectedValue = rb.value;
                break;
            }
        }

        fetch(`/api/task/${tid}/rating`, {
            method: 'POST',
            body: JSON.stringify({
                'rating': parseInt(selectedValue)
            }),
            headers: {
                "Content-type": "aplication/json; charset=UTF-8"
              }
          })
    }

    let link
    if (!task.last) {
        link = <Link to={'/task'+(parseInt(tid)+1)}> Next </Link>
    }
    else {
        link = <Link to='/'> Home </Link>
    }

    return(
        <>
        <TaskDisplay task={task.desc}/>
        <div>
            <h3> Your Result: </h3>
            {task.result}
        </div>        
        <div>
            <h3> How satisfied are you with your text? </h3>
                <form onChange={handle_change}>
                    <input type="radio" name="rating" value={1} /> not at all
                    <input type="radio" name="rating" value={2} /> 
                    <input type="radio" name="rating" value={3} /> 
                    <input type="radio" name="rating" value={4} /> 
                    <input type="radio" name="rating" value={5} /> very
                </form>
        </div>
        <div>
            {link}
        </div> 
        </>
    )
}