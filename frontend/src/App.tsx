import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './App.scss';
import InfoCard from './component/InfoCard';

class App extends React.Component {

  render() {
    return (
      <Container>
          <Row>
            <Col><InfoCard /></Col>
            <Col><InfoCard /></Col>
            <Col><InfoCard /></Col>
        </Row>
      </Container>
    );
  }
}

export default App;
