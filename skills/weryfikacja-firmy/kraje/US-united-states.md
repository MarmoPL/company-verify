# Stany Zjednoczone (US) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia (prawo federalne o BOI – wysoka; dane o konkretnych rejestrach stanowych – niska/średnia, większość potwierdzona tylko wynikami wyszukiwarki) · Ryzyko jurysdykcji: podwyższone (brak publicznego rejestru beneficjentów rzeczywistych; struktury LLC „słupów” w wielu stanach)

## 1. Najkrótsza ścieżka (TL;DR)

- **Nie ma jednego rejestru firm.** Każdy z 50 stanów (oraz DC i terytoria) prowadzi własny rejestr. Właściwy stan to ten, w którym firma została założona (zapisany w odpisie / na fakturze jako „State of formation”, „organized under the laws of…”, „a Delaware corporation” itp.). Samo miejsce prowadzenia działalności to co innego.
- **Za darmo w większości stanów:** nazwa, numer rejestrowy, status (nie we wszystkich), data utworzenia, adres i agent rejestrowy (registered agent). Nazwiska zarządu/członków są jawne tylko w niektórych stanach (np. Floryda) – patrz sekcja 5.
- **Za darmo zwykle nie ma:** certyfikatu dobrego standingu (good standing / certificate of status), apostille, kopii dokumentów założycielskich, danych o beneficjentach.
- **Beneficjenci rzeczywiści:** publicznego rejestru UBO w USA nie ma. Od 14.08.2026 obowiązuje ostateczna zasada FinCEN, która zwalnia firmy krajowe z obowiązku raportowania BOI (sekcja 6). Praktycznie: dane o właścicielach trzeba pozyskać od klienta i sprawdzić krzyżowo.
- **Najlepsza darmowa weryfikacja dla hurtowni:** (a) wyszukanie w rejestrze stanowym (nazwa + numer), (b) wydruk/PDF z rejestru lub certyfikat od klienta wraz z numerem kontrolnym, (c) EIN od klienta z dokumentem CP 575 lub Letter 147C, (d) sprawdzenie OFAC (darmowe), (e) oświadczenie klienta o beneficjentach z dokumentami (sekcja 6).

## 2. Rejestr firm (główny)

**Brak rejestru centralnego – rejestry prowadzą stany.** Typ: stanowe (organ: Secretary of State lub Division of Corporations, zależnie od stanu). Najczęściej spotykane w handlu z firmami z USA:

