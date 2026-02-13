import aiohttp
import asyncio
import time
import json
from .utils import get_random_headers, generate_variations

def load_sites():
    with open("sites.json", "r") as f:
        return json.load(f)

async def check_site(session, site_name, site_data, username, mode):
    url = site_data["url"].format(username)
    error_signature = site_data.get("error", "")

    headers = get_random_headers()
    start = time.perf_counter()

    try:
        async with session.get(url, headers=headers, timeout=8) as response:
            response_time = round(time.perf_counter() - start, 2)
            text = await response.text()

            exists = False

            # 🔥 DEEP MODE = agressivo
            if mode == "deep":
                if response.status == 200:
                    exists = True

            # 🔐 STRICT MODE = validar assinatura
            elif mode == "strict":
                if response.status == 200 and error_signature:
                    if error_signature.lower() not in text.lower():
                        exists = True

            # ⚖ NORMAL MODE
            else:
                if response.status == 200:
                    exists = True

            return {
                "site": site_name,
                "username": username,
                "exists": exists,
                "status": response.status,
                "time": response_time,
                "url": str(response.url)
            }

    except Exception:
        return {
            "site": site_name,
            "username": username,
            "exists": False,
            "status": "ERR",
            "time": 0,
            "url": "N/A"
        }

async def deep_scan(username: str, mode="normal"):
    sites = load_sites()

    if mode == "strict":
        usernames = [username]
    elif mode == "deep":
        usernames = generate_variations(username)
    else:
        usernames = [username]

    tasks = []

    async with aiohttp.ClientSession() as session:
        for u in usernames:
            for site_name, site_data in sites.items():
                tasks.append(check_site(session, site_name, site_data, u, mode))

        results = await asyncio.gather(*tasks)

    return results
