import React, { Component } from 'react'
import axios from 'axios'

import TopBar from '../template/topBar/topBar'
import PageHeader from '../template/pageHeader'
import SongsList from './songsList'

const URL = 'http://127.0.0.1:8000/api/v1/songs/'

export default class Songs extends Component {
  constructor(props){
    super(props)
    this.state = { data: []}

    this.refresh()
  }

  refresh(){
    axios.get(`${URL}`)
    .then(resp => {this.setState({...this.state, data: resp.data})
    console.log(resp.data)})
  }
  render() {
    return (
      <div>
        <TopBar />
        <div className='content'>
          <PageHeader name='Músicas' small=''></PageHeader>
          <SongsList
          data={this.state.data}/>
        </div>
      </div>
    )
  }
}
