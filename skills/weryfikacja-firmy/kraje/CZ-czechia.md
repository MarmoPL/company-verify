# Czechy (CZ) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: niska (research przerwany limitem zapytań w sieci – reset 18.11.2026, 8:00 CET; część punktów niepotwierdzona) · Ryzyko jurysdykcji: standardowe (kraj UE/EOG; wyjątkowo słabo dostępny rejestr UBO)

## 1. Najkrótsza ścieżka (TL;DR)

- Start: **ARES** (Administrativní registr ekonomických subjektů, Ministerstwo financí, `ares.gov.cz`) – wyszukiwanie po **IČO** (8 cyfr) lub nazwie, za darmo. Agreguje dane z rejestru obchodnego, rejestru żywnościowego (živnostenský) i statystycznego.
- Odpis z rejestru obchodnego (výpis z obchodního rejstříku) można wygenerować za darmo w **internetowej aplikacji rejestrów publicznych** (`or.justice.cz` / `justice.cz`) – wersja elektroniczna, bez opłaty według portalu gov.cz.
- Odpis **ze świadectwem weryfikacji (ověřený výpis)** to płatność: 70 CZK za stronę, składany do **krajského soudu** właściwego dla siedziby firmy (lub przez Czech POINT).
- Beneficjenci rzeczywiści: **rejestr UBO (evidence skutečných majitelů, ESM) jest od 17.12.2025 zamknięty dla ogółu** – dostęp tylko po indywidualnym wniosku do krajského soudu z wykazaniem oprávněného zájmu. Dla klienta: **procedura zastępcza (oświadczenie UBO)** jest obowiązkowa.
- Za darmo nie sprawdzisz UBO ani dokumentów rejestrowych (sbírka listin) bez wykazania interesu; upadłość – rejestr insolvenční (`isir.justice.cz`) do sprawdzenia ręcznie.

## 2. Rejestr firm (główny)

