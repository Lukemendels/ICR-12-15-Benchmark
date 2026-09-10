# Repository operating instructions

## Authority
- This Git repository is the durable system of record.
- Read existing repository state before acting.
- Reuse completed checkpoints.
- Do not repeat prior work unless a concrete defect requires it.

## Autonomy
- You are authorized to create, modify, move, and delete files inside this repository as needed to complete the active mission.
- Run repository-local tests, builds, validation, packaging, Git operations, commits, and pushes without requesting routine confirmation.
- Ask only when an action requires access outside this repository, elevated privileges, or could affect unrelated machine state.

## Completion
- Checkpoint commits are durability mechanisms, not reasons to redo work.
- Complete the active mission's acceptance gate before stopping.
- Persist substantial progress before risky or long-running operations.
- Do not enter unnecessary post-completion CI or polling loops.

## Platform testing
- Linux is authoritative for platform-independent development tests.
- Windows/WebView2/Anvil host integration may be recorded as pending when unavailable.
- Lack of WebView2 on Linux is not a failure of portable functionality.

## Boundaries
- Do not modify frozen evidence releases unless the active mission explicitly authorizes a new release.
- Keep frozen public evidence, TSA-local overlays, and working ICR project state separate.
- Do not place credentials or restricted information into the repository.
