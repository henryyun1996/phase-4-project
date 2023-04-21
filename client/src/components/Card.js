import React, { useState, useEffect } from "react"
import $ from 'jquery';
import transition from "semantic-ui-transition";



function Card({ vocab, handleFavoriteClick, isFavorited }) {
    const [favorite, setFavorite] = useState(isFavorited)
    

    useEffect(() => {
        setFavorite(isFavorited)
    }, [isFavorited])

    
    const [isClicked, setIsClicked] = useState(false)

    $.fn.transition = transition

    const { croatian_word, id, english_word, module_content_id } = vocab;


    const togglefav = () => {

        setFavorite(!favorite)

        handleFavoriteClick(id, favorite);

    }

    function handleFlip(event) {
        let card = event.target.closest('.ui.card')
        console.log($(`#${card.id}`))
        let text = event.target.closest('.word')
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
                <div className="description" onClick={(event) => handleFlip(event)}>
                    {isClicked ? <h3 className="word">{croatian_word}</h3> : <h3 className="word">{english_word}</h3>}
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
