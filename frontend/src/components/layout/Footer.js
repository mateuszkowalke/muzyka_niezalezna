import React, { Component } from "react";
import { render } from "react-dom";

export default class Footer extends Component {
  render() {
    return (
      <footer>
        <div class="kpmz">
          <p>Opieka prawna:</p>
          <a href="http://www.kpmz.pl">
            <img
              class="kpmz--img"
              src="/static/frontend/img/logo_kpmz.png"
              alt="KPMZ logo"
            />
          </a>
        </div>
        <p class="centered">reszta stopki</p>
      </footer>
    );
  }
}
