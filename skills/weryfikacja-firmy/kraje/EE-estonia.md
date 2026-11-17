# Estonia (EE) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia (rejestr handlowy i apostille potwierdzone w źródłach otwartych; dostęp do UBO i cennik – niska, źródła sprzeczne, do sprawdzenia ręcznie) · Ryzyko jurysdykcji: podwyższone (program e-Residency, udokumentowane zastrzeżenia AML; nie „zakaz”)

Uwaga o zakresie researchu: limit wyszukiwań/pobrań został wyczerpany w trakcie pracy (reset 18.11.2026). Część stron (ariregister.rik.ee – cennik, rik.ee, FATF, fin.ee – PDF) nie została otwarta lub zwróciła 403/404. Wszystko, czego nie potwierdzono, jest oznaczone „nie potwierdzono – do sprawdzenia ręcznie”.

## 1. Najkrótsza ścieżka (TL;DR)

- **Rejestr:** e-äriregister (Äriregister, e-Business Register) pod adresem `https://ariregister.rik.ee/eng` (wersja angielska istnieje). Wyszukiwanie po nazwie lub kodzie rejestrowym (registry code) jest dostępne w trybie „Quick search”; „Detailed search” pozwala szukać także osób prywatnych.
- **Za darmo (wg źródeł wtórnych, do potwierdzenia):** wyszukanie firmy i odczyt wpisu publicznego bez logowania. Podstawowe dane: kod rejestrowy, nazwa (także historyczne), status, forma prawna, adres siedziby, data wpisu.
- **Nie za darmo / za logowaniem:** strony oznaczone kłódką na portalu (dashboard, zgłoszenia, rejestracja, bulk query), wyszukiwania rozszerzone dla klientów umownych, certyfikowane wyciągi. **Cen nie potwierdzono** – cennik jest pod linkiem „Price list” (`ariregister.rik.ee/eng/pricelist`), którego nie udało się otworzyć.
- **Odpis od klienta:** sprawdź go z wpisem w rejestrze po kodzie rejestrowym. Estonia jest w Konwencji haskiej 1961 (apostille) – potwierdzone (sekcja 3).
- **Beneficjenci rzeczywiści (UBO):** portal wskazuje dział „beneficial owners” (dane BO spółek). **Status dostępu sprzeczny w źródłach** – część mówi o publicznym dostępie za darmo, część o ograniczeniu do osób z uzasadnionym interesem (sekcja 6). Traktuj jako niepewne do ręcznego sprawdzenia.
- **Czego za darmo nie ma (pewnie):** pełnego zestawu danych UBO bez ograniczeń, certyfikowanych wyciągów, ani oceny kondycji finansowej firmy (rejestr pokazuje status formalny).

## 2. Rejestr firm (główny)

