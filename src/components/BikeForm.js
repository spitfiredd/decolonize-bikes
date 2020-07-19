import React, { Component } from 'react';


async function postData(endpoint = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(endpoint, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}


class BikeForm extends Component {
  constructor() {
    super();
    this.state = {
      name: '',
      color: '',
    };
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit = (e) => {
    const { name, color } = this.state;
    // let bikeData = this.state;
    let bikeData = {
      "name": name,
      "color": color,
    }

    postData('api/v1/bikes', bikeData)
      .then(data => {
        console.log(data)
      });

  }

  render() {
    const { name, color } = this.state;

    return (
      <div>
        <h3>Bike Intake Form</h3>
        
        <form onSubmit={this.onSubmit}>
          <label >Bike</label> <br />
          <input
            type="text"
            name="name"
            value={ name }
            onChange={ this.onChange }
          /> <br />
          <label >Color</label> <br />
          <input
            type="test"
            name="color"
            value={ color }
            onChange={ this.onChange }
          /> <br />
          <button type="submit">Submit</button>
        </form>
      
      </div>
    );
  }
}

export default BikeForm;