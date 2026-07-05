import { useEffect, useState } from "react";
import Dashboard from "./pages/Dashboard";

function App() {

  const [darkMode, setDarkMode] = useState(
    () => localStorage.getItem("theme") === "dark"
  );

  useEffect(() => {

    if (darkMode) {

      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");

    } else {

      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");

    }

  }, [darkMode]);

  return (
    <Dashboard
      darkMode={darkMode}
      setDarkMode={setDarkMode}
    />
  );

}

export default App;