- **Nazwa rejestru:** Äriregister (e-äriregister, e-Business Register). Organ prowadzący: **Registrite ja Infosüsteemide Keskus (RIK – Centrum Rejestrów i Systemów Informacyjnych)** działające pod nadzorem Ministerstwa Sprawiedliwości (wg źródła wtórnego: abiinfo.rik.ee / topograph – potwierdzenie na stronie RIK nie udało się).
- **URL oficjalny:** `https://ariregister.rik.ee/eng` – otwarte w researchu. Strona informacyjna `https://abiinfo.rik.ee/en/e-business-register-queries` – otwarta.
- **Język:** estoński; **wersja angielska jest** (strona `/eng`).
- **Typ rejestru:** centralny, prowadzony centralnie przez RIK (nie sądowy regionalny). Obejmuje wszystkie osoby prawne zarejestrowane w Estonii, dane aktualne i historyczne.
- **Wyszukiwanie po:** nazwie lub kodzie rejestrowym (Quick search). Wyszukiwanie szczegółowe (Detailed search) – także po osobie prywatnej, wg strony „including a private person”. Wyszukiwanie po branży i lokalizacji – wg wtórnych opisów API, nie potwierdzono na stronie.
- **Za darmo (wg źródeł wtórnych, do potwierdzenia):** kod rejestrowy, nazwa, status rejestracyjny, forma prawna, adres siedziby, kod pocztowy, historia nazw.
- **Płatne / za logowaniem:** strona portalu oznacza kłódką: Dashboard, Submission of a report, Establishment, Bulk query, Artistic associations. Wyszukiwania rozszerzone, wpis z rozbudowanymi funkcjami, wizualizacja rejestru i usługa XML (API) są przeznaczone dla **klientów umownych** (abiinfo.rik.ee). **Ceny nie potwierdzono.**
- **Podpisy w portalu:** wnioski i zgłoszenia podpisuje się wyłącznie estońskim dowodem osobistym, Smart-ID lub mobile-ID (ariregister.rik.ee/eng). Cudzoziemiec bez e-Residency nie złoży tu zgłoszenia.
- **Format numeru:** kod rejestrowy (registry code) – 8 cyfr (zgodnie z wtórnymi opisami; nie potwierdzono na oficjalnej stronie formatu). Sprawdzenie poprawności: wyszukaj kod w rejestrze; brak potwierdzonej sumy kontrolnej.
- **Dane historyczne:** dostępne (potwierdzone na stronie RIK: „valid and historical information”).

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwa lokalna:** „äriregistri väljavõte” (wyciąg z rejestru handlowego); wydruk z portalu to „registrikaart” (karta rejestrowa) – nazwy do potwierdzenia na wzorcowym dokumencie.
- **Kto wystawia:** RIK (e-Business Register) jako wyciąg certyfikowany lub wydruk z portalu.
- **Cechy autentyczności:** nie potwierdzono szczegółów (kod weryfikacyjny, QR, podpis cyfrowy na wyciągu) – wymaga okazu wzorcowego.
- **Weryfikacja online:** najpewniej przez wyszukanie firmy po kodzie rejestrowym w `ariregister.rik.ee/eng` i porównanie nazwy, adresu, statusu i reprezentantów 1:1 z odpisem. Nie potwierdzono istnienia publicznego sprawdzenia kodu z wyciągu.
- **Apostille:** Estonia jest stroną **Konwencji haskiej z 5.10.1961** (zniesienie wymogu legalizacji). Wg tabeli statusu HCCH: przystąpienie 11.12.2000, wejście w życie **30.09.2001** – potwierdzone (`hcch.net`, tabela statusu, cid=41). Wystarczy apostille, bez legalizacji. Czy Estonia prowadzi e-Apostille: **nie potwierdzono**.
- **Sygnały podróbki / nieaktualności:** nie potwierdzono listy cech dla estońskich wyciągów. Rozbieżność nazw, adresu lub reprezentantów względem rejestru jest sygnałem alarmowym sama w sobie.
- **Aktualność odpisu:** przyjmij ważność nie dłuższą niż 3 miesiące (zasada z metodyki); przed decyzją porównaj z rejestrem online w dniu weryfikacji.

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy w rejestrze:** nie potwierdzono pełnej listy statusów z oficjalnej strony (strona RIK nie została otwarta). Do sprawdzenia ręcznie: aktywna / w likwidacji / po upadłości / wykreślona.
- **Upadłość i restrukturyzacja:** portal wymienia bazę „prohibitions on business and entrepreneurship” (zakazy prowadzenia działalności) i zaległości podatkowe (`ariregister.rik.ee/eng`). Osobny rejestr upadłościowy (insolvency register, Estonia) – **nie potwierdzono** nazwy i adresu.
- **Zaległości podatkowe:** portal deklaruje dane o zaległościach podatkowych („information on tax arrears”) – szczegóły dostępu i ceny nie potwierdzone.
- **Red flags specyficzne dla Estonii (ostrożnie, do potwierdzenia):**
  - Firmy zakładane zdalnie przez nierezydentów z e-Residency (sekcja 10 i 8) – to główne źródło zastrzeżeń AML wobec kraju (dane sprzed 2022, patrz źródła).
  - Adres siedziby będący wirtualnym biurem / adresem rejestracyjnym bez działalności.
  - Brak lokalnego rachunku bankowego lub rachunek w banku z innej jurysdykcji – banki estońskie często wymagają osobistego spotkania z przedstawicielem, co utrudnia nierezydentom.
  - Działalność w sektorach o podwyższonym ryzyku: kryptowaluty / usługi wirtualnych walut (rejestracja VASP była przedmiotem zmian prawnych; szczegóły nie potwierdzone).
  - Brak obecności operacyjnej (zatrudnienie, sprawozdania, historia finansowa) przy dużej aktywności handlowej.

## 5. Zarząd, wspólnicy, reprezentacja

