# Tool routing and recovery

Check capabilities once per session with tool metadata or one minimal read-only probe. Prefer native search and page tools; use an authorized browser only for interactive or logged-in pages. Use local code for deterministic transforms. Save brief, ledger and source log before risky recovery work.

## Repair before fallback

When a chosen tool fails, keep the failed route as primary until this loop finishes:

1. **Classify:** capture the shortest decisive error and identify one class: bad input, missing executable or dependency, expired authentication/session, disabled extension or adapter, network/rate limit, changed page/selector, permission boundary, corrupt data, or tool defect.
2. **Inspect:** check tool availability, version, help/status/doctor output, required local service or extension state, and the smallest failing input. Do not repeat the same command unchanged.
3. **Repair:** fix only the identified cause. Correct parameters or paths; reconnect an already authorized session; restart a local adapter; install or update a missing dependency only when permitted; patch a local adapter or script when source is available and the change is narrow. Never request or expose passwords, cookies, API keys, or private tokens in output.
4. **Verify:** run the smallest read-only test that proves the original capability works. A successful install, restart, or status command alone is not proof.
5. **Resume:** continue from saved state using the repaired route. Record repair and coverage impact once.

Use at most two materially different repair attempts for one cause. Stop sooner for account locks, anti-bot challenges, destructive changes, paid actions, or missing authorization. Ask the user only when repair needs login, permission, credentials, installation approval, or a choice that changes coverage.

Fallback is allowed only when the route cannot be repaired safely, the source itself is unavailable, or repair cost is disproportionate. State the lost coverage. Never present fallback as equivalent when it is not.

## Failure rules

- Search/page transient failure: retry once with backoff, then run repair loop.
- Login, challenge, or blocked page: do not bypass. Verify session/extension state; ask user to complete login or challenge when required.
- Missing command/dependency: locate existing installation first; inspect environment and PATH; install only with permission; verify with a real read-only action.
- Browser adapter or selector failure: confirm browser connection and page state, refresh element references, inspect current page structure, patch narrow adapter logic if locally editable, then retest original action.
- Script failure: retain input, reproduce on smallest record, fix cause, run focused test, then rerun full transform. Do not hand-rewrite large output to hide script failure.
- No live web access: repair connectivity/tool configuration when possible; otherwise request enablement or a supplied source. Never label stale data as current.
- Conflicting evidence or duplicate: retain sources, mark uncertain, and review before outreach; do not merge on name alone.
- Insufficient qualified leads: report count and searched coverage; never weaken gates without permission.
- Export failure: preserve canonical data; repair writer/runtime first, verify file opens, then use CSV or in-chat output only if repair fails.
- Interrupted run: resume from saved brief, ledger and source log without repeating completed work.

Report outcome, material coverage gap, and required user action only. Never dump long logs or claim recovery without the verification step.
