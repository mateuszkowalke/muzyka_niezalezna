import React, { Component } from "react";
import { render } from "react-dom";

export default class Index extends Component {
  render() {
    return (
      <>
        <img
          class="center-img main-img"
          src="/static/frontend/img/moby_main.png"
          alt="Moby Dick cover"
        />
        <div class="main-down">
          <h1 class="main-down--text centered-vertically">Co jest grane? </h1>
          <img
            class="main-down--img centered"
            src="/static/frontend/img/arrow_down.png"
            alt="down arrow"
          />
        </div>
        <h1 class="main-index--h1">Witaj w strefie niezależnej muzyki!</h1>
        <h4 class="main-index--h4">
          Jeśli szukasz świetnej muzyki skrojonej na Twoją miarę - dobrze
          trafiłeś. Dzięki tej platformie jesteś w stanie wypełnić swój lokal
          nastrojową melodią, znaleźć podkład muzyczny do Twojego filmiku, czy
          po prostu odkryć nowe utwory zespołów, o których nie miałeś pojęcia,
          że istnieją - wszystko w jednym miejscu.
        </h4>
        <div class="main-index--div">
          <a class="main-index--div--link" href="#">
            <img
              src="/static/frontend/img/icon_sluchaj.png"
              alt="Słuchaj muzyki"
            />
          </a>
          <h1>Czego masz ochotę posłuchać?</h1>
          <br />
          <h3>
            Muzyka niezależna pozwala Ci na stworzenie własnej playlisty z
            dostępnych utworów. Dopasuj ją do Twoich indywidualnych wymagań i
            preferencji.
          </h3>
        </div>
        <div class="main-index--div">
          <a class="main-index--div--link" href="#">
            <img src="/static/frontend/img/icon_kupuj.png" alt="Kupuj muzykę" />
          </a>
          <h3>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat.
          </h3>
        </div>
        <div class="main-index--div">
          <a class="main-index--div--link" href="#">
            <img
              src="/static/frontend/img/icon_odtwarzaj.png"
              alt="Odtwarzaj muzykę"
            />
          </a>
          <h3>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat.
          </h3>
        </div>
      </>
    );
  }
}
