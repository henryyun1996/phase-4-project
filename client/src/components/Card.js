import React, { useState, useEffect } from "react"
import $ from 'jquery';
import transition from "semantic-ui-transition";



function Card({ vocab, isFavorited, handleFavoriteClick }) {
    const [favorite, setFavorite] = useState(isFavorited)
    const [isClicked, setIsClicked] = useState(false)

    $.fn.transition = transition

    const { croatian_word, id, english_word, module_content, module_content_id } = vocab;


    const togglefav = () => {
        setFavorite(!favorite)
    }

    function handleFlip(event) {
        let card = event.target.closest('.ui.card')
        console.log($(`#${card.id}`))
        let text = event.target.closest('h3')
        console.log(text)

        text.style.color = '#FFFFFF'

        $(`#${card.id}`).transition('horizontal flip')
        $(`#${card.id}`).transition('horizontal flip')


        //transition
        setTimeout(() => {
            text.style.color = '#000000'
        }, 1000)

        setIsClicked(!isClicked)

    }



    return (
        <div id={id} className="ui card">
            <div className="content">
                <div className="description"  onClick={(event) => handleFlip(event)}>
                    {isClicked ? <h3>{croatian_word}</h3> : <h3>{english_word}</h3>}
                </div>
                <div className="extra content">
                    <span className="right floated heart icon" onClick={togglefav}>
                        <i id="heart" className={favorite ? "blue heart icon" : "heart icon"}></i>
                    </span>
                </div>
            </div>

        </div>
    )
}

export default Card;
