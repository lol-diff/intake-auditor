import httpx
import os

class ClioClient:
    def __init__(self):
        self.base_url = "https://app.clio.com/api/v4"
        # We'll pull the token dynamically when needed
        self.token = os.getenv("CLIO_ACCESS_TOKEN")

    async def get_matter(self, matter_id: str):
        headers = {"Authorization": f"Bearer {self.token}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/matters/{matter_id}", headers=headers)
            response.raise_for_status()
            return response.json()