| Stan | Organ / rejestr | Adres (status) | Uwagi z researchu |
|---|---|---|---|
| **Delaware** | Division of Corporations (Department of State) | https://icis.corp.delaware.gov/ecorp/entitysearch/namesearch.aspx – **otwarte** | Najczęstszy stan założenia spółek i LLC. Wyszukiwanie po nazwie lub numerze pliku (File Number). Za darmo: nazwa, numer pliku, data utworzenia, agent rejestrowy (nazwa, adres, telefon), rezydencja. Strona NIE pokazuje statusu wprost ani zarządu. Certyfikaty i kopie – płatne (kwoty niepotwierdzone). |
| **Wyoming** | Secretary of State – WyoBiz | https://wyobiz.wyo.gov/Business/FilingSearch.aspx – **otwarte** (strona wymagała przepisania kodu z obrazka) | Wyszukiwanie po nazwie lub Filing ID, bez konta. Wg wyników wyszukiwarki pokazuje status, agenta rejestrowego i historię dokumentów. Nie potwierdzono, czy pokazuje członków/zarząd. |
| **Nevada** | Secretary of State – Business Search (SilverFlume / portal Orion) | esos.nv.gov przekierowuje na https://orion.nv.gov/ – **otwarte, treść pusta, nie potwierdzono** | Wg wyników wyszukiwarki (nieoficjalnie): bezpłatne wyszukiwanie po nazwie, numerze, nazwisku zarządcy lub agencie; zarządcy/dyrektorzy wg źródeł wtórnych widoczni, choć źródła są sprzeczne co do domyślnego wyświetlania. Certyfikaty – płatne. |
| **Floryda** | Division of Corporations – Sunbiz | search.sunbiz.org oraz dos.fl.gov/sunbiz/ – **nie otwarto (HTTP 403)** | Wg wyników wyszukiwarki (nieoficjalnie): bezpłatne wyszukiwanie po nazwie, nazwisku osoby, agencie lub numerze FEI/EIN i numerze dokumentu; widoczni funkcjonariusze/członkowie z raportów rocznych. Źródła podają, że historia raportów rocznych sięga ok. 3 lat – nie potwierdzono. |
| **Teksas** | Secretary of State (SOS Direct Search) – corp | https://www.sos.state.tx.us/corp/sosda/index.shtml – **otwarte** | Strona podaje **opłatę 1,00 USD za wyszukanie** – czy dotyczy tej wyszukiwarki, czy tylko SOSDirect: nie potwierdzono. Nie potwierdzono zakresu wyników. |
| **Teksas (status podatkowy)** | Comptroller of Public Accounts – Franchise Tax Account Status | https://comptroller.texas.gov/taxes/franchise/account-status/search – adres z wyników wyszukiwarki (oficjalna domena), **nie otwarto** | Darmowe. Wyszukanie po numerze podatkowym (11 cyfr), EIN (9 cyfr), nazwie lub numerze SOS. Pokazuje status prawa do działania w Teksasie („Franchise Tax Account Status”), można wydrukować i zobaczyć Public Information Report (według pomocy urzędu; czy zawiera zarząd – nie potwierdzono). |
| **Kalifornia** | Secretary of State – bizfile Online | https://bizfileonline.sos.ca.gov/ – **otwarte, treść pusta** | Nie potwierdzono zakresu darmowego (status, agent, dane zarządu) ani opłat. Sprawdzić ręcznie. |
| **Nowy Jork** | Department of State – Corporation & Business Entity Database | dos.ny.gov/corps/bus_entity_search.html (przekierowanie HTTP, **nie otwarto**) | Nie potwierdzono zakresu darmowego ani opłat. Sprawdzić ręcznie. |

Ogólnie: wyszukiwanie po **nazwie** działa w każdym stanie, po **numerze rejestrowym** – także. Wyszukiwanie po **osobie** (nazwisku członka/zarządu) działa tylko tam, gdzie stan publikuje dane osób (np. Floryda, Nevada wg źródeł wtórnych) – nie potwierdzono dla pozostałych.

- **Format numeru:** nie ma jednego formatu. Delaware – numer pliku (File Number), format nie potwierdzony. Teksas – numer SOS i numer podatkowy 11-cyfrowy (zaczyna się od 1 lub 3, wg pomocy urzędu – źródło wtórne). **Identyfikator federalny: EIN – 9 cyfr w formacie XX-XXXXXXX** (format zgodny z powszechną praktyką IRS; sprawdzić w IRS.gov).
- **Jak sprawdzić, czy numer w ogóle istnieje:** wyszukać nazwę i numer w rejestrze stanu deklarowanego na dokumencie. Brak wyniku = czerwona flaga (sprawdzić, czy nie ma literówki lub innego stanu).

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwa dokumentu:** w USA nie ma jednego „odpisu z rejestru”. Typowe dokumenty to:
  - **Certificate of Good Standing** (Delaware, Wyoming, Nevada – „Certificate of Good Standing”; Floryda – „Certificate of Status”; Teksas – „Certificate of Account Status” / dawniej „Certificate of Fact”) – tłumaczenie: **zaświadczenie o dobrym standingu / statusie**.
  - **Certified copy of Certificate of Formation / Articles of Incorporation / Articles of Organization** – **poświadczony odpis aktu założycielskiego**.
  - **Certificate of Incumbency** – zaświadczenie o osobach uprawnionych do reprezentacji (nie zawsze wystawiane przez stan; często przez sekretarza spółki).
  - Odpis z rejestru z „sądu” – **nie dotyczy USA** (rejestr jest stanowy, nie sądowy).
