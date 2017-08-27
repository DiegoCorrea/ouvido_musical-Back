import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import SongsList from './songsList'

const URL = 'http://127.0.0.1:8000/recommendations/songs/'

export default class Songs extends Component {
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
        <TopBar />
        <PageHeader name='Músicas' small='Busque por uma música'></PageHeader>
        <SongsList
        data={this.state.data}/>
      </div>
    )
  }
}
