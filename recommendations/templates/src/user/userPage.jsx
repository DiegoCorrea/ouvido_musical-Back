import React, { Component } from 'react'
import axios from 'axios'

import PageHeader from '../template/pageHeader'
import UserInformation from './userInformation'
import RecommendationsList from '../recommendation/recommendationList'

const URL = 'http://127.0.0.1:8000/api/v1/users/'

export default class UserPage extends Component {
  constructor(props){
    super(props)
    this.state = { data: {}, recommendations: []}
    

    this.getUserInformation()
    this.getUserRecommendations()
  }

  getUserInformation(){
    const resource = URL + "b80344d063b5ccb3212f76538f3d9e43d87dca9e"
    axios.get(`${resource}`)
    .then(resp => {this.setState({...this.state, data: resp.data})
    console.log("[User Page - Get User Information]")
    console.log(this.state.data)})
  }
  getUserRecommendations(){
    const resource = URL + "b80344d063b5ccb3212f76538f3d9e43d87dca9e" + "/recommendations/"
    axios.get(`${resource}`)
    .then(resp => {this.setState({...this.state, recommendations: resp.data})
    console.log("[User Page - Get Recommendations]")
    console.log(this.state.recommendations)})
  }
  render() {
    return (
      <div>
        <UserInformation
        data={this.state.data}/>
        <RecommendationsList
        recList={this.state.recommendations}/>
      </div>
    )
  }
}
