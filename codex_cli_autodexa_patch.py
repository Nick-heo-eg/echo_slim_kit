#!/usr/bin/env python3
"""Slim Codex CLI + MCP patch (demo only).

In the real system this would wrap Codex CLI, run Dexa, then call
PlaywrightMCPClient to drive the UI and log proof artifacts.
Here we only simulate the flow.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from core.echo_core.mcp_clients.playwright_mcp_client import PlaywrightMCPClient


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Slim Codex + MCP demo runner (stub).")
    parser.add_argument("--mode", choices=["default", "ui"], default="default")
    parser.add_argument("--bridge", choices=["playwright"], default="playwright")
    parser.add_argument("--url", default="https://example.com")
    parser.add_argument("--screenshot-path", default="artifacts/dashboard/demo_slim.png")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    client = PlaywrightMCPClient()

    print(f"▶ Mode      : {args.mode}")
    print(f"▶ Bridge    : {args.bridge}")
    print(f"▶ URL       : {args.url}")
    print(f"▶ Screenshot: {args.screenshot_path}")
    Path("artifacts/dashboard").mkdir(parents=True, exist_ok=True)

    if args.mode == "ui":
        nav = client.navigate(args.url)
        shot = client.screenshot(args.screenshot_path, url=args.url)
        print("◎ navigate result :", nav)
        print("◎ screenshot result:", shot)
    else:
        print("◎ default mode (no UI automation in this slim stub).")

    print("✅ Slim Codex + MCP demo finished (stub).")


if __name__ == "__main__":
    main()
