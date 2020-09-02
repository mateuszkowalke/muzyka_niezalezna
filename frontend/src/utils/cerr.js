export const cerr = (res) => {
  if (!res.ok) throw Error(res.statusText);
  return res.json();
};
