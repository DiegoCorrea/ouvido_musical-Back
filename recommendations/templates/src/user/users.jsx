import React, { Component } from 'react'
import axios from 'axios'

import TopBar from '../template/topBar/topBar'
import PageHeader from '../template/pageHeader'
import UsersList from './usersList'

const URL = 'http://127.0.0.1:8000/api/v1/users/'

export default class Users extends Component {
  constructor(props){
    super(props)
    this.state = { data: []}

    this.getUsers()
  }

  getUsers(){
    axios.get(`${URL}`)
    .then(resp => {this.setState({...this.state, data: resp.data})
    console.log("[Users - Get Users]")
    console.log(resp.data)})
  }
  render() {
    return (
      <div>
        <TopBar />
        <div className="content">
          <PageHeader name='Usuários' small=''></PageHeader>
          <UsersList
          data={this.state.data}/>
        </div>
      </div>
    )
  }
}
