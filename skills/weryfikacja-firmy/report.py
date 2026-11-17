#!/usr/bin/env python3
"""Raport weryfikacji kontrahenta -> PDF. Użycie: python3 report.py dane.json raport.pdf"""
import json, sys, os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, PageBreak, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xml.sax.saxutils import escape

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

ss = getSampleStyleSheet()
N = ParagraphStyle("n", parent=ss["Normal"], fontName="DV", fontSize=8.5, leading=11)
S = ParagraphStyle("s", parent=N, fontSize=7, leading=9, textColor=colors.HexColor("#555555"))
H1 = ParagraphStyle("h1", parent=N, fontName="DVB", fontSize=15, leading=19, spaceAfter=4)
H2 = ParagraphStyle("h2", parent=N, fontName="DVB", fontSize=11, leading=14, spaceBefore=10, spaceAfter=4)
VERDICT = {"POTWIERDZONA": ("#1e7d32", "FIRMA POTWIERDZONA"),
           "POTWIERDZONA_Z_UWAGAMI": ("#b26a00", "FIRMA ISTNIEJE – SĄ UWAGI"),
           "NIEPOTWIERDZONA": ("#b71c1c", "NIE POTWIERDZONO / RYZYKO")}
STATUS = {"OK": "#1e7d32", "UWAGA": "#b26a00", "BLAD": "#b71c1c", "BRAK": "#777777"}


def p(t, st=N):
    return Paragraph(escape(str(t if t is not None else "–")).replace("\n", "<br/>"), st)


def link(url, label=None):
    if not url:
        return p("–")
    return Paragraph(f'<link href="{escape(url)}" color="blue">{escape(label or url)}</link>', S)