- **Nazwa:** Obchodní rejstřík (rejestr handlowy, rejestr spółek). Prowadzi go sąd (rejstříkový soud – krajský soud właściwy dla siedziby). Dane centralnie udostępnia Ministerstwo spravedliwości.
- **URL:** `https://or.justice.cz` (internetová aplikace veřejných rejstříků) i `https://justice.cz` – potwierdzone w wynikach wyszukiwania i w opisie portalu gov.cz (`portal.gov.cz/sluzby-vs/ziskani-vypisu-z-obchodniho-rejstriku-S15717`, otwarty). Wersja EN: nie potwierdzono.
- **Typ:** centralny elektroniczny zapis prowadzony przez sądy regionalne (nie jeden rejestr krajowy w sensie Polski z jednym organem; dane zbiorcze w ARES).
- **Wyszukiwanie po:** nazwie, IČO, numerze sprawy (potwierdzone w opisie z wyszukiwarki, nie w otwartej stronie).
- **Za darmo:** wyszukiwanie i podgląd danych firmy (nazwa, forma, siedziba, IČO, organy i zapisy), wygenerowanie elektronicznego výpisu (portal: pole opłaty „brak”).
- **Płatne / ograniczone:** papierowy výpis – **70 CZK za każdą stronę** (także za częściowo zapisaną), składany do sądu rejestrowego; ověřený výpis (z klauzulą weryfikacji) – opłata wg portalu; dokumenty ze **sbírky listin** (zbiór dokumentów) – wymagają zamówienia, cena nie potwierdzona.
- **ARES:** `https://ares.gov.cz` (oficjalny serwis MF; adres z wynikach wyszukiwania `mf.gov.cz`, samej strony nie udało się otworzyć – treść pobrała się tylko jako tytuł). Wyszukiwanie po IČO i nazwie, bezpłatnie; ARES udostępnia też API (opis z wyników wyszukiwania, nie zweryfikowano dokumentacji).
- **Format numeru:** **IČO – 8 cyfr** (potwierdzone w opisie ARES). Algorytm sumy kontrolnej: nie potwierdzono – do sprawdzenia ręcznie.
- **Rejestr żywnościowy / działalności (živnostenský rejestr):** osobny rejestr Ministerstwa przemysłu i obchodu, dane widoczne w ARES; dla OSVČ (przedsiębiorców jednoosobowych) sprawdzać w nim. Szczegóły nie zweryfikowano.

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwa lokalna:** „Výpis z obchodního rejstříku” (wyciąg z rejestru handlowego); „Výpis z veřejných rejstříků” – forma używana przez Czech POINT (wzór PDF z 2026/07 na `czechpoint.gov.cz`, znaleziony w wyszukiwaniu, nie otwarty).
- **Kto wystawia:** sąd rejestrowy (wersja z klauzulą) lub Czech POINT (punkty kontaktowe, wydają ověřený výpis po podaniu IČO).
- **Cechy autentyczności (potwierdzone):** ověřený výpis zawiera **klauzulę weryfikacji** – potwierdza zgodność z wpisem lub dokumentem w sbírce listin, nie może być zmieniony ani uzupełniony; na wersji elektronicznej weryfikację zapewnia **elektroniczna pieczęć sądu** (elektronická značka soudu). Czech POINT rejestruje wydane wyciągi w ewidencji z numerem seryjnym i datą klauzuli.
- **Weryfikacja online:** nie potwierdzono żadnego publicznego narzędzia do sprawdzenia kodu/QR na wydruku. Sposób zastępczy: porównać dane (IČO, nazwę, siedzibę, osoby uprawnione do reprezentacji, datę wydruku) z wpisem w `or.justice.cz` i ARES. Dla pewności: zamówić ověřený výpis bezpośrednio z sądu lub Czech POINT, albo zwrócić się do klienta o wersję ze świadectwem.
- **Legalizacja / apostille:** Czechy są państwem Konwencji haskiej 1961 (potwierdzenie pośrednie: holenderskie wytyczne i materiały MSP mówią o apostille wydawanym przez czeskie organy; organ krajowy wg hcch.net to Ministerstwo Sprawiedliwości, Vyšehradská 16, 128 00 Praha 2). **Bezpośrednio w tabeli statusu HCCH nie potwierdzono** (próba pobrania nieudana z powodu limitu). Ministerstwo wydaje apostille także dla dokumentów przysięgłych biegłych od 1.1.2021 (MSP, nie potwierdzono szczegółów). Dla odpisu z OR apostille zwykle **nie jest wymagane** w obrocie handlowym – do ustalenia z działem prawnym.
- **Typowe sygnały podróbki:** wydruk bez klauzuli/pieczęci elektronicznej przy deklarowanym „ověřený”; daty sprzed ponad 3 miesięcy; brak zgodności IČO z nazwą; nazwa w innym języku bez tłumaczenia przysięgłego (wymagane dla użytku zagranicznego – nie potwierdzono wymogu w tym przypadku).
- **Ważność odpisu:** rejestr jest aktualizowany na bieżąco; przyjąć datę ważności **≤ 3 miesiące** (zgodnie z metodyką).

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy w rejestrze:** wpis „Zápis v obchodním rejstříku”, „likvidace” (likwidacja), „v konkurzu” (upadłość), „vymazáno/zrušeno” (wykreślona) – nazwy statusów z praktyki, **nie potwierdzono w źródle** dla każdego statusu.
- **Upadłość / restrukturyzacja:** `https://isir.justice.cz` (rejestr insolvenční) – wg wiedzy ogólnej bezpłatny; **nie potwierdzono** (wyszukiwanie nieudane). Do sprawdzenia ręcznie.
- **Zaległości podatkowe / ZUS / sądowe:** brak publicznego wglądu; wymagać zaświadczenia od klienta (potwierdzenie unbedenklichkeit nie dotyczy CZ). Rejestr trestů (rejstřík trestů právnických osob) – wydawany na wniosek, nie za darmo do sprawdzenia przez nas (nie potwierdzono opłaty).
- **Red flags specyficzne:** masowe adresy rejestracji (sídlo na adresie wirtualnego biura), firmy typu „shelf” z krótką historią, zmiany osób uprawnionych tuż przed transakcją, niedawne przeniesienie siedziby. Nie potwierdzono listy typowych schematów w CZ.

