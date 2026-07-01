import UploadPanel from "../components/UploadPanel";
import ToolsPanel from "../components/ToolsPanel";
import ChatPanel from "../components/ChatPanel";
import HistoryPanel from "../components/HistoryPanel";

function Dashboard() {
  return (
    <div className="dashboard">

      <div className="hero">
        <h1>📚 StudyMate</h1>

        <p>
          AI-powered study assistant for
          generating summaries, quizzes,
          flashcards, exams, and chatting
          with your documents.
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
            <HistoryPanel />
          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;