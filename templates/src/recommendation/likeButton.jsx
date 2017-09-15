import React, { Component } from 'react'
import axios from 'axios'
import './css/likeButton.css'

const URL = 'http://127.0.0.1:8000/api/v1/users/'
export default class LikeButton extends Component {
  constructor(props) {
    super(props);
    this.state = {
      liked: null
    };
    
    this.handleClick = this.handleClick.bind(this);
    this.getLikeMusic = this.getLikeMusic.bind(this);
    this.getLikeMusic()
  }

  getLikeMusic(){
    const resource = URL + this.props.uuid + '/recommendations/' + this.props.song_id + '/like/'
    axios.get(`${resource}`)
    .then(resp => {this.setState({...this.state, liked: resp.data.iLike})
    })
  }
  
  handleClick() {
    const resource = URL + this.props.uuid + '/recommendations/' + this.props.song_id + '/like/'
    axios.post(`${resource}`, { iLike: !this.state.liked})
    this.setState({
      liked: !this.state.liked
    });
    console.log("Alterando estado para "+ this.state.liked)
  }
  
  render() {
    const label = this.state.liked ? 'Gostei' : 'Não gostei'
    console.log("Liked: " + this.state.liked)

    return (
      <div className="likeButton center">
        <div className="customContainer">
          <button className="waves-effect waves-light btn" onClick={this.handleClick}>
          {label}</button>
        </div>
      </div>
    );
  }
}
