import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './infocard.component.scss';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Link } from "react-router-dom";

export default class InfoCard extends Component {
  //process.env.REACT_APP_API_HOSTNAME
  // read more here: https://create-react-app.dev/docs/adding-custom-environment-variables/
  render() {
    return (
      <Card bg={this.props.color} text="white">
        <Card.Body>
        <Link className="white" to={this.props.path}>
            <Container>
              <Row>
                <Col><FontAwesomeIcon icon={this.props.icon} size="4x" /></Col>
                <Col md="auto">
                    {this.props.children}
                </Col>
              </Row>
            </Container>
            </Link>
        </Card.Body>
      </Card>
    );
  }
}        