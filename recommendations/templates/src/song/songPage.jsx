import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import SongInformation from './songInformation'

const URL = 'http://127.0.0.1:8000/recommendations/songs/SOAKIMP12A8C130995/'

export default class SongPage extends Component {
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
        <SongInformation
        data={this.state.data[0]}
        db={this.state.data[1]}/>
      </div>
    )
  }
}
