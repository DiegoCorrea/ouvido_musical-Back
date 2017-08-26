import React, { Component} from 'react'
import ReactDOM from 'react-dom';
import { Router, Route, Redirect, Link,hashHistory } from 'react-router'

import Users from '../user/users'
import UserPage from '../user/userPage'
import Songs from '../song/songs'
import SongPage from '../song/songPage'
import Recommendations from '../recommendation/recommendations'

export default props => (
    <Router history={hashHistory}>
        <Route path='/' component={Users} />
        <Route path='/users' component={Users} >
          <Route path='/users/:uuid' component={UserPage} />
        </Route>
        <Route path='/songs' component={Songs} >
          <Route path='/songs/:uuid' component={SongPage}/>
        </Route>
        <Route path='/recommendations' component={Recommendations} />
        <Redirect from='*' to='/recommendations' />
    </Router>
)
