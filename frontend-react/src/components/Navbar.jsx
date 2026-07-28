import { Link, useLocation } from "react-router-dom";

function Navbar() {
  const location = useLocation();

  const linkClass = (path) =>
    `text-xs font-mono tracking-[0.15em] uppercase transition ${
      location.pathname === path
        ? "text-starlight"
        : "text-slate-400 hover:text-white"
    }`;

  return (
    <nav className="border-b border-space-700 bg-space-950/70 backdrop-blur-sm">
      <div className="max-w-6xl mx-auto px-6 py-5 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-3">
          <span className="w-8 h-8 rounded-full border border-starlight/50 flex items-center justify-center text-starlight text-sm">
            ◎
          </span>
          <span className="leading-tight">
            <span className="block font-display text-base text-white tracking-wide">ARIES</span>
            <span className="block font-mono text-[10px] text-slate-500 tracking-[0.2em]">
              DEVASTHAL ARCHIVE
            </span>
          </span>
        </Link>

        <div className="hidden md:flex gap-8">
          <Link to="/" className={linkClass("/")}>Home</Link>
          <Link to="/search" className={linkClass("/search")}>Search</Link>
          <Link to="/upload" className={linkClass("/upload")}>Upload</Link>
        </div>

        <Link
          to="/search"
          className="bg-starlight hover:bg-starlight-dim text-space-950 text-xs font-mono font-semibold tracking-[0.1em] uppercase px-5 py-2.5 rounded-full transition"
        >
          Access Archive →
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;
