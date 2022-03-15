import React from "react";
import './App.css';
class App extends React.Component {

	// Constructor
	constructor(props) {
		super(props);

		this.state = {
			items: [],
			DataisLoaded: false,
      value: "",
		};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
	}

	// ComponentDidMount is used to
	// execute the code
/*	componentDidMount() {
		fetch("http://localhost:5000")
			.then((res) => res.json())
			.then((json) => {
console.log(json);
				this.setState({
					items: json,
					DataisLoaded: true
				});
			})
	}*/

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    fetch(`http://localhost:5000?name=${this.state.value}`)
      .then(res => res.json())
      .then(json => {
        console.log(json);
        this.setState({
          data: json
        })
      })
    event.preventDefault();
  }

	render() {
		const { DataisLoaded, items } = this.state;
		if (!DataisLoaded)
      return (
        <div>
			    <h1> Pleses wait some time.... </h1>
        </div>
      );

		return (
      <div className = "App">
        <form onSubmit={this.handleSubmit}>
          <label>Enter your name:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
        <h1> Fetch data from an api in react </h1> {
          [items].map((item) => (
          <ol key = { item.id } >
            Username: { item.User },
            </ol>
          ))
        }
      </div>
	  );
  }
}

export default App;

