import React, { Component } from 'react'
import axios from 'axios'
import './css/likeButton.css'

const URL = 'http://127.0.0.1:8000/api/v1/users/'
export default class LikeButton extends Component {
  constructor(props) {
    super(props);
    this.state = {
      liked: false
    };
    this.handleClick = this.handleClick.bind(this);

  } 
  
  handleClick() {
    this.setState({
      liked: !this.state.liked
    });
    const resource = URL + this.props.uuid + '/recommendations/' + this.props.song_id + '/like/'
    axios.post(`${resource}`, { iLike: this.state.liked})
    console.log("Resource")
    console.log(resource)
  }
  
  render() {
    const text = this.state.liked ? 'Gostar' : 'haven\'t liked';
    const label = this.state.liked ? 'Não gostar' : 'Gostar'
    return (
      <div  className="likeButton">
        <div className="customContainer">
          <button className="btn btn-primary" onClick={this.handleClick}>
          {label}</button>
        </div>
      </div>
    );
  }
}
