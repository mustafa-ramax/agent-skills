# Mustafa's Agent Skills

Portable Agent Skills for browser workflows and other agent tasks. Each skill lives in its own directory under `skills/` and can be installed independently.

## Available skills

### Instagram Manager in Browser

Inspect and search Instagram follower and following lists, unfollow selected accounts, and remove selected followers through a logged-in browser. Codex Desktop's in-app browser is the primary workflow. Other agents need their own browser or computer-use controls.

For example, you can ask it to “remove my 100 most recent followers”. It will first check whether Instagram's visible list makes that selection clear, show you the exact accounts, and wait for your confirmation. Larger requests are handled in batches of up to 10 accounts.

Install only this skill:

```sh
npx skills add mustafa-ramax/agent-skills --skill instagram-manager-in-browser
```

## Compatibility

The skill uses the open `SKILL.md` format. The format is portable; performing Instagram actions also requires browser/UI controls in the agent runtime. The skill never needs a separate Instagram password or API token.

## Growing the collection

Add unrelated skills as sibling directories under `skills/`. Keep additional Instagram relationship workflows in `instagram-manager-in-browser` while they share its browser-based account-selection and confirmation workflow. Add detailed references only when they improve on-demand guidance; list only capabilities that are implemented and tested.

The first release focuses on follower and following relationships. The Instagram skill can grow to cover more browser-based Instagram workflows over time; future ideas are not current capabilities until they are implemented and tested.

## Licence

This repository is available under the MIT licence. See [LICENSE](LICENSE).
