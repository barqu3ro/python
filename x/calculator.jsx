import React from 'react';

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentInput: '',
      fullEquation: ''
    };
  }

  handleClick = (buttonValue) => {
    if (buttonValue === '=') {
      this.setState({
        currentInput: eval(this.state.fullEquation),
        fullEquation: ''
      });
    } else {
      this.setState({
        currentInput: '',
        fullEquation: this.state.fullEquation + buttonValue
      });
    }
  }

  render() {
    return (
      <div>
        <div>{this.state.currentInput}</div>
        <div>{this.state.fullEquation}</div>
        <div>
          {['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '='].map(buttonValue =>
            <button onClick={() => this.handleClick(buttonValue)}>{buttonValue}</button>
          )}
        </div>
      </div>
    );
  }
}

export default Calculator;