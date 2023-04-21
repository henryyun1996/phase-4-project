import React, { useEffect, useState } from "react"
import Card from './Card'


function CardContainer({ vocabs, handleFavoriteClick, user }) {

    const vocabList = vocabs.map((vocab) => {
        
        const favorited_vocab = user?.favorites.filter(favorite => (favorite.vocab_id === vocab.id))
        
        let isFavorited = false

        if (favorited_vocab !== undefined && favorited_vocab.length > 0) {
            isFavorited = true;
        }


        return (
            <div key={vocab.id} className="column">
               <Card key={vocab.id} vocab={vocab} handleFavoriteClick={handleFavoriteClick} isFavorited={isFavorited} />
            </div>)

    })



    return (<div className="ui grid container">
            <div className="ui stackable three column grid">
                {vocabList}
            </div>
        </div>
    )

}

export default CardContainer;