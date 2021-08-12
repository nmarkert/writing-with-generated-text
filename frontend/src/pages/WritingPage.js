import React, {useState, useEffect} from "react";
import { Link } from "react-router-dom";
import { useParams } from "react-router";

import Version0 from "../versions/Version0";
import Version1 from '../versions/Version1';
import Version2 from '../versions/Version2';
import { TaskDisplay } from "../js_components/TaskDisplay";

export var WordCount = -1

export function WritingPage() {

    const { version, tid } = useParams()
    const [task, setTask] = useState([])
    const [textLength, setTLength] = useState(0)

    useEffect(() => {
        if(tid) {
            fetch(`/api/task/${tid}`)
            .then(response => response.json())
            .then(data => setTask(data))

            fetch(`/api/task/${tid}/start_timer`)

            return () => {
                fetch(`/api/task/${tid}/end_timer`)
            }
        }   
    }, [tid])

    const get_version = (vid) => {
        if(vid === 1) {
            return <Version1 set_length={setTLength}/>
        }
        else if (vid === 2) {
            return <Version2 set_length={setTLength}/>
        }
        else {
            return <Version0 set_length={setTLength}/>
        }
    }

    if(tid) {
    // The page is called by a task id, so there is a specific task to this page

        let li
        if (textLength < 10) {
            li = <label> Finish </label>
        }
        else {
            li = <Link to={'/task'+tid+'/result'}> Finish </Link>
        }

        return(
            <>
            <TaskDisplay task={task.desc} />
            <div>
                {get_version(task.method_id)}
            </div>
            <div>
                { li }
            </div>
            </>
        )
    }
    else {
    // The page is called by version, so this is free use with no specific task    

        return(
            <>
            <div>
                <Link to='/'> Back home </Link>
                <h1> prototype v{version} </h1>
            </div>
            <div>
                { get_version(parseInt(version)) }
            </div>
            </>
        )
    }
}