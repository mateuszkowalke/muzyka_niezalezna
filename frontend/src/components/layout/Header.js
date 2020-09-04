import React, { Component } from "react";
import { render } from "react-dom";

export default class Header extends Component {
  render() {
    return (
      <header>
        <a href="#">
          <img
            className="header header--img centered-vertically"
            src="/static/frontend/img/top_logo.png"
            alt="Logo Muzyka Niezależna"
          />
        </a>
        <nav className="header centered">
          <ul className="navbar">
            <li className="navbar">
              <a href="#">
                <img
                  className="navbar--img"
                  src="/static/frontend/img/icon_sluchaj.png"
                  alt="Słuchaj muzyki"
                />
              </a>
            </li>
            <li className="navbar">
              <a href="#">
                <img
                  className="navbar--img"
                  src="/static/frontend/img/icon_kupuj.png"
                  alt="Kupuj muzykę"
                />
              </a>
            </li>
            <li className="navbar">
              <a href="#">
                <img
                  className="navbar--img"
                  src="/static/frontend/img/icon_odtwarzaj.png"
                  alt="Odtwarzaj publicznie"
                />
              </a>
            </li>
          </ul>
        </nav>
        <div className="login">
          <h4 className="login--h4 centered">
            <a className="login--a" href="#">
              Zaloguj&nbsp;się
            </a>
          </h4>
          <p className="login--p">
            Nie masz konta?
            <br />
            <a className="login--a" href="#">
              Zarejestruj się
            </a>
          </p>
        </div>
      </header>
    );
  }
}
