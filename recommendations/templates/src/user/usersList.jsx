import React from 'react'
import './css/usersList.css'

export default props => {
  const renderRow = () => {
    const list = props.data || []
    return list.map(obj => (
      <div key={obj.user_id} className="col m4">
        <div className="card">
          <div className="card-image">
            <img src="http://www.ilikewallpaper.net/ipad-wallpapers/download/2268/Square-Pattern-ipad-wallpaper-ilikewallpaper_com.jpg" className='circle'/>
            <a href={"#/users/"+obj.user_id}><span className="card-title cardTitleRec" >{obj.user_id}</span></a>
          </div>
          <div className="card-content">
            <p>Nome: {obj.user_id}</p>
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