- **Kto wystawia:** organ rejestrowy stanu (Secretary of State / Division of Corporations) lub, dla odpisów poświadczonych, również ten organ. Sekretarz spółki lub prawnik może wystawić zaświadczenie o umocowaniu – to nie jest dokument rejestrowy i wymaga weryfikacji (sekcja 5).
- **Cechy autentyczności:** pieczęć stanu, podpis urzędnika, numer dokumentu/kontrolny (np. „verification code” lub „certification number”), data wystawienia. Nie potwierdzono szczegółów cech dla każdego stanu – sprawdzić na stronie stanu.
- **Weryfikacja online:**
  - Delaware: w Division of Corporations zapytanie po nazwie/numerze pliku (sekcja 2). Certyfikat z numerem można poprosić o weryfikację tylko przez stronę urzędu, której nie otwarto w całości – **nie potwierdzono** darmowego narzędzia do weryfikacji autentyczności certyfikatu.
  - Dla każdego stanu: porównać nazwę, numer, datę utworzenia i agenta z wynikiem wyszukiwania w rejestrze tego samego stanu. To jest jedyna darmowa, pewna kontrola.
- **Apostille (Konwencja haska):** USA są stroną Konwencji (potwierdzone wynikami wyszukiwarki z dokumentów stanowych; stanowe urzędy wystawiają apostille na dokumentach własnego stanu, np. Wyoming – płatne, 5–7 dni wg źródła wtórnego; Delaware – strona corp.delaware.gov/apost/ z wyników wyszukiwarki, nieotwarta). **Apostille nie jest zwykle wymagany do faktury w Polsce.** Potrzebny może być, gdy wymaga go umowa lub bank. Apostille wystawia stan, który wydał dokument, nie federalne Department of State (dla dokumentów stanowych – potwierdzone wynikami).
- **Legalizacja/tłumaczenie:** w Polsce wymagane jest tłumaczenie przysięgłe na język polski, jeżeli dokument ma mieć skutek urzędowy; nie potwierdzono wymogu dla faktur handlowych.
- **Typowe sygnały podróbki/nieaktualności:**
  - odpis bez numeru, bez daty, bez pieczęci stanu, wystawiony przez „agencję” zamiast urzędu stanu,
  - nazwa spółki z dodatkami („Inc.” / „LLC” / „Corp.”) różna od rejestrowej,
  - agent rejestrowy zmieniony w ostatnich miesiącach bez wyjaśnienia,
  - dokument z „Certificate of Formation” sprzed lat jako dowód aktualnego statusu (nie jest dowodem statusu!).
- **Ważność:** wg źródeł wtórnych certyfikaty z Delaware są zwykle akceptowane przez ok. 60 dni (niektóre instytucje wymagają 30 dni). **Praktyka dla hurtowni: akceptować ≤ 3 miesięcy od wystawienia**, a dla nowych kontrahentów – wyszukanie w rejestrze w dniu zawarcia umowy (darmowe).

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy:** w każdym stanie są inne nazwy. Typowe: aktywna/active/good standing; zawieszona/suspended/forfeited (np. za brak raportów rocznych lub podatków) ; rozwiązana/dissolved/cancelled/inactive; w likwidacji/winding up. Nie potwierdzono listy statusów dla każdego stanu – sprawdzić na stronie stanu. **Uwaga:** Delaware na stronie wyszukiwania wprost zastrzega, że wynik „nie jest wskazaniem obecnego statusu” – status trzeba sprawdzić osobno (certyfikat lub online status check; źródła wtórne wskazują corp.delaware.gov/onlinestatus – nie potwierdzono).
- **Upadłość (bankruptcy):** publiczne akta upadłościowe są w sądach federalnych – system **PACER** (płatny, opłata per strona; nie potwierdzono aktualnej stawki w researchu, sprawdzić na pacer.uscourts.gov). Darmowe: wyszukiwarka sądu przez „Case Locator” – nie potwierdzono w researchu. Dla skarg/sporów: wyszukiwanie w sądach stanowych (osobno, bez jednego indeksu).
- **Zaległości podatkowe:** brak publicznego rejestru zaległości federalnych IRS. W Teksasie – darmowy status Franchise Tax (sekcja 2) pokazuje, czy firma może działać. Pozostałe stany – nie potwierdzono publicznych wykazów zaległości.
- **Czerwone flagi specyficzne dla USA:**
  - **Słupy (nominee):** LLC zakładane przez agentów rejestrowych w Delaware/Wyoming/Nevada z adresem agenta jako „siedzibą” – sam adres agenta rejestrowego nie świadczy o rzeczywistej działalności.
  - **Shelf companies** i firmy „na sprzedaż” z pustymi sprawozdaniami.
  - **Adresy masowej rejestracji** (np. jeden adres biurowy z setkami firm; nie potwierdzono baz takich adresów – sprawdzić przez wyszukanie adresu w rejestrze stanu).
  - Firma zarejestrowana kilka dni przed zamówieniem, zmiana właściciela lub agenta bezpośrednio przed transakcją.
  - Rozbieżność między stanem założenia a adresem prowadzenia działalności bez wyjaśnienia.

