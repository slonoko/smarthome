import React, { Component } from 'react';
import './infodetails.component.scss';

export default class InfoDetails extends Component {
  render() {
    return (
      <div className="infodetails">
        { this.props.children }
      </div>
    )
  }
}
