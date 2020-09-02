import React, { Component } from "react";
import { render } from "react-dom";

export default class Header extends Component {
  render() {
    return (
      <header>
        <a href="#">
          <img
            class="header header--img centered-vertically"
            src="/static/frontend/img/top_logo.png"
            alt="Logo Muzyka Niezależna"
          />
        </a>
        <nav class="header centered">
          <ul class="navbar">
            <li class="navbar">
              <a href="#">
                <img
                  class="navbar--img"
                  src="/static/frontend/img/icon_sluchaj.png"
                  alt="Słuchaj muzyki"
                />
              </a>
            </li>
            <li class="navbar">
              <a href="#">
                <img
                  class="navbar--img"
                  src="/static/frontend/img/icon_kupuj.png"
                  alt="Kupuj muzykę"
                />
              </a>
            </li>
            <li class="navbar">
              <a href="#">
                <img
                  class="navbar--img"
                  src="/static/frontend/img/icon_odtwarzaj.png"
                  alt="Odtwarzaj publicznie"
                />
              </a>
            </li>
          </ul>
        </nav>
        <div class="login">
          <h4 class="login--h4 centered">
            <a class="login--a" href="#">
              Zaloguj&nbsp;się
            </a>
          </h4>
          <p class="login--p">
            Nie masz konta?
            <br />
            <a class="login--a" href="#">
              Zarejestruj się
            </a>
          </p>
        </div>
      </header>
    );
  }
}
