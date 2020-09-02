import { combineReducers } from "redux";
import player from "./player";
import song from "./song";

export default combineReducers({
  player,
  song,
});
