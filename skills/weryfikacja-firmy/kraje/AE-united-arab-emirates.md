# Zjednoczone Emiraty Arabskie (AE) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia (rejestry zweryfikowane tylko częściowo; większość szczegółów z wtórnych źródeł) · Ryzyko jurysdykcji: podwyższone (strefy wolnocłowe, pośrednictwo reeksportowe, UBO niedostępne publicznie)

## 1. Najkrótsza ścieżka (TL;DR)

- Najpierw ustal, **gdzie** firma ma licencję: w mainland (emirat: Dubaj, Abu Zabi, Szardża itd.) czy w strefie wolnocłowej (DMCC, JAFZA, DIFC, ADGM, RAKEZ itd.). Od tego zależy, który rejestr sprawdzać. Wyszukiwanie strefowej firmy w rejestrze mainland zwraca brak wyników – to nie jest dowód, że firmy nie ma.
- Poproś klienta o **trade licence** (licencję handlową) z numerem licencji, nazwą handlową i organem wydającym (DET/DED Dubaj, ADDED Abu Zabi, lub zarząd strefy). Zweryfikuj status i datę ważności w rejestrze tego organu. Wpisuj numer licencji, nie tylko nazwę.
- Darmowe publiczne wyszukiwanie daje zwykle: nazwę, numer licencji, status, datę ważności, adres i działalność. **Nie daje** reprezentantów, wspólników ani beneficjentów rzeczywistych (UBO) – te dane nie są publiczne.
- Beneficjentów rzeczywistych **nie zweryfikujesz w darmowym rejestrze**. Musisz poprosić klienta o oświadczenie i dokumenty (rejestr udziałowców, statut/MoA) i sprawdzić je krzyżowo z innymi źródłami.
- Numer podatkowy (TRN, 15 cyfr) sprawdzisz na stronie FTA, ale usługa wymaga, według strony FTA, logowania UAE PASS – bezpłatność nie została potwierdzona.

## 2. Rejestr firm (główny)

Kraj nie ma jednego publicznego rejestru firm. Działa kilka rejestrów zależnych od emiratu i strefy.

**a) Federalny rejestr gospodarczy – National Economic Register (NER), Ministerstwo Gospodarki**
- Nazwa oryginalna: National Economic Register (NER); w materiałach pojawia się też nazwa „Nomu”.
- Organ: Ministry of Economy (Ministerstwo Gospodarki). Strona rządowa `beta.government.ae` (podstrona „National Economic Register”) – **nie potwierdzono**: próba otwarcia zakończyła się błędem certyfikatu TLS.
- Wyszukiwanie: wg nazwy handlowej, numeru licencji, działalności (źródła wtórne). Adres portalu w źródłach jest sprzeczny (`ner.economy.ae/Search_By_BN.aspx` vs. `growth.gov.ae`) – **do sprawdzenia ręcznie**.
- Dostęp: źródła są sprzeczne – jedne mówią o wyszukiwaniu bez logowania, inne o logowaniu przez UAE PASS. **Nie potwierdzono – do sprawdzenia ręcznie.**
- Zakres: źródła mówią o mainland i „większości” stref, ale szczegóły rejestrów emiratów są pełniejsze.

**b) Dubaj – mainland (Department of Economy and Tourism, DET; dawniej DED)**
- Nazwa oryginalna: Department of Economy and Tourism (DET), dawniej Department of Economic Development (DED). Portal „Invest in Dubai” / e-services DET.
- Wyszukiwanie: numer licencji lub nazwa firmy (źródła wtórne).
- Adresy w źródłach są sprzeczne (`app.invest.dubai.ae`, `eservices.dubaided.gov.ae/Pages/Anon/TNSrch.aspx`, `ded.ae`). Strona `eservices.dubaided.gov.ae` zwróciła 403 – **nie potwierdzono**. Adres `det.gov.ae` nie został potwierdzony wyszukiwarką – **do sprawdzenia ręcznie**.
- Za darmo: wg źródeł wtórnych podstawowa weryfikacja jest bezpłatna. Nie potwierdzono szczegółów pól.
- Dubaj wydaje też „Dubai Unified Licence” – numer identyfikacyjny firmy w emiracie (wg DET, źródło wtórne).

