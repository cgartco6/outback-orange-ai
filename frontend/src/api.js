const API_URL = import.meta.env.VITE_API_URL;

export async function createCarousel(data, token) {
  return fetch(`${API_URL}/carousel`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: token
    },
    body: JSON.stringify(data)
  });
}
