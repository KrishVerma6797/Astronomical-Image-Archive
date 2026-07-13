from fastapi import APIRouter , UploadFile, File, HTTPException
from pathlib import Path
import shutil
from ingestion.ingest import ingest_image

router=APIRouter()
storage_folder=Path("storage")
allowed_ext={".fits",".fit",".fts"}

@router.post("/upload")
def upload_image(file:UploadFile=File(...)):
    file_ext=Path(file.filename).suffix.lower()
    if file_ext not in allowed_ext:
        raise HTTPException(status_code=400,detail="Only FITS files are allowed")
    storage_folder.mkdir(parents=True,exist_ok=True)
    file_path=storage_folder/file.filename

    try:
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        result=ingest_image(file_path)
        if result == "duplicate":
            raise HTTPException(
        status_code=409,
        detail="Image already archived"
    )

        if result is False:
            raise HTTPException(
        status_code=500,
        detail="Failed to ingest image"
    )

        return {
    "message": "Image uploaded and archived successfully"
}
        
    except HTTPException as e:
        raise 

    except Exception as e:
        raise HTTPException(status_code=500,detail=f"An error occurred during file upload: {str(e)}")
    
    finally:
        file.file.close()