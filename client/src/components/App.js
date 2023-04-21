import React from "react";
import { Switch, Route, redirect, useNavigate, useHistory } from "react-router-dom";
import LogIn from './LogIn';
import Home from './Home';
import { useState, useEffect } from 'react';
import CardContainer from './CardContainer'
import Header from "./Header";
import Signup from "./Signup";
import Modules from "./Modules";
import NavBar from "./NavBar";
import EditProfile from "./EditProfile";
import { useLocation } from 'react-router-dom'



function App() {
  const [vocabs, setVocabs] = useState([]);
  const [user, setUser] = useState();
  const [modules, setModules] = useState([]);

  const history = useHistory();

  let location = useLocation();
  let path = location.pathname
  

  useEffect(() => {
    fetch("/vocab")
      .then((resp) => resp.json())
      .then((vocabsArray) => {
        setVocabs(vocabsArray);

      })
    fetch("/module")
      .then((resp) => resp.json())
      .then((moduleArray) => {
        setModules(moduleArray);

      })

  }, [])

  useEffect(() => {
    fetch("/check_session")
      .then((r) => {
        if (r.ok) {
          r.json().then((user) => setUser(user));
        }
      });
  }, []);




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
          setUser(userObj)
          console.log(userObj)
        })

    } else {
      fetch(`/user/${user.id}`)
        .then(res => res.json())
        .then((userObj) => {

          if (userObj.favorites.length !== 0) {

            const favorite_to_delete = userObj.favorites.filter(favorite_i => favorite_i.vocab_id === vocab_id)[0]
            console.log('test', favorite_to_delete)

            if (favorite_to_delete !== undefined) {
              fetch(`/favorites/${favorite_to_delete.id}`, {
                method: "DELETE",
              });
            }

          }

        })

    }

  }

  const handleLogout = () => {
    fetch("/logout", { method: "DELETE" })
      .then((r) => {
        if (r.ok) {
          setUser(undefined)
        }
        history.push('/home')
      })
  }

  function handleModuleClick(module) {
    let progress;
    if (module.lesson_level === 1) {
      progress = 33
    } else if (module.lesson_level === 2) {
      progress = 50
    } else if (module.lesson_level === 3) {
      progress = 100
    }

    console.log(typeof(progress))

    fetch(`/user/${user.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        current_module_id: module.id,
        progress_percentage: progress
      }),
    })
    .then(resp => resp.json())
    .then(userObj => {
      setUser(userObj)
    })

  }

  return (
    <div className='App ui'>
      <Header />
      {user !== undefined && path !== '/' && <NavBar  path={path} progressPercentage={user?.progress_percentage} username={user?.username} handleLogout={handleLogout} />}
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
          <Modules moduleContent={modules} handleModuleClick={handleModuleClick} />
        </Route>
        <Route exact path='/cards/1'>
          <CardContainer vocabs={vocabs.filter(vocab => (vocab.module_content_id === 1))} handleFavoriteClick={handleFavoriteClick} user={user} />
        </Route>
        <Route exact path='/cards/2'>
          <CardContainer vocabs={vocabs.filter(vocab => (vocab.module_content_id === 2))} handleFavoriteClick={handleFavoriteClick} user={user} />
        </Route>
        <Route exact path='/cards/3'>
          <CardContainer vocabs={vocabs.filter(vocab => (vocab.module_content_id === 3))} handleFavoriteClick={handleFavoriteClick} user={user} />
        </Route>

        <Route>
          <EditProfile user={user} setUser={setUser} />
        </Route>
      </Switch>
    </div>
  )
}

export default App;
