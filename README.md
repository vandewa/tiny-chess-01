# tiny-chess-v1

A 4 KB chess engine in pure Python (stdlib only), built for the make.fun
tiny-chess-01 bounty: the strongest chess engine in 4 KB of Python.

`main.py` (4,081 bytes) is a 0x88 negamax engine: alpha-beta + PVS,
quiescence over captures/promotions/check replies, transposition table,
check extension, tapered PeSTO-style eval, fixed 50,000-node search —
deterministic, no clock, no randomness, no model calls.

It plays through the make.fun env protocol (`$MAKEFUN_ENV_URL`).

Practice results (kit grade-local, 3 trials): Elo 1,396 / 1,253 / 1,253,
mean 1,301 — above the 1,154 entry floor.
