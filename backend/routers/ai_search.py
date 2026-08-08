from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.ai.gemini_service import extract_filters
from backend.search import search_images

router = APIRouter()


class Query(BaseModel):
    query: str


@router.post("/ai-search")
def ai_search(data: Query):
    try:
        filters = extract_filters(data.query)

        result = search_images(
            object_name=filters.get("object_name"),
            telescope=filters.get("telescope_name"),
            instrument=filters.get("instrument_name"),
            observer=filters.get("observer_name"),
            filter=filters.get("filter_name"),
            date_from=filters.get("observation_date_after"),
            date_to=filters.get("observation_date_before"),
        )

        return {
            "status": "success",
            "filters": filters,
            "results": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
