---
name: instagram-manager-in-browser
description: Use Instagram in a logged-in browser to inspect and search follower or following lists, unfollow selected accounts, or remove selected followers. Codex Desktop's in-app browser is the primary workflow; use this skill for these tasks only when the agent has browser or UI controls.
license: MIT
---

# Instagram Manager in Browser

Use this skill for Instagram follower and following relationship tasks through the browser UI. The skill format is portable; browser access depends on the current agent. For Codex Desktop, read [the Codex Desktop guidance](references/codex-desktop.md) before browser interaction.

## Supported tasks

- Inspect the visible follower or following list, counts, and search results.
- Unfollow accounts selected by the user from the **Following** list.
- Remove accounts selected by the user from the **Followers** list.

Do not infer that an account should be removed or unfollowed from its name, profile photo, apparent inactivity, or other unrequested criteria. Do not post, message, like, block, or change account settings with this skill.

## Example requests

- “Unfollow @example” means remove that account from **Following**.
- “Remove my 100 most recent followers” means remove accounts from **Followers**. Use this selection only if the visible list makes recency clear; preview the exact accounts and get confirmation before acting. Process the approved selection in batches of no more than 10 accounts.

If the interface does not provide a reliable recent order, explain that and ask the user to choose specific accounts or another selection criterion.

## Before acting

1. Check that the current agent exposes browser or computer-use controls. If it does not, say that this environment cannot operate the Instagram UI and offer manual guidance. Never claim an action was completed without observing it.
2. Reuse the Instagram tab the user opened when available. Have the user sign in themselves. Never ask for, enter, or store their password, one-time code, recovery code, or session token.
3. Verify the visible Instagram account before inspecting or changing its relationships. If the account is not the one the user intends, stop and ask.
4. Resolve the action and source list before any change:
   - **Unfollow** means removing an account from the user's **Following** list.
   - **Remove follower** means removing an account from the user's **Followers** list.
   - If the user says “unfollow my followers” or otherwise mixes these, ask which action they mean.
5. For changes, identify the exact usernames or user-approved selection criteria and count. Show the intended action, source list, count, and selected accounts before acting; ask the user to confirm that preview. Do not expand the selection after confirmation.

## Use the browser UI

- Use the current agent's documented browser/UI controls. Do not assume that another agent exposes Codex's browser tools or that a second browser shares the user's login.
- Prefer accessible names, roles, and row context. If those are unavailable, inspect a fresh screenshot immediately before clicking. Never rely on remembered coordinates or button offsets.
- Confirm the page heading/list type and target username in the same row as the action control. Treat the search field and nearby list-navigation controls as separate targets; do not click based on proximity.
- Before an unfollow, confirm the row belongs to the selected account and exposes the expected **Following** action. If Instagram asks for confirmation, read the dialog and confirm only when it matches the approved unfollow. Afterwards, verify the row changed to **Follow** or disappeared from the Following list.
- Before removing a follower, confirm the selected account in the Followers list and use the explicit remove action. Read any confirmation dialog before accepting, then verify the account was removed.
- For larger approved selections, act in batches of no more than 10 accounts. After each batch, verify the completed changes and that the next targets still match the approved list. Honour any delay the user requested between UI actions, and wait for the interface to settle before continuing.
- Report completed, remaining, and unverifiable counts accurately. Do not claim a whole list was reviewed if the UI only exposed part of it.

## Stop conditions

Stop without retrying mutations if the account changes, the list or target becomes uncertain, an action produces an unexpected result, or Instagram shows a checkpoint, CAPTCHA, security prompt, warning, or action limit. Ask the user to handle sign-in or security checks themselves. Do not bypass them, use hidden/private APIs, scrape data unavailable in the visible UI, or use delays to evade platform limits.

## Future related workflows

Add future Instagram relationship tasks here only when they use the same logged-in browser model and account-selection safeguards. Keep new features out of the activation description until implemented and tested. Put unrelated skills in separate skill directories.
