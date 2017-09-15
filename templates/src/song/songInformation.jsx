import React from 'react'

export default props => {
  const renderRow = () => {
    const list = props.data || []
    const db = props.db || []
    return (
      <div key={list.song_id} className="col s12 m8 offset-m2 l6 offset-l3">
        <div className="card-panel grey lighten-5 z-depth-1">
          <div className="row">
            <div className="row valign-wrapper">
              <div className="col s2">
                <img src="images/yuna.jpg" alt="" className="circle responsive-img"/>
              </div>
              <div className="col s10">
                <span className="black-text">
                  <p><b>Musica:</b> {list.title}</p>
                  <p><b>Banda:</b> {list.artist}</p>
                  <p><b>Album:</b> {list.album} - {list.year}</p>
                  <p><b>Localidade:</b> {db.home}</p>
                </span>
              </div>
            </div>
          </div>
          <div className="row">
            <p><b>Sobre a Banda</b></p>
            <p className='justify'>{db.abstract}</p>
          </div>
          <div className="row">
            <div className="col s12 m6">
              <p><b>Generos</b></p>
              <p className='left'>{db.genres}</p>
            </div>
            <div className="col s12 m6">
              <p><b>Albuns</b></p>
              <p className='left'>{db.albuns}</p>
            </div>
          </div>
        </div>
      </div>
    )
  }
  return (
    <div className="songInfo">
      {renderRow()}
    </div>
  )
}
