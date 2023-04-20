import React, { useEffect, useState } from "react"
import Card from './Card'


function CardContainer({ vocabs, setCurrentUser }) {

    const vocabList = vocabs.map((vocab, index) => {

        return (
            <div class="column">
               <Card key={index} vocab={vocab} isFavorited={false} />
            </div>)

    })



    return (
        <div className="ui grid container">
            <div className="ui stackable three column grid">
                {vocabList}
            </div>
        </div>
    )

}

export default CardContainer;