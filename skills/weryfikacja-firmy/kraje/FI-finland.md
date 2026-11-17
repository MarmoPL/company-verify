# Finlandia (FI) – weryfikacja firmy i beneficjentów

> Stan wiedzy: 2026-11-16 · Pewność dokumentu: średnia · Ryzyko jurysdykcji: standardowe (kraj UE; brak potwierdzonego wpisu na listy FATF – patrz sekcja 4)

> Uwaga o researchu: limit wyszukiwarki (WebSearch) i pobrań (WebFetch) został wyczerpany w trakcie pracy. Część punktów opiera się na wynikach wyszukiwania, a nie na otwartej stronie. Każdy taki punkt jest oznaczony „(wynik wyszukiwania – niezweryfikowane)”. Przed decyzją o wysokiej wartości zweryfikować ręcznie pozycje oznaczone „do sprawdzenia ręcznie”.

## 1. Najkrótsza ścieżka (TL;DR)

- **Rejestr firm:** YTJ – Yritys- ja yhteisötietojärjestelmä (System informacji o przedsiębiorstwach i organizacjach), prowadzony wspólnie przez PRH (Patentti- ja rekisterihallitus – Urząd Patentów i Rejestrów) i Urząd Skarbowy. Wyszukiwarka: https://tietopalvelu.ytj.fi/yrityshaku.aspx?kielikoodi=3 (interfejs także po angielsku z ytj.fi).
- **Co wpisać:** numer Y-tunnus (Business ID, format `1234567-8`), nazwę, numer LEI, gminę siedziby, formę prawną lub przedmiot działalności. Wynik dla Business ID to jeden podmiot.
- **Co zobaczyć za darmo:** podstawowe dane identyfikacyjne i rejestrowe z YTJ (potwierdzone na stronie instrukcji ytj.fi: wyszukiwanie po nazwie, Business ID, LEI, gminie, formie prawnej i przedmiocie działalności, z możliwością wyboru spółek aktywnych lub zlikwidowanych). Opłatę za wyszukiwanie w YTJ potwierdza wyłącznie wynik wyszukiwania (prh.fi, do sprawdzenia ręcznie).
- **Czego za darmo NIE ma:** beneficjentów rzeczywistych (UBO) – dostęp wymaga umowy z PRH i wskazania celu zgodnego z ustawą o przeciwdziałaniu praniu pieniędzy; dane są płatne. Pełnych odpisów z rejestru handlowego (kaupparekisteriote) PRH nie opisuje jako darmowych – cennik do sprawdzenia u PRH.
- **Ocena jakości:** dla odpisu od klienta – porównać dane z YTJ 1:1 (nazwa, Y-tunnus, forma, adres, status, osoby uprawnione). Dla UBO – standardowa procedura zastępcza (sekcja 6 i 9).

## 2. Rejestr firm (główny)

- **Nazwa rejestru:** Kaupparekisteri (rejestr handlowy – Trade Register) oraz YTJ (Yritys- ja yhteisötietojärjestelmä – System informacji o przedsiębiorstwach i organizacjach; w szwedzkim: Företags- och samfundsdatasystemet, FO-system).
- **Organ prowadzący:** PRH – Patentti- ja rekisterihallitus (Patent and Registration Office, Finlandia). Technicznie YTJ utrzymuje PRH; wg wyniku wyszukiwania ustawa o systemie informacji o przedsiębiorstwach (244/2001) przypisuje PRH odpowiedzialność techniczną (do sprawdzenia ręcznie).
- **URL (oficjalny):**
  - wyszukiwarka YTJ: https://tietopalvelu.ytj.fi/yrityshaku.aspx?kielikoodi=3 (adres podany na stronie instrukcji ytj.fi, otwarta)
  - instrukcje wyszukiwania: https://www.ytj.fi/en/index/companysearch/searchinstructions.html (otwarta)
  - informacje PRH o YTJ: https://www.prh.fi/en/companiesandorganisations/tietopalvelut/ytj.html (wynik wyszukiwania – niezweryfikowane)
