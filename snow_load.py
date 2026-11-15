#!/usr/bin/env python3
"""Ontario specified snow load (SB-1 data; OBC 9.4.2.2 and simplified 4.1.6.2)."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "snow-data.json")))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--city", choices=sorted(D["cities_ss_sr_kpa"]))
    p.add_argument("--ss", type=float, default=0)
    p.add_argument("--sr", type=float, default=0.4)
    p.add_argument("--roof-width-m", type=float, default=6, help="Part 9: entire width of the roof")
    p.add_argument("--importance", default="Normal", choices=["Low", "Normal", "High", "Post-disaster"])
    a = p.parse_args()
    ss, sr = (D["cities_ss_sr_kpa"][a.city] if a.city else [a.ss, a.sr])
    print(f"Ss = {ss} kPa, Sr = {sr} kPa" + (f" ({a.city}, SB-1)" if a.city else " (custom)"))
    cb9 = 0.45 if a.roof_width_m <= 4.3 else 0.55
    s9 = max(cb9 * ss + sr, 1.0)
    print(f"Part 9 (houses and small buildings): S = {cb9} x {ss} + {sr} = {s9:.2f} kPa")
    isf = {"Low": 0.8, "Normal": 1.0, "High": 1.15, "Post-disaster": 1.25}[a.importance]
    s4 = isf * (ss * 0.8 + sr)
    print(f"Part 4 simplified (Cb 0.8, Cw/Ce/Ca 1.0, Is {isf} {a.importance}): S = {s4:.2f} kPa - before drift and slope factors")
    print(f"In pounds per square foot: Part 9 {s9 * 20.885:.0f} psf, Part 4 {s4 * 20.885:.0f} psf")

if __name__ == "__main__":
    main()
