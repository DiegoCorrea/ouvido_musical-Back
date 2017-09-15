import React from 'react'
import Image from 'react-image-file';

export default props => {
  const renderRow = () => {
    console.log("[User Information]")
    console.log(props.data)

    const f = require('./imgs/user-default-img.jpg')
    const obj = props.data[0] || []
    return (
      <div key={obj.user_id} className="col s12 m8 offset-m2 l6 offset-l3">
        <div className="card-panel grey lighten-5 z-depth-1">
          <div className="row">
            <div className="row valign-wrapper">
              <div className="col s2">
                <Image file={f} alt='some text' className="circle responsive-img"/>
              </div>
              <div className="col s10">
                <span className="black-text">
                  <p><b>UUID:</b> {obj.user_id}</p>
                  <p><b>Nome:</b> "usuario rede social"</p>
                  <p><b>Idade:</b> "usuario rede social"</p>
                  <p><b>Localidade:</b> "usuario rede social"</p>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
  return (
    <div className="userInfo">
      {renderRow()}
    </div>
  )
}