**c) Abu Dhabi – mainland (Department of Economic Development – Abu Dhabi, ADDED; dawniej ADDED/DED)**
- Usługa weryfikacji: **TAHAQAQ** (nazwa potwierdzona komunikatem WAM i źródłami ADDED; strona ADDED z opisem zwróciła 404 – **nie potwierdzono URL**).
- Wg WAM: TAHAQAQ służy do sprawdzania licencji komercyjnych zarejestrowanych w emiracie, w ramach Abu Dhabi Business Center (ADBC). Cel: ochrona przed oszukańczymi podmiotami.
- Strona wyszukiwania licencji handlowych w Abu Dhabi (ADBC, `adbc.gov.ae` / CitizenAccess) – cytowana na stronie Ministerstwa Gospodarki, **nie otwarta** (połączenie odrzucone).
- Infolinia ADDED: 800555 (wg źródła wtórnego). Opłaty: **nie potwierdzono**.
- Przy numerze licencji: Tamm (`tamm.abudhabi`) – cytowany na stronie Ministerstwa, nie otwarty.

**d) Pozostałe emiraty mainland (Szardża, Adżman, Ras al-Chajma, Umm al-Kuwejn, Fujairah)**
- Każdy emirat ma własny organ gospodarczy (DED-y). Strona Ministerstwa wskazuje przykładowo Ajman DED (`eservices.ajmanded.ae`) – **nie otwarto, nie potwierdzono**.
- Szardża (SEDD): **nie potwierdzono** adresu rejestru – do sprawdzenia ręcznie.

**e) Strefy wolnocłowe – każda ma własny rejestr lub portal (potwierdzenie ogólnej zasady: źródła wtórne zgodne)**

| Strefa | Rejestr / sprawdzenie | Status potwierdzenia |
|---|---|---|
| DMCC (Dubaj) | Public Register, `dmcc.ae/public-register` (również wersja arabska `dmcc.ae/ar/public-register`) | Strona **otwarta**: potwierdzono istnienie wyszukiwarki „Search our register of DMCC entities”. Pola i zasady dostępu **nie potwierdzono** (strona ich nie opisuje). Źródła wtórne: pola to numer licencji, data, ważność, adres, numer rejestrowy, status. Nazwy z przyrostkiem FZCO – **nie potwierdzono**. |
| JAFZA (Dubaj) | Strona `jafza.ae` – wyszukiwarka firm lub kontakt | **Nie potwierdzono** dedykowanego rejestru. Źródła wtórne: wyszukiwanie przez pasek wyszukiwania na jafza.ae lub kontakt z zarządem strefy. |
| DIFC (Dubaj) | Public Register (`difc.com/public-register`; `difc.ae` przekierowuje) | Strona otwarta, ale opis pól i dostępu **nie potwierdzono** (strona pokazuje tylko nagłówek i formularz zapisu). Źródła wtórne: wyszukiwanie bez konta, pola: nazwa, numer, status, siedziba, kategoria; rozbieżne co do dyrektorów i wspólników. |
| ADGM (Abu Dhabi) | Public Registers (`adgm.com/public-registers`) – lista rejestrów | Strona otwarta. Wymieniono m.in. rejestr podmiotów (Online Registry Solution). Bezpośredni link wyszukiwarki i pola **nie potwierdzono**. Źródła wtórne: wyszukiwanie bez logowania; opłata za odpis – **źródła sprzeczne** (jedno: darmo, inne: odpis ok. USD 100). Strona nie wspomina o UBO. |
| RAKEZ (Ras al-Chajma) | Portal 360 / `eportal.rakez.com` (ze strony checklisty licencyjnej RAKEZ – wtórnie) | **Nie potwierdzono** publicznej wyszukiwarki. Źródła wtórne: sprawdzanie po nazwie lub numerze rejestrowym. |
| Meydan Free Zone (Dubaj) | Narzędzie „name check” (wg bloga Meydan) | **Nie potwierdzono** adresu. |
| IFZA (Dubaj), SHAMS (Szardża) | Brak potwierdzonego oficjalnego rejestru | **Nie potwierdzono** – do sprawdzenia ręcznie (kontakt z zarządem strefy). |

- Ogólna zasada: wyszukiwanie firmy strefowej w DET/ADDED nic nie znajdzie. Źródła zgodnie zalecają weryfikację u organu wydającego licencję (nazwa podana na licencji).

