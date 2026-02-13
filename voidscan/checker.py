import aiohttp
import asyncio
import json

from .utils import generate_variations


async def check_site(session, site, username):
    url = site["url"].replace("{username}", username)

    try:
        async with session.get(url, timeout=10) as response:
            return {
                "site": site["name"],
                "username": username,
                "status": response.status,
                "url": url,
            }
    except:
        return {
            "site": site["name"],
            "username": username,
            "status": 0,
            "url": url,
        }


async def run_checks(usernames, sites):
    results = []

    async with aiohttp.ClientSession() as session:
        tasks = []

        for username in usernames:
            for site in sites:
                tasks.append(check_site(session, site, username))

        responses = await asyncio.gather(*tasks)

        for result in responses:
            results.append(result)

    return results


def scan_username(username, deep=False, strict=False):
    with open("sites.json", "r") as f:
        sites = json.load(f)

    usernames = [username]

    if deep:
        usernames = generate_variations(username)

    results = asyncio.run(run_checks(usernames, sites))

    return results
