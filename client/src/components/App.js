import React from "react";
import { Switch, Route } from "react-router-dom";
import LogIn from './LogIn';
import Home from './Home';

function App() {
  return (
    <div className='App ui'>
      <Switch>
        <Route exact path='/'>
          <LogIn />
        </Route>
        <Route exact path='/home'>
          <Home />
        </Route>
      </Switch>
    </div>
  )
}

export default App;