**Format numeru identyfikacyjnego**
- Licencja handlowa: numer licencji nadawany przez emirat lub strefę (format różni się per emirat i strefa – **nie potwierdzono wzorca**).
- Numer podatkowy: TRN, 15 cyfr (wg materiałów FTA; patrz pkt 3 i 7).
- Dubai Unified Licence (DET): format nie potwierdzony.

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwy dokumentów:** *Trade Licence* (licencja handlowa, wydawana przez DET/ADDED/strefę); *Certificate of Registration* / *Certificate of Incorporation* (zaświadczenie o rejestracji); *Memorandum of Association* (MoA, umowa spółki); *Register of Shareholders* (rejestr udziałowców). Nazw arabskich nie tłumaczę dosłownie – **sprawdź z tłumaczem przysięgłym**.
- **Wystawca:** organ emiratu lub zarząd strefy. Na licencji powinny być: numer licencji, nazwa, data wydania i ważności, działalność.
- **Cechy autentyczności:** nie potwierdzono wzorów zabezpieczeń poszczególnych organów. Praktyka: porównanie numeru licencji i nazwy z rejestrem organu, który ją wydał.
- **Weryfikacja online:** rejestry z sekcji 2 (wyszukiwanie po numerze licencji). Nie każdy rejestr ma kod QR lub funkcję weryfikacji dokumentu – **nie potwierdzono**.
- **Apostille / legalizacja:** **ZAMIAST apostille UAE używa legalizacji.** Strona Haskiej Konferencji (HCCH, tabela statusu dla Konwencji Haskiej z 1961 r.) **nie wymienia ZEA** wśród państw-stron – źródła twierdzące, że UAE przystąpiło w 2021 r., są błędne (wg HCCH). Dokumenty zagraniczne wystawione w UAE wymagają w praktyce legalizacji przez MSZ ZEA (MOFA). Dla dokumentu z UAE, który ma być użyty w Polsce: sprawdź, czy polski wymóg dotyczy legalizacji czy tłumaczenia – **nie potwierdzono w tym researchu**.
- **MOFA – Digital Attestation:** strona MSZ ZEA (`mofa.gov.ae`, Attestation Information) wskazuje usługę cyfrową, logowanie przez UAE PASS, termin „zwykle 2–3 dni robocze” (wg strony), oraz że fizyczne przesłanie oryginału jest wymagane. Wymienia też weryfikację dokumentów poświadczonych pod adresem `verify.mofa.gov.ae` (adres z tej strony, nie otwarty samodzielnie – **do sprawdzenia ręcznie**).
- **Rejestr zagraniczny:** nie dotyczy odpisu z UAE.
- **Świeżość odpisu:** nie potwierdzono wymogu ustawowego. Praktyka zgodna z szablonem: przyjmij ≤ 3 miesiące od daty wystawienia.
- **Typowe sygnały podróbki / nieaktualności:** licencja wystawiona przez „organ” nieistniejący w rejestrze emiratu; nazwa z innego emiratu niż adres; brak wpisu w rejestrze organu wydającego przy poprawnym numerze; sprzeczne dane między licencją a rejestrem. Źródła wtórne podkreślają, że przy rozbieżności między źródłami to sygnał ostrzegawczy.

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy:** w rejestrach mainland i stref pojawiają się statusy aktywna / wygasła / zawieszona / anulowana. **Nie potwierdzono** pełnej listy statusów i ich znaczenia dla każdego organu – do sprawdzenia ręcznie.
- **Upadłość / restrukturyzacja:** nie potwierdzono publicznego rejestru upadłości dla UAE. Sprawdź u klienta oświadczenie o braku postępowania i zapytaj o status w sądzie (organ i portal – **nie potwierdzono**).
- **Zaległości podatkowe / ZUS-owe:** nie potwierdzono publicznego wyszukiwania. Do potwierdzenia rejestracji VAT służy FTA (pkt 7).
- **Red flagi specyficzne dla kraju (źródła wtórne, zgodne z ogólną wiedzą AML):** firmy-słupy i nominee directors; adresy masowej rejestracji (virtual office); licencje „bez fizycznego biura”; spółki w strefach o niskich wymogach, gdy towar jest drogi i łatwo się przenosi; zmiana strefy lub emiratu tuż przed transakcją; sprzeczne nazwy (np. „DMCC” vs. „FZCO”).
- **Lista ryzyk pośrednictwa:** ZEA jest historycznie uznawane za jeden z głównych hubów reeksportowych (w tym do Rosji) – szczegóły w pkt 8.

