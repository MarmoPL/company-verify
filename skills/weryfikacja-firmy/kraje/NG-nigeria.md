# Nigeria (NG) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia · Ryzyko jurysdykcji: podwyższone (ocena własna na podstawie wyjścia z listy FATF i EU, ale z częstymi nadużyciami w fakturach i dużą skalą oszustw; nie ma sankcji państwowych wobec kraju)

## 1. Najkrótsza ścieżka (TL;DR)

- Rejestr firm: **CAC (Corporate Affairs Commission)**, portal publicznego wyszukiwania `search.cac.gov.ng` – wyszukiwanie po nazwie lub numerze RC; według źródeł wtórnych bez konta i opłat. Wejście bezpośrednio z przeglądarki nie zostało potwierdzone (strona zwróciła HTTP 403 na próbę otwarcia z narzędzia; nie potwierdzono – do sprawdzenia ręcznie).
- Za darmo widać (wg źródeł wtórnych): nazwę, numer RC, status, datę rejestracji, typ rejestracji. Wypisu z listą dyrektorów i adresem nie potwierdzono.
- Beneficjenci rzeczywiści: **rejestr PSC (Persons with Significant Control)** pod adresem `bor.cac.gov.ng` – na stronie FAQ podany próg **5%**. Wyszukiwanie po nazwie firmy lub numerze RC; wyszukiwanie po nazwisku osoby – źródła są sprzeczne.
- Za darmo **nie** ma: certyfikowanych odpisów (CTC, ok. ₦5 000 za dokument wg harmonogramu opłat z sierpnia 2025), raportów historycznych (₦20 000–30 000), „due diligence" self-service (₦50 000).
- Numer podatkowy: od 1.01.2026 zastąpiony 13-cyfrowym **Tax ID** wydawanym przez NRS. Portal `taxid.nrs.gov.ng` służy do pobrania własnego Tax ID przez NIN lub numer CAC – **nie potwierdzono, że działa jako publiczna weryfikacja cudzej firmy**.
- Jeśli odpis od klienta nie zgadza się z wyszukiwaniem w CAC albo brakuje numeru RC – nie przyjmować; poprosić o certyfikat z wyszukiwania w dniu weryfikacji.

## 2. Rejestr firm (główny)

- **Nazwa rejestru:** Rejestr przedsiębiorstw (Corporate Affairs Commission) – w źródłach „CAC Public Search" / „Company Registration Portal" (ICRP).
- **Organ prowadzący:** Corporate Affairs Commission (CAC), Abuja, na podstawie CAMA 2020 (Companies and Allied Matters Act 2020).
- **URL:** `https://search.cac.gov.ng` (wskazany w poradniku legit.ng – otwarty w czasie researchu: **nie**, błąd 403). Główna strona organu: `https://www.cac.gov.ng/` (zwrócona przez wyszukiwarkę, nie otwarta). Portal rejestracji i składania dokumentów: `icrp.cac.gov.ng` (wskazany przez legit.ng; nie otwarty).
- **Język:** interfejs w języku angielskim (nie potwierdzono wersji polskiej – oczywiste, że jest tylko angielska).
- **Typ rejestru:** centralny (jeden rejestr federalny dla spółek i LLP). Nazwy firm jednoosobowych (business names) są w osobnym rejestrze pod innym prefiksem numeru (BN) – nie potwierdzono szczegółów wyszukiwania BN na publicznym portalu.
- **Wyszukiwanie po:** nazwie (dopasowanie podobieństwa – źródło: wyszukiwanie po jednym słowie daje szerokie wyniki) oraz **numerze RC** (dokładne, zalecane). Wyszukiwanie po osobie – nie potwierdzono na portalu publicznym (patrz sekcja 6).
- **Wymagana weryfikacja reCAPTCHA** przed pokazaniem wyników (wg legit.ng i wyników wyszukiwania; sprawdzić ręcznie).
- **Za darmo (wg źródeł wtórnych):** nazwa, numer RC, status, data rejestracji, typ rejestracji (legit.ng, otwarty). Zwrócone w innym źródle: adres siedziby i dane zarejestrowanych funkcjonariuszy – **sprzeczne, nie potwierdzono** (do sprawdzenia ręcznie na żywym portalu).
- **Płatne / za opłatą:**
  - Certyfikowany odpis dokumentu lub wyciągu (CTC): **₦5 000** za dokument (harmonogram opłat wg Telegraph, obowiązuje od 1.08.2025; otwarty).
  - Raport historyczny z wyszukiwania: **₦20 000–30 000** za żądanie (Telegraph, otwarty).
  - Due diligence self-service: **₦50 000** (Telegraph, otwarty).
  - Szczegółowe wyszukiwania (dyrektorzy, udziały, obciążenia) w tabelach harmonogramu: ok. ₦10 000–20 000 – źródło wtórne, nie potwierdzono aktualnej stawki.
  - Opłata za publiczne wyszukiwanie podstawowe: według dokumentu CAC sprzed 2025 – darmowe; aktualna stawka nie potwierdzona (plik `Fees.pdf` zwrócił 404).
