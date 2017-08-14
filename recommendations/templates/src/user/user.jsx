import React from 'react'
import PageHeader from '../template/pageHeader'

export default props => {

    const card = () => {
        return (
            <div className="col s12 m6 offset-m2 l6 offset-l3">
                <div className="card-panel grey lighten-5 z-depth-1">
                    <div className="row valign-wrapper">
                        <div className="col s2">
                            <img src="images/yuna.jpg" alt="" className="circle responsive-img"/>
                        </div>
                        <div className="col s10">
                            <span className="black-text">
                                This is a square image. Add the "circle" class to it to make it appear circular.
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    const renderCards = () => {
        numrows = 12
        const list = []
        for (var i = 0; i < numrows; i++) {
            list[i] = card()
        }
        
        return (list)
    }

    return (
        <div className="row">
            <PageHeader name='Usuarios' small='Lista de Alguns usuarios'></PageHeader>
            <div className="col s12 sm12 md12 lg 12">
                {renderCards()}
            </div>
        </div>
    )
}
