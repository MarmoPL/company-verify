# Polska (PL) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia · Ryzyko jurysdykcji: standardowe (UE; ryzyko reeksportu wg `00-metodyka.md`)
>
> Uwaga o sesji researchu: limit WebFetch został wyczerpany w trakcie pracy (reset 18.11.2026, 8:00). Część punktów
> (CRBR, Biała lista VAT, VIES, CEIDG, KRZ) opiera się na wynikach wyszukiwarki z witryn wtórnych albo na
> niepełnym otwarciu stron. Oznaczenia „nie potwierdzono – do sprawdzenia ręcznie” są tam celowe.

## 1. Najkrótsza ścieżka (TL;DR)

- **Spółka (sp. z o.o., S.A., itd.)**: wejdź na wyszukiwarkę KRS **https://ekrs.ms.gov.pl/** (potwierdzone), wpisz numer KRS, NIP lub REGON. Wyszukiwanie nie wymaga konta.
- **Jednoosobowa działalność (JDG) i spółka cywilna**: NIE są w KRS. Szukaj w CEIDG (zob. sekcja 2b). Numer NIP/REGON sprawdzisz też w REGON.
- **Za darmo**: wyszukiwanie w KRS i REGON (bez logowania), wpisy w CEIDG (wg wtórnych źródeł), status na Białej liście VAT, dokumenty finansowe z KRS (wg gov.pl – „bezpłatne wyszukanie i pobranie dokumentu finansowego”).
- **Płatne**: odpisy urzędowe z KRS (cena nie potwierdzona w tej sesji), wydruk/zaświadczenie z CEIDG (nie potwierdzono).
- **Beneficjenci rzeczywiści (CRBR)**: rejestr istnieje (crbr.podatki.gov.pl), ale trwa zmiana ustawy AML, która ma ograniczyć dostęp. **Stan dostępu na dzień weryfikacji trzeba sprawdzić ręcznie.** Jeśli dostęp jest zamknięty – procedura zastępcza (sekcja 6).
- **Odpis od klienta**: porównaj nazwę, NIP, REGON, KRS, adres i osoby reprezentujące z wyszukiwarką. Weryfikację online samego dokumentu opisano w sekcji 3 – tu jest niepewność.

## 2. Rejestr firm (główny)

### 2a. Krajowy Rejestr Sądowy (KRS) – spółki i inne podmioty sądowe
- **Organ prowadzący:** Ministerstwo Sprawiedliwości; sądy rejestrowe (wydziały KRS sądów okręgowych).
- **Nazwa:** Krajowy Rejestr Sądowy (KRS). Wyszukiwarka: **https://ekrs.ms.gov.pl/** (potwierdzono – strona gov.pl wskazuje ten adres).
- **Portal Rejestrów Sądowych (PRS):** **https://prs.ms.gov.pl** (potwierdzono) – służy do składania wniosków, nie do przeglądu za darmo.
- **Typ rejestru:** centralny (dane z wydziałów KRS), prowadzony przez MS.
- **Język:** wyłącznie polski (nie potwierdzono wersji EN).
- **Wyszukiwanie po:** numerze KRS, NIP, REGON, nazwie (potwierdzono na gov.pl w zakresie „wyszukiwarka”; szczegółowe kryteria w ekrs – do sprawdzenia ręcznie).
- **Za darmo:**
  - „Centralna Informacja bezpłatnie udostępnia w ogólnodostępnych sieciach aktualne informacje o podmiotach wpisanych do KRS” (gov.pl, potwierdzono).
  - Bezpłatne wyszukanie i pobranie dokumentów finansowych (sprawozdań) – gov.pl, potwierdzono.
- **Płatne / ograniczone:** odpisy, wyciągi i zaświadczenia wydawane na wniosek są odpłatne (gov.pl). **Wysokości opłat nie potwierdzono** – wtórne źródło podaje 30 zł dla odpisu aktualnego, ale to starsza informacja; sprawdź w ekrs / cennik.
- **Format numeru:** KRS – 10 cyfr (wiedza ogólna; nie potwierdzono w tej sesji). Sprawdzaj również NIP (10 cyfr) i REGON (9 lub 14 cyfr – potwierdzono na stronie REGON).