- **Format numeru:** dla spółek **RC** + cyfry (przykład podany w legit.ng: `RC0000011`); dla nazw firm (business names) prefiks **BN**. Liczbę cyfr i dokładny format nie potwierdzono w oficjalnym źródle – sprawdzić na kilku odpisach.
- **Uwaga:** certyfikat rejestracji nazwy firmy (BN) to co innego niż certyfikat inkorporacji (RC). Odpis z BN nie uprawnia do zawarcia umowy w imieniu spółki – nie potwierdzono wprost, zalecane zweryfikowanie typu dokumentu.

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwa lokalna dokumentu:** *Certificate of Incorporation* (certyfikat inkorporacji spółki, dla spółek) oraz *Certified True Copy* (CTC – odpis poświadczony) oraz *Certificate of Registration* (dla nazw firm). Polskie tłumaczenie: „certyfikat inkorporacji", „odpis poświadczony", „certyfikat rejestracji nazwy firmy".
- **Wystawca:** Corporate Affairs Commission.
- **Cechy autentyczności (wg źródeł wtórnych):**
  - Od pewnego czasu dokumenty CAC (certyfikaty inkorporacji i CTC) mają elektroniczny stempel certyfikacyjny z **kodem QR** (źródło wtórne – YouVerify/Legit; nie potwierdzono w oficjalnym dokumencie CAC). Kod QR nie został zweryfikowany przez nas; nie potwierdzono, dokąd prowadzi.
  - Numer RC drukowany na certyfikacie.
  - Nie potwierdzono: kodu weryfikacyjnego, pieczęci wodnej, podpisu kwalifikowanego.
- **Jak zweryfikować online za darmo:** wpisać numer RC (dokładniej niż nazwę) na `search.cac.gov.ng`, porównać nazwę, numer RC, datę rejestracji i status z odpisem. Zrzut ekranu lub wydruk do PDF (wskazówka z legit.ng).
- **Ograniczenie:** CAMA 2020 s. 41(7) pozwala CAC cofnąć certyfikat uzyskany w sposób nieprawidłowy (źródło wtórne – YouVerify/Lawpadi; nie potwierdzono w tekście ustawy). Zgodność rejestru z odpisem to mocny dowód, ale nie wyłączny.
- **Legalizacja / apostille:** Nigeria według źródeł wtórnych **nie jest stroną Konwencji haskiej o apostille** (kancelaria prawnicza; strona MSZ Białorusi – oba wtórne). Dokumenty wystawiane w Nigerii do użytku za granicą wymagają notariusza i uwierzytelnienia w MSZ Nigerii (Pay4Me, wtórne). **Dla samego sprawdzenia firmy legalizacja nie jest potrzebna.** Czy wymagana jest w konkretnym przypadku – nie potwierdzono (do ustalenia z klientem).
- **Sygnały podróbki / nieaktualności (ogólne, nie z oficjalnego źródła):**
  - numer RC niezgodny z nazwą w rejestrze albo brak wyniku przy dokładnym numerze,
  - odpis bez numeru RC, z nazwą „Ltd" niezgodną z formą w rejestrze,
  - rozbieżność między nazwą na odpisie a nazwą na fakturze/umowie,
  - odpis z datą sprzed kilku lat przy statusie zmienionym w rejestrze (wykreślona / nieaktywna).
