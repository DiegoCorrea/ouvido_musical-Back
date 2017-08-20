import React from 'react'

export default props => {
  const renderRow = () => {
    const obj = props.data || []
    return (
      <div key={obj.user_id} className="col s12 m8 offset-m2 l6 offset-l3">
        <div className="card-panel grey lighten-5 z-depth-1">
          <div className="row">
            <div className="row valign-wrapper">
              <div className="col s2">
                <img src="images/yuna.jpg" alt="" className="circle responsive-img"/>
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
    <div className="songInfo">
      {renderRow()}
    </div>
  )
}
