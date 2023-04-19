import React from "react";
import { Switch, Route, redirect, useNavigate } from "react-router-dom";
import LogIn from './LogIn';
import Home from './Home';
import { useState, useEffect } from 'react';
import CardContainer from './CardContainer'
import Header from "./Header";



function App() {
  const vocabAPI = "/vocab"
  const [vocabs, setVocabs] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [favoritesOnly, setFavoritesOnly] = useState(false);
  const [signUpClicked, setSignUpClicked] = useState(false);
  
  //const navigate = useNavigate();

  useEffect(() => {
    fetch(vocabAPI)
      .then((resp) => resp.json())
      .then((vocabsArray) => {
        setVocabs(vocabsArray);
        console.log('vocabs', vocabs)


      })
  }, [favoritesOnly])
  



  return (
    <div className='App ui'>
      <Header />
      <Switch>
        <Route exact path='/'>
          <LogIn />
        </Route>
        <Route exact path='/home'>
        <CardContainer vocabs={vocabs} />
        </Route>
      </Switch>
    </div>
  )
}

export default App;