## 5. Zarząd, wspólnicy, reprezentacja

- **Kto reprezentuje:** dla spółek kapitałowych (Corporation/Inc.) – officers i directors, dla LLC – managers lub members. **Zakres publicznego ujawnienia zależy od stanu** (patrz tabela sekcji 2): Floryda i Nevada publikują osoby zarządzające (wg źródeł wtórnych); Delaware na stronie wyszukiwania nie wymienia zarządu; pozostałe – nie potwierdzono.
- **Sposób reprezentacji** (kto może podpisać umowę, czy jednoosobowo, czy łącznie): nie wynika z rejestru stanowego w sposób standardowy – **sprawdzić w dokumencie wewnętrznym**: operating agreement (LLC) lub bylaws + uchwała (corporation). Dla Florydy – raport roczny wskazuje osoby, ale nie zawsze sposób reprezentacji.
- **Pełnomocnictwo / Certificate of Incumbency:** żądać od klienta, z numerem kontrolnym, i sprawdzić, czy podpisujący figuruje w rejestrze stanu (Floryda/Nevada) – w innych przypadkach porównać z dokumentami wewnętrznymi.
- **Wspólnicy/akcjonariusze:** w większości stanów **nie są publiczni** (Delaware: certyfikat założycielski nie zawiera członków/zarządu – podstawa: 6 Del. C. § 18-201, wg źródła wtórnego; nie potwierdzono bezpośrednio w ustawie). Członkowie LLC mogą figurować w dokumencie tylko, jeśli sami to wpisali.
- **Dokumenty założycielskie / sprawozdania finansowe:**
  - Akt założycielski: dostępny za opłatą w większości stanów (Delaware – płatne; szczegóły nie potwierdzone).
  - Sprawozdania finansowe: prywatne spółki zwykle **nie publikują** sprawozdań. Spółki publiczne (SEC) – darmowo na **EDGAR** (sec.gov/edgar/search – otwarte; wyszukanie po nazwie, CIK, typie raportu; w wynikach 10-K/8-K/proxy – nie potwierdzono bezpośrednio na stronie, ale jest to standardowy zakres EDGAR).
  - Sprawozdania roczne stanowe (np. Floryda) – darmowe w wyszukiwarce, ograniczone historycznie (nie potwierdzono).

## 6. Beneficjenci rzeczywiści (UBO)