## 5. Zarząd, wspólnicy, reprezentacja

- **Osoby uprawnione do reprezentacji:** w mainland zwykle wpisane w licencji lub zaświadczeniu o rejestracji (manager / general manager). W strefach – wg rejestru strefy (np. DMCC pokazuje dyrektora). **Nie potwierdzono**, które rejestry pokazują to za darmo.
- **Wspólnicy / udziały:** w mainland udziałowców nie widać w publicznym wyszukiwaniu. Źródła wtórne mówią, że DIFC/ADGM mogą pokazywać dyrektorów lub wspólników – **sprzeczne, do sprawdzenia ręcznie** (pkt 2).
- **Dokumenty założycielskie:** umowa spółki (MoA) i statut nie są publiczne – zażądaj od klienta.
- **Sprawozdania finansowe:** nie potwierdzono publicznego dostępu. Zażądaj od klienta.
- **Zasady reprezentacji:** wymagany jest wzór podpisu i zakres uprawnień zarządu zgodnie z MoA; zalecamy odpis lub uchwałę zarządu – nie potwierdzono wymogu prawnego w tym researchu.

## 6. Beneficjenci rzeczywiści (UBO)

- **Czy istnieje rejestr UBO:** tak. Podstawa: **Cabinet Decision No. 58 of 2020** – zastąpiona przez **Cabinet Decision No. 109 of 2023** (źródła wtórne są rozbieżne: jedne mówią o uchyleniu, inne o zmianie). Kary: **Cabinet Decision No. 132 of 2023** (wg źródeł wtórnych). Wykonawczy akt z 2025 (Cabinet Resolution No. 134 of 2025) – **pojedyncze źródło wtórne, nie potwierdzono**. Ustawa: **Federal Decree-Law No. 10 of 2025** (AML/CFT), wg źródeł wtórnych wchodzi w życie 14 października 2025 – **nie potwierdzono w tekście urzędowym**.
- **Organ prowadzący:** Ministry of Economy (Ministerstwo Gospodarki) – wg źródeł wtórnych. Rejestr utrzymywany przez spółki i zgłaszany do Ministerstwa.
- **Dostęp:** **Nie publiczny.** Zgodnie z wieloma źródłami prawniczymi informacje są dostępne wyłącznie dla właściwych organów (Ministerstwo Gospodarki, FIU, organy licencyjne, organy ścigania, Centralny Bank i inne wskazane organy). Dostęp może też wynikać z nakazu sądowego. Jedno źródło wtórne (2026) podkreśla brak dostępu publicznego. **Potwierdzenie z tekstu urzędowego: nie potwierdzono – do sprawdzenia ręcznie.**
- **Czy bezpłatny:** nie dotyczy (brak publicznego dostępu).
- **Dane widoczne:** nie dotyczy publicznie. Według źródeł wtórnych rejestr zawiera m.in. dane osobowe UBO i procent udziałów.
- **Próg beneficjenta:** źródła wtórne podają **25%** udziałów lub praw głosu (oraz kontrolę w inny sposób; w razie braku – członek kierownictwa wyższego szczebla jako domniemany beneficjent). **Nie potwierdzono w tekście urzędowym.**
- **Trusty i fundacje:** nie potwierdzono szczegółów. Zakładamy, że podlegają obowiązkom ujawniania, ale tego nie zweryfikowano – do sprawdzenia ręcznie.

**Procedura zastępcza (brak publicznego dostępu do UBO):**
1. Zażądaj od klienta **oświadczenia o beneficjentach rzeczywistych** (imię, nazwisko, data urodzenia, obywatelstwo, adres, % udziałów/praw głosu, sposób kontroli), podpisanego przez osobę uprawnioną do reprezentacji.
2. Zażądaj **aktualnego rejestru udziałowców** (Register of Shareholders) i **rejestru UBO** w wersji wyciągu lub odpisu – spółka musi go prowadzić zgodnie z przepisami (źródła wtórne).
3. Zażądaj **umowy spółki (MoA)** i **licencji**. Sprawdź, czy udziałowcy zgadzają się z rejestrem.
4. Zażądaj **schematu struktury właścicielskiej** do poziomu osób fizycznych; jeśli udziałowcem jest spółka – to samo dla niej (w tym jurysdykcje spółek).
5. **Krzyżowa weryfikacja** z darmowymi źródłami: rejestr w emiracie/strefie (wspólnicy, jeśli widoczni), GLEIF (LEI – tylko przy większych podmiotach; adres do sprawdzenia ręcznie), media i zapytania do banku klienta (o ile klient wyrazi zgodę).
6. Przy struktury z trustem lub nominee directors – eskalacja do wzmocnionej weryfikacji (EDD).

