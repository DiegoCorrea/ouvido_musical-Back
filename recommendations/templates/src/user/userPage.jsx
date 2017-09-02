import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import TopBar from '../template/topBar/topBar'

import UserInformation from './userInformation'
import RecommendationsList from '../recommendation/recommendationList'

const URL = 'http://127.0.0.1:8000/api/v1/users/'

export default class UserPage extends Component {
  constructor(props){
    super(props)
    this.state = { data: {}, recommendations: []}
    console.log(this.props.params)

    this.getUserInformation()
    this.getUserRecommendations()
  }

  getUserInformation(){
    const resource = URL + this.props.params.uuid
    axios.get(`${resource}`)
    .then(resp => {this.setState({...this.state, data: resp.data})
    console.log("[User Page - Get User Information]")
    console.log(this.state.data)})
  }
  getUserRecommendations(){
    const resource = URL + this.props.params.uuid + "/recommendations/"
    axios.get(`${resource}`)
    .then(resp => {this.setState({...this.state, recommendations: resp.data})
    console.log("[User Page - Get Recommendations]")
    console.log(this.state.recommendations)})
  }
  render() {
    return (
      <div>
        <TopBar />
        <div className='content'>
          <UserInformation
          data={this.state.data}/>
          <RecommendationsList
          recList={this.state.recommendations}
          uuid={this.props.params.uuid}/>
        </div>
      </div>
    )
  }
}
