import React, { Component } from 'react'
import './css/likeButton.css'

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
