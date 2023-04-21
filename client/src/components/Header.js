import React from "react"
import { GiBrainTentacle } from 'react-icons/gi';

import { useState, useEffect } from "react"

function Header() {
 

    return (
        <div>
            <div id="header">
                <h1>{<GiBrainTentacle />}<br /><p>učiti</p></h1>

            </div>
        </div>
    )
}

export default Header;