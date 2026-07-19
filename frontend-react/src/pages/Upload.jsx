import { useState } from "react";
import { uploadImage } from "../api/client";
import Navbar from "../components/Navbar";

function Upload() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState(null);
  const [isError, setIsError] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setMessage(null);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please choose a FITS file first.");
      setIsError(true);
      return;
    }

    setUploading(true);
    setMessage(null);
    setIsError(false);

    try {
      const response = await uploadImage(file);

      if (response.status === 409) {
        setMessage("This image is already archived (duplicate detected).");
        setIsError(true);
      } else if (!response.ok) {
        const errorData = await response.json().catch(() => null);
        setMessage(errorData?.detail || "Upload failed. Please check the file and try again.");
        setIsError(true);
      } else {
        const data = await response.json();
        setMessage(data.message || "Upload successful!");
        setIsError(false);
        setFile(null);
      }
    } catch (err) {
      setMessage("Upload failed. Check your backend connection.");
      setIsError(true);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="min-h-screen bg-space-950 text-white">
      <Navbar />

      <div className="max-w-xl mx-auto px-6 py-10">
        <h1 className="font-display text-3xl font-semibold text-starlight mb-1">
          Upload Astronomical Image
        </h1>
        <p className="text-slate-400 text-sm mb-8 font-body">
          FITS files are parsed automatically for object, telescope, and coordinate metadata.
        </p>

        <div className="glow-card bg-space-900 border border-space-700 rounded-xl p-6">
          <label className="block mb-3 text-xs font-mono text-slate-500 uppercase tracking-wide">
            Choose a FITS file (.fits)
          </label>

          <input
            type="file"
            accept=".fits"
            onChange={handleFileChange}
            className="block w-full text-sm text-slate-300 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-starlight file:text-space-950 file:font-semibold hover:file:bg-starlight-dim bg-space-800 border border-space-700 rounded-lg"
          />

          {file && (
            <p className="mt-3 text-sm text-slate-400 font-mono">
              {file.name} &middot; {(file.size / 1024).toFixed(1)} KB
            </p>
          )}

          <button
            onClick={handleUpload}
            disabled={uploading}
            className="mt-6 bg-starlight hover:bg-starlight-dim text-space-950 font-semibold px-6 py-3 rounded-lg transition disabled:opacity-50"
          >
            {uploading ? "Uploading..." : "Upload Image"}
          </button>

          {message && (
            <p className={`mt-4 text-sm ${isError ? "text-red-400" : "text-green-400"}`}>
              {message}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}

export default Upload;