- **Osoby reprezentujące i sposób reprezentacji:** dostępne w wpisie w rejestrze (wg źródeł wtórnych i struktury portalu) – nie potwierdzono na konkretnym wpisie w researchu. Sprawdź „management board” / reprezentację w karcie firmy.
- **Wspólnicy / akcjonariusze:** w estońskim rejestrze zwykle dostępni (wg źródeł wtórnych) – nie potwierdzono zakresu darmowego ani czy udziały są widoczne publicznie bez opłaty.
- **Dokumenty założycielskie i sprawozdania finansowe:** dokumenty rejestrowe (m.in. statut / articles of association) dostępne przez portal; ich odpłatność **nie potwierdzono** (cennik nieotwarty). Sprawozdania roczne są składane do rejestru – czy są darmowe, nie potwierdzono.
- **Uwaga:** dane zarządu w rejestrze to to, co zgłosiła firma. Przy nierezydentach z e-Residency reprezentantem bywa osoba zdalna lub nominalna – traktuj to jako punkt do weryfikacji (sekcja 6), nie jako dowód rzeczywistej kontroli.

## 6. Beneficjenci rzeczywiści (UBO)

- **Rejestr:** Estonia **nie prowadzi osobnego rejestru UBO** w rozumieniu odrębnej bazy – dane beneficjentów są zintegrowane z e-Äriregister (wg wtórnego źródła topograph / ecovis; nie potwierdzono na oficjalnej stronie RIK). Portal wymienia „beneficial owners of legal entities” wśród swoich baz (`ariregister.rik.ee/eng`, potwierdzone).
- **Dostęp – STATUS SPRZECZNY, NIE POTWIERDZONO:**
  - Część źródeł (ecovis, kyckr) podaje, że dane UBO są publiczne i dostępne za darmo w e-Äriregister.
  - Inne (topograph, kyckr – część prawna) podają, że po wyroku TSUE z 22.11.2022 (C‑37/20 i C‑601/20) dostęp został **ograniczony** do organów, podmiotów obowiązanych AML i osób wykazujących uzasadniony interes.
  - Oficjalna strona portalu wspomina o zmianie („Change in access to beneficial ownership data”) – treść tej zmiany nie została otwarta.
  - Na stronie abiinfo.rik.ee w menu jest sekcja „Beneficial owners” z podstronami: przeglądanie danych BO oraz **wniosek o dostęp na podstawie uzasadnionego interesu (legitimate interest) – jednorazowe zapytanie**. To potwierdza, że dostęp przez uzasadniony interes istnieje; kryteria i cena nie zostały potwierdzone.
  - **Wniosek: traktuj UBO jako dane ograniczone** (do ręcznego sprawdzenia przed decyzją) i przyjmij procedurę zastępczą (sekcja 9).
- **Darmowość i zakres danych:** nie potwierdzono. Wtórne źródła wspominają opłatę 1 EUR z dawnego okresu wdrożenia – uznaj za nieaktualną, nie potwierdzoną.
- **Próg beneficjenta:** unijny próg 25% wynika z dyrektywy AML; **wartość w estońskiej ustawie (MLTFPA) i definicję „kontroli” – nie potwierdzono – do sprawdzenia ręcznie.**
- **Trusty i fundacje:** Estonia nie uznaje trustów jako podmiotów w rozumieniu prawa krajowego; fundacje (sihtasutus) są rejestrowane – zasady jawności nie potwierdzono.

## 7. Dodatkowe darmowe weryfikacje