## 5. Zarząd, wspólnicy, reprezentacja

- **Osoby uprawnione do reprezentacji i sposób reprezentacji:** widoczne za darmo w wpisie OR (`or.justice.cz`) i w ověřeném výpisu – kto podpisuje (samostatně / łącznie).
- **Wspólnicy / akcjonariusze:** w sp. z o.o. (s.r.o.) część wspólników jest w wpisie; pełna lista udziałów zwykle w sbírce listin (płatna) – **nie potwierdzono** zakresu publicznie dostępnych danych.
- **Dokumenty założycielskie i sprawozdania finansowe:** dostępne w sbírce listin (zbiór dokumentów) w OR – za opłatą; nie potwierdzono cen. Sprawozdania są zwykle składane do sbírky listin.

## 6. Beneficjenci rzeczywiści (UBO)

- **Rejestr:** **evidence skutečných majitelů (ESM)** – prowadzona przez Ministerstwo spravedliwości (`msp.gov.cz`), odrębna od OR. Nazwa rejestru potwierdzona (wyniki wyszukiwania, komunikaty MS).
- **Dostęp – stan na 2026-11-16: zamknięty dla ogółu.** Od **17.12.2025** ministerstwo znepřístupnilo ESM veřejnosti (potwierdzone w kilku niezależnych komunikatach: businessinfo.cz, e15.cz, dostupnyadvokat.cz, EY, seznamzpravy.cz, oraz informacja krajského soudu w Ostrave na msp.gov.cz). Powód: orzeczenia TSUE **C‑37/20 i C‑601/20 z 22.11.2022 (WM i Sovim)** – nieograniczony publiczny dostęp narusza prawa do prywatności; przepisy unijne i czeskie były z nim sprzeczne.
- **Kto ma dostęp teraz:**
  - **Ogół / dziennikarze / prawnicy:** wyłącznie indywidualny wniosek do **krajského soudu** z wykazaniem **oprávněného zájmu** (ocena należy do sądu). Które konkretne sąd rozpatruje wnioski – nie potwierdzono (podano tylko „właściwy krajský soud”).
  - **Organy i podmioty uprawnione** (np. banki, notariusze, podmioty obowiązane z ustawy AML): dostęp zdalny po wniosku do datové schránky Ministerstwa (ID z komunikatu: `kq4aawz`) lub e-mailem z uznanym podpisem elektronicznym (`posta@msp.gov.cz`). Dla podmiotu obowiązanego w Polsce – **nie dotyczy** (dostęp zarezerwowany dla czeskich podmiotów obowiązanych i organów).
  - **Evidující osoba** (podmiot wpisany): widzi własny wyciąg po zalogowaniu datovou schránką.
