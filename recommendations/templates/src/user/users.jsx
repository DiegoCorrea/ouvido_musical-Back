import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import UsersList from './usersList'

const URL = 'http://127.0.0.1:8000/recommendations/users/'

export default class Users extends Component {
  constructor(props){
    super(props)
    this.state = { data: []}

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
        <PageHeader name='Usuarios' small=''></PageHeader>
        <UsersList
        data={this.state.data}/>
      </div>
    )
  }
}