- **VAT (KMKR / VIES):** numer estoński zaczyna się od „EE” + 9 cyfr. Sprawdzenie w **VIES** (`ec.europa.eu/taxation_customs/vies`) – narzędzie unijne, nie otwarte w researchu; potwierdzenie „ważny/nieważny” i ewentualnie nazwa/adres zależnie od państwa. Krajowy rejestr podatkowy (Maksu- ja Tolliamet, MTA) – nie potwierdzono zakresu sprawdzenia online.
- **EORI:** nie potwierdzono wyszukiwania krajowego; użyj unijnej walidacji EORI (Komisja Europejska), jeśli dotyczy.
- **LEI (GLEIF):** zwykle tylko duże firmy – `search.gleif.org` (narzędzie z metodyki, nie otwarte w researchu).
- **Rejestr działalności regulowanych:** nie sprawdzono; zależy od towaru (np. alkohol, leki, broń – licencje innymi rejestrami).
- **Lokalne listy ostrzeżeń:** nie potwierdzono istnienia publicznej listy ostrzeżeń nadzoru finansowego (Finantsinspektsioon) – do sprawdzenia ręcznie.
- **Zakazy prowadzenia działalności:** portal wymienia je wśród danych (`ariregister.rik.ee/eng`, potwierdzone).
- **Członkowie partii politycznych:** portal wymienia listy członków partii (potwierdzone), przydatne do screeningu PEP.

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Ryzyko Estonii jako pośrednika:** najczęściej opisywany problem to program **e-Residency** i zdalne zakładanie spółek przez nierezydentów, w tym z krajów wysokiego ryzyka. Źródła prasowe (ERR, Bloomberg 2020, intellinews) opisują powiązania części spółek z oszustwami krypto i praniem pieniędzy – dane z lat 2019–2022.
- **Stanowisko krajowe:** Estońska jednostka FIU i ministerstwo finansów przyznawały, że usługa niesie realne ryzyko prania pieniędzy i finansowania terroryzmu (źródła: ERR / e-resident.gov.ee – wypowiedzi różnią się co do skali). Moneyval (Rada Europy) krytykował program (ERR, sierpień 2020–2022 – data nie potwierdzona w otwartym dokumencie).
- **Ograniczenia krajów:** wzmianka o projekcie ograniczenia e-Residency dla krajów wysokiego ryzyka AML – **nie potwierdzono, czy przepisy weszły w życie**.
- **Na co zwrócić uwagę w strukturze właścicielskiej:**
  - Udziały lub kontrola przez osoby z RU/BY (obywatelstwo, adres, transliteracja rosyjska).
  - Spółki estońskie z wieloma nominalnymi dyrektorami/wspólnikami z różnych krajów, zwłaszcza zakładane zdalnie przez e-Residency.
  - Zmiana właściciela po 24.02.2022.
  - Struktura pośrednia przez jurysdykcje wysokiego ryzyka (Cypr, ZEA, Turcja, Hongkong itd. – wg metodyki).
- **Krajowe listy sankcyjne:** Estonia stosuje sankcje UE; własnych rozszerzeń krajowych listy nie potwierdzono.
- **Oznacz zawsze flagą „RU/BY”:** każdy przypadek z beneficjentem/reprezentantem z RU/BY (zgodnie z `00-metodyka.md`, pkt 4).

## 9. Procedura krok po kroku (checklist)

1. Zapisz od klienta: nazwę, kod rejestrowy (8 cyfr wg źródeł wtórnych), adres, odpis z rejestru (≤ 3 miesiące), dane reprezentantów.
2. Otwórz `https://ariregister.rik.ee/eng`, wyszukaj po kodzie rejestrowym. Porównaj nazwę, formę prawną, adres, status i reprezentantów 1:1 z odpisem. Zrób zrzut z datą.
3. Jeśli status inny niż aktywny (likwidacja, upadłość, zakaz, brak wpisu) – stop, eskalacja.
4. Sprawdź wpis pod kątem zakazów prowadzenia działalności i zaległości podatkowych (sekcje dostępne na portalu – szczegóły do ręcznego sprawdzenia).
5. Odpis: sprawdź apostille (Estonia jest w Konwencji haskiej – apostille wystarczy, legalizacji nie trzeba). Porównaj z wzorcowym dokumentem RIK.
6. UBO: sprawdź w zakładce „Beneficial owners” na portalu. Jeśli dane są widoczne – zapisz. Jeśli zamknięte – wymagaj oświadczenia i struktury (metodyka, pkt 5).
7. Jeśli firma ma zdalnego właściciela/reprezentanta z e-Residency – wymagaj dodatkowo potwierdzenia lokalnej działalności (adres, rachunek, umowy) i wzmocnionej weryfikacji.
8. Screening sankcyjny osób i firmy: EU Sanctions Map, OFAC, UK, ONZ, OpenSanctions (wg metodyki) – zapisz wynik z datą.
9. Sprawdź numer VAT w VIES (format EE + 9 cyfr).
10. Sprawdź adres (mapa, wirtualne biuro?) i stronę/e-mail firmowy.
11. Ocena ryzyka: przy e-Residency lub zdalnym założeniu – poziom podwyższony.
12. Zapisz dowody (zrzuty, ID zapytań, daty) w aktach klienta.

## 10. Ograniczenia i ryzyka

