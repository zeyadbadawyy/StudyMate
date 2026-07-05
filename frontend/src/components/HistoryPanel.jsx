import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryPanel() {
  const [history, setHistory] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    fetchHistory();

  }, []);

  useEffect(() => {

    const refreshHistory =
      () => {

        fetchHistory();

      };

    window.addEventListener(
      "generationCreated",
      refreshHistory
    );

    window.addEventListener(
      "historyCleared",
      refreshHistory
    );

    return () => {

      window.removeEventListener(
        "generationCreated",
        refreshHistory
      );

      window.removeEventListener(
        "historyCleared",
        refreshHistory
      );

    };

  }, []);

  const fetchHistory =
    async () => {
      try {
        const response =
          await api.get(
            "/history"
          );

        setHistory(
          response.data
        );

      } catch (error) {
        console.error(error);

      } finally {
        setLoading(false);
      }
    };

    const downloadPdf =
  async (item) => {

    try {

      const response =
        await api.post(
          "/export/pdf",
          {
            content:
              item.content,

            filename:
              `${item.generation_type}_${item.id}.pdf`
          },
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
        `${item.generation_type}_${item.id}.pdf`;

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

  const clearHistory =
    async () => {

      const confirmed =
        window.confirm(
          "Delete all history?"
        );

      if (!confirmed)
        return;

      try {

        await api.delete(
          "/history/clear"
        );

        window.dispatchEvent(
          new Event(
            "historyCleared"
          )
        );

        setHistory([]);

      } catch (error) {

        console.error(error);

        alert(
          "Failed to delete history"
        );

      }

  };

  return (
    <div>
      <h2>
        📚 Generation History
      </h2>

      <button 
        className="history-delete"
        disabled={loading || history.length === 0}
        onClick={
          clearHistory
        }
      >
        Delete All History
      </button>

      {loading && (
        <p>
          Loading...
        </p>
      )}

      {!loading &&
        history.length ===
          0 && (
          <div className="empty-state">

            <h3>
              No generations yet
            </h3>

            <p>
              Generate summaries,
              quizzes, flashcards,
              or exams to see them here.
            </p>

          </div>
        )}

      {history.map(
        (item) => (
          <div
            key={item.id}
            className="history-card"
          >
            <h4>
              {
                item.generation_type
              }
            </h4>

            <p>
              <strong>
                File:
              </strong>{" "}
              {
                item.document_name
              }
            </p>

            <p>
              <strong>
                Date:
              </strong>{" "}
              {
                new Date(
                  item.created_at
                ).toLocaleString()
              }
            </p>

            <details>
              <summary>
                View Content
              </summary>

              <pre>
                {item.content}
              </pre>
            </details>

            <button
              onClick={() =>
                downloadPdf(item)
              }
            >
              Download PDF
            </button>
          </div>
        )
      )}
    </div>
  );
}

export default HistoryPanel;