def grid(rows, widths, head=True):
    t = Table(rows, colWidths=widths, repeatRows=1 if head else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#bbbbbb")),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    if head:
        st.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")))
    t.setStyle(TableStyle(st))
    return t


def build(data, out):
    W = A4[0] - 30 * mm
    c = data.get("company", {})
    story = [p("Raport weryfikacji kontrahenta", H1),
             p(f"Data i godzina weryfikacji: {data.get('checked_at', '–')}  •  "
               f"Dane wejściowe: {data.get('input_source', '–')}", S), Spacer(1, 6)]

    col, label = VERDICT.get(data.get("verdict"), ("#555555", data.get("verdict", "–")))
    vt = Table([[Paragraph(f'<font name="DVB" size="12" color="white">{escape(label)}</font>', N)],
                [Paragraph(f'<font color="white">{escape(data.get("verdict_note", ""))}</font>', N)]],
               colWidths=[W])
    vt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(col)),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story += [vt, Spacer(1, 4)]

    disc = data.get("discrepancies", [])  # najważniejsze na początku
    story.append(p("Rozbieżności i sygnały ryzyka", H2))
    if disc:
        rows = [[p(h, S) for h in ("Pole", "W dokumencie / podane", "W rejestrze", "Waga")]]
        for d in disc:
            rows.append([p(d.get("field")), p(d.get("document")), p(d.get("registry")), p(d.get("severity"))])
        story.append(grid(rows, [W * 0.18, W * 0.32, W * 0.36, W * 0.14]))
    else:
        story.append(p("Nie stwierdzono rozbieżności."))

    story.append(p("Dane rejestrowe", H2))
    keys = [("name", "Nazwa"), ("legal_form", "Forma prawna"), ("country", "Kraj"), ("nip", "NIP"),
            ("krs", "KRS"), ("regon", "REGON"), ("company_number", "Nr rejestrowy (zagr.)"),
            ("vat_eu", "VAT UE"), ("lei", "LEI"), ("address", "Adres siedziby"),
            ("registered_on", "Data rejestracji"), ("status", "Status w rejestrze"),
            ("capital", "Kapitał"), ("vat_status", "Status VAT")]
    rows = [[p(lbl, S), p(c[k])] for k, lbl in keys if c.get(k)]
    if rows:
        story.append(grid(rows, [38 * mm, W - 38 * mm], head=False))

    if data.get("representatives") or data.get("representation_method"):
        story.append(p("Reprezentacja", H2))
        if data.get("representation_method"):
            story.append(p("Sposób reprezentacji: " + data["representation_method"]))
            story.append(Spacer(1, 3))
        reps = [[p("Osoba", S), p("Funkcja", S)]] + [[p(r.get("name")), p(r.get("function"))]
                                                      for r in data.get("representatives", [])]
        if len(reps) > 1:
            story.append(grid(reps, [W * 0.45, W * 0.55]))
    if data.get("shareholders"):
        story.append(p("Wspólnicy / akcjonariusze", H2))
        sh = [[p("Podmiot / osoba", S), p("Udziały", S)]] + [[p(s.get("name")), p(s.get("shares"))]
                                                            for s in data["shareholders"]]
        story.append(grid(sh, [W * 0.45, W * 0.55]))

    story.append(p("Beneficjenci rzeczywiści (odbiorcy końcowi)", H2))
    story.append(p("Źródło: " + data.get("ubo_source", "–"), S))
    ubo = data.get("beneficial_owners", [])
    if ubo:
        rows = [[p(h, S) for h in ("Imię i nazwisko", "Obywatelstwo / zamieszkanie", "Charakter kontroli", "PESEL / ur.")]]
        for b in ubo:
            rows.append([p(b.get("name")), p(f"{b.get('citizenship', '–')} / {b.get('residence', '–')}"),
                         p(b.get("control")), p(b.get("pesel_masked") or b.get("born"))])
        story.append(grid(rows, [W * 0.24, W * 0.2, W * 0.4, W * 0.16]))
    else:
        story.append(p(data.get("ubo_note", "Brak danych o beneficjentach.")))

    story.append(p("Źródła i identyfikatory zapytań", H2))
    rows = [[p(h, S) for h in ("Źródło", "Wynik", "Szczegóły", "ID zapytania / czas", "Link")]]
    for s in data.get("sources", []):
        stc = STATUS.get(s.get("status"), "#555555")
        rows.append([p(s.get("name")),
                     Paragraph(f'<font name="DVB" color="{stc}">{escape(s.get("status", "–"))}</font>', N),
                     p(s.get("summary")), p(" ".join(x for x in (s.get("request_id"), s.get("timestamp")) if x) or "–", S),
                     link(s.get("url"), s.get("url_label", "otwórz"))])
    story.append(grid(rows, [W * 0.17, W * 0.09, W * 0.4, W * 0.2, W * 0.14]))

    if data.get("official_documents"):
        story.append(p("Pobrane dokumenty urzędowe", H2))
        for d in data["official_documents"]:
            story.append(p(f"• {d.get('name')} — {d.get('where', '')}"))
    if data.get("notes"):
        story.append(p("Uwagi", H2))
        for n in data["notes"]:
            story.append(p("• " + n))

    shots = [s for s in data.get("screenshots", []) if os.path.exists(s.get("path", ""))]
    if shots:
        story.append(PageBreak())
        story.append(p("Załączniki – zrzuty ekranu z rejestrów", H2))
        for s in shots:
            img = Image(s["path"])
            ratio = img.imageHeight / float(img.imageWidth)
            w = min(W, 160 * mm)
            h = w * ratio
            if h > 112 * mm:  # dwa zrzuty na stronę
                h, w = 112 * mm, 112 * mm / ratio
            img.drawWidth, img.drawHeight = w, h
            story.append(KeepTogether([p(s.get("caption", ""), S), Spacer(1, 2), img, Spacer(1, 8)]))

    def footer(cv, doc):
        cv.saveState()
        cv.setFont("DV", 6.5)
        cv.setFillColor(colors.HexColor("#777777"))
        cv.drawString(15 * mm, 10.5 * mm, "Raport pomocniczy na podstawie danych z rejestrów publicznych w chwili weryfikacji.")
        cv.drawString(15 * mm, 7.5 * mm, "Moc dokumentu urzędowego mają wyłącznie dokumenty pobrane bezpośrednio z rejestrów.")
        cv.drawRightString(A4[0] - 15 * mm, 7.5 * mm, f"str. {doc.page}")
        cv.restoreState()

    SimpleDocTemplate(out, pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=14 * mm,
                      bottomMargin=16 * mm, title="Weryfikacja: " + str(c.get("name", "")),
                      ).build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build(json.load(open(sys.argv[1], encoding="utf-8")), sys.argv[2])
    print("OK ->", sys.argv[2])
