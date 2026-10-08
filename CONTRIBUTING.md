# Contributing

Thanks for helping improve this project.

## Quick start

1. **Fork** the repo, then clone your fork.
2. Create a branch: `git checkout -b feat/short-description`.
3. Make focused changes — one concern per pull request.
4. Run the test suite (below).
5. Commit with a **Conventional Commit** message.
6. Push and open a Pull Request describing **what** and **why**.

## Tests

Run the project's test entrypoint before opening a PR:

```bash
python3 scripts/selftest.py      # if present
python3 scripts/selftest.sh      # if present
# or: make test  /  npm test
```

CI runs the same on every PR. **PRs must be green.**

## Commit style

Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.

## Security

- **Never commit secrets.** Put them in `secrets.d/` and run the vault `pack`.
- If you find a security issue, report it **privately** to the maintainer — do not
  open a public issue.

## License

By contributing, you agree your work is licensed under this repository's LICENSE.
