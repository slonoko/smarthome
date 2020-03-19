import React, { Fragment } from 'react';
import CardDeck from 'react-bootstrap/CardDeck';
import './App.scss';
import InfoCard from './components/infocard/infocard.component';
import InfoDetails from './components/infodetails/infodetails.component';
import { Route, Switch } from "react-router-dom";
import Container from 'react-bootstrap/Container';

interface IState {
  temperature: any,
  dust: any
}

interface IProps {
}

class App extends React.Component<IProps, IState> {
  poller:any;
  hostname:string;

  constructor(props: IProps) {
    super(props);
    this.state = {
      temperature: {},
      dust: {}
    };
    this.hostname = `http://${window.location.hostname}/api/v1`; 
    this.pullData = this.pullData.bind(this);
  }

  componentDidMount() {
    this.poller = setInterval(this.pullData, 60000);
    this.pullData();
  }

  pullData() {
    fetch(this.hostname + '/temperature/')
      .then(res => res.json())
      .then((data) => {
        this.setState({ temperature: data });
      })
      .catch(err =>{
        clearTimeout(this.poller);
        console.error("Error occured, stopping timer!\n"+err.message);
      })
    fetch(this.hostname + '/dust/')
      .then(res => res.json())
      .then((data) => {
        this.setState({ dust: data });
      })
      .catch(err => {
        clearInterval(this.poller);
        console.error("Error occured, stopping timer!\n"+err.message);
      });
  }

  render() {
    return (
      <Fragment>
        <CardDeck className="no-margin">
          <InfoCard color="success" icon="thermometer-half" path="/temperature">
            <div className="float-right">
              <div className="float-left big-text">{(this.state.temperature.temperature === undefined) ? "-" : this.state.temperature.temperature}</div><div className="float-right small-text">°C</div>
            </div>
            <div>
              <div className="float-left big-text">{(this.state.temperature.humidity === undefined) ? "-" : this.state.temperature.humidity}</div><div className="float-right small-text">%</div>
            </div>
          </InfoCard>
          <InfoCard color="info" icon="wind" path="/dust">
            <div className="float-right">
              <div className="float-left big-text">{(this.state.dust.density === undefined) ? "-" : (Math.round(this.state.dust.density * 100) / 100)}</div><div className="float-right small-text">µg/m<sup>3</sup></div><br />
            </div>
          </InfoCard>
          <InfoCard color="warning" icon="bullhorn" path="/noise">

          </InfoCard>
        </CardDeck>
        <Container className="margin-fix" fluid>
        <Switch>
          <Route path="/temperature" exact>
            <InfoDetails title="Temperature / Humidity"></InfoDetails>
          </Route>
          <Route path="/dust" exact>
            <InfoDetails title="Dust"></InfoDetails>
          </Route>
          <Route path="/noise" exact>
            <InfoDetails chartType="scatter" title="Noise"></InfoDetails>
          </Route>
        </Switch>
        </Container>
      </Fragment>
    );
  }
}

export default App;
