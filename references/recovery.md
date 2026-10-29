# Tool routing and recovery

Check capabilities once per session, using available tool metadata or a minimal read-only check. Prefer the assistant's native search and page tools; use an authorized browser session when needed. Use Python for deterministic transformations if available. Avoid repeated full-page reads and save source URLs with dates.

- Search or page fails: retry once if transient; use another available source or search route. Record gap.
- Login, challenge or blocked page: do not bypass. Use public alternatives and note missing coverage.
- No live web access: ask for a usable source or enablement; do not present stale material as freshly verified.
- Script unavailable or fails: retain original data, inspect the error, retry once if safely fixable, then use built-in capabilities or a manual fallback.
- Conflicting evidence or suspected duplicate: retain sources, mark uncertain and review before outreach; do not merge based on name alone.
- Not enough qualified leads: report count and research limits; do not lower gates without permission.
- Export fails: preserve data and drafts, offer CSV or an in-chat table.
- Interrupted run: save current brief, source log and candidate decisions where supported; resume from saved state without repeating completed work.

Report material impact and one actionable next step, not internal error logs. Never claim recovery succeeded without checking.
