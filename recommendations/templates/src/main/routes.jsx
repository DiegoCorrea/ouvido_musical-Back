import React from 'react'
import { Router, Route, Redirect, hashHistory } from 'react-router'

import User from '../user/user'
import Song from '../song/song'
import Recommendation from '../recommendation/recommendation'

export default props => (
    <Router history={hashHistory}>
        <Route path='/users' component={User} />
        <Route path='/songs' component={Song} />
        <Route path='/recommendations' component={Recommendation} />
        <Redirect from='*' to='/recommendations' />
    </Router>
)