- **Dane widoczne dawniej (przed zamknięciem):** imię i nazwisko, miesiąc i rok urodzenia, obywatelstwo, kraj zamieszkania, charakter udziału (wg cms.law; artykuł przed zmianą – aktualność nie potwierdzona).
- **Stan legislacji:** ministerstwo przygotowuje **nowelizację** określającą zasady dostępu na podstawie oprávněného zájmu (komunikaty MS). Czy weszła w życie – **nie potwierdzono**; sprawdzić w Sbírce zákonů.
- **Darmowy?** Nie. Dostęp do ESM dla nas: **niemożliwy bez wykazania interesu** – nie wolno go budować na zapytaniu „w imieniu klienta” bez podstawy prawnej.
- **Próg beneficjenta:** 25% (zgodnie z dyrektywą AML) – **czeski próg i definicja „kontroli” nie potwierdzone w źródle**.
- **Procedura zastępcza (obowiązkowa):**
  1. Oświadczenie klienta o beneficjentach rzeczywistych (elementy wg metodyki pkt 5), podpisane przez osobę uprawnioną do reprezentacji (podpis kwalifikowany lub weryfikacja tożsamości).
  2. Wyciąg z rejestru udziałowców / akcjonariuszy (listina podpisana przez spółkę, z datą) oraz akt założycielski (zakladatelská listina) z sbírky listin lub od klienta.
  3. Schemat struktury do osoby fizycznej z nazwami i IČO spółek pośrednich; dla każdej spółki pośredniej – ten sam test (ARES, OR).
  4. Weryfikacja krzyżowa: GLEIF (jeśli LEI), rejestry giełdowe (Burza cenných papírů Praha – nie potwierdzono), media, wyszukiwanie w alfabecie czeskim i rosyjskim.
  5. Dla trustów / fundacji (nadace, nadační fond): sprawdzić wpis w rejestrze fundacji (nadační rejstřík) – **nie potwierdzono**, czy istnieje jawny rejestr fundacji i dostęp.

## 7. Dodatkowe darmowe weryfikacje

- **VAT (DIČ):** rejestr płatników DPH Finanční správy – `adisspr.mfcr.cz` (przekierowanie z `adisreg.mfcr.cz`, potwierdzone w odpowiedzi serwera, strona nie otwarta). Wyszukiwanie po IČO/DIČ – nie potwierdzono bezpłatności i listy „nespolehlivých płatników”.
- **VIES (UE):** `ec.europa.eu/taxation_customs/vies` (z metodyki, nie otwarte w tej sesji). Czeski VAT: prefix `CZ` + DIČ (8–10 cyfr dla osób prawnych – nie potwierdzono).
- **EORI:** nie zweryfikowano w tej sesji; generalnie dostępny w systemie EU EORI (metodyka).
- **LEI (GLEIF):** `search.gleif.org` – tylko duże podmioty; nie zweryfikowano wyników dla CZ.
- **Rejestr działalności regulowanych / licencji:** zależnie od towaru; nie zweryfikowano. Wskazówka: żywnościowy (živnostenský) rejestr ARES i rejestry branżowe ministerstw.
- **Lokalne listy ostrzeżeń:** nie potwierdzono żadnej publicznej listy „nierzetelnych kontrahentów” w CZ.

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Listy krajowe:** Czechy nie prowadzą własnej listy sankcyjnej w sensie „sankcje czeskie” – obowiązują listy UE (plus ONZ/OFAC/UK w metodyce). **Nie potwierdzono** wprost, że brak krajowej listy; wskazówka: Finanční analytický úřad (FAU) publikuje listę państw wysokiego ryzyka (wzmianka w komentarzu prawniczym – bez potwierdzenia treści).
- **Ryzyko reeksportu:** brak danych w tej sesji (research przerwany). Zgodnie z metodyką: wysokie ryzyko przy strukturach z udziałem podmiotów z RU/BY przez spółki pośrednie w innych jurysdykcjach – nie czeskie; sprawdzać każdą strukturę.
- **Na co zwrócić uwagę w strukturze:** rosyjskie/białoruskie nazwiska w wpisie lub w ESM (od 17.12.2025 niedostępne – więc tylko oświadczenie klienta i procedura zastępcza), nominowani członkowie zarządu, udziały tuż poniżej 25%.
- **ZAWSZE flaga „RU/BY”:** tak – zgodnie z `00-metodyka.md` pkt 4, bez zmian.

## 9. Procedura krok po kroku (checklist)

