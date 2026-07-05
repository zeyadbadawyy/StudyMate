import {
  useEffect,
  useState
} from "react";
import api from "../services/api";

function SettingsModal({ onClose }) {

  const [settings, setSettings] =
    useState(null);

  useEffect(() => {

    loadSettings();

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

  const loadSettings =
    async () => {

      try {

        const response =
          await api.get(
            "/settings"
          );

        setSettings(
          response.data
        );

      } catch (error) {

        console.error(error);

      }

    };

  const saveSettings =
    async () => {

      try {

        await api.put(
          "/settings",
          settings
        );

        window.dispatchEvent(
          new Event(
            "settingsUpdated"
          )
        );

        onClose();

      } catch (error) {

        console.error(error);

        alert(
          "Failed to save settings"
        );

      }

    };

  if (!settings)
    return null;

  return (

    <div className="modal-overlay"
      onClick={onClose}>

      <div className="settings-modal"
        onClick={(e) => e.stopPropagation()}>

        <h2>
          Settings
        </h2>

        <label>
          Quiz Difficulty
        </label>

        <select
          value={
            settings.default_quiz_difficulty
          }
          onChange={(e) =>
            setSettings({
              ...settings,
              default_quiz_difficulty:
                e.target.value
            })
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

        <label>
          Quiz Count
        </label>

        <select
          value={
            settings.default_quiz_count
          }
          onChange={(e) =>
            setSettings({
              ...settings,
              default_quiz_count:
                Number(
                  e.target.value
                )
            })
          }
        >
          <option value={5}>
            5
          </option>

          <option value={10}>
            10
          </option>

          <option value={15}>
            15
          </option>

          <option value={20}>
            20
          </option>
        </select>

        <label>
          Exam Difficulty
        </label>

        <select
          value={
            settings.default_exam_difficulty
          }
          onChange={(e) =>
            setSettings({
              ...settings,
              default_exam_difficulty:
                e.target.value
            })
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

        <div className="checkbox-row">

          <input
            type="checkbox"
            id="watermark"
            checked={
              settings.export_watermark
            }
            onChange={(e) =>
              setSettings({
                ...settings,
                export_watermark:
                  e.target.checked
              })
            }
          />

          <label htmlFor="watermark">
            Show PDF Watermark
          </label>

        </div>

        <div className="modal-actions">

          <button
            className="cancel-btn"
            onClick={onClose}
          >
            Cancel
          </button>

          <button
            className="save-btn"
            onClick={
              saveSettings
            }
          >
            Save
          </button>

        </div>

      </div>

    </div>

  );

}

export default SettingsModal;