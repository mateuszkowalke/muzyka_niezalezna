import { GET_SONG } from "./types";
import cerr from "../utils/cerr";

export const getSong = () => (dispatch) => {
  fetch
    .get("/api/song_repo/")
    .then(cerr)
    .then((data) => {
      dispatch({
        type: "GET_SONG",
        payload: data,
      });
    })
    .catch((error) => console.log(error));
};