## 7. Dodatkowe darmowe weryfikacje

- **Numer podatkowy / VAT (TRN):** Federal Tax Authority (FTA, `tax.gov.ae`) udostępnia usługę weryfikacji TRN/TIN (formularz z captchą – wg strony). **Strona FTA wskazuje, że usługi FTA są dostępne wyłącznie przez UAE PASS** – bezpłatność i wymóg logowania dla tej konkretnej usługi **nie potwierdzono** (sprzeczne sygnały: zwrot „only available through UAEPass” i opis weryfikacji jako publicznej). Sprawdź ręcznie.
- **VIES (UE):** nie dotyczy – UAE nie jest krajem UE, VIES nie obejmuje ZEA.
- **EORI / rejestr celny:** nie dotyczy kontrahenta z UAE w kontekście UE, o ile nie jest importerem do UE – **do sprawdzenia ręcznie w zależności od transakcji**.
- **LEI (GLEIF):** zwykle tylko większe podmioty; adres GLEIF nie został otwarty w researchu – **do sprawdzenia ręcznie**.
- **Rejestr działalności regulowanych:** towar jest regulowany? Sprawdź zezwolenia organu sektorowego (np. Ministerstwo Energii, organy ds. substancji kontrolowanych – **nie potwierdzono listy**). Dla handlu wyrobami podlegającymi kontroli eksportowej – sprawdź u klienta zezwolenia.
- **Listy ostrzeżeń:** brak potwierdzonej publicznej listy ostrzeżeń dla kontrahentów w UAE – do sprawdzenia ręcznie.
- **Rejestr znaków towarowych / domen:** nie sprawdzono w tym researchu.

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Ryzyko pośrednictwa:** ZEA są uznawane w materiałach analitycznych za ważny hub reeksportowy dla Rosji i Białorusi (towary podwójnego zastosowania, elektronika, części lotnicze/maszynowe). To ogólna ocena, nie potwierdzona liczbą w tym researchu.
- **Listy krajowe:** Executive Office for Control & Non-Proliferation (EOCN, `uaeiec.gov.ae`) publikuje **Local Terrorist List** (wg strony EOCN: PDF i Excel) oraz odsyła do **listy UN Consolidated List** (`un.org`). Lista lokalna nie zawiera RU/BY jako państw – to lista terrorystyczna. Lista wyszukiwalna przez wyszukiwarkę – **nie** (pliki do przeszukania lokalnie).
- **Listy UE/ONZ/OFAC/UK:** sprawdź w odpowiednich narzędziach (nie sprawdzono w tym researchu). Pamiętaj, że UE i USA mają osobne sankcje dla podmiotów z UAE.
- **Struktura właścicielska – sygnały:** rosyjscy lub białoruscy udziałowcy (także przez spółki z innych jurysdykcji); nominee directors; trusty; firmy z adresem w UAE i właścicielami bez dokumentów; nagła zmiana właściciela przed transakcją.
- **ZAWSZE oznacz flagą „RU/BY” (wg `00-metodyka.md`):** kontrahent z UAE, którego UBO lub udziałowcem jest osoba lub podmiot z RU/BY, lub który dostarcza towar pochodzący z RU/BY, albo którego transakcje mają trasę przez UAE do RU/BY.
- **Historia listy UE:** wg źródeł wtórnych UAE zostało usunięte z unijnej listy państw wysokiego ryzyka AML (delegowane rozporządzenie z 2025 r., wejście w życie sierpień 2025; **numer rozporządzenia podany wyłącznie w źródle wtórnym**). Wcześniej UAE wyszło z listy FATF (luty 2024, źródła wtórne). Aktualność listy UE sprawdź ręcznie na stronie Komisji Europejskiej.

## 9. Procedura krok po kroku (checklist)

