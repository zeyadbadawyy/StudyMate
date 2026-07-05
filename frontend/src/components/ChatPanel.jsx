import {
  useEffect,
  useRef,
  useState
} from "react";
import api from "../services/api";


function ChatPanel() {
  const [question, setQuestion] =
    useState("");

  const [messages, setMessages] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const messagesEndRef =
    useRef(null);

  const [documentLoaded, setDocumentLoaded] =
    useState(false);

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

    messagesEndRef.current
      ?.scrollIntoView({
        behavior: "smooth"
      });

  }, [messages]);

  useEffect(() => {

    const reset =
      async () => {

        setMessages([]);

        setQuestion("");

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

  const sendMessage =
    async () => {

      if (
        !question.trim() ||
        loading
      ) {
        return;
      }

      const currentQuestion =
        question;

      setQuestion("");

      const userMessage = {
        role: "user",
        content:
          currentQuestion,
      };

      setMessages(
        (prev) => [
          ...prev,
          userMessage,
        ]
      );

      try {
        setLoading(true);

        const response =
          await api.post(
            "/chat",
            {
              question:
                currentQuestion,
            }
          );

        const aiMessage = {
          role: "assistant",
          content:
            response.data.answer,
        };

        setMessages(
          (prev) => [
            ...prev,
            aiMessage,
          ]
        );
        
      } catch (error) {
        console.error(error);

        alert(
          "Chat failed"
        );

      } finally {
        setLoading(false);
      }
    };

  return (
    <div>
      <h2>💬 Chat With Document</h2>

      <div className="chat-container">
        {messages.map(
          (
            message,
            index
          ) => (
            <div
              key={index}
              className={
                message.role === "user"
                  ? "user-message"
                  : "ai-message"
              }
            >
              <strong>
                {message.role ===
                "user"
                  ? "You"
                  : "StudyMate"}
                :
              </strong>

              <p>
                {
                  message.content
                }
              </p>
            </div>
          )
        )}

        <div ref={messagesEndRef} />
      </div>

      <input
        type="text"
        value={question}
        placeholder="Ask about your document..."
        maxLength={500}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        onKeyDown={(e) => {
          if (
            e.key ===
              "Enter" &&
            !loading &&
            documentLoaded
          ) {
            sendMessage();
          }
        }}
      />
      <p className="char-count">
        {
          question.length
        } / 500
      </p>

      <button
        onClick={
          sendMessage
        }
        disabled={
          loading
          || !documentLoaded
        }
      >
        Send
      </button>

      {loading && (
        <div
          className="thinking"
        >
          Thinking...
        </div>
      )}
    </div>
  );
}

export default ChatPanel;