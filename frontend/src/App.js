import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      await axios.post("http://127.0.0.1:8000/upload", formData);
      alert("File uploaded & indexed!");
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  };

  const handleAsk = async () => {
    if (!question) return;

    setLoading(true);
    setAnswer("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/ask", {
        query: question,
      });

      setAnswer(res.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Error fetching answer");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h1>RAG Document QA System</h1>

      {/* Upload Section */}
      <div style={{ marginBottom: "20px" }}>
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button onClick={handleUpload}>Upload</button>
      </div>

      {/* Question Section */}
      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{ width: "70%" }}
        />
        <button onClick={handleAsk}>Ask</button>
      </div>

      {/* Answer Section */}
      <div>
        <strong>Answer:</strong>
        {loading ? <p>Loading...</p> : <p>{answer}</p>}
      </div>
    </div>
  );
}

export default App;