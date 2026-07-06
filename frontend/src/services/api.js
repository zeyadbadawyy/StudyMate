import axios from "axios";

const api = axios.create({
  baseURL: "https://studymate-production-2c5e.up.railway.app",
});

export default api;