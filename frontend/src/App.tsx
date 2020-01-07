import React, { Fragment } from 'react';
import CardGroup from 'react-bootstrap/CardGroup';
import './App.scss';
import InfoCard from './components/infocard/infocard.component';
import InfoDetails from './components/infodetails/infodetails.component';
import { Route, Switch } from "react-router-dom";

class App extends React.Component {

  render() {
    return (
      <Fragment>
        <CardGroup>
          <InfoCard color="success" icon="thermometer-half" path="/temperature">
            <div className="float-right">
              Temperature 25</div>
            <div className="float-right">
              Humidity 45</div>
          </InfoCard>
          <InfoCard color="info" icon="wind" path="/dust">
            <div className="float-right">
              Dust density 20</div>
            <div className="float-right">
              Normal</div>
          </InfoCard>
          <InfoCard color="warning" icon="bullhorn" path="/noise">

          </InfoCard>
        </CardGroup>
        <Switch>
          <Route path="/temperature" exact>
            <InfoDetails>temperature</InfoDetails>
          </Route>
          <Route path="/dust" exact>
            <InfoDetails>dust</InfoDetails>
          </Route>
          <Route path="/noise" exact>
            <InfoDetails>noise</InfoDetails>
          </Route>
        </Switch>

      </Fragment>
    );
  }
}

export default App;
