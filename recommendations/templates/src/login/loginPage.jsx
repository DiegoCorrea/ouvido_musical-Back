import React, { Component } from 'react'
import { Link } from 'react-router'

import './css/login.css'

export default class Login extends Component {
  render() {
    return (
      <div id="login">
        <div className="section"></div>
        <main>
          <center>
            <img className="responsive-img" src="https://s-media-cache-ak0.pinimg.com/originals/09/3a/2c/093a2ca8c22d2e4670a4573ea862fe25.gif" />
            <div className="section"></div>

            <h5 className="indigo-text">Por Favor, escolha uma forma de login</h5>
            <div className="section"></div>

            <div className="container">
              <div className="z-depth-1 grey lighten-4 row container-center">
                <form className="col s12" method="post">
                  <div className='row'>
                    <div className='col s12'></div>
                  </div>

                  <div className='row'>
                    <div className='input-field col s12'>
                      <input className='validate' type='email' name='email' id='email' />
                      <label htmlFor='email'>Digite o seu email</label>
                    </div>
                  </div>

                  <div className='row'>
                    <div className='input-field col s12'>
                      <input className='validate' type='password' name='password' id='password' />
                      <label htmlFor='password'>Senha</label>
                    </div>
                    <label className='label-float'>
                      <a className='pink-text' href='#!'><b>Esqueceu a senha?</b></a>
                    </label>
                  </div>

                  <br />
                  <center>
                    <div className='row'>
                      <Link to={"/users/"} type='submit' name='btn_login' className='col s12 btn btn-large waves-effect indigo'>Entrar</Link>
                    </div>
                  </center>
                </form>
              </div>
            </div>
            <a href="#!">Crie sua conta!</a>
          </center>

          <div className="section"></div>
          <div className="section"></div>
        </main>
      </div>
    )
  }
}
{
  //<button type='submit' name='btn_login' className='col s12 btn btn-large waves-effect indigo'>Entrar</button>
}