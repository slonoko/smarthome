import React, { Component } from 'react';

export default class InfoDetails extends Component {
  render() {
    return (
      <div className="infodetails">
        { this.props.children }
      </div>
    )
  }
}
