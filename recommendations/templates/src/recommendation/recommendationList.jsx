import React from 'react'
import { Link } from 'react-router'
import LikeButton from './likeButton'
import './css/recommendation.css'

export default props => {
  const recommendationCards = () => {
    console.log("[Recommendation List]")
    console.log(props.recList)
    const list = props.recList || []
    console.log(list)
    return list.map(obj => (
      <div key={`recommendation-${obj.song_id}`} className="col m3">
        <div className="card">
          <div className="card-image">
            <img src="http://www.ilikewallpaper.net/ipad-wallpapers/download/2268/Square-Pattern-ipad-wallpaper-ilikewallpaper_com.jpg"/>
            <Link to={"/songs/"+ obj.song_id}><span className="card-title cardTitleRec" >{obj.title}</span></Link>
          </div>
          <div className="card-content">
            <p>{obj.artist}</p>
            <p>{obj.album} - {obj.year}</p>
          </div>
          <LikeButton 
          uuid={obj.song_id}/>
        </div>
      </div>
    ))
  }
  return (
    <div className="row">
      {recommendationCards()}
    </div>
  )
}
