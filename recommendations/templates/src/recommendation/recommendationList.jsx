import React from 'react'
import IconButton from '../template/iconButton'
import './recommendation.css'

export default props => {
  const renderRow = () => {
    const list = props.data || []
    return list.map(obj => (
      <div key={obj.song_id} className="col m4">
        <div className="card">
          <div className="card-image">
            <img src="http://www.ilikewallpaper.net/ipad-wallpapers/download/2268/Square-Pattern-ipad-wallpaper-ilikewallpaper_com.jpg"/>
            <span className="card-title cardTitleRec" >{obj.title}</span>
          </div>
          <div className="card-content">
            <p>{obj.artist}</p>
            <p>{obj.album} - {obj.year}</p>
          </div>
          <div className="card-action">
            <a href="#songs" className="left">Ir para Música</a>
            <a href="#" className="right">Wiki</a>
          </div>
        </div>
      </div>
    ))
  }
  return (
    <div className="row">
      {renderRow()}
    </div>
  )
}