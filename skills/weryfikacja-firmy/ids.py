#!/usr/bin/env python3
"""Walidacja sum kontrolnych: NIP, REGON (9/14), KRS (format), rachunek NRB/IBAN.
Użycie: python3 ids.py 5252674798 365331553 0000635012 PL44114011240000516508001061"""
import re, sys


def digits(s):
    return re.sub(r"\D", "", s)


def nip_ok(n):
    n = digits(n)
    if len(n) != 10:
        return False
    s = sum(int(a) * w for a, w in zip(n, (6, 5, 7, 2, 3, 4, 5, 6, 7))) % 11
    return s != 10 and s == int(n[9])


def regon_ok(r):
    r = digits(r)
    w = {9: (8, 9, 2, 3, 4, 5, 6, 7), 14: (2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8)}.get(len(r))
    if not w:
        return False
    return sum(int(a) * b for a, b in zip(r, w)) % 11 % 10 == int(r[-1])


def iban_ok(a):
    a = re.sub(r"\s", "", a).upper()
    if re.fullmatch(r"\d{26}", a):
        a = "PL" + a
    if not re.fullmatch(r"[A-Z]{2}\d{2}[A-Z0-9]{10,30}", a):
        return False
    x = "".join(str(int(ch, 36)) for ch in a[4:] + a[:4])
    return int(x) % 97 == 1


def classify(v):
    d = digits(v)
    if "KRS" in v.upper() or (len(d) == 10 and d[0] == "0"):  # NIP nigdy nie zaczyna się od 0
        return "KRS", 0 < len(d) <= 10, d.zfill(10)
    if re.search(r"[A-Za-z]{2}\d{2}", v.replace(" ", "")) or len(d) == 26:
        return "rachunek", iban_ok(v), "PL" + d if len(d) == 26 else re.sub(r"\s", "", v).upper()
    if len(d) == 14 and d.endswith("00000"):  # KRS zapisuje 9-cyfrowy REGON z dopełnieniem zerami
        d = d[:9]
    if len(d) == 10:
        return "NIP", nip_ok(d), d
    if len(d) in (9, 14):
        return "REGON", regon_ok(d), d
    return "nieznany", False, v


if __name__ == "__main__":
    for v in sys.argv[1:]:
        kind, ok, norm = classify(v)
        print(f"{v!r}: {kind} {'OK' if ok else 'BŁĘDNA SUMA KONTROLNA / FORMAT'} -> {norm}")
