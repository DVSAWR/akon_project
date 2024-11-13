from typing import Optional

from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import RedirectResponse

from db import initialize_db
from service import get_traffic, validate_iso_format

app = FastAPI()
initialize_db()


@app.get("/")
async def redirect_to_docs():
    """Redirect to /docs."""
    return RedirectResponse(url="/docs")


@app.get("/traffic/")
def get_traffic_route(
    customer_name: Optional[str] = Query(None, description="Сustomer"),
    start_date: Optional[str] = Query(None, description="YYYY-MM-DD HH:MM:SS"),
    end_date: Optional[str] = Query(None, description="YYYY-MM-DD HH:MM:SS"),
    ip: Optional[str] = Query(None, description="IP"),
):
    """Get data from BD using params."""

    try:
        validate_iso_format(start_date)
        validate_iso_format(end_date)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

    try:
        traffic_records = get_traffic(customer_name, start_date, end_date, ip)
        return traffic_records
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
