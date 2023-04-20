import React from "react";
import { Switch, Route, redirect, useNavigate } from "react-router-dom";
import LogIn from './LogIn';
import Home from './Home';
import { useState, useEffect } from 'react';
import CardContainer from './CardContainer'
import Header from "./Header";
import Signup from "./Signup";



function App() {
  const [vocabs, setVocabs] = useState([]);
  const [user, setUser] = useState();
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [signUpClicked, setSignUpClicked] = useState(false);
  const [userFavorites, setUserFavorites] = useState([]);
  const [username, setUsername] = useState('');


  //const navigate = useNavigate();

  useEffect(() => {
    fetch("/vocab")
      .then((resp) => resp.json())
      .then((vocabsArray) => {
        setVocabs(vocabsArray);
        //console.log('vocabs', vocabs)

      })
    fetch('/user/1')
      .then(resp => resp.json())
      .then(gail => {
        setUser(gail)
        setUsername(gail.username)
        setUserFavorites(gail.favorites)
      })

  }, [])

  function handleFavoriteClick(vocab_id, favorite) {
    if (!favorite) {
      const formData = {
        vocab_id: vocab_id,
        user_id: user.id
      };

      fetch(`/user/${user.id}/favorites`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })

      fetch(`/user/${user.id}`)
        .then((resp) => resp.json())
        .then((userObj) => {
          setUserFavorites(userObj.favorites)
        })

    } else {
      fetch(`/user/${user.id}`)
        .then(res => res.json())
        .then((userObj) => {

          if (userObj.favorites.length !== 0) {

            const favorite_to_delete = userObj.favorites.filter(favorite_i => favorite_i.vocab_id === vocab_id)[0]
            console.log('test', favorite_to_delete)

            if (favorite_to_delete !== null) {
              fetch(`/favorites/${favorite_to_delete.id}`, {
                method: "DELETE",
              });
            }

          }

        })

    }

  }


  return (
    <div className='App ui'>
      <Switch>
        <Route exact path='/'>
          <LogIn 
            setUser={setUser} 
          />
        </Route>
        <Route exact path='/signup'>
          <Signup 
            setUser={setUser} 
          />
        </Route>
        <Route exact path='/home'>
        <CardContainer vocabs={vocabs} />
        </Route>
      </Switch>
    </div>
  )
}

export default App;
