from fastapi import APIRouter, HTTPException
from database.connections import get_connection
from typing import Optional
from datetime import date

router = APIRouter()


@router.get("/search")
def search_images(
    object_name: Optional[str] = None,
    telescope: Optional[str] = None,
    instrument: Optional[str] = None,
    observer: Optional[str] = None,
    filter: Optional[str] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    image_format: Optional[str] = None
):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT
                i.image_id,
                i.object_name,
                i.observation_date,
                TIME_FORMAT(i.observation_time, '%%H:%%i:%%s') AS observation_time,
                t.telescope_name,
                ins.instrument_name,
                o.observer_name,
                f.filter_name,
                i.exposure_time,
                i.ra,
                i.dec_coord,
                i.file_path,
                i.thumbnail_path,
                i.image_format,
                i.image_size_mb,
                i.created_at
            FROM images i
            LEFT JOIN telescopes t
                ON i.telescope_id = t.telescope_id
            LEFT JOIN instruments ins
                ON i.instrument_id = ins.instrument_id
            LEFT JOIN observers o
                ON i.observer_id = o.observer_id
            LEFT JOIN filters f
                ON i.filter_id = f.filter_id
            WHERE 1=1
        """

        values = []

        if object_name:
            query += " AND i.object_name LIKE %s"
            values.append(f"%{object_name}%")

        if telescope:
            query += " AND t.telescope_name LIKE %s"
            values.append(f"%{telescope}%")

        if instrument:
            query += " AND ins.instrument_name LIKE %s"
            values.append(f"%{instrument}%")

        if observer:
            query += " AND o.observer_name LIKE %s"
            values.append(f"%{observer}%")

        if filter:
            query += " AND f.filter_name LIKE %s"
            values.append(f"%{filter}%")

        if date_from:
            query += " AND i.observation_date >= %s"
            values.append(date_from)

        if date_to:
            query += " AND i.observation_date <= %s"
            values.append(date_to)

        if image_format:
            query += " AND i.image_format = %s"
            values.append(image_format)

        query += " ORDER BY i.observation_date DESC"

        cursor.execute(query, values)
        images = cursor.fetchall()

        return {
            "total_results": len(images),
            "images": images
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Search Failed: {e}"
        )

    finally:
        if conn:
            conn.close()