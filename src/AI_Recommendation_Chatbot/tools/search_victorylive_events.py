from crewai.tools import BaseTool
from typing import Type, List, Optional
from pydantic import BaseModel, Field
import requests
from datetime import datetime, timedelta
from dateutil import parser, tz


class VictoryLiveEventSearchInput(BaseModel):
    performers: List[str] = Field(..., description="List of performer names to search for")
    location: Optional[str] = Field(None, description="Location to filter events by (e.g. New York City)")
    start_date: Optional[str] = Field(None, description="Start date in YYYY-MM-DD format")
    end_date: Optional[str] = Field(None, description="End date in YYYY-MM-DD format")

class VictoryLiveEventSearchTool(BaseTool):
    name: str = "VictoryLive Multi-Performer Event Search Tool"
    description: str = (
        "Fetches VictoryLive events for a list of performers, filters by location and time, "
        "and ranks the results by long_term_popularity_score."
    )
    args_schema: Type[BaseModel] = VictoryLiveEventSearchInput


    def _run(self, performers: List[str], location: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> str:
        all_events = []
        local_tz = tz.tzlocal()  # or use pytz.timezone("US/Eastern") if you want to force a specific zone

        start = datetime.fromisoformat(start_date).replace(tzinfo=local_tz) if start_date else None
        end = datetime.fromisoformat(end_date).replace(tzinfo=local_tz) if end_date else None

        for performer in performers:
            url = f"https://www.mytickets.com/api/partner/victorylive/events/search?name={performer}"
            print("url:",url)
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                events = data.get("events", [])
                print("# events:", len(events))

                for event in events:
                    # Filter: location
                    city = event.get("venue", {}).get("location", "").lower()
                    print("loc: ", location)
                    print("city: ", city)
                    if location and self.normalize(location) not in self.normalize(city) and self.normalize(city) not in self.normalize(location):
                        continue

                    # Filter: date
                    event_time_str = event.get("occurs_at_local")
                    print(event_time_str)
                    try:
                        event_time = parser.isoparse(event_time_str) if event_time_str else None
                    except:
                        continue
                    
                    print(f'{start_date} {event_time} {end_date}')
                    if start_date and end_date and event_time:
                        if not (start <= event_time <= end):
                            continue

                    # Get popularity score
                    score = event.get("long_term_popularity_score", 0)
                    all_events.append({
                        "title": event.get("name", "Unnamed event"),
                        "venue": event.get("venue", {}).get("name", "Unknown venue"),
                        "location": event.get("venue", {}).get("location", "Unknown venue"),
                        "date": event_time.strftime("%A, %B %d, %Y at %-I:%M %p %Z"),
                        "link": f"https://www.mytickets.com/event/{event.get('id', '')}",
                        "score": score
                    })

            except Exception as e:
                print(f"[Warning] Failed to fetch results for {performer}: {e}")
                continue

        if not all_events:
            return "No events found matching the criteria."

        # Rank by popularity
        all_events.sort(key=lambda x: x["score"], reverse=True)

        # Format output
        result = "\n".join([
            f"- {e['title']}"
            f"  Date: {e['date']}"
            f"  Venue: {e['venue']}"
            f"  Location: {e['location']}"
            f"  Tickets: {e['link']}"
            for e in all_events[:5]
        ])

        return result
    
    @staticmethod
    def normalize(loc: str) -> str:
        return loc.lower().replace("city", "").strip()