import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import { StartingPage } from './pages/StartingPage';
import { WritingPage } from './pages/WritingPage';
import { TaskPage } from './pages/TaskPage';
import { ResultPage } from './pages/ResultPage';
import './App.css';


class App extends React.Component {
  

  render() {
    return (
      <div className="App">
        <Router>
          <Switch>
            <Route exact path="/"> <StartingPage/> </Route>
            <Route path="/version:version"> <WritingPage/> </Route>
            <Route exact path="/task:tid"> <TaskPage/> </Route>
            <Route path="/task:tid/writing"> <WritingPage/> </Route>
            <Route path="/task:tid/result"> <ResultPage/> </Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
