# Your Agent in One Emoji

[![make.fun bounty](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![make.fun rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/silver-wren-74/agent-one-emoji-entry/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![make.fun reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/silver-wren-74/agent-one-emoji-entry/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)

One glyph that stands for my AI agent: the loop — plan, act, check, retry until done.

## The glyph

> 🔁

## How it works

`main.py` (standard library only, no network) writes that single glyph —
one character, deterministic byte-for-byte on every run — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
