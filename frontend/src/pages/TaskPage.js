import { TaskDisplay } from "../js_components/TaskDisplay";
import React, {useState, useEffect} from "react";
import { useParams } from "react-router";
import { Link } from "react-router-dom";

export function TaskPage(props) {
    const { tid } = useParams()
    const [task, setTask] = useState([])

    useEffect(() => {
        fetch(`/api/task/${tid}`)
        .then(response => response.json())
        .then(data => setTask(data))
    }, [tid])

    return(
        <>
        <TaskDisplay task={task.desc}/>
        <div>
            <h3> Method </h3>
            {task.method}
        </div>
        <div>
            <Link to={'/task'+tid+'/writing'}> Start </Link>
        </div>
        </>
    )
}