- **Nie da się za darmo** potwierdzić: cennika certyfikowanych wyciągów (strona nieotwarta), pełnego dostępu do UBO (status sprzeczny), statusów insolvencyjnych (nazwa rejestru nie potwierdzona), zaległości podatkowych (zakres nieznany).
- **Opóźnienia / aktualność:** dane rejestrowe są aktualizowane przez zgłaszających; wpis może nie odzwierciedlać zmian bieżących.
- **Transliteracja:** nazwy estońskie zawierają litery Ä, Ö, Ü, Õ; warianty zapisu (ä/a, õ/o) mogą powodować fałszywe niedopasowania – szukaj też bez znaków diakrytycznych i po kodzie rejestrowym.
- **e-Residency jako ryzyko strukturalne:** zdalne założenie przez nierezydenta to zwykle brak lokalnej obecności; sam wpis w rejestrze nie świadczy o rzeczywistej działalności.
- **Eskalacja do wzmocnionej weryfikacji (EDD):** gdy UBO niedostępne, dane sprzeczne, reprezentant zdalny/e-Residency bez lokalnej działalności, struktura przez jurysdykcje wysokiego ryzyka, lub jakikolwiek sygnał RU/BY.
- **Ryzyko stanu prawnego:** rozbieżne źródła co do dostępu do UBO i możliwych ograniczeń e-Residency – przed decyzją o wysokiej wartości zweryfikuj ręcznie.

## 11. Źródła

- [e-Äriregister – strona angielska (Quick/Detailed search, portal)](https://ariregister.rik.ee/eng) – oficjalne (RIK) – otwarte w czasie researchu: tak
- [e-Business Register Queries – abiinfo.rik.ee (sekcje, klienci umowni, Beneficial owners)](https://abiinfo.rik.ee/en/e-business-register-queries) – oficjalne (RIK) – otwarte w czasie researchu: tak
- [HCCH – tabela statusu Konwencji z 5.10.1961 (Estonia: 11-XII-2000 / 30-IX-2001)](https://www.hcch.net/en/instruments/conventions/status-table/?cid=41) – oficjalne (HCCH) – otwarte w czasie researchu: tak
- [e-Residency – oficjalna strona programu (rejestracja zdalna, brak opłaty w treści)](https://www.e-resident.gov.ee/) – oficjalne (Rząd Estonii) – otwarte w czasie researchu: tak
- [Cennik RIK (`/eng/pricelist`) – link z portalu, niedostępny w researchu](https://ariregister.rik.ee/eng/pricelist) – oficjalne – otwarte w czasie researchu: nie (nie próbowano; link ze strony portalu)
- [FATF – Estonia, detail (403)](https://www.fatf-gafi.org/en/countries/detail/Estonia.html) – oficjalne (FATF) – otwarte w czasie researchu: nie (HTTP 403)
- [FATF – increased monitoring (403)](https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-june-2026.html) – oficjalne (FATF) – otwarte w czasie researchu: nie (HTTP 403)
- [RIK – e-Business Register (404)](https://www.rik.ee/en/e-business-register) – oficjalne (RIK) – otwarte w czasie researchu: nie (HTTP 404)
- [Ministerstwo Finansów Estonii – „E-residency risks” (PDF, analiza ryzyka krajowego, z wyników wyszukiwania)](https://www.fin.ee/sites/default/files/documents/2022-02/4.3.%20E-residency%20risks.pdf) – oficjalne (MF) – otwarte w czasie researchu: nie (limit wyczerpany)
- [ERR – Council of Europe / Moneyval krytyka e-residency (z wyników wyszukiwania)](https://news.err.ee/1608865556/research-education) – publiczne media (ERR) – otwarte w czasie researchu: nie (tylko wynik wyszukiwania)
- [ERR – finance ministry vs LHV o ryzyku prania w e-residency (z wyników wyszukiwania)](https://news.err.ee/949260/sports) – publiczne media (ERR) – otwarte w czasie researchu: nie (tylko wynik wyszukiwania; adres URL zawiera nietypowy slug)
- [Bloomberg 2020 – klienci e-residency powiązani z oszustwami krypto (z wyników wyszukiwania)](https://www.bloomberg.com/news/articles/2020-09-28/clients-of-estonia-s-e-residency-project-linked-to-crypto-scams) – publiczne media – otwarte w czasie researchu: nie (tylko wynik wyszukiwania; dane 2020)
- [Topograph – rejestry biznesowe Estonii (źródło wtórne, sprzeczne informacje o UBO)](https://www.topograph.co/guides/business-registers-in-estonia) – nieoficjalne – otwarte w czasie researchu: nie (tylko wynik wyszukiwania)
- [Ecovis – UBO w Estonii (źródło wtórne, dostęp publiczny za darmo)](https://global.ecovis.com/estonia/ubo/) – nieoficjalne – otwarte w czasie researchu: nie (tylko wynik wyszukiwania)
- [Kyckr – przewodnik po rejestrze Estonii (źródło wtórne)](https://kyckr.com/guides-and-reports/estonia-company-registry-guide) – nieoficjalne – otwarte w czasie researchu: nie (tylko wynik wyszukiwania)
