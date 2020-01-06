import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';
import './InfoCard.scss';

class InfoCard extends Component {
  render() {
    return (
      <Card bg="info" text="white" style={{ minWidth: '18rem' }}>
        <Card.Header>Header</Card.Header>
        <Card.Body>
          <Card.Title>Card Title</Card.Title>
          <Card.Text>
            Some quick example text to build on the card title and make up the bulk of
            the card's content.
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default InfoCard;