- **Język interfejsu:** fiński, szwedzki, angielski (YTJ – potwierdzone na stronie instrukcji).
- **Typ rejestru:** centralny (YTJ, jeden system dla spółek i organizacji) + rejestr handlowy prowadzony przez PRH (dane z kaupparekisteri); niezależny rejestr sądowy nie istnieje – Finlandia nie ma systemu „KRS”.
- **Wyszukiwanie po:** nazwie (wpisuje się fragment, system dopasowuje ciąg liter), Business ID, numerze LEI, gminie siedziby (kotipaikka), formie prawnej, przedmiocie działalności. Można zawęzić do firm aktywnych lub zlikwidowanych i sortować po nazwie lub Business ID.
- **Za darmo (wg YTJ):** nazwa, Business ID, forma prawna, siedziba, status, przedmiot działalności, dane kontaktowe. Wyniki można przeglądać w tabeli, otworzyć szczegóły firmy, wydrukować i pobrać jako CSV (potwierdzone na stronie instrukcji; to, że są bezpłatne, strona nie stwierdza wprost – do sprawdzenia ręcznie).
- **Płatne / za logowaniem:**
  - Usługi aplikacyjne PRH (Virre) – wymagają umowy z PRH i połączenia technicznego: opłata konfiguracyjna 1 882,50 EUR (z VAT 25,5%), ceny pojedynczych zapytań od 0,00 do 10,67 EUR (z VAT). Zakres obejmuje m.in. dane podstawowe, wpisy z rejestru handlowego, statut (PDF), osoby uprawnione do reprezentacji, sposób reprezentacji, dane fundacji i hipoteki przedsiębiorstwa (potwierdzone – strona usług aplikacyjnych PRH).
  - Sprawozdania finansowe – interfejs PRH, głównie PDF (potwierdzone na tej samej stronie; ceny nie podano).
  - Odpis z rejestru handlowego i jego weryfikacja elektroniczna – strona PRH nie opisuje cennika; kontakt: tietopalvelut@prh.fi, +358 29 509 5675 (do sprawdzenia ręcznie – adres e-mail na stronie zapisany jako „tietopalvelut(a)prh.fi”).
  - Otwarte dane: https://avoindata.prh.fi/en – bezpłatny dostęp do podstawowych danych firm (potwierdzone na stronie usług PRH). Należy podać źródło (PRH / BIS).
- **Format numeru identyfikacyjnego:** Business ID (Y-tunnus, fin. „yritys-tunnus”) – 7 cyfr, myślnik, cyfra kontrolna, np. `1234567-8` (wzór z wiedzy ogólnej; strona YTJ potwierdza istnienie Business ID, nie opisuje wprost algorytmu – do sprawdzenia ręcznie). Numer VAT: patrz sekcja 7.

## 3. Jak sprawdzić odpis, który dostaliśmy od klienta

- **Nazwa dokumentu:** Kaupparekisteriote (fiński) / Handelsregisterutdrag (szwedzki) – odpis / wyciąg z rejestru handlowego (Trade Register extract). Dla spółek zarejestrowanych w YTJ: wydruk z YTJ (nie jest odpisem urzędowym) – wymaga odróżnienia od odpisu urzędowego PRH.
- **Kto wystawia:** PRH. Pozostałe formy (np. wyciąg z YTJ) nie mają mocy dokumentu urzędowego – do sprawdzenia ręcznie.
- **Cechy autentyczności:** nie potwierdzono szczegółów zabezpieczeń odpisu (kod weryfikacyjny, QR, podpis elektroniczny) – do sprawdzenia ręcznie u PRH na przykładzie aktualnego odpisu. Nie zakładać ich istnienia bez wzoru.
- **Weryfikacja online:** najpewniej wyszukać firmę po Business ID w YTJ i porównać dane (nazwa, forma, adres, status, osoby uprawnione). Osoby uprawnione do reprezentacji są w usługach aplikacyjnych PRH (płatne) – w YTJ nie potwierdzono ich wyświetlania (do sprawdzenia ręcznie).
- **Legalizacja / apostille:** Finlandia jest stroną Konwencji haskiej z 5 października 1961 r. (zniesienie wymogu legalizacji). Według tabeli HCCH (otwarta 2026-11-16, ostatnia aktualizacja tabeli 30-VI-2026): podpisanie 13-III-1962, ratyfikacja 27-VI-1985, wejście w życie dla Finlandii 26-VIII-1985; brak wpisanych sprzeciwów. Apostille wystawia wg wyniku wyszukiwania (niezweryfikowane) DVV (Digital and Population Data Services Agency, Väestörekisterikeskus/Digi- ja väestötietovirasto); opłata 38 EUR wg źródła trzeciego – nie potwierdzono, do sprawdzenia ręcznie. Dokumenty z państw spoza konwencji wymagają odrębnej legalizacji (wynik wyszukiwania ze strony um.fi – niezweryfikowane).
- **Czy odpis może być nieaktualny:** przyjąć datę ważności ≤ 3 miesiące (zasada z metodyki). Dane z YTJ są aktualizowane przez PRH; częstotliwość aktualizacji nie potwierdzona – do sprawdzenia ręcznie.
- **Typowe sygnały podróbki / nieaktualności:** niezgodność Business ID z nazwą; nazwa w odpisie zapisana inaczej niż w YTJ (np. bez „Oy”, „Ky”, „Oyj”); adres siedziby w gminie innej niż w YTJ; osoby uprawnione inne niż w YTJ/PRH; brak daty wydania. Lista nie jest wyczerpująca.

