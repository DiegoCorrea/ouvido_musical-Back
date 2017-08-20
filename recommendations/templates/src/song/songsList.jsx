import React from 'react'

export default props => {
  const renderRow = () => {
    const list = props.data || []
    return list.map(songs => (
      <tr key={songs.song_id}>
        <td>{songs.title}</td>
        <td>{songs.artist}</td>
      </tr>
    ))
  }
  return (
    <table className='table'>
      <thead>
        <tr>
          <th>Musica</th>
          <th>Artista</th>
        </tr>
      </thead>
      <tbody>
        {renderRow()}
      </tbody>
    </table>
  )
}
