import React from "react"
import { GiBrainTentacle } from 'react-icons/gi';
import $ from 'jquery';
import { useState, useEffect } from "react"
import transition from "semantic-ui-transition";

function Modules({ moduleContent, handleModuleClick }) {



    const moduleList = moduleContent.map((module, index) => {
        let route = `/cards/${module.lesson_level}`

        return (
            <div key={index} className="item" id="item-div">
                <div id="thumbnail" className="ui image"><p><iframe src={module.video_url} frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">Video</iframe></p></div>
                <div className="middle aligned content">
                    <div id="module_description" className="description">
                        <div id="module-number" className="ui header" onClick={() => handleModuleClick(module)}><a href={route} >Module {module.lesson_level} </a></div>
                        {module.content}
                    </div>
                </div>

            </div>)
    })

    return (
        <div id="module">
            <div className="ui unstackable items">
                {moduleList}
            </div>
        </div>
    )
}

export default Modules;