## 4. Status firmy i sygnały ostrzegawcze

- **Formy prawne (wiedza ogólna, do potwierdzenia na przykładach z YTJ):** Oy (osakeyhtiö – spółka z o.o./akcyjna wg. prawa fińskiego, najczęstsza), Oyj (publiczna spółka akcyjna), Ky (kommandiittiyhtiö – spółka komandytowa), Toiminimi (jednoosobowa działalność wpisana do rejestru – pojęcie fińskie, nie spółka), Avoin yhtiö (Ay – spółka jawna).
- **Statusy:** YTJ pokazuje status podmiotu i wybór „aktywne / zlikwidowane”. Dokładne nazwy statusów (np. w likwidacji, upadłość, wykreślenie) nie zostały potwierdzone – do sprawdzenia ręcznie na przykładzie firmy w likwidacji.
- **Upadłość / restrukturyzacja:** rejestr upadłości (konkurssi, yrityssaneeraus) – nie potwierdzono, czy jest bezpłatny i gdzie. Prowadzi go sąd (Käräjäoikeus / Tingsrätt) – do sprawdzenia ręcznie (wyszukiwanie w rejestrze sądowym oraz w ogłoszeniach).
- **Zaległości podatkowe / ZUS-owe:** Finlandia nie publikuje zaległości podatkowych firm w YTJ (w YTJ wyszukiwanie tytułu zaległości dla prywatnych przedsiębiorców wynika z uwagi na stronie instrukcji – szczegóły do sprawdzenia ręcznie). Zaległości nie są w dostępnym publicznie zakresie – nie potwierdzono.
- **Red flags specyficzne dla kraju:** firmy zarejestrowane pod adresem wirtualnego biura lub adresem „kotipaikka” w gminie bez działalności; wielokrotna zmiana zarządu i gminy siedziby w krótkim czasie; nowe spółki Oy o przedmiocie „konsulting”/„holding” bez zatrudnienia; wspólne adresy wielu spółek. Są to ogólne wskaźniki – do potwierdzenia z doświadczenia zespołu.

## 5. Zarząd, wspólnicy, reprezentacja

- **Osoby uprawnione do reprezentacji i sposób reprezentacji:** w usługach aplikacyjnych PRH (płatne, wymaga umowy – sekcja 2). W YTJ nie potwierdzono wyświetlania tych danych bez umowy (do sprawdzenia ręcznie na przykładzie podmiotu).
- **Wspólnicy / akcjonariusze:** rejestr akcjonariuszy spółki nie jest prowadzony centralnie przez PRH jako publiczny – nie potwierdzono. W spółkach niepublicznych (Oy) lista akcjonariuszy jest w księdze akcyjnej spółki i nie jest publiczna – wg wiedzy ogólnej, do sprawdzenia ręcznie. Wymagać od klienta.
- **Dokumenty założycielskie / sprawozdania finansowe:** statut (PDF) i sprawozdania finansowe są dostępne w usługach aplikacyjnych PRH (płatne, potwierdzone – strona usług PRH). W bezpłatnym YTJ nie potwierdzono ich wyświetlania.
- **Reprezentacja a odpis:** przy umowie sprawdzić, czy podpisujący jest osobą uprawnioną wg odpisu (osobno, czy samodzielnie, czy łącznie – „kaksi yhdessä”).