- **Czy istnieje rejestr beneficjentów rzeczywistych?** Brak publicznego rejestru UBO. Federalny rejestr **BOI (Beneficial Ownership Information)** prowadzony przez **FinCEN** na podstawie Corporate Transparency Act (CTA) **nie jest publiczny** – nawet w pierwotnej konstrukcji dostęp miały wyłącznie organy i instytucje finansowe za zgodą klienta.
- **Stan prawny (potwierdzony na stronie FinCEN, researchu 2026-11-16):**
  - **1 marca 2024:** w sprawie *National Small Business United v. Yellen* sąd federalny wydał wyrok deklaratoryjny; rząd nie egzekwuje CTA wobec powodów (wg fincen.gov/boi).
  - **21 marca 2025:** FinCEN ogłosił zwolnienie z obowiązku raportowania BOI dla firm amerykańskich i osób amerykańskich.
  - **26 marca 2025:** opublikowano interim final rule (tymczasowy przepis) – zwolnienie domestic reporting companies.
  - **25 kwietnia 2025:** termin zgłoszenia dla zagranicznych firm zarejestrowanych przed 26.03.2025 (wg fincen.gov/boi).
  - **11 sierpnia 2026:** FinCEN wydał **final rule** („Beneficial Ownership Information Reporting Requirement Revision”); dokument w public inspection o numerze 2026-16576 (wg fincen.gov/boi). Numer Federal Register podany w wynikach wyszukiwarki (91 FR 52508, RIN 1506-AB67) – **nie potwierdzono w źródle urzędowym**.
  - **14 sierpnia 2026:** final rule w mocy. **Firmy krajowe (U.S. companies) są zwolnione** z raportowania; osoby amerykańskie nie muszą podawać BOI spółkom zagranicznym i nie są raportowane przez zagraniczne spółki w zakresie swoich danych; osoby z FinCEN ID nie muszą aktualizować wcześniej podanych danych. FinCEN ma też usunąć dotychczasowe BOI dotyczące osób amerykańskich (wg źródeł prawniczych – do potwierdzenia w Federal Register).
  - **Zagraniczne spółki** (foreign reporting companies) nadal raportują – tylko w zakresie beneficjentów będących osobami nieamerykańskimi (ok. 28 000 podmiotów wg szacunku FinCEN, wg źródła wtórnego).
- **Dostęp:** w praktyce **brak darmowego dostępu** do danych o beneficjentach dla firm handlowych (także wcześniej nie było publicznego dostępu). Dostęp dla instytucji finansowych – w ramach CDD rule (31 CFR 1010.230) – nie dotyczy hurtowni.
- **Czy darmowy:** **nie** – nic do wyszukania bezpłatnie. Dane widoczne tylko w rejestrze stanowym (sekcja 2): nazwa, agent, czasem zarząd.
- **Próg beneficjenta:** w przepisach CDD (dla instytucji finansowych) próg to zwykle 25% udziałów lub kontroli; **nie potwierdzono w researchu** (nie znaleziono tekstu 31 CFR 1010.230 w tej sesji) – sprawdzić na ecfr.gov przed użyciem.
- **Trusty i fundacje:** w USA nie ma rejestru publicznego trustów; nie potwierdzono wymogów jawności dla fundacji (fundacje non-profit mają publiczne dane w IRS Tax Exempt Organization Search – nie potwierdzono na stronie w tej sesji).

**Procedura zastępcza (obowiązkowa, bo rejestr UBO nie istnieje):**

1. Oświadczenie klienta o beneficjentach rzeczywistych: pełne dane każdej osoby fizycznej posiadającej ≥ 25% udziałów lub prawa kontroli (imię, nazwisko, data urodzenia, kraj, adres, % udziałów, rodzaj kontroli) – podpisane przez osobę uprawnioną do reprezentacji.
2. Dokument udziałowców: **member register** (LLC) lub **stock ledger / register of shareholders** (corporation) – z datą aktualności.
3. **Operating agreement** (LLC) lub **bylaws** i ostatnia uchwała o zmianie udziałowców.
4. **Schemat struktury właścicielskiej** (łańcuch do osób fizycznych; jeśli właściciel jest inną firmą – każda kolejna warstwa z numerem rejestrowym i stanem).
5. Certyfikat dobrego standingu / certyfikat statusu z rejestru stanu (nie starszy niż ok. 3 miesiące).
6. Dokument tożsamości osoby podpisującej (paszport/ID) i wyciąg/pełnomocnictwo do reprezentacji.
7. **Krzyżowa weryfikacja** darmowymi źródłami: rejestr stanu (nazwiska zarządu, jeśli publiczne); **EDGAR** (spółki publiczne); **GLEIF** (search.gleif.org – LEI, dla większych firm; strona nie otwarta w pełni – sprawdzić ręcznie); **SAM.gov** (UEI – dla kontrahentów federalnych; strona nie otwarta w pełni – sprawdzić ręcznie); **OFAC** (sekcja 8).
8. Wizja lokalna/kontakt przez numer z oficjalnej strony firmy, nie z dokumentu klienta.
9. Jeżeli struktura ma warstwy spółek zagranicznych – wymagać tego samego zestawu dla każdej warstwy.
10. Eskalacja, gdy: właściciel w jurysdykcji wysokiego ryzyka, nominee directors/shareholders, zmiana właściciela tuż przed transakcją, brak możliwości potwierdzenia nazwisk (EDD).