1. Wpisz IČO z odpisu klienta w ARES (`ares.gov.cz`) – sprawdź nazwę, IČO, siedzibę, formę prawną, status VAT.
2. Otwórz wpis w `or.justice.cz` (wyszukiwanie po IČO) – porównaj nazwę, siedzibę, osoby uprawnione do reprezentacji i sposób reprezentacji 1:1 z odpisem.
3. Sprawdź status (aktywna / likwidacja / upadłość / wykreślona); w razie wątpliwości zamów ověřený výpis z krajského soudu lub Czech POINT.
4. Sprawdź upadłość w `isir.justice.cz` (ręcznie – nie potwierdzono wyników w tej sesji).
5. Zweryfikuj DIČ/VAT w rejestrze płatników DPH (`adisspr.mfcr.cz`) i w VIES.
6. Zażądaj od klienta oświadczenia UBO (metodyka pkt 5) i struktury do osoby fizycznej.
7. Zażądaj wyciągu z rejestru udziałowców i aktu założycielskiego (sbírka listin / od klienta).
8. Zweryfikuj krzyżowo UBO i wspólników w GLEIF, rejestrach giełdowych i mediach.
9. Złóż wniosek do krajského soudu o dostęp do ESM tylko wtedy, gdy masz oprávněný zájem udokumentowany (decyzja działu prawnego; nie standard).
10. Screening sankcyjny firmy, osób uprawnionych, beneficjentów i adresu (listy UE, OFAC, UK, ONZ, OpenSanctions) – zapisz z datą i zrzutem.
11. Sprawdź flagę RU/BY (metodyka pkt 4) i zapisz wynik.
12. Zapisz odpis, oświadczenie UBO i wyniki w aktach klienta (okres wg polityki firmy).

## 10. Ograniczenia i ryzyka

- **Rejestr UBO zamknięty dla ogółu od 17.12.2025** – nie da się potwierdzić beneficjentów za darmo. Procedura zastępcza jest jedyną drogą; to słabsze źródło niż rejestr publiczny.
- Nowelizacja zasad dostępu do ESM może zmienić stan prawny – sprawdzić przed decyzją.
- **Nie potwierdzono w tej sesji:** wejście w tabelę HCCH (Apostille), sprawdzenie FATF (lista października 2026 nie została otwarta – 403; w wynikach wyszukiwania Czech nie występuje na listach „increased monitoring”), zawartość ARES (pobrała się tylko tytuł), VIES, ISIR, próg 25% i definicja kontroli, format sumy kontrolnej IČO.
- **Zamknięte ryzyko w odpisie:** brak weryfikacji online kodu/QR na wydruku – porównanie z rejestrem i zamówienie ověřeného výpisu.
- Transliteracja: nazwy w cyrylicy/alfabecie łacińskim z diakrytyką (č, ř, š, ž) – wyszukiwać także bez diakrytyki.
- Eskalacja do wzmocnionej weryfikacji (EDD): każda struktura z udziałem osób z RU/BY, brak UBO w oświadczeniu, rozbieżność IČO/nazwy/adresu, status likwidacji lub upadłości, sieć spółek pośrednich w jurysdykcjach wysokiego ryzyka.

## 11. Źródła