- **Aktualność odpisu:** częstotliwość odświeżania – nie potwierdzono. Praktycznie: przyjąć wyszukiwanie z dnia weryfikacji; odpis traktować jako ważny ≤ 3 miesiące (zasada z szablonu).

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy w rejestrze (wg legit.ng i wyników wyszukiwania):** *Active* (aktywna), *Registered* (zarejestrowana – spotykane w poradniku obok „Active", nie potwierdzono różnicy), *Inactive* / *Dormant* (nieaktywna / uśpiona), *Struck Off* (wykreślona). Według legit.ng „Inactive" lub „Struck Off" oznacza brak dobrego statusu regulacyjnego i wymaga wyjaśnienia.
- **Likwidacja / upadłość / restrukturyzacja:** postępowania upadłościowe mają być zgłaszane do CAC po zatwierdzeniu przez sąd (źródło wtórne, Mondaq). **Nie potwierdzono**, czy wpisy o likwidacji/zarządcy są widoczne w publicznym wyszukiwaniu CAC. Nie znaleziono publicznego, przeszukiwalnego rejestru upadłości. Do sprawdzenia ręcznie: zapytać CAC lub sprawdzić w sądach (Federal High Court / sądy stanowe – nie potwierdzono zakres).
- **Zaległości podatkowe / ZUS / sądowe:** nie potwierdzono żadnego publicznego, darmowego źródła. Nie zakładać, że są dostępne.
- **Specyficzne red flags Nigerii (ocena ogólna, do traktowania ostrożnie):**
  - wysoka skala oszustw płatniczych i BEC – firmy-słupy zakładane pod wyłudzenia, fałszywe faktury z podobnymi nazwami do znanych firm,
  - nazwy zbliżone do znanych marek (np. z dodanym „Global", „International", „Nigeria Ltd") – weryfikować numer RC, nie nazwę,
  - konta bankowe przeniesione na osoby trzecie lub BDC zamiast firmy – zawsze sprawdzać, czy rachunek należy do podmiotu z odpisu,
  - brak wpisu CAC mimo „certyfikatu" – traktować jako sygnał ostrzegawczy.
- Brak danych o „free zones" i listach firm-słupów – nie potwierdzono.

## 5. Zarząd, wspólnicy, reprezentacja

- **Osoby reprezentujące (dyrektorzy):** wg legit.ng publiczne wyszukiwanie **nie pokazuje dyrektorów**; wg innego źródła wyszukiwanie CAC pokazuje „names and addresses of registered officers". **Sprzeczne – nie potwierdzono.** Do sprawdzenia ręcznie na żywym portalu dla konkretnej firmy.
- **Sposób reprezentacji:** nie potwierdzono publicznego źródła. Zwykle wynika ze statutu / umowy spółki (memorandum & articles) – żądać od klienta.
- **Wspólnicy / akcjonariusze:** wykaz wspólników i udziałów – nie potwierdzono w publicznym wyszukiwaniu. Lepsze źródło: rejestr PSC (sekcja 6), który wg strony CAC pokazuje osoby mające ≥ 5% udziałów.
- **Sprawozdania finansowe i dokumenty założycielskie:** płatne (CTC ₦5 000 – dla dokumentów; zakres wg harmonogramu nie potwierdzono co do sprawozdań). Nie potwierdzono darmowego dostępu.

## 6. Beneficjenci rzeczywiści (UBO)

- **Rejestr:** Open Central Register of Persons with Significant Control (PSC) / „Beneficial Ownership Register", prowadzony przez CAC. Strona: `https://bor.cac.gov.ng/` (otwarta w czasie researchu – strona zawiera FAQ i opis rejestru; bez pełnych danych o formularzu wyszukiwania).
- **Podstawa prawna (wg źródeł wtórnych):** sekcja 119 CAMA 2020 oraz Persons with Significant Control Regulations 2022. Uruchomiony publicznie 25.05.2023 (Nairametrics, wtórne); według komunikatów CAC w 2026 roku rejestr jest „w pełni operacyjny" (wtórne).
- **Dostęp:** **publiczny i darmowy** – według Registrar-General CAC (cytowane w wyniku wyszukiwania, źródło wtórne) oraz opisu w raporcie Open Ownership z 15.06.2026 (otwarte): „public search functions" do weryfikacji podstawowych informacji o firmie. Dostęp wymagający loginu/uprawnień mają **organy właściwe** (NFIU, część organów ścigania) przez API i osobne dane logowania. **Nie znaleziono żadnych zapisów o zawężeniu dostępu dla podmiotów prywatnych w 2026 r.** Nie potwierdzono wprost, że publiczna wyszukiwarka nie wymaga konta – wg strony bor.cac.gov.ng nie ma wymogu logowania do przeglądania wyszukiwarki (weryfikować ręcznie).
- **Wyszukiwanie:** wg strony bor.cac.gov.ng – po **nazwie firmy lub numerze RC**. Wg raportu Open Ownership (2026, wtórny w tym zakresie) – także po **nazwie osoby**. **Sprzeczne – nie potwierdzono.**
- **Jakie dane widać:** wg Regulation 10(1) (cytowane w wyniku wyszukiwania, źródło wtórne) publicznie: imię i nazwisko, data rozpoczęcia kontroli, zawód, adres do doręczeń, obywatelstwo, charakter kontroli i unikalny identyfikator. Adres zamieszkania – nie potwierdzono. Strona bor.cac.gov.ng pokazuje przykładowy rekord w formacie BODS-JSON i wykresy udziałów i praw głosu; **pełnej listy pól na stronie nie znaleziono** – do sprawdzenia ręcznie na przykładzie firmy.
- **Próg beneficjenta:** **5%** (strona FAQ `bor.cac.gov.ng` cytuje CAMA: „any person holding directly or indirectly not less than 5% shares"). Inne źródło wtórne podaje 25% – **uznać 5% jako wiążący wg oficjalnej strony CAC**, ale weryfikować ręcznie w tekście ustawy.
- **Kontrola:** wg definicji CAMA kontrolą jest też: ≥ 5% praw głosu, prawo powoływania/odwoływania większości dyrektorów, znaczący wpływ lub kontrola bezpośrednia (wg FAQ bor.cac.gov.ng).
- **Jeśli rejestr nie zwraca wyniku:** nie oznacza to braku beneficjenta – poprosić klienta o oświadczenie beneficjentów, rejestr udziałowców (register of members) i schemat struktury; zweryfikować krzyżowo z rejestrem CAC i mediami.
- **Trusty / fundacje:** nie potwierdzono obowiązku jawności trustów w Nigerii. Nie sprawdzono regulacji fundacji.

## 7. Dodatkowe darmowe weryfikacje

- **Numer podatkowy (Tax ID):**
  - od 1.01.2026 NRS (Nigeria Revenue Service, następca FIRS) wprowadził 13-cyfrowy **Tax ID**; dla firm wyprowadzany z numeru RC (źródło wtórne – Regfollower, Nairametrics z 18.05.2026).
  - Portal `https://taxid.nrs.gov.ng/` (otwarty): formularz do **pobrania Tax ID** przez NIN lub numer CAC/dane rejestracyjne; wybór kategorii: Individuals / Corporate / Others; wymagana zgoda na przetwarzanie danych. **Nie potwierdzono, czy portal pozwala zweryfikować cudzą firmę bez dostępu do jej danych.** Pozostałe portale (apps.firs.gov.ng/tinverification, tinverification.jtb.gov.ng) to starsze adresy z poradników – nie otwarte, nie potwierdzone jako aktualne.
  - Wniosek praktyczny: nie uzależniać weryfikacji od TIN/Tax ID. Poprosić klienta o zaświadczenie o numerze Tax ID wystawione przez NRS (nie potwierdzono nazwy dokumentu) i porównać numer RC.
- **VAT:** brak potwierdzonego publicznego, darmowego odpowiednika VIES. Nie potwierdzono.
- **Numer celny / EORI:** nie sprawdzano (poza zakresem researchu).
- **LEI (GLEIF):** nie sprawdzano w tym researchu – do sprawdzenia ręcznie na `search.gleif.org` (zwykle tylko większe firmy).
- **Rejestr działalności regulowanych / licencji:** zależne od branży (np. CBN dla banków i BDC, SEC dla rynku kapitałowego, NAFDAC dla żywności i leków). Nie sprawdzano list licencji; dla towaru – weryfikować w odpowiednim regulatorze.
- **Listy ostrzeżeń:** brak potwierdzonego publicznego krajowego rejestru nierzetelnych kontrahentów. Nie sprawdzono.

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Status FATF:** Nigeria trafiła na szarą listę 2.2023, a **wyszła z niej 24.10.2025** (Nairametrics, wtórne). Oficjalna strona FATF nie została otwarta (błąd 403) – **do sprawdzenia ręcznie** na fatf-gafi.org.
- **Lista UE high-risk (AML):** Nigeria została usunięta z listy państw wysokiego ryzyka UE, decyzją Komisji C(2025) 8460 z 4.12.2025, obowiązującą od **29.01.2026** (źródła wtórne: ThisDay, Arise, NFIU). Oficjalny tekst rozporządzenia nie został otwarty – **do sprawdzenia ręcznie** w Dzienniku Urzędowym UE.
- **Krajowe listy sankcyjne:** Nigeria prowadzi własną **Nigeria Sanctions List** na podstawie Terrorism (Prevention and Prohibition) Act 2022, administrowaną przez Nigeria Sanctions Committee. Wg źródeł z 2026 roku (SEC, CBN, Nairametrics, Arise) lista była aktualizowana m.in. w kwietniu i czerwcu 2026 r.; ostatnia wzmianka o aktualizacji: 18.06.2026. **Nie potwierdzono adresu publicznej listy** – do sprawdzenia ręcznie u NFIU / Nigeria Sanctions Committee. Liczby pozycji w różnych źródłach są sprzeczne – nie podawać liczby.
- **Sankcje ONZ (1267) i ich wdrożenie w Nigerii:** nie potwierdzono (wyniki nie opisały tego zagadnienia).
- **Ryzyko RU/BY (reeksport):** w wynikach wyszukiwania nie znaleziono żadnej informacji o Nigerii jako szczególnym pośredniku dla Rosji/Białorusi (pytanie badane ogólnie – wyniki dotyczyły Kirgistanu, Armenii, Hongkongu, Chin). Nie stwierdzono znanych przypadków w źródłach. Ogólnie: nie zakładać braku ryzyka tylko dlatego, że brak publicznych doniesień.
- **Na co zwrócić uwagę w strukturze właścicielskiej:** obywatele RU/BY lub podmioty z tych krajów wśród PSC (≥ 5%), nominee directors, firmy-powłoki z zarejestrowanym adresem agenta, nagłe zmiany dyrektorów przed transakcją.
- **Co ZAWSZE oznaczyć flagą „RU/BY":** zgodnie z `00-metodyka.md` (nie odczytano w tym researchu – zastosować wg tego pliku). Każde powiązanie z podmiotem rosyjskim lub białoruskim w strukturze PSC lub w dokumentach – flaga obowiązkowa.

## 9. Procedura krok po kroku (checklist)

1. Pobrać od klienta odpis / certyfikat inkorporacji lub CTC i zapisać numer RC oraz nazwę dokładnie tak, jak na dokumencie.
2. Wejść na `https://search.cac.gov.ng` (sprawdzić ręcznie, czy działa – 403 w researchu), wyszukać po numerze RC.
3. Porównać nazwę, numer RC, datę rejestracji i status z odpisem. Niezgodność = zatrzymać proces.
4. Zapisać wynik: zrzut ekranu lub wydruk do PDF z datą i godziną.
5. Sprawdzić status: *Active* – OK; *Inactive/Dormant/Struck Off* – wstrzymać, wyjaśnić z klientem.
6. Wejść na `https://bor.cac.gov.ng/`, wyszukać po numerze RC lub nazwie firmy; zapisać listę PSC z ≥ 5% udziałów (lub kontroli). Zapisać datę wyszukiwania.
7. Jeżeli PSC nie są widoczne lub sprzeczne z oświadczeniem klienta – poprosić o rejestr udziałowców i schemat struktury; zweryfikować nazwiska/nazwy krzyżowo w rejestrze CAC.
8. Sprawdzić numer Tax ID (13 cyfr): poprosić klienta o potwierdzenie z NRS; nie uznawać za zweryfikowany bez potwierdzenia od NRS (portal `taxid.nrs.gov.ng` może nie służyć do weryfikacji cudzych danych – nie potwierdzono).
9. Sprawdzić listy sankcyjne: Nigeria Sanctions List (adres do ustalenia), listy UE/ONZ/OFAC/UK, z zapisem daty.
10. Sprawdzić, czy kraj pochodzenia podmiotów z PSC nie jest RU/BY – jeśli tak, flaga.
11. Sprawdzić konto bankowe: czy rachunek należy do podmiotu z odpisu (nazwa beneficjenta przelewu = nazwa z CAC).
12. Zapisać wynik w teczce klienta: odpis, zrzuty, daty, numery RC, flagi. Eskalować (EDD) przy jakiejkolwiek niezgodności, PSC z RU/BY lub braku odpowiedzi klienta.

## 10. Ograniczenia i ryzyka

- **Nie da się za darmo sprawdzić (lub nie potwierdzono):** zaległości podatkowych i ZUS-owych, upadłości i likwidacji w publicznym rejestrze, sprawozdań finansowych, listy dyrektorów (sprzeczne źródła), wykazu wspólników w pełnym brzmieniu, weryfikacji Tax ID cudzej firmy, VAT.
- **Płatne alternatywy (ostatnia opcja):** CTC CAC ~₦5 000, raport historyczny ₦20 000–30 000, due diligence ₦50 000 (ceny wg harmonogramu z 1.08.2025; sprawdzić aktualność na cac.gov.ng przed płatnością). Komercyjni dostawcy KYB (np. wskazane w wynikach YouVerify, Dojah, InfobelPRO) – nie oceniano, pozostają poza „za darmo".
- **Opóźnienia i aktualność:** dane mogą być z opóźnieniem; rejestr PSC zawiera dane zgłoszone przez spółki – spółki mogą nie aktualizować. Dla każdej pozycji zapisać datę sprawdzenia.
- **Transliteracja:** nazwy w Nigerii mogą zawierać znaki diakrytyczne lub wpisy w językach lokalnych (Yoruba, Hausa, Igbo) – sprawdzać warianty pisowni; wyszukiwanie po RC unika problemu.
- **Podobieństwo nazw w wyszukiwarce:** wyszukiwanie po jednym słowie zwraca szerokie wyniki (wg źródła) – zawsze zawęzić do numeru RC.
- **Ryzyko podróbki:** kod QR i stempel na odpisie nie zostały zweryfikowane w tym researchu – traktować je jako dodatkowy element, nie zastępujący wyszukiwania w rejestrze.
- **Kiedy eskalować do wzmocnionej weryfikacji (EDD):** brak numeru RC w rejestrze; status inny niż aktywny; PSC z RU/BY lub z listy sankcyjnej; konto na osobę trzecią; żądanie płatności do kraju trzeciego; nagła zmiana dyrektorów lub właścicieli; brak odpowiedzi klienta na prośbę o dokumenty.

## 11. Źródła

Otwarte w czasie researchu (WebFetch – treść odczytana):
- [Rejestr beneficjentów rzeczywistych (PSC) CAC – FAQ i opis](https://bor.cac.gov.ng/) – oficjalne – otwarte w czasie researchu: tak
- [Tax ID / TIN – portal NRS/JRB](https://taxid.nrs.gov.ng/) – oficjalne – otwarte w czasie researchu: tak
- [Telegraph.ng – nowy harmonogram opłat CAC od 1.08.2025](https://www.telegraph.ng/?p=23575) – nieoficjalne (prasa) – otwarte w czasie researchu: tak
- [Legit.ng – jak zweryfikować certyfikat CAC online](https://www.legit.ng/ask-legit/guides/1730212-how-verify-a-cac-certificate-online-minutes-office-visit-required/) – nieoficjalne – otwarte w czasie researchu: tak
- [Open Ownership – raport o rejestrze beneficjentów w Nigerii, część 2 (15.06.2026)](https://www.openownership.org/en/publications/enhancing-beneficial-ownership-data-collection-and-use-in-nigeria/part-2-the-beneficial-ownership-ecosystem/) – nieoficjalne (organizacja non-profit) – otwarte w czasie researchu: tak

Zwrócone przez wyszukiwarkę, nieotwarte (błąd 403/404 lub nieodczytane):
- [CAC Public Search – search.cac.gov.ng](https://search.cac.gov.ng) – oficjalne – otwarte w czasie researchu: nie (403)
- [Strona główna CAC](https://www.cac.gov.ng/) – oficjalne – otwarte w czasie researchu: nie (zwrócona przez wyszukiwarkę)
- [Harmonogram opłat CAC (Fees.pdf)](https://cac.gov.ng/wp-content/uploads/2021/01/Fees.pdf) – oficjalne – otwarte w czasie researchu: nie (404)
- [FATF – Nigeria](https://www.fatf-gafi.org/en/countries/detail/Nigeria.html) – oficjalne – otwarte w czasie researchu: nie (403)
- [FATF – increased monitoring, październik 2025](https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-october-2025.html) – oficjalne – otwarte w czasie researchu: nie (403)
- [Nairametrics – FATF usuwa Nigerię z szarej listy (24.10.2025)](https://nairametrics.com/2025/10/24/fatf-removes-nigeria-from-grey-list-boosting-investor-confidence/) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [ThisDay – EU usuwa Nigerię z listy wysokiego ryzyka (16.01.2026)](https://www.thisdaylive.com/2026/01/16/eu-removes-nigeria-from-high-risk-financial-list/) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [Arise – EU usuwa Nigerię z listy wysokiego ryzyka](https://www.arise.tv/eu-removes-nigeria-from-high-risk-financial-list-after-aml-reforms/) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [Mondaq – Nigeria, insolvency (wpis CAC po zatwierdzeniu sądu)](https://www.mondaq.com/nigeria/insolvencybankruptcy/1565402/insolvency-proceedings-in-nigeria) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [YouVerify – jak sprawdzić, czy firma jest zarejestrowana w Nigerii](https://youverify.co/en/blogs/how-to-check-if-a-company-is-registered-in-nigeria) – nieoficjalne (dostawca komercyjny) – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [Pay4Me – legalizacja dokumentów w Nigerii](https://pay4me.app/blog/277/legalization-and-authentication-of-certificates-a-complete-guide) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [Ambasada Belgii w Nigerii – legalizacja dokumentów](https://nigeria.diplomatie.belgium.be/en/legalisation-documents) – oficjalne (dyplomatyczne) – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [Nairametrics – NRS wprowadza jednolity Tax ID (18.05.2026)](https://nairametrics.com/2026/05/18/nrs-introduces-unified-tax-id-system-for-all-taxable-persons-in-nigeria/) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [NFIU – komunikat o usunięciu z listy UE](https://thewhistler.ng/nfiu-welcomes-eu-delisting-of-nigeria-from-high-risk-money-laundering-jurisdictions) – nieoficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania)
- [Cross-check: lista wysokiego ryzyka UE (Dz.Urz. UE, rozporządzenie 2016/1675 ze zmianami)](https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/anti-money-laundering-and-terrorist-financing-directive-4_en) – oficjalne – otwarte w czasie researchu: nie (wynik wyszukiwania, nieodczytany)