### 2b. CEIDG – jednoosobowa działalność gospodarcza i spółka cywilna
- **Organ prowadzący:** Minister właściwy ds. gospodarki (wg wtórnych źródeł).
- **Wyszukiwarka:** https://aplikacja.ceidg.gov.pl/ceidg/ceidg.public.ui/search.aspx – **próba otwarcia zwróciła 403; nie potwierdzono bezpośrednio.** Wtórne źródła wskazują także wejście przez „Baza przedsiębiorców” w prod.ceidg.gov.pl – do sprawdzenia ręcznie.
- **Za darmo (wtórnie):** wyszukiwanie po NIP, REGON, nazwie firmy lub danych właściciela; widoczny status działalności i data rozpoczęcia. Ministerstwo ma podawać, że czynności wpisowe są bezpłatne (cytat z komunikatu w wyniku wyszukiwarki – nie otwarte bezpośrednio).
- **Płatne:** wydruk / zaświadczenie – **nie potwierdzono**.
- **Ostrzeżenie:** komunikaty ostrzegają przed firmami pobierającymi opłaty za wpis do CEIDG (wynik wyszukiwarki, nie otwarte bezpośrednio).

### 2c. REGON – GUS (Wyszukiwarka REGON / Baza Internetowa REGON)
- **Organ prowadzący:** Główny Urząd Statystyczny (GUS).
- **URL:** **https://wyszukiwarkaregon.stat.gov.pl/appBIR/index.aspx** (potwierdzono – otwarto).
- **Język:** polski.
- **Wyszukiwanie po:** REGON (9 lub 14 znaków), NIP, KRS; oraz adres (województwo, powiat, gmina, miejscowość, ulica, fragment nazwy, nr nieruchomości) – potwierdzono.
- **Dane zwracane:** identyfikatory, nazwa, formy prawne, organ rejestrowy, adres siedziby, daty zmian, PKD, jednostki lokalne, dane kontaktowe podmiotów prawnych – potwierdzono.
- **Za darmo / bez logowania:** strona podaje, że można korzystać „bez konieczności logowania”; brak captcha (potwierdzono). Opłat strona nie podaje wprost, ale nie wskazuje żadnej.
- **Ważne:** REGON dotyczy także JDG i spółek cywilnych – to dobra druga ścieżka, gdy CEIDG jest niedostępne.

### 2d. Monitor Sądowy i Gospodarczy (MSiG)
- Gov.pl (sekcja KRS) wspomina o opłatach za ogłoszenia w **Monitorze Sądowym i Gospodarczym** przy wnioskach do wydziałów KRS (potwierdzono).
- **Adres i zakres bezpłatnego przeglądu MSiG: nie potwierdzono – do sprawdzenia ręcznie.**

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwy lokalne:** „Odpis z Krajowego Rejestru Sądowego” (odpis aktualny / odpis pełny / wyciąg). Odpis z CEIDG nazywa się „wydruk z CEIDG” (lub zaświadczenie – nie potwierdzono różnicy). Odpis z REGON to „zaświadczenie / wydruk z REGON” (nie potwierdzono).
- **Typy odpisów z KRS (potwierdzono na gov.pl):**
  - **odpis pełny** – treść wszystkich wpisów od pierwszego wpisu, z wyjątkiem nieujawnianych;
  - **odpis aktualny** – aktualna treść wpisów pod danym numerem KRS;
  - **wyciąg** – aktualne wpisy wybranych działów (wniosek).
  Gov.pl nie wymienia „odpisu zwykłego”. Dla celów weryfikacji najlepszy jest **odpis aktualny** (nie starszy niż 3 miesiące, zgodnie z szablonem).
