import React, { Component } from 'react';  
// import logo from './logo.svg';
import './App.css';
import BikeForm from './components/BikeForm';



class App extends Component {  
  render() {
    return (
      <div className="container">
        <BikeForm />
      </div>
    );
  }
}

export default App;