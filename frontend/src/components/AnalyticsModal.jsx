import { useEffect, useState } from "react";
import api from "../services/api";

function AnalyticsModal({ onClose }) {

  const [analytics, setAnalytics] =
    useState(null);

  useEffect(() => {

    loadAnalytics();

  }, []);

  useEffect(() => {

    const handleEsc =
      (event) => {

        if (
          event.key === "Escape"
        ) {

          onClose();

        }

      };

    window.addEventListener(
      "keydown",
      handleEsc
    );

    return () => {

      window.removeEventListener(
        "keydown",
        handleEsc
      );

    };

  }, [onClose]);

  const loadAnalytics =
    async () => {

      try {

        const response =
          await api.get(
            "/analytics"
          );

        setAnalytics(
          response.data
        );

      } catch (error) {

        console.error(error);

      }

    };

  if (!analytics)
    return null;

  return (

    <div className="modal-overlay"
      onClick={onClose}>

      <div className="analytics-modal"
        onClick={(e) => e.stopPropagation()}>

        <h2>
          📊 Analytics
        </h2>

        <div className="analytics-grid">

          <div className="analytics-card">
            <h3>
              Documents Uploaded
            </h3>
            <p>
              {
                analytics.documents_uploaded
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Total Generations
            </h3>
            <p>
              {
                analytics.generations_created
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Summaries
            </h3>
            <p>
              {
                analytics.summary_count
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Flashcards
            </h3>
            <p>
              {
                analytics.flashcards_count
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Quizzes
            </h3>
            <p>
              {
                analytics.quiz_count
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Exams
            </h3>
            <p>
              {
                analytics.exam_count
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Study Guides
            </h3>
            <p>
              {
                analytics.study_guide_count
              }
            </p>
          </div>

          <div className="analytics-card">
            <h3>
              Revision Notes
            </h3>
            <p>
              {
                analytics.revision_notes_count
              }
            </p>
          </div>

        </div>

        <div className="analytics-footer">

          <p>
            <strong>
              Most Used Tool:
            </strong>{" "}
            {
              analytics.most_used_tool
            }
          </p>

          <p>
            <strong>
              Latest Activity:
            </strong>{" "}
            {
              analytics.latest_activity
            }
          </p>

        </div>

        <div className="modal-actions">

          <button
            className="save-btn"
            onClick={onClose}
          >
            Close
          </button>

        </div>

      </div>

    </div>

  );

}

export default AnalyticsModal;