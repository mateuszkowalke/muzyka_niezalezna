import React, { Component } from "react";
import { render } from "react-dom";

export default class Footer extends Component {
  render() {
    return (
      <footer>
        <div className="kpmz">
          <p>Opieka prawna:</p>
          <a href="http://www.kpmz.pl">
            <img
              className="kpmz--img"
              src="/static/frontend/img/logo_kpmz.png"
              alt="KPMZ logo"
            />
          </a>
        </div>
        <p className="centered">reszta stopki</p>
      </footer>
    );
  }
}
