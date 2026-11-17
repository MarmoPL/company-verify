# Cypr (CY) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia · Ryzyko jurysdykcji: podwyższone (kraj UE, ale znany pośrednik kapitału z RU; nie na listach FATF wg dostępnych źródeł, brak sankcji na sam kraj)

## 1. Najkrótsza ścieżka (TL;DR)

- **Rejestr firm:** e-wyszukiwarka Departamentu Rejestrador Spółek i Urzędnika Urzędowego (DRCOR, *Department of the Registrar of Companies and Official Receiver*, Nikozja) – portal `companies.gov.cy`, formularz wyszukiwania `efiling.drcor.mcit.gov.cy/DrcorPublic/SearchForm.aspx` (URL podany na stronie urzędowej, sam formularz nie został przeze mnie otwarty). Szukasz po **nazwie** lub **numerze rejestrowym** (format `HE` + cyfry, do potwierdzenia na odpisie).
- **Za darmo:** nazwa, data rejestracji, typ, status, adres siedziby, aktualni dyrektorzy i sekretarz (dla spółek), podgląd składanych dokumentów, data ostatniego sprawozdania rocznego.
- **Za pieniądze:** pełna historia pliku (akcjonariusze/członkowie, historia kapitału, hipoteki i zastawy, lista dokumentów) – ok. **10 EUR** za wyszukanie (wg strony urzędowej; starszy artykuł podaje 8,54 EUR – traktuj jako nieaktualne).
- **Beneficjenci rzeczywiści (UBO):** rejestr istnieje (prowadzi go DRCOR), ale **publiczny dostęp został zniesiony** po wyroku TSUE. Dla nas, jako podmiotu niezobowiązanego do AML w Cyprze, **nie ma darmowego ani realnego dostępu** – stosuj procedurę zastępczą z sekcji 6 (oświadczenie + struktura + weryfikacja krzyżowa).
- **VAT:** VIES (UE) – potwierdza ważność numeru i zwykle nazwę/adres. Ważny VIES to tylko dowód rejestracji VAT, nie dowód wiarygodności.
- **Odpis od klienta:** nie ma w Cyprze jednego, prostego kodu weryfikacyjnego online do odpisu (patrz sekcja 3) – porównujesz dane z odpisu z e-wyszukiwarką DRCOR i VIES.

## 2. Rejestr firm (główny)

