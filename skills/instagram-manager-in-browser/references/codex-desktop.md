# Codex Desktop browser guidance

Use this reference when the current runtime is Codex Desktop and provides browser control.

- Follow the live instructions exposed by the Codex browser-control tool for session initialisation and tab selection. Tool names and APIs can change; do not invent method names.
- Inspect the available browser tabs and reuse the user's existing Instagram tab in the Codex in-app browser. Do not switch to Chrome, Edge, or another browser session just because it is available.
- If the tab cannot be selected safely, ask the user to bring the Instagram tab forward or identify it. Do not navigate an unknown tab or assume it shares the same login.
- Let the user sign in directly in the in-app browser. Wait for them to confirm they are ready, then verify the visible account handle before continuing.
- Mobile-sized layout is optional. Offer a viewport around 390 × 844 CSS pixels only if the browser tool supports a per-tab viewport and the current layout makes the list hard to use. Do not resize the desktop window by guessing, and restore the prior viewport if the tool can do so.
- Instagram's list controls can appear close to search fields. Verify each control's visible label, role, and page context before using it; never repeat a click when the expected navigation did not happen.
