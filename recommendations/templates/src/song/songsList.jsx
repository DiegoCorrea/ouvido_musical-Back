import React from 'react'
import { Link } from 'react-router'

import './css/songsList.css'

export default props => {
  const renderRow = () => {
    const list = props.data || []
    return list.map(obj => (
      <div key={obj.song_id} className="col m4">
        <div className="card">
          <div className="card-image">
            <img src="http://www.ilikewallpaper.net/ipad-wallpapers/download/2268/Square-Pattern-ipad-wallpaper-ilikewallpaper_com.jpg" className='circle'/>
            <a href={"#/songs/"+ obj.song_id}><span className="card-title cardTitleRec" >song</span></a>
          </div>
          <div className="card-content">
            <Link to={"/songs/"+ obj.song_id} uuid={{uuid: obj.song_id}}><p>Nome: {obj.song_id}</p></Link>
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