## 6. Beneficjenci rzeczywiści (UBO)

- **Rejestr:** rejestr tosiasiallisten edunsaajien (tosiasiallisten edunsaajien tiedot – beneficial owner details) prowadzony przez PRH jako część kaupparekisteri, ale nieujawniany w odpisie publicznym (wynik wyszukiwania ze strony PRH o naruszeniach obowiązku zgłoszenia – niezweryfikowane, strona zwróciła 404 przy próbie otwarcia).
- **Obowiązek zgłoszenia:** wg wyniku wyszukiwania (niezweryfikowane): zgłoszenie w YTJ jest bezpłatne; nieterminowe zgłoszenie po wezwaniu PRH wiąże się z karą 300 EUR (źródło: yrittajat.fi – nie PRH; do sprawdzenia ręcznie).
- **Dostęp – stan potwierdzony:**
  - Strona suomi.fi (otwarta 2026-11-16): dostęp do danych o beneficjentach jest ograniczony do podmiotów, których cel mieści się w ustawie o przeciwdziałaniu praniu pieniędzy: organy nadzoru wymienione w tej ustawie; podmioty objęte obowiązkiem CDD (banki, zakłady ubezpieczeń, inne instytucje finansowe, pośrednicy w obrocie nieruchomościami, biegli rewidenci); przedstawiciele mediów; inne podmioty, których cel jest zgodny z ustawą.
  - Cel: „zapobieganie praniu pieniędzy i finansowaniu terroryzmu”.
  - Wymagane: identyfikacja osoby (PRH „must identify the person”), możliwa autentykacja online, **umowa z PRH** jako klient-kontrakt.
  - Opłata: „subject to a fee” – cennik na stronie PRH (nie otwarto).
  - Strona nie opisuje pól danych ani wymogu uzasadnionego interesu.
- **Dostęp – stan po wyroku TSUE C-37/20 i C-601/20 (WM i Sovim, 22.11.2022):** wynik wyszukiwania potwierdza, że ogólny publiczny dostęp został zniesiony w UE; Transparency International (wrzesień 2025, wynik wyszukiwania – niezweryfikowane) podaje, że Finlandia oferuje zarówno dostęp ogólny z umową, jak i tryb wniosku e-mailowego. Raport e-Justice o Finlandii (BOR_Finland_EU_en.pdf) – nie udało się otworzyć (limit pobrań); według wyniku wyszukiwania opisuje uwierzytelnianie, autoryzację, umowę z PRH i opłaty.
- **Uwaga:** w wyniku wyszukiwania pojawił się wpis o „nowelizacji” z 1.10.2025 określonej jako fińska implementacja – źródło było oczywiście błędne (dotyczy austriackiego WiEReG); nie opierać się na nim. Konkretny akt fiński po wyroku (nowelizacja ustawy o rejestrze handlowym) – nie potwierdzono.
- **Próg beneficjenta:** 25% udziałów lub praw głosu, lub inna kontrola (podstawa: dyrektywa AML i ustawa fińska – próg 25% przyjęty jako standard, nie potwierdzono na stronie fińskiej – do sprawdzenia ręcznie). Definicja na suomi.fi: osoba, która „either owns the company or otherwise controls it”.
- **Dane widoczne (dla uprawnionego podmiotu):** wg wyniku wyszukiwania (niezweryfikowane): imię i nazwisko, data urodzenia, obywatelstwo, gmina zamieszkania. Nie potwierdzono na stronie PRH.
- **Trusty i fundacje:** nie potwierdzono zasad jawności trustów w Finlandii (Finlandia nie ma tradycyjnego prawa trustów); fundacje (säätiö) są w rejestrze fundacji PRH – do sprawdzenia ręcznie.