## 7. Dodatkowe darmowe weryfikacje

- **Numer podatkowy (EIN):** brak darmowej wyszukiwarki EIN innej firmy. Wg wyników wyszukiwarki IRS nie udostępnia internetowego potwierdzenia EIN dla osób trzecich (nie potwierdzono bezpośrednio na irs.gov). **Sposób weryfikacji:** dokument CP 575 (wydany przy nadaniu EIN) lub **Letter 147C** (duplikat; wg źródeł wtórnych wydawany na telefon 800-829-4933 dla upoważnionej osoby – nie potwierdzono na irs.gov). Numer EIN na fakturze musi zgadzać się z dokumentem IRS i nazwą w rejestrze stanu.
- **VAT:** USA nie mają VAT. Brak odpowiednika VIES.
- **Numer w rejestrze celnym (EORI itp.):** nie dotyczy; w USA odpowiednikiem jest **importer number (IRS EIN lub CBP-assigned)** – nie potwierdzono szczegółów.
- **LEI (GLEIF):** zwykle tylko większe firmy; sprawdzenie na search.gleif.org (strona nie otwarta w pełni).
- **SAM.gov (UEI):** rejestracja dla kontrahentów federalnych; sprawdzenie statusu w SAM.gov (strona nie otwarta w pełni – nie potwierdzono, co jest bez logowania).
- **Licencje branżowe:** zależą od stanu i branży (np. FDA, CPSC dla niektórych towarów) – nie potwierdzono w researchu; sprawdzić wymogi dla konkretnego towaru.
- **Listy ostrzeżeń:** brak wspólnej federalnej listy nierzetelnych kontrahentów; **FTC** i **Better Business Bureau** (BBB) mają wyszukiwarki skarg – nie potwierdzono bezpośrednio w researchu.

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Najważniejsza luka:** brak publicznego rejestru beneficjentów oznacza, że nie da się łatwo wykryć rosyjskich/białoruskich właścicieli spółek amerykańskich. Ryzyko słupów (nominee shareholders, nominee directors, LLC z agentem rejestrowym) jest tu największe.
- **Krajowa lista sankcyjna:** brak krajowej listy niezależnej od OFAC; obowiązują listy OFAC (SDN i inne).
- **OFAC – darmowe narzędzie:** https://sanctionssearch.ofac.treas.gov/ (otwarte) – wyszukiwanie po nazwie, adresie, numerze ID, typie (Entity/Individual), programie i kraju, z ustawialnym progiem dopasowania. Strona zastrzega, że nie zastępuje należytej staranności. Bezpłatne pobranie list: SDN List i Consolidated Non-SDN List (z tej samej strony).
- **Zasada 50%:** podmiot, w którym blokowane osoby łącznie posiadają ≥ 50% (także pośrednio, wiele szczebli), jest sam objęty blokadą – nawet jeśli nie jest na liście. Nie ma publicznego rejestru takich podmiotów; trzeba prześledzić udziały (źródło: wyniki wyszukiwarki, opracowania prawnicze – nie oryginał OFAC; do sprawdzenia w wytycznych OFAC).
- **Kontrola bez udziałów** nie uruchamia zasady 50% automatycznie – wymaga osobnej analizy.
- **Co ZAWSZE oznaczyć flagą „RU/BY”:** każda firma, w której w zakresie udziałów, zarządu lub adresów pojawia się obywatelstwo, adres lub podmiot rosyjski/białoruski; agent rejestrowy lub adres wspólny z podmiotami objętymi sankcjami; firma założona w ostatnich 12 miesiącach z kapitałem wpłaconym z jurysdykcji wysokiego ryzyka; brak możliwości ustalenia beneficjentów.
- **Reeksport:** USA jako pośrednik – ryzyko przy sprzedaży towarów podwójnego zastosowania (EAR/BIS). Nie potwierdzono listy w tej sesji – sprawdzić Entity List BIS.

## 9. Procedura krok po kroku (checklist)