- **Wydawca / cechy autentyczności:** wydruk komputerowy z KRS ma moc dokumentu, jeśli ma cechy umożliwiające weryfikację z danymi w KRS (potwierdzono na gov.pl). Gov.pl **nie podaje konkretnego adresu weryfikacji ani wymaganych danych**.
- **Weryfikacja online:** wtórne wyniki wyszukiwarki (prawo.pl) wskazywały weryfikację na **ems.ms.gov.pl** z użyciem identyfikatora wydruku z lewego górnego rogu. **Nie potwierdzono – nie otwarto tej strony.** Sprawdź ręcznie; jeśli adres nie działa, porównaj dane z odpisem w ekrs (najpewniejsza ścieżka).
- **Legalizacja / apostille:** Polska jest stroną Konwencji haskiej z 5 października 1961 (apostille). Wtórny wynik wskazywał HCCH status table: wejście w życie dla Polski 14.08.2005 (status table nie otwarta bezpośrednio, ale domena hcch.net pochodzi z wyniku wyszukiwania). Gov.pl stosuje apostille dla krajów-stron. Dla dokumentów **polskich** używanych za granicą zwykle wystarcza apostille; dla dokumentów zagranicznych w Polsce – zależnie od kraju.
- **Sygnały podróbki / nieaktualności:**
  - odpis bez numeru KRS albo z numerem nieistniejącym w ekrs,
  - inna nazwa, adres lub skład zarządu niż w wyszukiwarce,
  - brak daty wydruku lub daty sprzed > 3 miesięcy,
  - odpis z CEIDG przedstawiony jako odpis z KRS (JDG nie ma KRS).
- **Aktualność:** dane w ekrs są aktualne; odpis jest „zamrożony” w dniu wydruku. Przyjmij ważność ≤ 3 miesiące (zgodnie z metodyką).

## 4. Status firmy i sygnały ostrzegawcze

- **Statusy w KRS:** podmiot wpisany / wykreślony; w ekrs widoczne są m.in. informacje o likwidacji, upadłości i postępowaniu restrukturyzacyjnym (wg ogólnej wiedzy – nie potwierdzono w tej sesji brzmienia wszystkich statusów). **Do sprawdzenia ręcznie:** oznaczenia „w likwidacji” i „w upadłości” w odpisie.
- **Statusy w CEIDG (wtórnie):** aktywna, zawieszona, wykreślona. Status „zawieszona” jest częsty u JDG; nie oznacza automatycznie problemu.
- **Upadłość / restrukturyzacja / zadłużenie:**
  - **KRZ – Krajowy Rejestr Zadłużonych** (krz.ms.gov.pl): publiczna, bezpłatna wyszukiwarka prowadzona przez MS, działa od 1.12.2021 i zastąpiła Rejestr Dłużników Niewypłacalnych (wtórnie, potwierdzenia nie uzyskano – strona zwróciła pustą treść). Wyszukiwanie bez konta (wtórnie). **Szczegóły wyszukiwania (NIP/KRS/nazwa) – nie potwierdzono.**
  - Brak publicznego API; masowe sprawdzanie tylko przez komercyjnych dostawców (wtórnie).
- **Zaległości podatkowe / ZUS / sądowe:** nie publiczne. Klient może dostarczyć zaświadczenie z US (o niezaleganiu) i z ZUS – **nie potwierdzono zakresu i trybu wydawania** w tej sesji. Zaświadczenie od klienta traktuj jako twierdzenie.
- **Red flags w Polsce (ogólnie):**
  - wiele podmiotów z tym samym adresem siedziby (wirtualne biura, adresy rejestracyjne),
  - firmy zarejestrowane niedawno z dużym obrotem zamówień,
  - zmiany zarządu tuż przed zamówieniem,
  - KRS z nowym wspólnikiem-osobą bez innej działalności.
  To ogólne wskazówki, nie potwierdzone źródłem.

## 5. Zarząd, wspólnicy, reprezentacja

- **Reprezentacja i osoby uprawnione:** KRS – dział 2 (zarząd, sposób reprezentacji, prokura). Dostępne w odpisie aktualnym z ekrs (potwierdzono, że odpis zawiera wpisy aktualne; sposób reprezentacji – wiedza ogólna, nie potwierdzono w tej sesji dokładnego brzmienia).
- **Wspólnicy / akcjonariusze:** KRS odpis aktualny zwykle **nie** zawiera pełnej listy udziałów – część informacji jest w dokumentach (lista wspólników, akt założycielski). Wyszukiwarka KRS daje dokumenty finansowe za darmo (potwierdzono). **Listę wspólników trzeba zażądać od klienta** i porównać z CRBR (sekcja 6).
- **Dokumenty założycielskie / sprawozdania finansowe:** sprawozdania – bezpłatnie w ekrs (potwierdzono). Akt założycielski – nie potwierdzono dostępu publicznego.
- **Spółki cywilne** – patrz sekcja 9.

## 6. Beneficjenci rzeczywiści (UBO)

