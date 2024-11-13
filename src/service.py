import sqlite3
from datetime import datetime
from typing import List, Optional

from db import get_connection
from models import TrafficModel


def validate_iso_format(date_str: Optional[str]) -> None:
    if date_str:
        try:
            datetime.fromisoformat(date_str)
        except ValueError:
            raise ValueError("Wrong date format use YYYY-MM-DD HH:MM:SS.")


def get_traffic(
    customer_name: Optional[str],
    start_date: Optional[str],
    end_date: Optional[str],
    ip: Optional[str],
) -> List[TrafficModel]:

    validate_iso_format(start_date)
    validate_iso_format(end_date)

    connection = get_connection()
    cursor = connection.cursor()
    cursor.row_factory = sqlite3.Row

    query = """
        SELECT t.id, c.customer_name, t.ip, t.date, t.received_traffic
        FROM traffic t
        LEFT JOIN customers c ON t.customer_id = c.id
        WHERE 1=1
    """
    params = []

    if customer_name is not None:
        query += " AND c.customer_name = ?"
        params.append(customer_name)

    if start_date is not None:
        query += " AND t.date >= ?"
        params.append(start_date)

    if end_date is not None:
        query += " AND t.date <= ?"
        params.append(end_date)

    if ip is not None:
        query += " AND t.ip = ?"
        params.append(ip)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    traffic_data = [
        TrafficModel(
            id=row["id"],
            customer_name=row["customer_name"],
            ip=row["ip"],
            date=row["date"],
            received_traffic=row["received_traffic"],
        )
        for row in rows
    ]

    connection.close()
    return traffic_data
