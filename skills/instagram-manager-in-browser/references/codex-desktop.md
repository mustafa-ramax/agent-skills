# Codex Desktop browser guidance

Use this reference when the current runtime is Codex Desktop and provides browser control.

- Follow the live instructions exposed by the Codex browser-control tool for session initialisation and tab selection. Tool names and APIs can change; do not invent method names.
- Inspect the available browser tabs and reuse the user's existing Instagram tab in the Codex in-app browser. Do not switch to Chrome, Edge, or another browser session just because it is available.
- If the tab cannot be selected safely, ask the user to bring the Instagram tab forward or identify it. Do not navigate an unknown tab or assume it shares the same login.
- Let the user sign in directly in the in-app browser. Wait for them to confirm they are ready, then verify the visible account handle before continuing.
- Mobile-sized layout is optional. Offer a viewport around 390 × 844 CSS pixels only if the browser tool supports a per-tab viewport and the current layout makes the list hard to use. Do not resize the desktop window by guessing, and restore the prior viewport if the tool can do so.
- Instagram's list controls can appear close to search fields. Verify each control's visible label, role, and page context before using it; never repeat a click when the expected navigation did not happen.

## Efficient unfollow execution

For each account in the approved selection:

1. Identify the row containing the exact username and its **Following** action in the verified Following list.
2. Open that row's action using a fresh accessibility control or a narrow locator containing both the username and action.
3. If a confirmation appears, verify its exact target username and unfollow action, then accept it. Follow the confirmation and stopping rules in `SKILL.md`.
4. Wait for **Follow** or verified removal from the same list with unchanged filters, using the bounded wait in `SKILL.md`. Do not repeat the action while its outcome is pending or uncertain.
5. Record the username and verified completion outcome in task memory before moving to the next approved account.

- Refresh accessibility controls after UI changes; never reuse stale element indices. Derive controls from the current state rather than assuming fixed positions or runtime-specific APIs.
- Use the smallest observation needed for each transition, such as the selected row or confirmation. Inspect broader context when the account, list or result becomes uncertain, and follow any observation requirements of the browser tool.
- Keep mutations sequential and batches at no more than 10 accounts. At each boundary, review the latest batch's verified outcomes and check the next approved targets. Reinspect uncertainty or contradictory observations rather than routinely scanning all earlier completions.
- Reduced observation overhead improved one run from roughly 5–6 to 3–4 seconds per account. This is an observation, not a performance guarantee or a reason to omit safety checks.