**Procedura zastępcza (obowiązkowa w praktyce, bo dostęp do UBO nie jest darmowy):**
1. Zażądać od klienta oświadczenia o beneficjentach zgodnie z pkt 5 metodyki (imię, nazwisko, data i miejsce urodzenia, obywatelstwo, kraj zamieszkania, % udziałów/kontrola, schemat struktury, oświadczenie PEP / RU/BY / listy sankcyjne).
2. Zażądać aktualnego wyciągu z rejestru akcjonariuszy (osakasluettelo / aktieboken) lub umowy spółek.
3. Potwierdzić z YTJ: Business ID, nazwę, siedzibę, status, osoby uprawnione (oraz ich zgodność z oświadczeniem).
4. Krzyżowo: GLEIF (LEI, jeśli istnieje, zwykle tylko duże podmioty), OpenCorporates (pomocniczo), media i wyniki wyszukiwania (także w języku fińskim i szwedzkim).
5. Jeśli struktura obejmuje spółki zagraniczne – powtórzyć procedurę dla każdej warstwy.
6. Jeśli zamawiający musi mieć potwierdzone UBO z rejestru – zapytać PRH o umowę/cennik (tietopalvelut@prh.fi) lub rozważyć płatne narzędzie – tylko jako ostatnia opcja, koszt do sprawdzenia.

## 7. Dodatkowe darmowe weryfikacje

