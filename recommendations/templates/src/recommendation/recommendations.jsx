import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import RecommendationsList from './recommendationList'

const URL = 'http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/recommendations/'

export default class Recommendations extends Component {
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
        <PageHeader name='Musicas Recomendadas' small='-'></PageHeader>
        <RecommendationsList
        data={this.state.data}/>
      </div>
    )
  }
}