- **Nazwa rejestru:** Rejestr przedsiębiorstw (*Business Entities Register*, w praktyce „Registrar of Companies"), organ: **Department of the Registrar of Companies and Official Receiver (DRCOR)** – w części źródeł używana jest nazwa „Registrar of Companies and Intellectual Property". Nazwę należy potwierdzić na stronie urzędowej.
- **URL (oficjalny):** `https://companies.gov.cy/en/company-lifecycle/search-for-company-information` (otwarte w researchu – strona podaje link do e-wyszukiwarki). Bezpośredni formularz: `https://efiling.drcor.mcit.gov.cy/DrcorPublic/SearchForm.aspx` (podany na stronie urzędowej, nie otwarty).
- **Język:** interfejs po angielsku i po grecku (wersja EN dostępna).
- **Typ rejestru:** centralny (jeden rejestr dla spółek, spółek osobowych, nazw firm, spółek zagranicznych). Sądowy nie – rejestr prowadzi urząd administracyjny.
- **Wyszukiwanie po:** nazwie firmy lub numerze rejestrowym (oba działają, według strony urzędowej). Wyszukiwanie po osobie fizycznej – nie potwierdzono (w pełnym rejestrze nie wiem, czy działa; sprawdzić ręcznie).
- **Za darmo:** nazwa, data rejestracji, typ, status, adres siedziby (spółki), aktualni dyrektorzy i sekretarz (spółki) lub właściciel/wspólnicy (nazwy firm, spółki osobowe), podglądy składanych dokumentów, data ostatniego sprawozdania rocznego.
- **Płatne / za logowaniem:** pełna historia pliku od rejestracji (członkowie i udziały historycznie, historia kapitału, hipoteki i zastawy od 2000 r., lista wszystkich dokumentów) – **ok. 10 EUR** za wyszukanie (strona urzędowa). Wymagane jest konto na portalu (opcje Sign Up / Sign In); czy wyszukiwanie publiczne wymaga konta – nie potwierdzono.
- **Format numeru:** prefiks `HE` (spółki z o.o./akcyjne/cywilne) lub numer nazwy firmy/partnerstwa wg typu – do potwierdzenia na odpisie. Źródła potwierdzają, że numer HE **nie jest** numerem VAT.

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwa dokumentu:** *Certificate of Incorporation* (odpis rejestracji) i *Certificate of Good Standing / Certificate of Registration* (zaświadczenie o istnieniu/aktywności). Po grecku „Πιστοποιητικό" (certyfikat), „Πιστοποιητικό εγγραφής" (rejestracja). Odpis z pełną historią to „Επίσημο αντίγραφο / Εκτύπωση πλήρους αρχείου" – nazwy do potwierdzenia na wzorze z urzędu.
- **Kto wystawia:** DRCOR (Registrar). Odpisy urzędowe mają podpis/pieczęć urzędu i numer dokumentu.
- **Cechy autentyczności:** numer dokumentu, data wydania, podpis urzędnika i pieczęć; wzór z kodem weryfikacyjnym/QR – **nie potwierdzono**, czy DRCOR stosuje kod QR na odpisach. Sprawdź wzór w materiałach urzędu.
- **Autentyczność ONLINE:** brak potwierdzonego publicznego narzędzia do weryfikacji konkretnego odpisu. Porównujesz **nazwę, numer HE, adres i daty** z e-wyszukiwarką DRCOR (sekcja 2). Rozbieżność = sygnał ostrzegawczy.
- **Apostille:** Cypr jest stroną Konwencji haskiej z 1961 r. – **potwierdzone** w tabeli HCCH (przystąpienie 26.07.1972, wejście w życie dla Cypru 30.04.1973; brak zastrzeżeń). Dla polskiej hurtowni: odpis z Cypru z **apostille** jest zwykle wymagany, jeśli dokument ma służyć za podstawę w Polsce w formie urzędowej; w zwykłej relacji handlowej można przyjąć kopię + sprawdzenie w rejestrze. Wymóg polityki firmy – do decyzji.
- **Typowe sygnały podróbki / nieaktualności:** numer HE zgodny z odpisem, ale inna nazwa lub adres w rejestrze; firma o niedawnej rejestracji z wieloma zmianami dyrektorów; odpis wystawiony przez pośrednika zamiast urzędu; brak zgodności daty w odpisie z datą wpisu w e-wyszukiwarce.
- **Ważność odpisu:** praktyka – nie starszy niż 3 miesiące (zgodnie z metodyką). Dane w rejestrze są aktualizowane po złożeniu dokumentów; opóźnienia są normalne. Sprawdź na dzień weryfikacji.

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy w rejestrze (nazwy do potwierdzenia na portalu):** aktywna (*Active*), w likwidacji (*In liquidation*), zawieszona / wykreślona (*Struck off*), w procesie usunięcia z rejestru (*Striking off*), upadłość/zarząd komisaryczny (*Insolvency / Official Receiver*). Dokładne brzmienia – nie potwierdzono; odczytaj z ekranu.
- **Upadłość/restrukturyzacja/likwidacja:** Cypr ma **Sekcję Upadłości (Bankruptcies Section)** przy DRCOR, zajmującą się majątkiem osób fizycznych i prawnych w upadłości (wg e-Justice). Czy wyszukiwanie w tym rejestrze jest publiczne i darmowe – **nie potwierdzono**. Źródło: `https://e-justice.europa.eu/topics/registers-business-insolvency-land/bankruptcy-and-insolvency-registers/cy_en` (wynik wyszukiwania, nie otwarte).
- **Zaległości podatkowe / VAT:** rejestracja w systemie podatkowym (TIC/TFA – Tax For All) dla zarejestrowanych użytkowników; publiczny wgląd w zaległości – **nie potwierdzono**, zwykle niedostępny. Traktuj jako wymóg od klienta (zaświadczenie od doradcy podatkowego lub deklaracja).
- **Sygnały specyficzne dla Cypru (red flags):**
  - **Firmy-słupy i shelf companies** – ICIJ *Cyprus Confidential* (14.11.2023) opisuje ok. 650 spółek i trustów cypryjskich powiązanych z sankcjonowanymi Rosjanami oraz „frontman directors" dostarczanych przez małe firmy usługowe (https://www.icij.org/investigations/cyprus-confidential/about-cyprus-confidential-investigation/ – otwarte).
  - **Nominowani dyrektorzy** – ta sama dokumentacja ICIJ i raport z 2025 r. (wynik wyszukiwania) wskazują powtarzające się nominalne zarządy.
  - **Adresy usługowe (virtual office) w Nikozji i Limassol** – częsta praktyka rejestrowa; sprawdź, czy adres to rzeczywiste biuro.
  - **Strefy wolnocłowe** – Cypr ma strefy wolnocłowe (Larnaka, Limassol) – *nie potwierdzono szczegółów* w tym researchu; traktuj jako element podwyższonej uwagi.
  - **Zmiany dyrektorów i udziałów tuż po 24.02.2022** – silny sygnał (metodyka pkt 4).

## 5. Zarząd, wspólnicy, reprezentacja

- **Zarząd i sposób reprezentacji:** w e-wyszukiwarce za darmo widać aktualnych dyrektorów i sekretarza (spółki). **Sposób reprezentacji** (np. dwóch dyrektorów łącznie) nie jest w bezpłatnym widoku – wymaga statutu (*Memorandum and Articles of Association*) lub odpisu pełnego.
- **Wspólnicy/akcjonariusze:** w bezpłatnym widoku – nie. Pełna historia członków i udziałów jest w płatnym wyszukiwaniu (ok. 10 EUR). Udziały aktualne mogą być w sprawozdaniu rocznym – nie potwierdzono dostępności za darmo.
- **Dokumenty założycielskie i sprawozdania finansowe:** statut i akt założycielski – do pobrania z DRCOR odpłatnie (zakres opłat – nie potwierdzono cennika). Sprawozdania finansowe spółek – składane do rejestru; czy dostępne za darmo – **nie potwierdzono**. Żądaj od klienta, a weryfikuj z rejestrem.
- **Osoby fizyczne w zarządzie:** wymagaj dokumentu tożsamości i pełnomocnictwa (paszport), porównaj z listą dyrektorów w rejestrze.

## 6. Beneficjenci rzeczywiści (UBO)

- **Rejestr:** **Register of Ultimate Beneficial Owners** (UBO), prowadzony przez DRCOR; zgłoszenia przez e-usługę na portalu DRCOR (strona urzędowa wskazuje „Register of Beneficial Owners" i e-usługę rejestracji danych UBO oraz FAQ). Organ: DRCOR.
- **Dostęp – stan prawny (najważniejsze):**
  - **Publiczny dostęp** uruchomiony 1 czerwca 2022 r. został **wycofany** po wyroku TSUE z **22 listopada 2022 r.** (połączone sprawy **C‑37/20 i C‑601/20** – potwierdzone w omówieniu Harris Kyriakides, z datą publikacji 17.01.2023). Od ok. stycznia 2023 r. dostęp jest ograniczony – różne źródła podają różne daty zawieszenia (część mówi o 28.11.2022, część o 3.01.2023); do sprawdzenia ręcznie.
  - **Dostęp przyznany obliczeniowo (as of 2023):** organy (policja, MOKAS, Urząd Skarbowy, Bank Centralny) oraz **podmioty obowiązane AML** (audytorzy, prawnicy, doradcy podatkowi, dostawcy usług fiducjarnych, instytucje finansowe) – po złożeniu oficjalnego oświadczenia o statusie i związku z obowiązkami AML. Źródło: Harris Kyriakides, `https://www.harriskyriakides.law/insights/news/access-to-cyprus-ubo-register-restored-for-obliged-entities` (otwarte, z 17.01.2023).
  - **„Uzasadniony interes" (legitimate interest):** w 2023 r. nie było go dla osób trzecich; w 2026 r. trwa proces legislacyjny. CySEC w marcu 2026 r. (konsultacja, termin zgłoszeń 24.03.2026) zaproponował, by dostęp miały **wyłącznie** podmioty wykazujące uzasadniony interes (`https://cyprus-mail.com/2026/03/06/cysec-proposes-limits-on-access-to-beneficial-ownership-data` – otwarte). Źródło wtórne (Kyckr) podaje Law 25(I)/2026 i akt CySEC 243/2026 oraz twierdzi, że trasa dla osób z uzasadnionym interesem **nie działa operacyjnie** – **nie potwierdzono** w źródłach urzędowych.
  - **Wniosek:** dla nas (poza zakresem obowiązanych AML) **brak darmowego dostępu** i prawdopodobnie brak działającej ścieżki wnioskowej. Jeśli kiedyś będzie możliwy wniosek z uzasadnionym interesem – jednorazowo, płatnie (opłata za wniosek – źródło podaje 3,50 EUR, **nie potwierdzono**).
- **Czy darmowy:** nie (dla nas). Dane, które widać dla uprawnionych: imię, nazwisko, data urodzenia, obywatelstwo/kraj, adres zamieszkania, udział procentowy i rodzaj kontroli (zgodnie z prawem AML – *nie potwierdzono szczegółów zakresu pola w rejestrze*).
- **Próg beneficjenta:** **25%** udziałów lub praw głosu, albo kontrola (wg OpenOwnership – źródło wtórne, do sprawdzenia w ustawie 188(I)/2007). Kontrola obejmuje m.in. prawo powoływania zarządu, wpływ na decyzje.
- **Trusty / fundacje:** Cypr ma **osobny rejestr beneficjentów trustów** (*express trusts and similar arrangements*), prowadzony przez **CySEC** (zamiast DRCOR) – konsultacja zmian w marcu 2026 (źródło: Cyprus Mail, otwarte). Dostęp podobnie ograniczony. Trusty z trustee w Cyprze są typowym elementem struktur pośrednich.

### Procedura zastępcza (obowiązkowa, bo rejestr jest zamknięty)

1. **Oświadczenie o beneficjentach** podpisane przez osobę uprawnioną do reprezentacji (z podpisem kwalifikowanym, jeśli możliwe): dla każdego UBO imię, nazwisko, data i miejsce urodzenia, obywatelstwo, kraj zamieszkania, % udziałów/praw głosu lub opis kontroli; schemat struktury do osoby fizycznej z nazwami i numerami spółek pośrednich; deklaracja PEP, obywatelstwa/rezydencji RU/BY i na listach sankcyjnych; zobowiązanie do aktualizacji (wzór z metodyki pkt 5).
2. **Dokumenty do zażądania od klienta:** wyciąg z rejestru udziałowców (*Register of Members*) – cypryjski wyciąg z rejestru spółki (*Register of Members*), statut (*Articles of Association*), umowa wspólników/akcjonariuszy (*Shareholders' Agreement*) jeśli istnieje, akt powierniczy (*Trust Deed*) i lista beneficjentów trustu jeśli dotyczy, **certyfikat członkostwa** lub zgłoszenie UBO do DRCOR (zrzut z e-usługi, potwierdzający, że zgłoszenie zostało złożone – nie treść rejestru).
3. **Weryfikacja krzyżowa:** e-wyszukiwarka DRCOR (dyrektorzy, status), płatne wyszukanie historii pliku (ok. 10 EUR – udziały historyczne), sprawozdanie finansowe (nota o jednostkach powiązanych), GLEIF (sekcja 7), OpenCorporates, OCCRP Aleph/ICIJ Offshore Leaks (sekcja 7 metodyki), wyszukiwanie w cyrylicy (nazwy po rosyjsku/greku).
4. **Sprawdź struktury przez Cypr:** czy po stronie pośredniej stoi kolejna jurysdykcja offshore lub trust; czy udział tuż poniżej 25%.

## 7. Dodatkowe darmowe weryfikacje

- **Numer VAT (VIES):** `https://ec.europa.eu/taxation_customs/vies` (adres z metodyki – **nie otwierano w researchu**). Format cypryjskiego VAT: prefiks **CY** + numer; źródła (wyniki wyszukiwania, komercyjne) podają CY + 8 cyfr + litera (TIC), ale różnią się w opisie – **do potwierdzenia**. VIES potwierdza zarejestrowanie i często zwraca nazwę/adres (może być po grecku). Uwaga: numer podatkowy (TIC, do celów dochodowych) może **nie być** tym samym co numer VAT.
- **Numer podatkowy (TIC/TFA):** weryfikacja tylko dla zarejestrowanych użytkowników systemu Tax For All – nie darmowa dla nas.
- **EORI (UE):** rejestr EORI Komisji Europejskiej (validation tool) – nie sprawdzono w researchu; wiarygodne dla importu/eksportu, jeśli klient ma numer `CY…`.
- **LEI (GLEIF):** `https://search.gleif.org` (z metodyki, nie otwarto). Zwykle tylko większe podmioty.
- **Licencje branżowe:** jeśli towar wymaga licencji (np. finanse, pośrednictwo) – nadzór nad finansami Cypru (CySEC, Central Bank of Cyprus) – nie sprawdzono zakresu rejestrów publicznych.
- **Lokalne listy ostrzeżeń:** Cypr ma CySEC (lista podmiotów nielicencjonowanych) i Central Bank of Cyprus (lista ostrzeżeń) – *nie potwierdzono adresów i zakresu list w tym researchu*; sprawdzić ręcznie.
- **Adresy / nieruchomości:** brak publicznego katastru online dla osób trzecich – *nie potwierdzono*.

## 8. Sankcje i powiązania RU/BY w tym kraju

To jest najważniejsza część dla Cypru.

- **Rola jako pośrednika:** Cypr jest historycznie jednym z głównych centrów rosyjskiego kapitału w UE. Źródła:
  - **ICIJ *Cyprus Confidential*** (14.11.2023; ok. 3,6 mln plików od sześciu cypryjskich dostawców usług finansowych i jednej łotewskiej firmy sprzedającej dokumenty rejestrowe): ok. 800 spółek i trustów w jurysdykcjach „secrecy-friendly" powiązanych z sankcjonowanymi Rosjanami, w tym **ponad 650 cypryjskich**; PwC Cyprus przed inwazją miał 12 sankcjonowanych rosyjskich klientów, po inwazji kolejnych 39; PwC zakończył ok. 150 relacji po 2022 r. (60 z powodów sankcyjnych, 90 w przeglądzie „de-risking"). Zarzuty dotyczą m.in. przeniesienia udziałów przez Abramowicza, zaplecza dla Mordaszowa (1,4 mld USD) i Awena (źródło: strona ICIJ – otwarta).
  - **Nominowani dyrektorzy i „frontmen"** w małych firmach usługowych (ICIJ, j.w.).
  - **Sankcje USA i UK** nałożone na **13 cypryjskich osób i firm** uznanych za pomocników rosyjskich oligarchów, w tym prawników i księgowych tworzących sieci trustów i spółek-przykrywek (wynik wyszukiwania – źródło wtórne, nie otwarte; zweryfikować listy OFAC/OFSI).
  - **Dane o rezydencjach (2025):** Rosjanie prowadzili liczbą wydanych zezwoleń pobytu – wg Dom.com.cy 40 735 z 175 677 (stan na 30.09.2025), co daje ok. 23% (źródło wtórne, do sprawdzenia w statystykach MSW Cypru). Wg rosyjskiego raportu (Business Petersburg, cytowanego przez Cyprus Mail) Rosjanie kupili 51% zagranicznych nieruchomości mieszkalnych na Cyprze w 2025 r. – **źródło rosyjskie, traktować ostrożnie**.
- **Ostatnie działania Cypru:**
  - **Ustawa 149(I)/2025** (*Criminalization of the Violation of the Restrictive Measures of the EU Law of 2025*, z 25.07.2025) – kryminalizacja naruszeń unijnych środków; kary do 40 mln EUR i do 5 lat więzienia za poważne przypadki; obejmuje też ukrywanie własności lub kontroli nad aktywami objętymi sankcjami (źródło: Mondaq/prawnicy, wyniki wyszukiwania).
  - **Ustawa 150(I)/2025** – powołanie **NSIU / EMEK** (National Sanctions Implementation Unit) pod Ministerstwem Finansów: egzekwowanie sankcji UE, ONZ i krajowych; kary administracyjne do 100 000 EUR + 100 EUR/dzień (źródło: Mondaq). Pełnej operacyjności nie potwierdzono.
  - **Sankcje krajowe:** prawna podstawa do własnych sankcji istnieje; **nie znaleziono publicznej krajowej listy osób objętych sankcjami** – traktuj listy UE/ONZ/OFAC/UK jako obowiązkowe.
  - **Zgłoszenia i postępowania:** w mediach wspomina się o dochodzeniach Rejestratora Spółek i Izby Adwokackiej w sprawie próby obejścia sankcji (źródło wtórne, nie potwierdzone w źródle urzędowym); Politis (2025–2026) opisuje dalsze przypadki firm cypryjskich powiązanych z kapitałem z otoczenia Putina (wynik wyszukiwania, nie otwarty).
  - **Pakiet 20 UE (kwiecień 2026):** wg relacji (wynik wyszukiwania) obejmuje ograniczenia wobec czterech banków trzecich i pierwsze użycie narzędzia antyobejściowego – kraj nie jest wymieniony jako sankcjonowany.
- **Na co zwrócić uwagę w strukturze właścicielskiej (dla Cypru):**
  - spółka cypryjska jako właściciel pośredni nad spółką z RU/BY lub z kapitałem rosyjskim;
  - trust lub fundacja z trustee w Cyprze, a beneficjentem rezydent RU/BY lub osoba z rosyjskim paszportem/rezydencją cypryjską uzyskaną po 2022 r.;
  - nominowani dyrektorzy (ten sam nazwisko w wielu spółkach, usługodawca fiducjarny jako dyrektor);
  - zmiana właściciela/dyrektorów po 24.02.2022 r.;
  - płatności z kont cypryjskich od osób trzecich, zwłaszcza z bankowości w Limassol/Nikozji.
- **Co ZAWSZE oznaczyć flagą „RU/BY”:** każda firma z Cypru, której beneficjent, dyrektor lub udziałowiec ma rosyjskie lub białoruskie obywatelstwo, adres w RU/BY lub zarejestrowaną siedzibę w RU/BY; każda struktura z cypryjską spółką pośrednią i beneficjentem z RU/BY; każde zlecenie płatności od podmiotu z Cypru, jeśli beneficjent nie jest jasny.

## 9. Procedura krok po kroku (checklist)

1. Pobierz od klienta odpis (Certificate of Incorporation / Good Standing) z datą nie starszą niż 3 miesiące; sprawdź, czy ma numer HE, nazwę i daty.
2. Wejdź na `companies.gov.cy` → e-wyszukiwarka (sekcja 2). Wpisz numer HE; porównaj nazwę, status, adres, dyrektorów z odpisem. Zrzut ekranu z datą.
3. Jeśli rozbieżność lub status inny niż „aktywna" – stop, eskalacja.
4. Opcjonalnie (~10 EUR): pełne wyszukanie historii pliku – zapisz udziały historyczne i daty zmian.
5. Poproś o statut, umowę wspólników i wyciąg z rejestru udziałowców (*Register of Members*). Porównaj z e-wyszukiwarką.
6. Ustal beneficjentów: wymagaj **oświadczenia UBO** (sekcja 6, procedura zastępcza) + potwierdzenie zgłoszenia do rejestru DRCOR (zrzut, nie treść). Brak zgłoszenia = odmowa lub EDD.
7. Sprawdź VAT w VIES (`ec.europa.eu/taxation_customs/vies`). Zapisz wynik ze zrzutem; sprawdź zgodność nazwy i adresu.
8. Screening sankcyjny: EU Sanctions Map, OFAC, UK, ONZ, OpenSanctions – firma, dyrektorzy, UBO, adres. Zapisz wynik z datą.
9. Flaga RU/BY (metodyka pkt 4) + sekcja 8 tego dokumentu – jeśli choć jeden wskaźnik, wzmocniona weryfikacja.
10. Sprawdź adres (mapa, czy to biuro czy wirtualne biuro), stronę WWW i domenę e-mail (zgodność z firmą).
11. Dla zamówień od podmiotów z Cypru: jeśli struktura ma spółkę pośrednią lub trust – EDD i kontrola czterech oczu.
12. Odnotuj decyzję i dowody (data, źródło, numer zapytania VIES, zrzuty). Odśwież dokument raz na 6 miesięcy lub przy zmianie sytuacji.

## 10. Ograniczenia i ryzyka

- **Nie da się za darmo:** UBO (rejestr zamknięty dla nas), pełna historia udziałów (10 EUR), statut i sprawozdania (opłaty za odpisy – cennik nie potwierdzony), status upadłości (nie potwierdzono publicznego dostępu), zaległości podatkowe (zwykle niedostępne).
- **Płatna alternatywa jako ostatnia opcja:** agregator (np. Kyckr, opisany jako dostęp do rejestrów wielu krajów) – orientacyjnie nieznany koszt; **nie potwierdzono cennika ani zakresu cypryjskiego** (strona Kyckr otwarta, nie zawiera danych o Cyprze). Prawnik/doradca z Cypru z uprawnieniami – koszt do ustalenia.
- **Opóźnienia danych:** rejestr aktualizuje się po złożeniu dokumentów; zmiany UBO są zgłaszane do DRCOR z opóźnieniem; sprawozdania roczne mogą być opóźnione.
- **Zmiany prawne:** w 2026 r. trwa przebudowa dostępu do UBO (konsultacja CySEC, ustawa 25(I)/2026 – wg źródła wtórnego). Stan może się zmienić między researchem a decyzją – sprawdzić przed użyciem.
- **Język i transliteracja:** nazwy po grecku (w VIES często) i po rosyjsku (u beneficjentów) – ryzyko błędu przy transliteracji, zwłaszcza przy nazwiskach z cyrylicy. Porównuj także w alfabecie oryginalnym.
- **Źródła wtórne:** część informacji (historia dostępu do UBO, stawki, sankcje krajowe, NSIU) pochodzi z komercyjnych blogów i kancelarii – traktuj jako wskazówkę, nie dowód.
- **Kiedy eskalować do EDD:** RU/BY w łańcuchu; trust lub spółka pośrednia w jurysdykcji trzeciej; brak zgłoszenia UBO; zmiany właściciela po 2022 r.; rozbieżność odpisu z rejestrem; towar objęty restrykcjami.
- **Status FATF/EU:** z wyników wyszukiwania wynika, że Cypr **nie jest na liście FATF „increased monitoring" ani „call for action"** (luty 2026: dodano Kuwejt i Papuę-Nową Gwineę, nikogo nie usunięto – źródło: CGC Cyprus, wynik wyszukiwania) i nie jest na unijnej liście państw trzecich wysokiego ryzyka (państwa członkowskie UE nie są na niej z definicji). **Strona FATF (`fatf-gafi.org/en/countries/detail/Cyprus.html`) zwróciła 403 – nie potwierdzono bezpośrednio; sprawdzić ręcznie.** MONEYVAL: follow-up z czerwca 2025 odnotował postępy (wynik wyszukiwania).

## 11. Źródła

- [Strona DRCOR – Searching the Business Register](https://companies.gov.cy/en/company-lifecycle/search-for-company-information) – oficjalne – otwarte w czasie researchu: tak
- [DRCOR – Online search system (artykuł z 2011 r., nieaktualny cennik)](https://www.companies.gov.cy/en/knowledgebase/online-search-system) – oficjalne (archiwalne) – otwarte: tak
- [Harris Kyriakides – Access to Cyprus UBO register restored for obliged entities (17.01.2023)](https://www.harriskyriakides.law/insights/news/access-to-cyprus-ubo-register-restored-for-obliged-entities) – nieoficjalne (kancelaria) – otwarte: tak
- [Cyprus Mail – CySEC proposes limits on access to beneficial ownership data (06.03.2026)](https://cyprus-mail.com/2026/03/06/cysec-proposes-limits-on-access-to-beneficial-ownership-data) – nieoficjalne (prasa) – otwarte: tak
- [HCCH – Status table, Konwencja Apostille (cid=41)](https://www.hcch.net/en/instruments/conventions/status-table/?cid=41) – oficjalne (międzynarodowe) – otwarte: tak
- [ICIJ – Cyprus Confidential, about the investigation (14.11.2023)](https://www.icij.org/investigations/cyprus-confidential/about-cyprus-confidential-investigation/) – nieoficjalne (dziennikarskie, ICIJ) – otwarte: tak
- [Kyckr – Cyprus UBO Register Guide 2025](https://www.kyckr.com/blog/cyprus-registry-company-search-ubo-guide-2025) – komercyjne – otwarte: tak (brak danych o Cyprze w treści; nie używać jako źródła faktów)
- [e-Justice – Bankruptcy and insolvency registers, Cyprus](https://e-justice.europa.eu/topics/registers-business-insolvency-land/bankruptcy-and-insolvency-registers/cy_en) – oficjalne (UE) – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [CGC Cyprus – FATF February 2026: Kuwait and Papua New Guinea added to grey list](https://www.cgc.org.cy/en/fatf-february-2026-kuwait-and-papua-new-guinea-added-to-grey-list/) – oficjalne (Cypryjska Komisja Giełdy/regulator) – otwarte: nie (wynik wyszukiwania)
- [FATF – Cyprus country page](https://www.fatf-gafi.org/en/countries/detail/Cyprus.html) – oficjalne – otwarte: **nie (HTTP 403)**
- [VIES – ec.europa.eu/taxation_customs/vies](https://ec.europa.eu/taxation_customs/vies) – oficjalne (UE) – otwarte: nie (z metodyki)
- [GLEIF Search – search.gleif.org](https://search.gleif.org) – oficjalne – otwarte: nie (z metodyki)
- [OpenOwnership – Cyprus](https://www.openownership.org/en/map/country/cyprus/) – nieoficjalne (organizacja) – otwarte: nie (wynik wyszukiwania; źródło progu 25%)
- [Dom.com.cy – residence permits 2025](https://dom.com.cy/en/live/digest/russians-are-the-main-recipients-of-cyprus-residence-permit-in-2025) – nieoficjalne (prasa) – otwarte: nie (wynik wyszukiwania)
- [Politis – Cyprus under scrutiny in new Russian sanctions probe](https://en.politis.com.cy/economy/982239/cyprus-under-scrutiny-in-new-russian-sanctions-probe) – nieoficjalne (prasa) – otwarte: nie (wynik wyszukiwania)
- [Mondaq – Cyprus launches National Sanctions Implementation Unit](https://www.mondaq.com/cyprus/fin-tech/1654030/cyprus-launches-national-sanctions-implementation-unit) – nieoficjalne (kancelarie) – otwarte: nie (wynik wyszukiwania)
- [Mondaq – New sanctions law in Cyprus (criminalisation law 2025)](https://www.mondaq.com/cyprus/crime/1705244/new-sanctions-law-in-cyprus-the-criminalization-of-violation-of-union-restrictive-measures-law-of-2) – nieoficjalne (kancelarie) – otwarte: nie (wynik wyszukiwania)
- [Kyckr – Cyprus company registry search](https://kyckr.com/guides-and-reports/cyprus-company-registry-search) – komercyjne – otwarte: nie (wynik wyszukiwania)
- [Business Petersburg / Cyprus Mail – Russians lead foreign property buyers (14.07.2026)](https://cyprus-mail.com/2026/07/14/russians-remain-leading-foreign-property-buyers-in-cyprus) – nieoficjalne (prasa; źródło rosyjskie) – otwarte: nie (wynik wyszukiwania)