- **VIES (VAT):** https://ec.europa.eu/taxation_customs/vies/ – strona otwarta tylko w tytule (pełna treść nie została pobrana). Format fińskiego numeru VAT: prefiks `FI` + 8 cyfr (wiedza ogólna – do sprawdzenia ręcznie). Czy VIES zwraca nazwę i adres dla Finlandii – nie potwierdzono.
- **EORI:** do sprawdzenia ręcznie (system EORI Komisji Europejskiej, weryfikacja online); nie potwierdzono wyniku dla Finlandii.
- **LEI (GLEIF):** https://search.gleif.org – dla większości małych spółek brak LEI; wyszukiwanie po LEI także w YTJ (potwierdzone).
- **Rejestr działalności regulowanych / licencji:** zależnie od towaru – do sprawdzenia ręcznie (np. Tukes, Traficom, Ruokavirasto); nie potwierdzono adresów.
- **Listy ostrzeżeń:** Finanssivalvonta (Urząd Nadzoru Finansowego) – publikuje informacje o międzynarodowej współpracy w zakresie AML (https://finanssivalvonta.fi/en/prevention-of-money-laundering-and-terrorist-financing/international-cooperation – wynik wyszukiwania, niezweryfikowane). Krajowych list nierzetelnych kontrahentów nie potwierdzono.
- **Adres:** sprawdzić, czy adres siedziby (kotipaikka / hemort) to rzeczywiste miejsce działalności (mapa; w YTJ często podawana tylko gmina).

## 8. Sankcje i powiązania RU/BY w tym kraju

- **Sankcje:** Finlandia stosuje sankcje UE (rozporządzenia Rady, w tym 833/2014 i 765/2006 wymienione w metodyce). Krajowej listy sankcyjnej nie potwierdzono – do sprawdzenia ręcznie (lista ministerstw spraw zagranicznych Finlandii, Ulkoministeriö/Utrikesministeriet).
- **Screening:** EU Sanctions Map (sanctionsmap.eu) i Financial Sanctions Files – podstawowe źródło dla Finlandii; OFAC i OpenSanctions zgodnie z metodyką.
- **Ryzyko reeksportu do RU/BY:** Finlandia graniczy z Rosją (ok. 1340 km granicy lądowej – wiedza ogólna, do potwierdzenia). Ryzyko reeksportu jest podwyższone dla towarów dual-use, technologicznych i pojazdów/części; nie potwierdzono konkretnych przypadków z pośrednictwem fińskich spółek – do sprawdzenia ręcznie w doniesieniach.
- **Na co zwrócić uwagę w strukturze właścicielskiej:** rosyjscy lub białoruscy udziałowcy w spółkach fińskich (także przez spółki pośrednie w Cyprze, ZEA, Turcji, Hongkongu, Kazachstanie); nominalni dyrektorzy; niedawne zmiany właściciela po 24.02.2022; obecność w rejestrze osób z obywatelstwem rosyjskim lub białoruskim jako członków zarządu.
- **Flaga „RU/BY”:** zgodnie z `00-metodyka.md` pkt 4 – oznaczać w systemie każdą rejestrację z beneficjentem z RU/BY, także gdy kraj rejestracji to Finlandia.

## 9. Procedura krok po kroku (checklist)

1. Zebrać od klienta: nazwę, Business ID (Y-tunnus), adres, odpis z rejestru (nie starszy niż 3 miesiące), dane osób uprawnionych, oświadczenie o beneficjentach (sekcja 6), stronę WWW, e-mail firmowy.
2. Wyszukać firmę po Business ID w YTJ (https://tietopalvelu.ytj.fi/yrityshaku.aspx?kielikoodi=3). Zapisać datę, godzinę i zrzut ekranu wyniku.
3. Porównać nazwę, Business ID, formę prawną, adres i status z odpisem klienta. Każdą rozbieżność odnotować.
4. Potwierdzić status: aktywna / zlikwidowana / inne (YTJ – filtr „aktywne”); sprawdzić wzmiankę o upadłości w sądzie właściwym (do sprawdzenia ręcznie).
5. Sprawdzić autentyczność odpisu: jeśli wątpliwość – zapytać PRH (tietopalvelut@prh.fi, +358 29 509 5675) o potwierdzenie wydanego dokumentu.
6. Osoby uprawnione do reprezentacji: zweryfikować z odpisem i z oświadczeniem; wymagać dokumentu tożsamości tych osób.
7. Ustalić beneficjentów: zażądać oświadczenia i rejestru akcjonariuszy; krzyżowo z GLEIF/OpenCorporates/mediami. Jeśli potrzebna urzędowa weryfikacja UBO – rozważyć umowę z PRH (płatne, wymaga celu z ustawy AML).
8. Screening sankcyjny firmy, zarządu, beneficjentów, adresu (EU Sanctions Map, OFAC, UK, ONZ, OpenSanctions). Zapisać wynik z datą.
9. Sprawdzić VAT w VIES (FI + 8 cyfr) i zapisać wynik.
10. Ocenić powiązania RU/BY (sekcja 8) i oznaczyć flagą w razie wskaźników.
11. Zapisać dowody w aktach klienta (odpis, zrzut YTJ, wynik screeningu, oświadczenie UBO).
12. Decyzja: akceptacja / akceptacja ze wzmocnionym nadzorem / odmowa; powtórzyć screening co najmniej raz w roku.

## 10. Ograniczenia i ryzyka

- **Nie da się za darmo sprawdzić UBO** – to największa luka. Procedura zastępcza (sekcja 6) jest jedynym darmowym sposobem.
- **Pełny odpis z rejestru handlowego i jego weryfikacja elektroniczna:** cennik i procedura nie zostały potwierdzone (PRH – kontakt bezpośredni).
- **Osoby uprawnione i statut:** płatne w usługach aplikacyjnych PRH (potwierdzone), w YTJ nie potwierdzono.
- **Transliteracja:** nazwy w fińskim i szwedzkim (ä, ö, å) – wyszukiwać także wariant bez znaków diakrytycznych; uważać na pomyłki w nazwach z „Oy/Oyj”.
- **Dane w YTJ mogą być opóźnione** względem rejestru – częstotliwość aktualizacji nie potwierdzona.
- **Wynik wyszukiwania o „obowiązku zgłoszenia UBO” i karze 300 EUR** pochodzi od źródeł branżowych, nie z prh.fi – do potwierdzenia.
- **Eskalacja do wzmocnionej weryfikacji (EDD):** przy anonimowym UBO (brak zgody na udostępnienie oświadczenia), strukturze z udziałem RU/BY, spółkach-przykrywkach w jurysdykcjach offshore w łańcuchu, zmianie właściciela po 2022, lub gdy PRH nie potwierdza danych.
- **Listy FATF:** nie potwierdzono pełnej aktualnej listy (strona FATF zwróciła 403; wyniki wyszukiwania nie zawierały Finlandii wśród jurysdykcji pod zwiększonym monitoringiem; Finlandia jest członkiem FATF od 1991 r., ostatnia ocena wzajemna – wg wyniku wyszukiwania – 2019). Sprawdzić ręcznie na fatf-gafi.org przed decyzją.
- **Lista UE państw trzecich wysokiego ryzyka:** Finlandia nie jest na niej – nie potwierdzono w tym researchu; sprawdzić ręcznie.
- **e-Justice / BRIS:** strona e-Justice o rejestrach Finlandii została wyszukana, ale nie została otwarta (limit). Wejście publiczne przez BRIS: https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-eu-countries/fi_fi (adres z wyniku wyszukiwania, do sprawdzenia ręcznie).

## 11. Źródła

- [Wyszukiwarka YTJ – instrukcje (ytj.fi)](https://www.ytj.fi/en/index/companysearch/searchinstructions.html) – oficjalne – otwarte w czasie researchu: tak
- [Wyszukiwarka YTJ (tietopalvelu.ytj.fi)](https://tietopalvelu.ytj.fi/yrityshaku.aspx?kielikoodi=3) – oficjalne (adres podany na stronie instrukcji) – otwarte: nie (tylko adres z instrukcji)
- [Usługi aplikacyjne PRH – cennik i zakres (prh.fi)](https://www.prh.fi/en/companiesandorganisations/tietopalvelut/sahkoisetpalvelut/sovelluspalvelut.html) – oficjalne – otwarte: tak
- [Dane beneficjentów rzeczywistych – usługa Suomi.fi (PRH)](https://www.suomi.fi/services/details-on-beneficial-owners-from-the-finnish-trade-register-finnish-patent-and-registration-office/9901ba79-a51f-47ac-9cec-5cf04f16d42b) – oficjalne – otwarte: tak
- [HCCH – status Konwencji haskiej 1961 (apostille), wiersz Finlandii](https://www.hcch.net/en/instruments/conventions/status-table/?cid=41) – oficjalne – otwarte: tak
- [VIES – sprawdzanie numerów VAT (Komisja Europejska)](https://ec.europa.eu/taxation_customs/vies/) – oficjalne – otwarte: tylko tytuł strony
- [PRH – informacje o rejestrze beneficjentów i naruszeniach (prh.fi)](https://prh.fi/en/kaupparekisteri/beneficial_owner_details/supervision/deficiencies-beneficial-owner-details.html) – oficjalne – otwarte: nie (404); wynik wyszukiwania
- [PRH – YTJ (prh.fi)](https://www.prh.fi/en/companiesandorganisations/tietopalvelut/ytj.html) – oficjalne – otwarte: nie; wynik wyszukiwania
- [PRH – otwarte dane (avoindata.prh.fi)](https://avoindata.prh.fi/en) – oficjalne – otwarte: nie; wynik wyszukiwania
- [e-Justice – raport o rejestrze beneficjentów Finlandii (BOR_Finland_EU_en.pdf)](https://e-justice.europa.eu/sites/default/files/2022-08/BOR_Finland_EU_en.pdf) – oficjalne (UE) – otwarte: nie (429); wynik wyszukiwania
- [e-Justice – rejestry handlowe państw UE, Finlandia](https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-eu-countries/fi_fi) – oficjalne (UE) – otwarte: nie (limit); wynik wyszukiwania
- [Transparency International – analiza rejestrów UBO po 2025 r.](https://www.transparency.org/en/news/countdown-to-new-eu-beneficial-ownership-rules) – nieoficjalne – otwarte: nie; wynik wyszukiwania
- [Finanssivalvonta – międzynarodowa współpraca AML](https://finanssivalvonta.fi/en/prevention-of-money-laundering-and-terrorist-financing/international-cooperation) – oficjalne (nadzór Finlandii) – otwarte: nie; wynik wyszukiwania
- [FATF – jurysdykcje pod zwiększonym monitoringiem, październik 2026](https://www.fatf-gafi.org/content/fatf-gafi/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-october-2026.html) – oficjalne – otwarte: nie (403); wynik wyszukiwania
- [Ministerstwo Spraw Zagranicznych Finlandii – legalizacja dokumentów](https://um.fi/legalising-documents-abroad) – oficjalne – otwarte: nie; wynik wyszukiwania
- [yrittajat.fi – obowiązek zgłoszenia UBO i kara 300 EUR](https://www.yrittajat.fi/uutiset/pida-yrityksen-edunsaajatiedot-ajan-tasalla-ja-valta-300-euron-maksu) – nieoficjalne (organizacja przedsiębiorców) – otwarte: nie; wynik wyszukiwania
