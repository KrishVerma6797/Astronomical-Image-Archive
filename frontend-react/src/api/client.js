const BASE_URL = "http://127.0.0.1:8000";

export async function searchImages(params) {
  const query = new URLSearchParams(
    Object.entries(params).filter(([_, v]) => v)
  ).toString();
  const response = await fetch(`${BASE_URL}/search?${query}`);
  if (!response.ok) throw new Error("Search failed");
  return response.json();
}

export async function uploadImage(file) {
  const formData = new FormData();
  formData.append("file", file);
  const response = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });
  return response;
}

export function getThumbnailUrl(imageId) {
  return `${BASE_URL}/images/${imageId}/thumbnail`;
}

export function getFileUrl(imageId) {
  return `${BASE_URL}/images/${imageId}/file`;
}