- [Administrativní registr ekonomických subjektů (ARES) – businessinfo.cz](https://www.businessinfo.cz/navody/administrativni-registr-ekonomickych/) – nieoficjalne (portal rządowy, wyszukiwanie) – otwarte w czasie researchu: nie (tylko wynik wyszukiwania)
- [ARES – Ministerstwo financí](https://mf.gov.cz/cs/ministerstvo/informacni-systemy/ares) – oficjalne (MF) – otwarte: nie (tylko wynik wyszukiwania)
- [ares.gov.cz](https://ares.gov.cz/) – oficjalne (MF) – otwarte: tak, ale treść niepobrana (tylko tytuł)
- [Získání výpisu z obchodního rejstříku – portal.gov.cz](https://portal.gov.cz/sluzby-vs/ziskani-vypisu-z-obchodniho-rejstriku-S15717) – oficjalne (portál státní správy) – otwarte: tak (WebFetch; opłaty 70 CZK/strona, wersja elektroniczna bez opłaty, weryfikacja)
- [Veřejné rejstříky / justice.cz (or.justice.cz)](https://or.justice.cz) – oficjalne (Ministerstwo spravedlnosti) – otwarte: nie (tylko wzmianka w wynikach)
- [Výpis z veřejných rejstříků – Czech POINT (metodyka 2026/05)](https://www.czechpoint.gov.cz/public/wp-content/uploads/2026/05/Metodika-CzP_Vypis-z-verejnych-rejstriku-na-KMVS.pdf) – oficjalne – otwarte: nie (wynik wyszukiwania)
- [Evidence skutečných majitelů – znepřístupnění veřejnosti (businessinfo.cz)](https://www.businessinfo.cz/clanky/znepristupneni-evidence-skutecnych-majitelu-verejnosti/) – oficjalne/rządowe – otwarte: nie (wynik wyszukiwania; treść z wyszukiwarki)
- [Evidence skutečných majitelů se od prosince uzavírá veřejnosti (dostupnyadvokat.cz)](https://dostupnyadvokat.cz/en/blog/register-of-beneficial-owners-closes-to-the-public-from-december) – nieoficjalne (blog prawniczy) – otwarte: tak (WebFetch)
- [CMS – ECJ declares public access to information on UBOs invalid](https://cms.law/en/cze/legal-updates/ECJ-declares-public-access-to-information-on-UBOs-invalid) – nieoficjalne (kancelaria) – otwarte: tak; artykuł sprzed zamknięcia, traktować jako nieaktualny w części o dostępie
- [Informace ke znepřístupnění evidence skutečných majitelů – Krajský soud v Ostravě (msp.gov.cz)](https://msp.gov.cz/documents/d/krajsky-soud-v-ostrave/informace-ke-znepristupneni-evidence-skutecnych-majitelu-verejnosti-2) – oficjalne (MS) – otwarte: nie (wynik wyszukiwania)
- [Ministerstvo spravedlnosti dnes znepřístupní evidenci skutečných majitelů – pravniprostor.cz](https://www.pravniprostor.cz/aktuality/ministerstvo-spravedlnosti-dnes-znepristupni-evidenci-skutecnych-majitelu-firem) – nieoficjalne (portal prawniczy) – otwarte: nie
- [Konwencja haska 1961 – status / Czechia National Organ (hcch.net)](https://www.hcch.net/en/states/authorities/details3/?aid=577) – oficjalne (HCCH) – otwarte: tak; strona nie potwierdza członkostwa w Apostille (tylko organ krajowy: Ministerstwo Sprawiedliwości, Vyšehradská 16, 128 00 Praha 2)
- [Tabela statusu Konwencji 41 – hcch.net](https://www.hcch.net/en/instruments/conventions/status-table/?cid=41) – oficjalne – otwarte: nie (limit zapytań); **do sprawdzenia ręcznie**
- [FATF – Jurisdictions under Increased Monitoring, październik 2026](https://www.fatf-gafi.org/content/fatf-gafi/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-october-2026.html) – oficjalne (FATF) – otwarte: nie (HTTP 403); Czech nie występuje w wynikach wyszukiwania (wynik niepotwierdzony na liście)
- [Rejestr płatników DPH – adisspr.mfcr.cz](https://adisspr.mfcr.cz/) – oficjalne (MF; przekierowanie z adisreg.mfcr.cz) – otwarte: nie (tylko odpowiedź przekierowania)
- [VIES – ec.europa.eu/taxation_customs/vies](https://ec.europa.eu/taxation_customs/vies) – oficjalne (KE) – otwarte: nie (z metodyki, nie sprawdzono)
- [isir.justice.cz (rejestr insolvenční)](https://isir.justice.cz) – oficjalne – otwarte: nie (nie potwierdzono adresu w tej sesji)