- **Rejestr:** Centralny Rejestr Beneficjentów Rzeczywistych (CRBR), prowadzony przez Ministra Finansów (KAS).
- **URL:** **http://crbr.podatki.gov.pl/adcrbr/** – zaobserwowano przekierowanie z crbr.podatki.gov.pl; **treści strony nie udało się otworzyć (limit WebFetch).** Nazwa i adres potwierdzone tylko przez przekierowanie.
- **Stan dostępu – NIEPEWNY, do sprawdzenia ręcznie:**
  - Historycznie: rejestr uruchomiony 13.10.2019; „od początku funkcjonowania” bezpłatny i nieograniczony dostęp (wtórnie, cytat z artykułu).
  - Wyrok TSUE z 22.11.2022 w połączonych sprawach **C-37/20 i C-601/20** – ogólny dostęp społeczeństwa uznany za poważną ingerencję w prywatność (potwierdzone w wyniku wyszukiwania; cytat z artykułu).
  - Projekt nowelizacji ustawy AML (projekt UC75, implementacja dyrektywy UE 2024/1640) zastępuje jawny dostęp: **dostęp bezpośredni** dla wskazanych organów i instytucji obowiązanych oraz **dostęp na wniosek** dla podmiotów wykazujących uzasadniony interes (wyniki z gov.pl i prawo.pl – plik gov.pl nie został otwarty bezpośrednio).
  - **Terminy są sprzeczne w źródłach:** 1.07.2026 (tagalliances, ASB Group – wtórne), 1.01.2027 (Super Express – wtórne), okna 22.10–11.11.2026 (Dudkowiak – niejasny zakres). Ostatni wynik wyszukiwania (wrzesień 2026) mówi o planie, nie o obowiązującym prawie.
  - **Wniosek:** nie potwierdzono wejścia w życie ograniczenia. W dniu weryfikacji sprawdź stan w CRBR i w RCL (projekt UC75).
- **Dostęp (do sprawdzenia):** publiczny / na wniosek / tylko organy i podmioty obowiązane. Dla dokumentu 16.11.2026 – **nie potwierdzono**.
- **Darmowy?** Historycznie tak. Do sprawdzenia, czy po zmianie pozostanie.
- **Próg beneficjenta:** **nie potwierdzono w tej sesji** (szablon zakłada 25% – do weryfikacji w ustawie AML). Pojęcie „kontroli” – do sprawdzenia w ustawie.
- **Trusty i fundacje:** obowiązek zgłoszenia do CRBR dotyczy także trustów i fundacji (wiedza ogólna z artykułów wtórnych – nie potwierdzono szczegółów).
- **Procedura zastępcza (jeśli CRBR zamknięty lub niedostępny):**
  1. Oświadczenie klienta o beneficjentach (elementy wg `00-metodyka.md`, pkt 5), podpisane przez osobę uprawnioną do reprezentacji (z KRS).
  2. Dokumenty do zażądania: lista wspólników / akcjonariuszy, akt założycielski, schemat struktury, zaświadczenie o zgłoszeniu do CRBR (jeśli klient je ma – zwykle wydruk z potwierdzeniem zgłoszenia).
  3. Krzyżowa weryfikacja: KRS (sprawozdanie – nota o jednostkach powiązanych), GLEIF (dla dużych podmiotów), wyszukiwanie osoby w KRS (osoby fizyczne na listach wspólników innych firm), media, Open Ownership (tylko jeśli kraj publikuje).
  4. Screening sankcyjny beneficjentów (sekcja 8).

## 7. Dodatkowe darmowe weryfikacje

- **NIP / VAT – Biała lista podatników VAT (Ministerstwo Finansów / KAS):**
  - **API:** https://wl-api.mf.gov.pl/ (wynik wyszukiwarki – nie otwarto; wtórnie potwierdzony w zapowiedzi „API Rejestr WL”, wersja 1.6.0 wg wyniku wyszukiwania, kontakt podany w materiale: WykazPodatnikow@mf.gov.pl – **nie otwarto oficjalnej dokumentacji**).
  - **Wyszukiwarka www:** próba https://podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka → przekierowanie 301 na **https://podatki-arch.mf.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/** (nazwa „arch” sugeruje archiwum – **do sprawdzenia ręcznie, czy to aktualne miejsce**). Wtórne źródło podaje inny adres: wykaz.podatnicy.gov.pl – **niespójne, nie potwierdzono**.
  - **Limity:** wtórnie: wyszukiwanie po NIP z limitem dziennym, batch do 30 podmiotów na zapytanie, reset o północy dni roboczych – **nie potwierdzono w oficjalnej dokumentacji.**
  - **Co sprawdzić:** czy NIP jest zarejestrowany jako podatnik VAT czynny/zwolniony/niezarejestrowany, nazwa i adres zgodne z odpisem, rachunki bankowe (do płatności – ważne przy weryfikacji rachunku).