1. Ustalić stan założenia firmy z dokumentu (faktura, umowa, odpis). Jeśli nie podano – zapytać klienta na piśmie.
2. Wejść w rejestr tego stanu (sekcja 2), wyszukać po nazwie i po numerze; zapisać zrzut ekranu z datą.
3. Porównać: nazwę (z „Inc./LLC/Corp.”), numer, datę założenia, agenta rejestrowego, status (jeśli widoczny) z dokumentem klienta.
4. Poprosić klienta o certyfikat dobrego standingu / statusu wystawiony przez stan, nie starszy niż ok. 3 miesiące.
5. Sprawdzić EIN: poprosić o kopię CP 575 lub Letter 147C; porównać z nazwą i numerem stanowym.
6. Pobrać oświadczenie o beneficjentach rzeczywistych i dokumenty udziałowców (sekcja 6, procedura zastępcza, punkty 1–4).
7. Sprawdzić osoby reprezentujące: zarząd/członkowie w rejestrze stanu (jeśli publiczni) lub w dokumentach wewnętrznych; zweryfikować podpisującego dokument tożsamości.
8. Sprawdzić OFAC (nazwa firmy, każdy wskazany beneficjent i członek zarządu) i zapisać wynik z datą.
9. Dla spółek publicznych – EDGAR; dla firm z LEI – GLEIF; dla kontrahentów federalnych – SAM.gov (sprawdzić ręcznie).
10. Ocenić sygnały ostrzegawcze (sekcja 4) i zapisać je w karcie klienta.
11. Jeżeli struktura obejmuje zagraniczne podmioty lub nominee – zastosować EDD i wymagać dokumentów dla każdej warstwy.
12. Odnowić weryfikację co najmniej raz w roku lub przy zmianie nazwy, agenta, adresu lub właściciela.

## 10. Ograniczenia i ryzyka

- **Nie da się sprawdzić za darmo:** beneficjentów rzeczywistych, zaległości podatkowych federalnych, sprawozdań finansowych spółek prywatnych, pełnej historii statusów, oryginalnych aktów założycielskich (w większości stanów płatne). Płatna alternatywa tylko jako ostatnia opcja: certyfikaty i odpisy od stanu (opłaty wg urzędu, sprawdzić na stronie stanu); usługi komercyjne (np. wyszukiwania w bazach płatnych) – **nie testowano, nie podano cen**.
- **Płatne narzędzia w researchu:** Teksas – wyszukiwanie w SOS z opłatą 1,00 USD (wg strony urzędu; czy dotyczy tej wyszukiwarki – nie potwierdzono). PACER – płatny (stawka nie potwierdzona).
- **Opóźnienia danych:** rejestry stanowe bywają nieaktualne o kilka dni do tygodni; statusy mogą się zmienić po ostatnim raportowaniu.
- **Transliteracja i nazwy:** w USA nazwy są w alfabecie łacińskim; rozbieżności mogą wynikać z pisowni nazwisk w polskim (ł, ą, ę) i w paszportach. Porównywać po numerze, nie po nazwie.
- **Nazwa podobna do znanej firmy** – ryzyko podszywania się; zawsze sprawdzać numer i stan.
- **Brak centralnej bazy** oznacza, że firma o tej samej nazwie może istnieć w kilku stanach – zawsze podać stan.
- **Zmiany prawa:** CTA i przepisy FinCEN zmieniały się w 2024–2026 kilkukrotnie. Ta ocena odnosi się do stanu na 2026-11-16 i trzeba ją przeglądać co pół roku.
- **Nowy Jork – LLC Transparency Act:** wg wyników wyszukiwarki obowiązuje od 1 stycznia 2026 i po wecie gubernatora z grudnia 2025 obejmuje wyłącznie zagraniczne LLC prowadzące działalność w NY (daty w źródłach różnią się). Nie znaleziono informacji o zawieszeniu go sądownie; status po stycznia 2026 **nie potwierdzono** – sprawdzić na dos.ny.gov. Zagraniczne LLC z NY mogą mieć dodatkowe dane publiczne/niepubliczne do sprawdzenia.
- **Eskalacja do EDD:** gdy firma nie podaje beneficjentów, struktura zawiera zagraniczne spółki bez jawnych właścicieli, adres agenta rejestrowego jest wspólny dla setek podmiotów, pojawia się zmiana właściciela przed transakcją, lub klient unika wyjaśnienia.

