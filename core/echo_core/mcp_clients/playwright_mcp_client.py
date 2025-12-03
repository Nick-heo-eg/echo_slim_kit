from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class PlaywrightMCPConfig:
    endpoint: str = "http://127.0.0.1:3928/mcp"


class PlaywrightMCPClient:
    """Minimal stub of the real Playwright MCP client.

    This version only logs payloads and returns fake responses.
    Replace with the real implementation from your full repo for production use.
    """

    def __init__(self, config: Optional[PlaywrightMCPConfig] = None) -> None:
        self.config = config or PlaywrightMCPConfig()

    # Generic call
    def call_tool(self, name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "status": "stub",
            "tool": name,
            "payload": payload,
            "endpoint": self.config.endpoint,
        }

    def navigate(self, url: str, wait_until: str = "domcontentloaded") -> Dict[str, Any]:
        return self.call_tool("navigate", {"url": url, "wait_until": wait_until})

    def click(self, selector: str, button: str = "left") -> Dict[str, Any]:
        return self.call_tool("click", {"selector": selector, "button": button})

    def fill(self, selector: str, text: str) -> Dict[str, Any]:
        return self.call_tool("fill", {"selector": selector, "text": text})

    def evaluate(self, script: str) -> Dict[str, Any]:
        return self.call_tool("evaluate", {"script": script})

    def screenshot(
        self,
        path: str,
        url: Optional[str] = None,
        *,
        full_page: bool = True,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {"path": path, "full_page": full_page}
        if url:
            payload["url"] = url
        return self.call_tool("screenshot", payload)

    def wait_for_selector(self, selector: str, timeout_ms: Optional[int] = None) -> Dict[str, Any]:
        payload: Dict[str, Any] = {"selector": selector}
        if timeout_ms is not None:
            payload["timeout_ms"] = timeout_ms
        return self.call_tool("wait_for_selector", payload)