- **VIES (UE):** https://ec.europa.eu/taxation_customs/vies/ – otwarto, ale treść zwróciła tylko tytuł („Vies on-the-Web”). **Nie potwierdzono** zakresu danych zwracanych ani wsparcia PL. Polski numer VAT = „PL” + NIP (wiedza ogólna, do potwierdzenia).
- **REGON** – patrz 2c (potwierdzono).
- **LEI (GLEIF):** zwykle tylko duże podmioty; **nie sprawdzano** w tej sesji.
- **EORI:** do sprawdzenia w systemie celnym UE (wg metodyki); **nie potwierdzono** dla PL w tej sesji.
- **Rejestry regulowane / licencje:** zależnie od towaru (np. Główny Inspektorat Farmaceutyczny, UKE, Urząd Dozoru Technicznego) – **nie badano**.
- **Lokalne listy ostrzeżeń:** brak potwierdzonej publicznej listy „nierzetelnych kontrahentów” w tej sesji; KNF publikuje ostrzeżenia dot. nielegalnych podmiotów finansowych – **nie potwierdzono adresu**.

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Sankcje:** Polska stosuje sankcje UE (bezpośrednio obowiązujące rozporządzenia, m.in. 833/2014 i 765/2006 – wg `00-metodyka.md`). Krajowa lista sankcyjna: MSWiA (wg metodyki) – **adres i zawartość nie potwierdzone w tej sesji**.
- **Ryzyko RU/BY:** Polska nie jest znanym centrum przekierowania do RU/BY w tej sesji, ale firmy handlowe z PL są częstym pośrednikiem w reeksporcie przez państwa sąsiednie (ogólnie – do potwierdzenia przez compliance).
- **Sygnały w strukturze właścicielskiej (PL):**
  - udziałowcy z RU/BY lub z jurysdykcji pośrednich (metodyka pkt 4),
  - spółka z PL o kapitale „zagranicznym” bez jasnego beneficjenta,
  - nominowani zarządy (osoby o adresie zagranicznym, nietypowe zarządy w wielu spółkach),
  - masowa rejestracja spółek z tym samym adresem lub tymi samymi osobami.
- **ZAWSZE flaga „RU/BY”:** każde połączenie z RU/BY (obywatelstwo, adres, transliteracja nazwiska, pełnomocnik) – zgodnie z `00-metodyka.md`.
- **Sprawdź też:** wyszukiwanie w OpenSanctions (wiele list naraz) i OFAC/UK/UN (pozycje z metodyki, nie sprawdzano w tej sesji).

## 9. Jednoosobowe działalności (CEIDG) i spółki cywilne

- **JDG (jednoosobowa działalność gospodarcza):**
  - Podmiot **nie jest osobą prawną** i **nie jest w KRS**. Jej rejestrem jest CEIDG (potwierdzono w wynikach wyszukiwania, nie otwarto CEIDG).
  - Beneficjentem rzeczywistym jest **sama osoba fizyczna** (właściciel). Nie ma CRBR-owej „struktury” – wystarczy weryfikacja tożsamości właściciela (dowód / paszport, zgodność z wpisem w CEIDG).
  - Odpis: wydruk z CEIDG (nie odpis z KRS). Klient z JDG, który przysyła „odpis z KRS”, to sygnał do dopytania.
  - NIP i REGON JDG są w REGON (potwierdzono).
  - **Uwaga RODO:** wydruk z CEIDG zawiera dane osobowe właściciela – przechowuj zgodnie z polityką firmy.
