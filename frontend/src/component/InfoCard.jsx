import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';
import './InfoCard.scss';

class InfoCard extends Component {
  render() {
    return (
      <Card bg="success" text="white" style={{ minWidth: '18rem' }}>
        <Card.Body>
          <Card.Text>
            Some quick example text to build on the card title and make up the bulk of
            the card's content.
          </Card.Text>
        </Card.Body>
        <Card.Footer className="light">2 days ago</Card.Footer>
      </Card>
    );
  }
}

export default InfoCard;