1. Zbierz od klienta: pełną nazwę, numer licencji handlowej, numer TRN (jeśli jest), adres siedziby, nazwę organu wydającego licencję.
2. Ustal typ rejestru: mainland (który emirat) czy strefa (która). Jeśli niepewne – zapytaj o organ wydający na licencji.
3. Wyszukaj licencję w rejestrze właściwego organu po **numerze licencji** (nie po nazwie). Zapisz: datę, numer ID wyszukiwania, status, datę ważności, nazwę i adres. Zrób zrzut ekranu.
4. Jeśli to strefa, sprawdź rejestr tej strefy (DMCC, DIFC, ADGM, JAFZA, RAKEZ itd. – adresy w pkt 2). Jeśli strefy nie masz na liście – zapytaj zarząd strefy (kontakt do ustalenia).
5. Porównaj dane z dokumentem klienta (nazwa, numer, adres, status). Każda rozbieżność = zapytanie do klienta.
6. Sprawdź numer TRN w usłudze FTA (pamiętaj o UAE PASS). Jeśli niedostępna bezpłatnie – zapisz to w karcie kontrahenta.
7. Zażądaj: oświadczenia o UBO, rejestru udziałowców, MoA i schematu struktury (pkt 6).
8. Sprawdź nazwiska UBO, zarządu i udziałowców na listach sankcyjnych (EU, UN, OFAC, UK) oraz w lokalnej liście EOCN (pliki PDF/Excel).
9. Ustal, czy w łańcuchu jest RU/BY (lub transakcja ma trasę przez UAE do RU/BY). Jeśli tak – flaga „RU/BY” i eskalacja.
10. Sprawdź upadłość i zaległości – zapytanie do klienta o oświadczenie i ewentualnie zapytanie do banku klienta (za zgodą klienta).
11. Zapisz wynik z datą sprawdzenia i numerami ID zapytań. Odpis z UAE traktuj jako ważny maksymalnie 3 miesiące.
12. Przy niepełnej weryfikacji UBO lub sygnałach z pkt 4 i 8 – eskalacja do wzmocnionej weryfikacji (EDD).

## 10. Ograniczenia i ryzyka

- **Nie da się za darmo sprawdzić:** UBO i ich danych; listy wspólników w większości mainland; statusu upadłości (brak publicznego rejestru potwierdzonego); zaległości podatkowych i ZUS-owych. Płatna alternatywa (jako ostatnia opcja): firmy raportowe lub konsultanci lokalni – **nie wyceniono w tym researchu**.
- **Opóźnienia danych:** rejestry emiratów i stref aktualizują się z opóźnieniem. Status „aktywna” na dzień sprawdzenia nie gwarantuje stanu z dnia transakcji.
- **Transliteracja:** nazwy arabskie są zapisywane w różnych wariantach (np. „Al”/„El”, „Dubai”/„Dubayy”). Porównuj po numerze licencji, nie po nazwie.
- **Źródła wtórne:** większość szczegółów o rejestrach pochodzi z blogów i serwisów konsultingowych. Pozycje oznaczone „nie potwierdzono” wymagają ręcznego sprawdzenia przed użyciem w decyzji.
- **Sprzeczności w źródłach (do rozstrzygnięcia ręcznie):** adres portalu NER; wymóg logowania UAE PASS w NER i w TRN; opłata za odpis ADGM; czy DMCC zmienia przyrostek na FZCO; repealed vs. amended dla Cabinet Decision 58/2020 i 109/2023; numer rozporządzenia UE.
- **Kiedy eskalować do EDD:** brak UBO lub niespójne oświadczenie; struktura z trustem lub nominee; udziałowcy z RU/BY; towar objęty kontrolą eksportową; firma w strefie z adresem wirtualnym; nagła zmiana właściciela lub zarządu.

## 11. Źródła

