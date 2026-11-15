# Ontario Snow Load Calculator

Returns the specified snow load for Ontario municipalities using SB-1 ground snow (Ss) and rain (Sr) values, the OBC Part 9 formula (Article 9.4.2.2), and a simplified Part 4 uniform load (Article 4.1.6.2 with Cb 0.8 and Cw/Ce/Ca at 1.0).

**Live web tool:** https://dust2engineering.github.io/ontario-snow-load-calculator/web/

## How it works

- Part 9: S = Cb x Ss + Sr, Cb 0.45 / 0.55 by roof width, minimum 1.0 kPa.
- Part 4 simplified: S = Is (0.8 x Ss + Sr), Is by importance category; drift (Ca) and slope effects are separate design steps.

## Data in this repository

- snow-data.json — Ss and Sr for the listed municipalities, machine-readable.

## Command line

```bash
python3 snow_load.py --city Bracebridge --roof-width-m 6
```

## Worked examples

- [toronto-house-roof.md](examples/toronto-house-roof.md)
- [bracebridge-cottage-roof.md](examples/bracebridge-cottage-roof.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Structural. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
