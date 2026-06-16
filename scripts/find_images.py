#!/usr/bin/env python3
"""Search openly-licensed images (Openverse) for a lesson, license-first.

Defaults to CC0 and Public Domain Mark so results are safe to use without attribution,
though attribution is still returned and should be recorded. No API key required.

Usage:
    python3 find_images.py "water cycle diagram"
    python3 find_images.py "fraction circles" --license cc0,pdm,by --download images/ --n 3

Prints a JSON list of results. With --download, saves files and includes 'local_path'.
If nothing suitable is found, prints an empty list — that is the agent's signal to ask
the teacher before generating a replacement image, not to invent one silently.
"""
import argparse
import json
import os
import sys

try:
    import requests
except ImportError:
    sys.exit("This script needs 'requests'. Install with: pip install requests")

API = "https://api.openverse.org/v1/images/"
UA = {"User-Agent": "teacher-deck-skill (https://github.com/ryseymour/teacher-deck-skill)"}


def search(query, license_codes="cc0,pdm", n=5):
    params = {"q": query, "license": license_codes, "page_size": n, "mature": "false"}
    resp = requests.get(API, params=params, headers=UA, timeout=30)
    resp.raise_for_status()
    results = []
    for item in resp.json().get("results", []):
        results.append(
            {
                "title": item.get("title"),
                "creator": item.get("creator"),
                "license": item.get("license"),
                "license_version": item.get("license_version"),
                "source": item.get("source"),
                "url": item.get("url"),
                "landing_page": item.get("foreign_landing_url"),
                "attribution": item.get("attribution"),
            }
        )
    return results


def download(results, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for i, item in enumerate(results, 1):
        url = item.get("url")
        if not url:
            continue
        try:
            r = requests.get(url, headers=UA, timeout=60)
            r.raise_for_status()
            ext = os.path.splitext(url.split("?")[0])[1] or ".jpg"
            path = os.path.join(out_dir, f"image_{i}{ext}")
            with open(path, "wb") as fh:
                fh.write(r.content)
            item["local_path"] = path
        except Exception as exc:  # noqa: BLE001
            item["download_error"] = str(exc)
    return results


def main():
    ap = argparse.ArgumentParser(description="Find openly-licensed images for a lesson.")
    ap.add_argument("query", help="Search terms")
    ap.add_argument(
        "--license",
        default="cc0,pdm",
        help="Comma-separated Openverse license codes (default: cc0,pdm). "
        "Add 'by','by-sa' to widen, but those require visible attribution.",
    )
    ap.add_argument("--n", type=int, default=5, help="Number of results (default 5)")
    ap.add_argument("--download", metavar="DIR", help="Download results into DIR")
    args = ap.parse_args()

    results = search(args.query, args.license, args.n)
    if args.download and results:
        results = download(results, args.download)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
