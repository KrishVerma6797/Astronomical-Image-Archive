import { useState } from "react";
import { searchImages, getThumbnailUrl, getFileUrl } from "../api/client";
import Navbar from "../components/Navbar";

function Search() {
  const [filters, setFilters] = useState({
    object_name: "",
    telescope: "",
    instrument: "",
    observer: "",
    filter: "",
    date_from: "",
    date_to: "",
    image_format: "",
  });

  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  const handleSearch = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await searchImages(filters);
      setResults(data);
    } catch (err) {
      setError("Search failed. Check your backend connection.");
    } finally {
      setLoading(false);
    }
  };

  const inputClass =
    "bg-space-900 border border-space-700 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-starlight transition placeholder:text-slate-500";

  return (
    <div className="min-h-screen bg-space-950 text-white">
      <Navbar />

      <div className="max-w-6xl mx-auto px-6 py-10">
        <h1 className="font-display text-3xl font-semibold text-starlight mb-1">
          Search Astronomical Images
        </h1>
        <p className="text-slate-400 text-sm mb-8 font-body">
          Filter by any combination of parameters below.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-3xl">
          <input
            name="object_name"
            value={filters.object_name}
            onChange={handleChange}
            placeholder="Object Name"
            className={inputClass}
          />
          <input
            name="telescope"
            value={filters.telescope}
            onChange={handleChange}
            placeholder="Telescope"
            className={inputClass}
          />
          <input
            name="instrument"
            value={filters.instrument}
            onChange={handleChange}
            placeholder="Instrument"
            className={inputClass}
          />
          <input
            name="observer"
            value={filters.observer}
            onChange={handleChange}
            placeholder="Observer"
            className={inputClass}
          />
          <input
            name="filter"
            value={filters.filter}
            onChange={handleChange}
            placeholder="Filter"
            className={inputClass}
          />
          <select
            name="image_format"
            value={filters.image_format}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="">Any Format</option>
            <option value="FITS">FITS</option>
            <option value="PNG">PNG</option>
            <option value="JPG">JPG</option>
            <option value="JPEG">JPEG</option>
            <option value="TIFF">TIFF</option>
          </select>
          <div>
            <label className="text-xs text-slate-500 font-mono">DATE FROM</label>
            <input
              type="date"
              name="date_from"
              value={filters.date_from}
              onChange={handleChange}
              className={`w-full mt-1 ${inputClass}`}
            />
          </div>
          <div>
            <label className="text-xs text-slate-500 font-mono">DATE TO</label>
            <input
              type="date"
              name="date_to"
              value={filters.date_to}
              onChange={handleChange}
              className={`w-full mt-1 ${inputClass}`}
            />
          </div>
        </div>

        <button
          onClick={handleSearch}
          disabled={loading}
          className="mt-6 bg-starlight hover:bg-starlight-dim text-space-950 font-semibold px-6 py-3 rounded-lg transition disabled:opacity-50"
        >
          {loading ? "Searching..." : "Search Images"}
        </button>

        {error && <p className="mt-4 text-red-400 font-body">{error}</p>}

        {results && (
          <p className="mt-8 text-slate-400 font-mono text-sm">
            {results.total_results} images found
          </p>
        )}

        {results && (
          <div className="mt-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {results.images.map((image) => (
              <div
                key={image.image_id}
                className="glow-card bg-space-900 rounded-xl p-4 border border-space-700"
              >
                <img
                  src={getThumbnailUrl(image.image_id)}
                  alt={image.object_name}
                  className="w-full h-48 object-cover rounded-lg mb-3"
                />
                <h3 className="font-display text-lg font-semibold text-starlight">
                  {image.object_name}
                </h3>
                <div className="mt-2 space-y-1 font-mono text-xs text-slate-400">
                  <p>DATE&nbsp;&nbsp;&nbsp;{image.observation_date}</p>
                  <p>SCOPE&nbsp;&nbsp;{image.telescope_name}</p>
                  <p>INSTR&nbsp;&nbsp;{image.instrument_name}</p>
                  <p>FORMAT&nbsp;{image.image_format}</p>
                </div>
                <a
                  href={getFileUrl(image.image_id)}
                  className="inline-block mt-4 bg-nebula hover:bg-nebula-dim text-white text-sm font-semibold px-4 py-2 rounded-lg transition"
                >
                  Open FITS File
                </a>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Search;