Oficjalne strony otwarte w czasie researchu (WebFetch, 2026-11-16):
- [DMCC – Public Register](https://www.dmcc.ae/public-register) – oficjalne – otwarte w czasie researchu: tak
- [DMCC – Public Register (wersja arabska)](https://www.dmcc.ae/ar/public-register) – oficjalne – otwarte w czasie researchu: tak
- [DIFC – Public Register (przekierowanie z difc.ae na difc.com)](https://www.difc.com/public-register) – oficjalne – otwarte w czasie researchu: tak (treść ograniczona)
- [ADGM – Public Registers](https://www.adgm.com/public-registers) – oficjalne – otwarte w czasie researchu: tak (treść ograniczona)
- [Ministerstwo Gospodarki – Establishing companies](https://www.moet.gov.ae/en/web/guest/establishing-companies) – oficjalne – otwarte w czasie researchu: tak
- [Ministerstwo Gospodarki – Establishing business in the UAE](https://www.moet.gov.ae/en/establishing-business-in-the-uae) – oficjalne – otwarte w czasie researchu: tak
- [Ministerstwo Gospodarki – AML/CFT (DNFBP)](https://www.moet.gov.ae/en/aml) – oficjalne – otwarte w czasie researchu: tak (bez informacji o UBO)
- [EOCN – TFS / listy sankcyjne](https://www.uaeiec.gov.ae/en-us/un-page) – oficjalne – otwarte w czasie researchu: tak
- [MSZ ZEA – Attestation Information](https://www.mofa.gov.ae/en/Missions/The-Hague/Services/Services-for-Individuals/Attestation-Information) – oficjalne – otwarte w czasie researchu: tak
- [HCCH – status tabeli Konwencji Haskiej (1961, cid=41)](https://www.hcch.net/en/instruments/conventions/status-table/?cid=41) – oficjalne – otwarte w czasie researchu: tak (brak ZEA na liście)
- [FTA – strona główna (wskazana w serwisie TRN)](https://tax.gov.ae/en/default.aspx) – oficjalne – otwarte w czasie researchu: nie (wskazana na innej stronie; podstrona TRN zwróciła sprzeczne wyniki)
- [Lista ONZ – UN Consolidated List](https://www.un.org/securitycouncil/content/un-sc-consolidated-list) – oficjalne – otwarte w czasie researchu: nie (wskazana przez EOCN)

Adresy wskazane na oficjalnych stronach, ale **nieotwarte** (błąd, 403, brak połączenia lub brak potwierdzenia):
- `beta.government.ae` – strona usług rządowych o rejestrach (NER, sprawdzanie licencji) – oficjalne – otwarte: nie (błąd certyfikatu TLS)
- `eservices.dubaided.gov.ae/Pages/Anon/TNSrch.aspx` – wyszukiwarka nazwy handlowej Dubaj – oficjalne (wskazana na stronie MoE) – otwarte: nie (403)
- `adbc.gov.ae` (CitizenAccess, wyszukiwanie licencji Abu Dhabi) – oficjalne (wskazana na stronie MoE) – otwarte: nie (połączenie odrzucone)
- `tamm.abudhabi` (Trade Licence Enquiry) – oficjalne (wskazana na stronie MoE) – otwarte: nie
- `added.gov.ae/Our-Initiatives/Tahaqaq` – oficjalne (wskazana w wynikach wyszukiwania) – otwarte: nie (404)
- `verify.mofa.gov.ae` – weryfikacja dokumentów poświadczonych – oficjalne (wskazana na stronie MSZ) – otwarte: nie
- `eportal.rakez.com` – portal RAKEZ – wtórne (ze strony checklisty) – otwarte: nie
- `ner.economy.ae/Search_By_BN.aspx` – NER – nieoficjalne/do potwierdzenia – otwarte: nie
- `app.invest.dubai.ae` / `det.gov.ae` / `ded.ae` – portale DET – nie potwierdzono – otwarte: nie

Źródła wtórne (wyszukiwarka, bez potwierdzenia w oficjalnym tekście):
- Komunikat WAM o usłudze TAHAQAQ (ADDED) – oficjalne (media rządowe) – otwarte: nie (tylko wynik wyszukiwania)
- Artykuły prawnicze o UBO (Cabinet Decision 58/2020, 109/2023, 132/2023, 134/2025; Federal Decree-Law 10/2025) – nieoficjalne – otwarte: nie
- Dane o FATF (usunięcie UAE z listy szarej, 23.02.2024) – nieoficjalne (media, kancelarie) – otwarte: nie
- Dane o usunięciu UAE z listy UE (delegowane rozporządzenie 2025) – nieoficjalne (kancelarie, media) – otwarte: nie
- Blogi o weryfikacji licencji (wiele, rozbieżne adresy) – nieoficjalne – otwarte: nie
