import {
  useState,
  useEffect
} from "react";
import api from "../services/api";

function UploadPanel() {

  const [file, setFile] = useState(null);

  const [documentInfo, setDocumentInfo] =
    useState(null);

  const [success, setSuccess] =
    useState("");

  useEffect(() => {

    fetchDocumentInfo();

  }, []);

  const fetchDocumentInfo =
  async () => {

    try {

      const response =
        await api.get(
          "/document/info"
        );

      if (
        response.data.loaded
      ) {

        setDocumentInfo(
          response.data
        );

      }

    } catch (error) {

      console.error(error);

    }

  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    try {
      const response = await api.post(
        "/upload",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      console.log(response.data);

      fetchDocumentInfo();

      window.dispatchEvent(
        new Event(
          "documentUploaded"
        )
      );

      setSuccess(
        "Document uploaded successfully"
      );

    } catch (error) {
      console.error(error);

      alert("Upload failed");
    }
  };

  return (
    <div>
      <h2>Upload Document</h2>

      <input
        type="file"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <button
        disabled={!file}
        onClick={handleUpload}
      >
        Upload
      </button>
      {documentInfo && (
        <div className="document-card">

          <h3>
            Current Document
          </h3>

          <p>
            <strong>
              Filename:
            </strong>{" "}
            {documentInfo.filename}
          </p>

          <p>
            <strong>
              Characters:
            </strong>{" "}
            {documentInfo.characters}
          </p>

        </div>
      )}
      {
        success && (
          <div
            className="success-message"
          >
            ✓ {success}
          </div>
        )
      }
    </div>
  );
}

export default UploadPanel;