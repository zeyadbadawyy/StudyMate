import { useState } from "react";

import UploadPanel from "../components/UploadPanel";
import ToolsPanel from "../components/ToolsPanel";
import ChatPanel from "../components/ChatPanel";
import HistoryPanel from "../components/HistoryPanel";
import SettingsModal from "../components/SettingsModal";
import ExportPanel from "../components/ExportPanel";
import AnalyticsModal from "../components/AnalyticsModal";

function Dashboard({
  darkMode,
  setDarkMode
}) {

  const [
    showSettings,
    setShowSettings
  ] = useState(false);

  const [
    showAnalytics,
    setShowAnalytics
  ] = useState(false);

  return (

    <div className="dashboard">

      {showSettings && (

        <SettingsModal
          onClose={() =>
            setShowSettings(false)
          }
        />

      )}

      {showAnalytics && (

        <AnalyticsModal
          onClose={() =>
            setShowAnalytics(false)
          }
        />

      )}

      <div className="hero">

        <div className="hero-top">

          <div className="badge">
            ✨ AI Powered
          </div>

          <div className="hero-actions">

            <button
              className="settings-button"
              onClick={() =>
                setShowSettings(true)
              }
            >
              ⚙️
            </button>
            
            <button
              className="settings-button"
              onClick={() =>
                setShowAnalytics(true)
              }
            >
              📊
            </button>

            <button
              className="theme-toggle"
              onClick={() =>
                setDarkMode(
                  !darkMode
                )
              }
            >
              {darkMode
                ? "☀️"
                : "🌙"}
            </button>

          </div>

        </div>

        <img
          src="src/assets/logo.png"
          alt="StudyMate"
          className="hero-logo"
        />

        <p>
          Generate summaries, quizzes,
          flashcards, exams, and chat
          with your documents instantly.
        </p>

      </div>

      <div className="dashboard-grid">

        <div>

          <div className="section">
            <ToolsPanel />
          </div>

          <div className="section">
            <ChatPanel />
          </div>

        </div>

        <div>

          <div className="section">
            <UploadPanel />
          </div>
          
          <div className="section">
            <ExportPanel />
          </div>

          <div className="section">
            <HistoryPanel />
          </div>

        </div>

      </div>

    </div>

  );

}

export default Dashboard;