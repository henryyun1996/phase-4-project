import React from "react"
import { GiBrainTentacle } from 'react-icons/gi';
import $ from 'jquery';
import { useState, useEffect } from "react"
import transition from "semantic-ui-transition";

function Header({ username }) {

    useEffect(() => {
        $.fn.transition = transition
        $('#text').transition('fade right');
        $('#text').transition('fade right');

    },[])
    


    return (
        <div>
            <div id="header">
            <div id="banner"><h3 id="text"> Dobrodošli, {username} </h3></div>
                <h1>{<GiBrainTentacle />}<br /><p>učiti</p></h1>

            </div>
        </div>
    )
}

export default Header;