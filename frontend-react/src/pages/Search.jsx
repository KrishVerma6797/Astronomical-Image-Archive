import { useState } from "react";
import { searchImages, getThumbnailUrl, getFileUrl } from "../api/client";
import Navbar from "../components/Navbar";

function Search() {
  const [filters, setFilters] = useState({
  // Basic Filters
  object_name: "",
  telescope: "",
  instrument: "",
  observer: "",
  filter: "",
  image_format: "",
  date_from: "",
  date_to: "",

  // Advanced Filters
  observatory: "",
  location: "",
  exposure_time: "",
  ra: "",
  dec_coord: "",
  wavelength_nm: "",
  department: "",
  instrument_type: "",
});

  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [expandedCard, setExpandedCard] = useState(null);
  const [showAdvanced, setShowAdvanced] = useState(false);

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

      <div className="mt-6 flex items-center justify-between">
  <button
    type="button"
    onClick={() => setShowAdvanced(!showAdvanced)}
    className="text-starlight font-semibold hover:underline"
  >
    {showAdvanced
      ? "Hide Advanced Filters ▲"
      : "Show Advanced Filters ▼"}
  </button>

  <button
    onClick={handleSearch}
    disabled={loading}
    className="bg-starlight hover:bg-starlight-dim text-space-950 font-semibold px-8 py-3 rounded-lg transition disabled:opacity-50"
  >
    {loading ? "Searching..." : "Search Images"}
  </button>
</div>

        {/* <button
  type="button"
  onClick={() => setShowAdvanced(!showAdvanced)}
  className="mt-5 text-starlight font-semibold hover:underline"
>
  {showAdvanced ? "Hide Advanced Filters ▲" : "Show Advanced Filters ▼"}
</button> */}
        {showAdvanced && (

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-5">

  <input
    name="observatory"
    value={filters.observatory}
    onChange={handleChange}
    placeholder="Observatory"
    className={inputClass}
  />

  <input
    name="location"
    value={filters.location}
    onChange={handleChange}
    placeholder="Location"
    className={inputClass}
  />

  <input
    type="number"
    name="exposure_time"
    value={filters.exposure_time}
    onChange={handleChange}
    placeholder="Exposure Time (sec)"
    className={inputClass}
  />

  <input
    type="number"
    step="0.000001"
    name="ra"
    value={filters.ra}
    onChange={handleChange}
    placeholder="Right Ascension (RA)"
    className={inputClass}
  />

  <input
    type="number"
    step="0.000001"
    name="dec_coord"
    value={filters.dec_coord}
    onChange={handleChange}
    placeholder="Declination (DEC)"
    className={inputClass}
  />

  <input
    type="number"
    name="wavelength_nm"
    value={filters.wavelength_nm}
    onChange={handleChange}
    placeholder="Wavelength (nm)"
    className={inputClass}
  />

  <input
    name="department"
    value={filters.department}
    onChange={handleChange}
    placeholder="Observer Department"
    className={inputClass}
  />

  <input
    name="instrument_type"
    value={filters.instrument_type}
    onChange={handleChange}
    placeholder="Instrument Type"
    className={inputClass}
  />

</div>

)}

        {/* <button
          onClick={handleSearch}
          disabled={loading}
          className="mt-6 bg-starlight hover:bg-starlight-dim text-space-950 font-semibold px-6 py-3 rounded-lg transition disabled:opacity-50"
        >
          {loading ? "Searching..." : "Search Images"}
        </button> */}

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
                {/* <div className="mt-2 space-y-1 font-mono text-xs text-slate-400">
                  <p>DATE&nbsp;&nbsp;&nbsp;{image.observation_date}</p>
                  <p>SCOPE&nbsp;&nbsp;{image.telescope_name}</p>
                  <p>INSTR&nbsp;&nbsp;{image.instrument_name}</p>
                  <p>FORMAT&nbsp;{image.image_format}</p>
                  <p>OBJECT_NAME&nbsp;{image.object_name}</p>
                </div> */}
                <div className="mt-2 space-y-1 font-mono text-xs text-slate-400">
  <p><strong>DATE:</strong> {image.observation_date}</p>
  <p><strong>SCOPE:</strong> {image.telescope_name}</p>
  <p><strong>INSTR:</strong> {image.instrument_name}</p>
  <p><strong>FORMAT:</strong> {image.image_format}</p>

  {expandedCard === image.image_id && (
    <>
      <p><strong>Observer:</strong> {image.observer_name || "N/A"}</p>
<p><strong>Department:</strong> {image.department || "N/A"}</p>
<p><strong>Filter:</strong> {image.filter_name || "N/A"}</p>
<p><strong>Wavelength:</strong> {image.wavelength_nm ?? "N/A"}</p>
<p><strong>Observatory:</strong> {image.observatory || "N/A"}</p>
<p><strong>Location:</strong> {image.location || "N/A"}</p>
<p><strong>Exposure:</strong> {image.exposure_time ?? "N/A"}</p>
<p><strong>RA:</strong> {image.ra || "N/A"}</p>
<p><strong>DEC:</strong> {image.dec_coord || "N/A"}</p>
<p><strong>Size:</strong> {image.image_size_mb ?? "N/A"} MB</p>
    </>
  )}
</div>
<div className="mt-4 flex items-center justify-between">
  <button
    onClick={() =>
      setExpandedCard(
        expandedCard === image.image_id ? null : image.image_id
      )
    }
    className="text-starlight hover:underline text-sm font-semibold"
  >
    {expandedCard === image.image_id ? "View Less ▲" : "View More ▼"}
  </button>

  <a
    href={getFileUrl(image.image_id)}
    className="bg-nebula hover:bg-nebula-dim text-white text-sm font-semibold px-4 py-2 rounded-lg transition"
  >
    Open FITS File
  </a>
</div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Search;