- **Spółka cywilna:**
  - Nie jest wpisana do KRS (wiedza ogólna, zgodna z wynikami – nie potwierdzono wprost w tej sesji).
  - Ma NIP i REGON (do potwierdzenia na stronach REGON/CEIDG).
  - Wspólnicy będący osobami fizycznymi są w CEIDG (wg wiedzy ogólnej – **nie potwierdzono w tej sesji, do sprawdzenia ręcznie**; dotyczy to zwłaszcza wpisu spółki cywilnej do CEIDG).
  - Beneficjenci: wspólnicy-osoby fizyczne. Sprawdź, czy klient wskazał wszystkich wspólników i czy zgadza się to z wpisem.
  - Reprezentacja: wspólnicy, zgodnie z umową spółki (potwierdź z dokumentem).
- **Praktyczna zasada:** nie przyjmuj „odpisu z KRS” od JDG i spółki cywilnej bez wyjaśnienia; zażądaj wydruku z CEIDG i dowodu tożsamości osoby reprezentującej.

## 10. Procedura krok po kroku (checklist)

1. Pobierz od klienta: nazwę, NIP, REGON, KRS (jeśli dotyczy), adres siedziby, odpis (aktualny z KRS lub wydruk z CEIDG, nie starszy niż 3 miesiące).
2. Ustal typ podmiotu: spółka (KRS) / JDG (CEIDG) / spółka cywilna (CEIDG, do potwierdzenia).
3. Sprawdź numer w **ekrs.ms.gov.pl** (KRS) albo w **CEIDG** (JDG – próba 403, sprawdź ręcznie); w obu przypadkach porównaj nazwę, adres, formę prawną, osoby reprezentujące.
4. Sprawdź numer w **wyszukiwarkaregon.stat.gov.pl** (NIP/REGON/KRS) – zgodność danych i status.
5. Sprawdź status VAT w **Białej liście** (podatki-arch.mf.gov.pl – sprawdź, czy to aktualny adres) i rachunek bankowy klienta.
6. Sprawdź wpis w **KRZ** (krz.ms.gov.pl) – upadłość, restrukturyzacja, zadłużenie – i ewentualnie status w MSiG.
7. Ustal beneficjentów: sprawdź **CRBR** (stan dostępu!); jeśli zamknięty – procedura zastępcza (sekcja 6).
8. Screening sankcyjny firmy, osób reprezentujących i beneficjentów (EU, OFAC, UK, UN, OpenSanctions, lista MSWiA).
9. Flaga RU/BY (metodyka pkt 4).
10. Zapisz zrzuty ekranu, daty sprawdzeń i numery wydruków; zachowaj w aktach klienta.
11. Decyzja i ocena ryzyka wg metodyki.

## 11. Ograniczenia i ryzyka

- **Nie da się potwierdzić za darmo:** dokładnych opłat za odpisy KRS, zawartości CEIDG i wydruku z CEIDG (strona 403 w tej sesji), statusu CRBR i zakresu jego dostępu, limitów Białej listy, zakresu danych VIES dla PL. Płatna alternatywa tylko jako ostatnia opcja (np. oficjalny odpis z ekrs z opłatą) – cena do sprawdzenia.
- **Opóźnienia i aktualność:** dane w KRS/CEIDG są aktualne, ale odpis to migawka. Biała lista i VIES mogą mieć opóźnienia dla świeżych wpisów.
- **Transliteracja:** polskie znaki (ą, ę, ł, ś, ż, ź, ć, ń, ó) – w wyszukiwarkach działa różnie; wyszukuj też bez znaków diakrytycznych i po NIP/KRS.
- **Zmiana prawa:** trwa nowelizacja AML (UC75) – dostęp do CRBR może się zmienić w trakcie roku; sprawdzaj przed każdą większą decyzją.
- **Eskalacja do EDD (wzmocnionej weryfikacji):** gdy CRBR zamknięty i brak lustrzanego dowodu UBO; gdy NIP nie jest czynnym podatnikiem VAT przy transakcjach wewnątrzwspólnotowych; gdy wspólnik ma adres lub obywatelstwo RU/BY; gdy KRZ pokazuje postępowanie.
- **Dane osobowe:** wydruki z KRS/CEIDG/CRBR zawierają dane osobowe – RODO, minimalizacja.

## 12. Źródła