## 11. Źródła

- [FinCEN – Beneficial Ownership Information (strona urzędu, aktualizacja 11.08.2026)](https://www.fincen.gov/boi) – oficjalne – otwarte w czasie researchu: tak
- [Delaware Division of Corporations – General Information Name Search](https://icis.corp.delaware.gov/ecorp/entitysearch/namesearch.aspx) – oficjalne – otwarte w czasie researchu: tak
- [WyoBiz – Business Filing Search (Wyoming SOS)](https://wyobiz.wyo.gov/Business/FilingSearch.aspx) – oficjalne – otwarte w czasie researchu: tak (strona z kodem weryfikacyjnym, bez treści wyszukiwarki)
- [Nevada Secretary of State – portal Orion](https://orion.nv.gov/) – oficjalne – otwarte w czasie researchu: tak, treść pusta
- [Texas Secretary of State – SOS Direct Search (corp)](https://www.sos.state.tx.us/corp/sosda/index.shtml) – oficjalne – otwarte w czasie researchu: tak
- [Texas Comptroller – Franchise Tax Account Status Search](https://comptroller.texas.gov/taxes/franchise/account-status/search) – oficjalne (adres z wyników wyszukiwarki) – otwarte w czasie researchu: nie
- [Delaware Division of Corporations – Apostille](https://corp.delaware.gov/apost/) – oficjalne (adres z wyników wyszukiwarki) – otwarte w czasie researchu: nie
- [California bizfile Online](https://bizfileonline.sos.ca.gov/) – oficjalne – otwarte w czasie researchu: tak, treść pusta
- [New York Department of State – Corporation and Business Entity Database](https://dos.ny.gov/corps/bus_entity_search.html) – oficjalne – otwarte w czasie researchu: nie (przekierowanie HTTP)
- [Florida Division of Corporations – Sunbiz](https://dos.fl.gov/sunbiz/) – oficjalne – otwarte w czasie researchu: nie (HTTP 403); wyszukiwarka: https://search.sunbiz.org/ – nie otwarta
- [OFAC – Sanctions List Search](https://sanctionssearch.ofac.treas.gov/) – oficjalne – otwarte w czasie researchu: tak
- [SEC – EDGAR Full-Text Search](https://www.sec.gov/edgar/search/) – oficjalne – otwarte w czasie researchu: tak
- [GLEIF – LEI Search](https://search.gleif.org/) – oficjalne – otwarte w czasie researchu: nie (tylko tytuł strony)
- [SAM.gov – wyszukiwarka podmiotów](https://www.sam.gov/search/) – oficjalne – otwarte w czasie researchu: nie (tylko tytuł strony)
- [U.S. Department of State – Authentications](https://www.state.gov/authentications) – oficjalne – otwarte w czasie researchu: nie (HTTP 403)
- Korporacyjne i prawnicze opracowania CTA/BOI (MoFo, Mayer Brown, Davis Polk, Morgan Lewis, Harvard Law School Forum) – nieoficjalne, wyniki wyszukiwarki – otwarte w czasie researchu: nie (tylko tytuły/fragmenty)
- Opracowania o Delaware, Floryda, Nevada, Teksas (ZenBusiness, UpCounsel, Bizee, Infobelpro, delawareinc.com i inne) – nieoficjalne, wyniki wyszukiwarki – otwarte w czasie researchu: nie
- [Learnsignal – US CDD Rule / FIN-2026-R001](https://www.learnsignal.com/blog/us-cdd-rule-31-cfr-1010-230-beneficial-ownership-legal-entity-customers-fin-2026-r001-exceptive-relief-faqs-guide/) – nieoficjalne – otwarte w czasie researchu: nie
- [Golenbock / Eckert Seamans – NY LLC Transparency Act](https://www.eckertseamans.com/legal-updates/new-yorks-llc-transparency-act-took-effect-january-1-2026-covering-non-u-s-llcs-only) – nieoficjalne – otwarte w czasie researchu: nie
