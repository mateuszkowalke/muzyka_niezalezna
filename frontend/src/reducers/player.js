import { GET_PLAYER } from "../actions/types";

const initialState = {
  songs: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_PLAYER:
      return {
        ...state,
        songs: action.payload,
      };
    default:
      return state;
  }
}
