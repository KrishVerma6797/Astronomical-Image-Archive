from fastapi import APIRouter,HTTPException
from backend.ai.caption_service import generate_caption
from database.connections import get_connection

router=APIRouter()

@router.get("/caption/{image_id}")
def caption(image_id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT file_path FROM images WHERE image_id=%s",(image_id,))
    image=cursor.fetchone()
    conn.close()
    if not image:
        raise HTTPException(status_code=404,detail="image not found")
    caption=generate_caption(image['file_path'])
    return {"image_id":image_id,"caption":caption}
