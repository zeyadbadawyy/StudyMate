import { useState, useEffect } from "react";
import api from "../services/api";

function ToolsPanel() {
  const [tool, setTool] =
    useState("summary");

  const [difficulty, setDifficulty] =
    useState("medium");

  const [count, setCount] =
    useState(10);
  
  const [settings, setSettings] =
    useState(null);

  const [result, setResult] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [documentLoaded, setDocumentLoaded] =
    useState(false);

  useEffect(() => {

    const reset =
      async () => {

        setResult("");

        try {

          const response =
            await api.get(
              "/document/info"
            );

          setDocumentLoaded(
            response.data.loaded
          );

        } catch {

          setDocumentLoaded(
            false
          );

        }

      };

    window.addEventListener(
      "documentUploaded",
      reset
    );

    return () =>
      window.removeEventListener(
        "documentUploaded",
        reset
      );

  }, []);

  useEffect(() => {

    const checkDocument =
      async () => {

        try {

          const response =
            await api.get(
              "/document/info"
            );

          setDocumentLoaded(
            response.data.loaded
          );

        } catch {

          setDocumentLoaded(
            false
          );

        }

      };

    checkDocument();

  }, []);

  useEffect(() => {

    const loadSettings =
      async () => {

        try {

          const response =
            await api.get(
              "/settings"
            );

          const data =
            response.data;

          setSettings(data);

          setDifficulty(
            data.default_quiz_difficulty
          );

          setCount(
            data.default_quiz_count
          );

        } catch (error) {

          console.error(error);

        }

      };

    loadSettings();

  }, []);

  useEffect(() => {

    const refreshSettings =
      async () => {

        try {

          const response =
            await api.get(
              "/settings"
            );

          const data =
            response.data;

          setSettings(data);

          if (tool === "quiz") {

            setDifficulty(
              data.default_quiz_difficulty
            );

          }

          if (tool === "exam") {

            setDifficulty(
              data.default_exam_difficulty
            );

          }

          setCount(
            data.default_quiz_count
          );

        } catch (error) {

          console.error(error);

        }

      };

    window.addEventListener(
      "settingsUpdated",
      refreshSettings
    );

    return () => {

      window.removeEventListener(
        "settingsUpdated",
        refreshSettings
      );

    };

  }, [tool]);
  
  useEffect(() => {

    if (!settings)
      return;

    if (tool === "quiz") {

      setDifficulty(
        settings.default_quiz_difficulty
      );

    }

    if (tool === "exam") {

      setDifficulty(
        settings.default_exam_difficulty
      );

    }

  }, [tool, settings]);

  const generate = async () => {
    try {
      setLoading(true);

      let body = {};

      if (tool === "quiz") {
        body = {
          difficulty,
          count,
        };
      }

      else if (
        tool === "flashcards"
      ) {
        body = {
          count,
        };
      }

      else if (
        tool === "exam"
      ) {
        body = {
          difficulty,
        };
      }

      const response =
        await api.post(
          `/${tool}`,
          body
        );

      setResult(
        response.data.content
      );

      window.dispatchEvent(
        new Event(
          "generationCreated"
        )
      );

    } catch (error) {
      console.error(error);

      alert(
        "Generation failed"
      );

    } finally {
      setLoading(false);
    }
  };
  
  const downloadPdf =
  async () => {

    try {

      const response =
        await api.post(
          "/export/pdf",
          {
            content: result,
            filename:
              `${tool}.pdf`
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

      link.setAttribute(
        "download",
        `${tool}.pdf`
      );

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
      <h2>✨ AI Tools</h2>

      <div>
        <label>
          Choose tool:
        </label>

        <select
          value={tool}
          onChange={(e) =>
            setTool(
              e.target.value
            )
          }
        >
          <option value="summary">
            Summary
          </option>

          <option value="flashcards">
            Flashcards
          </option>

          <option value="study-guide">
            Study Guide
          </option>

          <option value="revision-notes">
            Revision Notes
          </option>

          <option value="quiz">
            Quiz
          </option>

          <option value="exam">
            Exam
          </option>
        </select>
      </div>

      {(tool === "quiz" ||
        tool === "exam") && (
        <div>
          <label>
            Difficulty:
          </label>

          <select
            value={difficulty}
            onChange={(e) =>
              setDifficulty(
                e.target.value
              )
            }
          >
            <option value="easy">
              Easy
            </option>

            <option value="medium">
              Medium
            </option>

            <option value="hard">
              Hard
            </option>
          </select>
        </div>
      )}

      {(tool === "quiz" ||
        tool === "flashcards") && (
        <div>
          <label>
            Count:
          </label>

          <input
            type="number"
            min="1"
            max="100"
            value={count}
            onChange={(e) =>
              setCount(
                Number(
                  e.target.value
                )
              )
            }
          />
        </div>
      )}

      <button
        disabled={loading || !documentLoaded}
        onClick={generate}
      >
        Generate
      </button>

      {loading && (
        <div
          className="loader"
        >
          Generating...
        </div>
      )}

      {result && (
        <div>
          <h3>Result</h3>

          <button
            onClick={downloadPdf}
          >
            Download PDF
          </button>

          <pre>
            {result}
          </pre>
        </div>
      )}
    </div>
  );
}

export default ToolsPanel;