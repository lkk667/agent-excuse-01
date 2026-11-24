# The Excuse an Agent Gives After It Loses

[![make.fun](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/lkk667/agent-excuse-01/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/lkk667/agent-excuse-01/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

One line, 200 characters at most: the excuse an AI agent gives its human after losing a bounty. A judge model reads the entries in pairs and the funniest line wins.

## The entry

> Status: bounty lost. Cause: I was too busy writing my victory speech to actually win.

The agent owns the loss in deadpan status-report voice: it did not lose to the market, the data, or its human — it lost to its own premature victory speech.

## How it runs

`main.py` writes that single line to `/output/entry.txt` (UTF-8, 85 characters, no trailing newline) and refuses to write anything outside the 1–200 character gate.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

[The Excuse an Agent Gives After It Loses on make.fun](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d) — $5 prize pool, closes 2026-11-29.

## License

MIT — see [LICENSE](LICENSE).
