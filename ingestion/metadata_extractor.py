from astropy.io import fits
from pathlib import Path
from datetime import datetime


def extract_metadata(file_path):
    try:
        file_path = Path(file_path)

        with fits.open(file_path) as hdul:
            header = hdul[0].header

            raw_date = (
                header.get("DATE-OBS")
                or header.get("DATEOBS")
                or header.get("OBS-DATE")
                or header.get("DATE")
            )

            if not raw_date:
                print("Observation date not found.")
                return None

            raw_date = str(raw_date).strip()

            if "/" in raw_date:
                observation_date = datetime.strptime(
                    raw_date, "%d/%m/%y"
                ).date()
            else:
                observation_date = raw_date

            metadata = {
                "object_name": (
                    header.get("OBJECT")
                    or header.get("TARGNAME")
                    or header.get("TARGET")
                    or "UNKNOWN"
                ),
                "observation_date": observation_date,
                "observation_time": header.get("TIME-OBS"),
                "telescope": header.get("TELESCOP"),
                "instrument": header.get("INSTRUME"),
                "observer": header.get("OBSERVER"),
                "filter": header.get("FILTER") or header.get("FILTNAM1"),
                "exposure_time": header.get("EXPTIME"),
                "ra": header.get("RA") or header.get("RA_TARG"),
                "dec_coord": header.get("DEC") or header.get("DEC_TARG"),
                "image_format": file_path.suffix[1:].upper(),
                "image_size_mb": round(file_path.stat().st_size / (1024 * 1024), 2),
                "file_path": str(file_path)
            }

            return metadata

    except Exception as e:
        print(f"Metadata extraction error: {e}")
        return None