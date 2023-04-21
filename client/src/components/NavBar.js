import React, { useState, useEffect } from 'react'
import transition from "semantic-ui-transition";
import $ from 'jquery';
import progress from 'semantic-ui-progress'


const NavBar = ({ path, progressPercentage, username, handleLogout }) => {

  useEffect(() => {
    $.fn.transition = transition
    $('#text').transition('fade right');
    $('#text').transition('fade right');

    $.fn.progress = progress
    $('#example1').progress();



  }, [])


  return (
    <div>
      <h5 className="item right floated" id="text"> Dobrodošli, {username} </h5>
      {path !== '/edit-profile' &&
      <div className="ui teal progress" data-percent={progressPercentage} id="example1">
        <div className="bar"></div>
      </div>}
      <div className="ui menu">
        <a className="item" href="/home">Home</a>
        <a className='item' href='/edit-profile'>Edit Your Profile</a>
        <a className='item right floated' href='/' onClick={handleLogout}> Log Out </a>
      </div>
    </div>
  )
}

export default NavBar