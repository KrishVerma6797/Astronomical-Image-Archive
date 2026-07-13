from fastapi import APIRouter,HTTPException
from fastapi.responses import FileResponse
from database.connections import get_connection
from pathlib import Path
router=APIRouter()

@router.get("/images/{image_id}")

#getting image details:
def get_image_details(image_id:int):
    conn=None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
            SELECT 
            i.image_id,
                i.object_name,
                i.observation_date,
                i.observation_time,
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
                LEFT JOIN telescopes t ON i.telescope_id=t.telescope_id
                LEFT JOIN instruments ins ON i.instrument_id = ins.instrument_id
                LEFT JOIN observers o ON i.observer_id = o.observer_id
                LEFT JOIN filters f ON i.filter_id = f.filter_id

                WHERE i.image_id=%s
            """
        cursor.execute(query,(image_id,))
        image=cursor.fetchone()
        if image is None:
            raise HTTPException (status_code=404,detail=f"Image with ID {image_id} not found")
        return image
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"An error occurred while retrieving image details: {e}")
    finally:
        if conn:
            conn.close()


#get image thumbnail:
@router.get("/images/{image_id}/thumbnail")
def get_thumbnail(image_id:int):
    conn=None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="SELECT thumbnail_path FROM images WHERE image_id=%s"
        cursor.execute(query,(image_id,))
        image=cursor.fetchone()
        if image is None:
            raise HTTPException(status_code=404,detail=f"Image with ID {image_id} not found")
        thumbnail_path=Path(image['thumbnail_path'])
        if not thumbnail_path.exists():
            raise HTTPException(status_code=404,detail=f"Thumbnail for image ID {image_id} not found")
        return FileResponse(path=str(thumbnail_path),media_type="image/jpeg")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"An error occurred while retrieving thumbnail: {e}")
    finally:
        if conn:
            conn.close()

#get original fits file
@router.get("/images/{image_id}/file")
def get_image_file(image_id:int):
    conn=None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""SELECT file_path FROM images WHERE image_id=%s""",(image_id,))
        image=cursor.fetchone()

        if image is None:
            raise HTTPException(status_code=404,detail=f"Image with ID {image_id} not found")
        file_path=Path(image['file_path'])
        
        if not file_path.exists():
            raise HTTPException(status_code=404,detail=f"Original file for image ID {image_id} not found")
        
        return FileResponse(path=str(file_path),media_type='application/fits')
    except HTTPException:
        raise   
    except Exception as e:  
        raise HTTPException(status_code=500,detail=f"An error occurred while retrieving original file: {e}")
    finally:
        if conn:
            conn.close()
            