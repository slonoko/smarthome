import React, { Component } from "react";
import "./infodetails.component.scss";
import Chart from "chart.js";
import Card from "react-bootstrap/Card";

export default class InfoDetails extends Component {
  prepareChart() {
    let myChart = new Chart("detailsChart", {
      type: this.props.chartType===undefined? "line":this.props.chartType,
      data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [
          {
            label: "Temperature",
            data: [12, 19, 3, 5, 2, 3],
            fill: false,
            borderColor: "rgba(255, 99, 132, 1)",
            backgroundColor: "rgba(255, 99, 132, 1)"
          },
          {
            label: "Humidity",
            data: [6, 2, 7, 15, 5, 24],
            fill: false,
            borderColor: "blue",
            backgroundColor: "blue"
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        aspectRatio: 0.7
      }
    });
    return myChart;
  }

  componentDidMount() {
    this.prepareChart();
  }

  render() {
    return (
      <Card >
        <Card.Header as="h6">{this.props.title}</Card.Header>
        <Card.Body>
          <canvas id="detailsChart"></canvas>
        </Card.Body>
      </Card>
    );
  }
}
// { this.props.children }
