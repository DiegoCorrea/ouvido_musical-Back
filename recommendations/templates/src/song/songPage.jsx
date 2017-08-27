import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import TopBar from '../template/topBar/topBar'

import SongInformation from './songInformation'

const URL = 'http://127.0.0.1:8000/api/v1/songs/'

export default class SongPage extends Component {
  constructor(props){
    super(props)
    this.state = { data: {}}

    this.refresh()
  }

  refresh(){
    const resource = URL + 'SOAKIMP12A8C130995'
    axios.get(`${resource}`)
    .then(resp => {this.setState({...this.state, data: resp.data})
    console.log("[Song Page - Get Song Information]")
    console.log(this.state.data)})
  }

  render() {
    return (
      <div>
        <TopBar />
        <div className='content'>
          <SongInformation
          data={this.state.data[0]}
          db={this.state.data[1]}/>
        </div>
      </div>
    )
  }
}