- [Wyszukiwarka KRS (eKRS)](https://ekrs.ms.gov.pl/) – oficjalne (adres podany na gov.pl) – otwarte w czasie researchu: tak (adres z gov.pl; sama strona nie otwarta bezpośrednio)
- [Uzyskaj informacje z KRS – gov.pl](https://www.gov.pl/web/sprawiedliwosc/uzyskaj-informacje-z-krs) – oficjalne – otwarte: tak
- [Krajowy Rejestr Sądowy – gov.pl](https://www.gov.pl/web/sprawiedliwosc/krajowy-rejestr-sadowy) – oficjalne – otwarte: tak (wyciąg z treści; podano prs.ms.gov.pl)
- [Portal Rejestrów Sądowych](https://prs.ms.gov.pl) – oficjalne – adres z gov.pl, otwarte: nie (tylko informacja z gov.pl)
- [Wyszukiwarka REGON (GUS)](https://wyszukiwarkaregon.stat.gov.pl/appBIR/index.aspx) – oficjalne – otwarte: tak
- [CRBR – przekierowanie](http://crbr.podatki.gov.pl/adcrbr/) – oficjalne (MF/KAS) – otwarte: nie (limit WebFetch; zaobserwowano przekierowanie z crbr.podatki.gov.pl)
- [CEIDG – wyszukiwarka](https://aplikacja.ceidg.gov.pl/ceidg/ceidg.public.ui/search.aspx) – oficjalne – otwarte: nie (403)
- [Biała lista VAT – archiwum wyszukiwarki](https://podatki-arch.mf.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/) – oficjalne (MF) – otwarte: nie (przekierowanie z podatki.gov.pl; limit WebFetch)
- [API Wykazu podatników VAT](https://wl-api.mf.gov.pl/) – oficjalne (adres z wyniku wyszukiwania) – otwarte: nie
- [VIES on-the-Web](https://ec.europa.eu/taxation_customs/vies/) – oficjalne (KE) – otwarte: tak, treść tylko tytuł
- [KRZ – Krajowy Rejestr Zadłużonych](https://krz.ms.gov.pl) – oficjalne (MS) – otwarte: nie (pusta treść przy fetchu; adres z wyniku wyszukiwania)
- [HCCH – status table, Konwencja z 5.10.1961](https://www.hcch.net/en/instruments/conventions/status-table/?cid=41) – oficjalne (HCCH) – otwarte: nie (wynik wyszukiwania; dane o Polsce z wyniku)
- [Projekt AML / CRBR – gov.pl (załącznik)](https://www.gov.pl/attachment/277f91c5-9d2f-457e-835a-bb9c328f1adc) – oficjalne – otwarte: nie (wynik wyszukiwania)
- [Lex/prawo.pl – CRBR koniec jawności](https://www.prawo.pl/prawo/crbr-koniec-jawnosci-dla-kazdego,532591.html) – nieoficjalne – otwarte: nie (wynik wyszukiwania)
- [Akademia LTCA – projekt nowelizacji AML](https://akademialtca.pl/blog/projekt-nowelizacji-ustawy-aml-crbr-z-ograniczonym-dostepem) – nieoficjalne – otwarte: nie (wynik wyszukiwania)
- [Tagalliances – planned changes CRBR](https://www.tagalliances.com/corporate-and-maa/15590-access-to-the-central-register-of-beneficial-owners-planned-changes-in-poland) – nieoficjalne – otwarte: nie (wynik wyszukiwania)
- [Super Express/Superbiz – koniec jawności CRBR](https://superbiz.se.pl/wiadomosci/rzad-zamyka-popularny-rejestr-to-koniec-jawnosci-dla-firm-aa-v8N4-KtBx-msKz.html) – nieoficjalne – otwarte: nie (wynik wyszukiwania; termin 1.01.2027 niepotwierdzony)
- [Fakturownia – wskazówki CEIDG](https://fakturownia.pl/firma-w-praktyce/jak-skutecznie-wyszukiwac-firmy-w-ceidg) – nieoficjalne – otwarte: nie (wynik wyszukiwania)
- [Prawo.pl – odpis z KRS i weryfikacja](https://www.prawo.pl/samorzad/czy-odpis-z-krs-musi-byc-poswiadczony-za-zgodnosc-z-oryginalem,228952.html) – nieoficjalne – otwarte: nie (wynik wyszukiwania; wskazanie ems.ms.gov.pl do sprawdzenia)
