import React from 'react'
import { Router, Route, Redirect, hashHistory } from 'react-router'

import User from '../user/user'
import Songs from '../song/songs'
import SongPage from '../song/songPage'
import Recommendations from '../recommendation/recommendations'

export default props => (
    <Router history={hashHistory}>
        <Route path='/users' component={User} />
        <Route path='/songs' component={Songs} />
        <Route path='/song' component={SongPage}/> 
        <Route path='/recommendations' component={Recommendations} />
        <Redirect from='*' to='/recommendations' />
    </Router>
)
