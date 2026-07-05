import api from "../services/api";
import { useState, useEffect } from "react";

function ExportPanel() {

  const [hasHistory, setHasHistory] =
    useState(false);
  
  useEffect(() => {

    checkHistory();

  }, []);

  const checkHistory =
    async () => {

      try {

        const response =
          await api.get(
            "/history"
          );

        setHasHistory(
          response.data.length > 0
        );

      } catch {

        setHasHistory(
          false
        );

      }

    };

  useEffect(() => {

    const refresh =
      () => {

        checkHistory();

      };

    window.addEventListener(
      "generationCreated",
      refresh
    );

    window.addEventListener(
      "historyCleared",
      refresh
    );

    return () => {

      window.removeEventListener(
        "generationCreated",
        refresh
      );

      window.removeEventListener(
        "historyCleared",
        refresh
      );

    };

  }, []);

  const exportPackage =
    async () => {

      try {

        const response =
          await api.post(
            "/package/download",
            {},
            {
              responseType:
                "blob"
            }
          );

        const url =
          window.URL.createObjectURL(
            new Blob([
              response.data
            ])
          );

        const link =
          document.createElement(
            "a"
          );

        link.href = url;

        link.download =
          "StudyPackage.zip";

        document.body.appendChild(
          link
        );

        link.click();

        link.remove();

      } catch (error) {

        console.error(error);

        alert(
          "Export failed"
        );

      }

    };

  return (

    <div>

      <h2>
        📦 Exports & Downloads
      </h2>

      <p>

        Download a complete study
        package containing the
        latest generated version
        of each study tool.

      </p>

      <p>

        Only the most recent
        Summary, Flashcards,
        Quiz, Exam, Study Guide,
        and Revision Notes
        will be included.

      </p>

      <button
        disabled={!hasHistory}
        onClick={
          exportPackage
        }
      >
        Export Study Package
      </button>

    </div>

  );

}

export default ExportPanel;