import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import { StartingPage } from './pages/StartingPage';
import { WritingPage } from './pages/WritingPage';
import './App.css';


class App extends React.Component {
  

  render() {
    return (
      <div className="App">
        <Router>
          <Switch>
            <Route exact path="/"> <StartingPage/> </Route>
            <Route path="/version1"> <WritingPage version={1}/> </Route>
            <Route path="/version2"> <WritingPage version={2}/> </Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
