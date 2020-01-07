import React, { Fragment } from 'react';
import CardDeck from 'react-bootstrap/CardDeck';
import './App.scss';
import InfoCard from './components/infocard/infocard.component';
import InfoDetails from './components/infodetails/infodetails.component';
import { Route, Switch } from "react-router-dom";

interface IState {
  temperature: any,
  dust: any
}

interface IProps {
}

class App extends React.Component<IProps, IState> {

  constructor(props: IProps) {
    super(props);
    this.state = {
      temperature: {},
      dust: {}
    };
  }

  componentDidMount() {
    fetch(process.env.REACT_APP_API_HOSTNAME + '/temperature/')
      .then(res => res.json())
      .then((data) => {
        this.setState({ temperature: data })
      })
      .catch(console.error)
    fetch(process.env.REACT_APP_API_HOSTNAME + '/dust/')
      .then(res => res.json())
      .then((data) => {
        this.setState({ dust: data })
      })
      .catch(console.error)
  }

  render() {
    return (
      <Fragment>
        <CardDeck>
          <InfoCard color="success" icon="thermometer-half" path="/temperature">
            <div className="float-right">
              <div className="float-left big-text">{(this.state.temperature.temperature == undefined) ? "-" : this.state.temperature.temperature}</div><div className="float-right small-text">°C</div>
            </div>
            <div>
              <div className="float-left big-text">{(this.state.temperature.humidity == undefined) ? "-" : this.state.temperature.humidity}</div><div className="float-right small-text">g/m<sup>3</sup></div>
            </div>
          </InfoCard>
          <InfoCard color="info" icon="wind" path="/dust">
            <div className="float-right">
              <div className="float-left big-text">{(this.state.dust.density == undefined) ? "-" : (Math.round(this.state.dust.density * 100) / 100)}</div><div className="float-right small-text">µg/m<sup>3</sup></div><br />
            </div>
          </InfoCard>
          <InfoCard color="warning" icon="bullhorn" path="/noise">

          </InfoCard>
        </CardDeck>
        <Switch>
          <Route path="/temperature" exact>
            <InfoDetails>temperature</InfoDetails>
          </Route>
          <Route path="/dust" exact>
            <InfoDetails>dust</InfoDetails>
          </Route>
          <Route path="/noise" exact>
            <InfoDetails>{process.env.REACT_APP_API_HOSTNAME}</InfoDetails>
          </Route>
        </Switch>

      </Fragment>
    );
  }
}

export default App;
