import React, { Component } from "react";
import { render } from "react-dom";
import { Provider } from "react-redux";

import store from "../store";

import Header from "./layout/Header";
import Main from "./layout/Main";
import Footer from "./layout/Footer";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <Provider store={store}>
        <Header />
        <Main />
        <Footer />
      </Provider>
    );
  }
}

const container = document.getElementById("app");
render(<App />, container);

export default App;
