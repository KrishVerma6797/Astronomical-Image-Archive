import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

function Home() {
  return (
    <div className="min-h-screen bg-space-950 text-white">
      <Navbar />

      <div
        className="relative min-h-[calc(100vh-77px)] bg-cover bg-center"
        style={{
          backgroundImage:
            "url('https://images.unsplash.com/photo-1502134249126-9f3755a50d78?auto=format&fit=crop&q=80&w=2400')",
        }}
      >
        {/* Dark overlay - lighter than before so the starfield photo still shows through */}
        <div className="absolute inset-0 bg-space-950/55"></div>

        {/* Decorative coordinate readout, top right - Devasthal Observatory's real location */}
        <div className="hidden md:block absolute top-8 right-8 z-10 text-right font-mono text-[11px] text-slate-400 space-y-1">
          <p><span className="text-slate-600">──</span> N 29° 21′ 41″</p>
          <p><span className="text-slate-600">──</span> E 79° 41′ 04″</p>
          <p><span className="text-slate-600">──</span> ALT 1951 M</p>
        </div>

        <div className="relative z-10 max-w-3xl px-6 md:px-12 pt-20 pb-16 flex flex-col justify-center min-h-[calc(100vh-77px)]">
          <p className="font-mono text-[11px] tracking-[0.25em] text-starlight/80 uppercase mb-6">
            <span className="text-slate-600 mr-2">──</span>
            Aryabhatta Research Institute &middot; Est. 1954
          </p>

          <h1 className="font-display text-4xl md:text-5xl leading-[1.1] mb-6">
            The <span className="italic text-starlight">Devasthal</span> Astronomical{" "}
            <span className="italic">Image</span> Archive.
          </h1>

          <p className="text-slate-400 text-base leading-relaxed mb-9 max-w-lg font-body">
            A curated repository of observations from India's largest optical
            telescope. Upload FITS data, retrieve historical frames by object,
            telescope, or celestial coordinates.
          </p>

          <div className="flex flex-wrap gap-3">
            <Link
              to="/search"
              className="bg-starlight hover:bg-starlight-dim text-space-950 text-xs font-mono font-semibold tracking-[0.1em] uppercase px-6 py-3.5 rounded-full transition"
            >
              Search the Archive →
            </Link>
            <Link
              to="/upload"
              className="border border-space-700 hover:border-nebula text-white text-xs font-mono font-semibold tracking-[0.1em] uppercase px-6 py-3.5 rounded-full transition"
            >
              Upload FITS Observation
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
