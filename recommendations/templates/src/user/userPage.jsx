import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import UserInformation from './userInformation'

const URL = 'http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e'

export default class UserPage extends Component {
  constructor(props){
    super(props)
    this.state = { data: {}}

    this.handleChange = this.handleChange.bind(this)

    this.refresh()
  }

  refresh(){
    axios.get(`${URL}`)
    .then(resp => {this.setState({...this.state, data: resp.data})
    console.log(resp.data)})
  }

  handleChange(e){
    this.setState({...this.state, description: e.target.value})
  }

  render() {
    return (
      <div>
        <UserInformation
        data={this.state.data}/>
      </div>
    )
  }
}
