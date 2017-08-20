import React, { Component} from 'react'
import ReactDOM from 'react-dom';
import { Router, Route, Redirect, Link,hashHistory } from 'react-router'
import FacebookLogin from 'react-facebook-login'

import Users from '../user/users'
import UserPage from '../user/userPage'
import Songs from '../song/songs'
import SongPage from '../song/songPage'
import Recommendations from '../recommendation/recommendations'

export default props => (
    <Router history={hashHistory}>
        <Route path='/' component={Base} />
        <Route path='/users' component={Users} />
        <Route path='/users/:uuid' component={UserPage} />
        <Route path='/songs' component={Songs} />
        <Route path='/song' component={SongPage}/>
        <Route path='/recommendations' component={Recommendations} />
        <Redirect from='*' to='/recommendations' />
    </Router>
)
const responseFacebook = (response) => {
  console.log(response);
};

class Base extends Component {
  render() {
    return (
      <div>
        <Link to="/dummy">Route to dummy page</Link>
        <FacebookLogin
          appId="1420911897974648"
          autoLoad
          callback={responseFacebook}
          icon="fa-facebook"
        />
      </div>
    );
  }
}

class Dummy extends Component {
  render() {
    return (
      <div>
        <Link to="/">Back</Link>
        <h1>
          This is just a dummy page to test the button<br />
          <a href="https://github.com/keppelen/react-facebook-login/pull/76#issuecomment-262098946">
            survives back and forth routing
          </a>
        </h1>
      </div>
    );
  }
}
