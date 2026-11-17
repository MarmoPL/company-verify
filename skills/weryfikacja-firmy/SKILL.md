---
name: "weryfikacja-firmy"
description: "Weryfikuje firmę lub kontrahenta w oficjalnych rejestrach (KRS, CEIDG, biała lista VAT, CRBR – beneficjenci rzeczywiści, VIES, GLEIF, Companies House, rejestry UE) z dokumentu (faktura, umowa, PDF, zdjęcie) lub danych (NIP, KRS, REGON, nazwa, rachunek). Daje werdykt, rozbieżności, linki z ID zapytań, zrzuty, oficjalne PDF-y i raport PDF. Używaj też, gdy ktoś wkleja sam NIP albo pyta, czy faktura lub firma jest legit."
---

# Weryfikacja firmy w oficjalnych rejestrach

Cel: potwierdzić w źródłach urzędowych, że firma istnieje i jest aktywna, ustalić jej beneficjentów rzeczywistych i zestawić to z dokumentem lub danymi od użytkownika.

Rezultat (domyślnie wszystkie cztery):
1. krótkie podsumowanie w czacie z werdyktem i linkami,
2. raport PDF z danymi, rozbieżnościami, linkami i identyfikatorami zapytań,
3. zrzuty ekranu ze stron rejestrów (jako załącznik raportu),
4. oficjalne PDF-y pobrane z rejestrów (odpis KRS, wydruk CRBR, …).

Potwierdzeniem jest tylko rejestr urzędowy. Serwisy agregujące (aleo, rejestr.io, OpenCorporates, wywiadownie) mogą być nieaktualne — używaj ich najwyżej do znalezienia numeru, nigdy jako dowodu.

## 0. Czym odpytujesz rejestry — ustal to najpierw

Sandbox zwykle nie ma dostępu do rejestrów: shell dostaje 403 od proxy, a WebFetch odrzuca adresy, których nie podał użytkownik. Nie trać na to wywołań. Kolejność:

1. **Przeglądarka** — Claude in Chrome (`mcp__claude-in-chrome__*`) albo przeglądarka wbudowana. To tryb podstawowy: wszystkie źródła z sekcji 2–3 działają w niej bez captchy. Wczytaj narzędzia jednym ToolSearch (tabs_context_mcp, tabs_create_mcp, navigate, get_page_text, javascript_tool, computer, find, read_page, browser_batch, tabs_close_mcp), pracuj w nowej karcie i zamknij ją na koniec.
2. Shell z dostępem do sieci (np. lokalny Claude Code) — te same URL-e API pobierzesz `curl`; kroki „klikane” (CRBR, wyszukiwarka KRS) i tak wymagają przeglądarki.
3. Bez przeglądarki: zbuduj linki z sekcji 2 (API białej listy, KRS, VIES, GLEIF zwracają JSON wprost w przeglądarce, także na telefonie) i poproś użytkownika, żeby je otworzył albo odesłał w wiadomości — link wysłany przez użytkownika WebFetch już przeczyta. Raport oznacz wtedy jako „częściowo niezweryfikowany”.

Praktyka w Chrome:
- `navigate` wysyłaj osobno; kolejne kroki na tej samej karcie (czekanie, `get_page_text`, `javascript_tool`, kliknięcia, zrzut) łącz w `browser_batch`.
- Wynik `javascript_tool` jest obcinany po ok. 1,5 tys. znaków — zwracaj małe obiekty, a duży JSON czytaj przez `get_page_text`.
- Zrzut do raportu: `computer` → `screenshot` z `save_to_disk: true` (plik ląduje w sandboxie, ścieżka jest w wyniku jako „Image source”). Krótki JSON (np. sprawdzenie rachunku) fotografuj akcją `zoom` z regionem obejmującym tylko tekst; długi — po zaznaczeniu „Pretty-print”. Strony SPA (CRBR, wyszukiwarka KRS) potrzebują 2–3 s na załadowanie wyniku.
- Banery cookies: odrzucaj niekonieczne („Reject analytics cookies”), zanim zrobisz zrzut.
- Pobranie pliku z SPA (KRS, CRBR) nie zostawia śladu w sandboxie. Żeby je potwierdzić, przed kliknięciem przechwyć blob i kliknij przyciskiem z JS (działa też, gdy przycisk przykrywa okno modalne):
```js
window.__dl=[];const oc=URL.createObjectURL;URL.createObjectURL=function(b){window.__dl.push({type:b.type,size:b.size});return oc.apply(this,arguments)};
[...document.querySelectorAll('button')].find(x=>/Pobierz (plik )?PDF/.test(x.innerText)).click();await new Promise(r=>setTimeout(r,4000));JSON.stringify(window.__dl)
```
  Niepusta lista = plik poszedł do folderu Pobrane. Pusta — powiedz użytkownikowi, żeby sprawdził folder, albo pobierz ręcznie przyciskiem.

## 1. Dane wejściowe

- **Dokument** (PDF, skan, zdjęcie, .docx): odczytaj go i wypisz „dane deklarowane”: nazwa, forma prawna, NIP, KRS, REGON, adres, nr rachunku, osoby podpisujące i ich funkcje, data dokumentu, kwota brutto (próg 15 000 zł), nr VAT UE lub zagraniczny numer rejestrowy.
- **Same dane**: to, co podał użytkownik. Gdy jest tylko nazwa — znajdź numer w wyszukiwarce biznes.gov.pl (obejmuje KRS i CEIDG) lub w wyszukiwarce KRS; przy kilku trafieniach zapytaj, o którą firmę chodzi.
- **Sumy kontrolne**: uruchom `ids.py` (sekcja 8). Zła suma kontrolna NIP, REGON albo rachunku w dokumencie to sygnał ryzyka (literówka albo podróbka) — zapisz jako rozbieżność i szukaj dalej po nazwie.

Ścieżka: sp. z o.o., S.A., PSA, spółki osobowe, fundacje, stowarzyszenia, spółdzielnie → KRS. Jednoosobowa działalność, wspólnicy spółki cywilnej → CEIDG. Firma zagraniczna → sekcja 3.

## 2. Źródła polskie

Sprawdź wszystkie pasujące. Każde źródło to wiersz `sources` w raporcie: nazwa, status (OK / UWAGA / BLAD / BRAK), podsumowanie, link, ID zapytania, czas.

### 2a. Biała lista VAT (Ministerstwo Finansów)
- `https://wl-api.mf.gov.pl/api/search/nip/{NIP}?date={RRRR-MM-DD}` (też `/search/regon/{REGON}`, `/search/bank-account/{NRB}`) → `get_page_text`.
- Weź: `statusVat` (Czynny / Zwolniony; brak podmiotu = niezarejestrowany lub wykreślony — wtedy sprawdź `removalDate`, `removalBasis`, `registrationDenialBasis`), `krs`, `regon`, `residenceAddress` / `workingAddress`, `accountNumbers`, `hasVirtualAccounts` oraz zawsze **`requestId` i `requestDateTime`** — to identyfikator wyszukiwania, który MF potwierdza na żądanie.
- Rachunek z dokumentu sprawdź osobnym endpointem (obsługuje też rachunki wirtualne, których nie ma na liście): `https://wl-api.mf.gov.pl/api/check/nip/{NIP}/bank-account/{NRB_26_cyfr}?date={RRRR-MM-DD}` → `accountAssigned: TAK/NIE` + `requestId`. Data = dzień zlecenia przelewu (domyślnie dziś).
- Dlaczego to ważne: przy płatności powyżej 15 000 zł brutto na rachunek spoza białej listy nabywca traci koszt podatkowy i ryzykuje solidarną odpowiedzialność za VAT dostawcy, chyba że zapłaci split paymentem albo w 7 dni od zlecenia przelewu złoży ZAW-NR (art. 117ba Ordynacji podatkowej). Dlatego „NIE” przy takiej kwocie ma wagę wysoką.
- API ma dzienne limity — nie odpytuj w pętli.

### 2b. KRS — API Ministerstwa Sprawiedliwości (dane spółki)
- `https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/{KRS}?rejestr=P&format=json`. Stowarzyszenia i fundacje bez działalności gospodarczej: `rejestr=S`. Historia zmian: `OdpisPelny`. Błąd/404 = brak w tym rejestrze, spróbuj drugiego.
- API maskuje osoby (`M***** K*******`) — pełne imiona i nazwiska weź z wyszukiwarki KRS (2c) lub CRBR (2e).
- Ekstrakcja dwoma małymi wywołaniami `javascript_tool` na stronie z JSON-em:
```js
// 1) podmiot
const o=JSON.parse(document.body.innerText).odpis,d=o.dane,p=d.dzial1.danePodmiotu,a=d.dzial1.siedzibaIAdres?.adres||{};
JSON.stringify({naglowek:o.naglowekA,nazwa:p.nazwa,forma:p.formaPrawna,...p.identyfikatory,
 adres:[a.ulica,a.nrDomu,a.nrLokalu&&'lok. '+a.nrLokalu,a.kodPocztowy,a.miejscowosc,a.kraj].filter(Boolean).join(' '),
 kapital:d.dzial1.kapital?.wysokoscKapitaluZakladowego,
 wspolnicy:(d.dzial1.wspolnicySpzoo||d.dzial1.wspolnicy||[]).map(w=>({kto:w.nazwa||[w.imiona?.imie,w.nazwisko?.nazwiskoICzlon].join(' '),udzialy:w.posiadaneUdzialy})),
 dzial4:Object.keys(d.dzial4||{}),dzial6:Object.keys(d.dzial6||{})})
```
```js
// 2) reprezentacja
const d=JSON.parse(document.body.innerText).odpis.dane,r=d.dzial2?.reprezentacja,os=x=>[x.imiona?.imie,x.nazwisko?.nazwiskoICzlon,x.nazwisko?.nazwiskoIICzlon].filter(Boolean).join(' ');
JSON.stringify({organ:r?.nazwaOrganu,sposob:r?.sposobReprezentacji,sklad:(r?.sklad||[]).map(s=>os(s)+' — '+s.funkcjaWOrganie+(s.czyZawieszona?' (zawieszony)':'')),prokurenci:(d.dzial2?.prokurenci||[]).map(s=>os(s)+' — '+s.rodzajProkury)})
```
- Sygnały: klucze działu 6 inne niż `polaczeniePodzialPrzeksztalcenie` (likwidacja, upadłość, restrukturyzacja, rozwiązanie, kurator) → sprawdź szczegóły, zwykle waga wysoka. Wpisy w dziale 4 (zaległości, wierzytelności) → uwaga. Rejestracja młodsza niż 6 miesięcy przy dużej transakcji → uwaga. Świeża zmiana zarządu, adresu lub nazwy tuż przed transakcją → uwaga (data ostatniego wpisu jest w `naglowek`).
- Gdy adres, nazwa lub osoba z dokumentu nie zgadza się z obecnym stanem — sprawdź historię w `OdpisPelny`. Stary adres siedziby na fakturze to typowy ślad podszycia (oszust kopiuje dawny wzór dokumentu):
```js
const o=JSON.parse(document.body.innerText).odpis,A=o.dane.dzial1.siedzibaIAdres.adres,W=Object.fromEntries((o.naglowekP.wpis||[]).map(w=>[w.numerWpisu,w.dataWpisu]));
JSON.stringify((Array.isArray(A)?A:[A]).map(a=>({adres:[a.ulica,a.nrDomu,a.kodPocztowy,a.miejscowosc].join(' '),od:W[a.nrWpisuWprow],do:W[a.nrWpisuWykr]||'obecny'})))
```

### 2c. Wyszukiwarka KRS — pełne nazwiska i oficjalny odpis PDF
- `https://wyszukiwarka-krs.ms.gov.pl/` → pole „Numer KRS” (formularz pamięta poprzednią wartość — zaznacz pole potrójnym kliknięciem i wpisz od nowa; można też NIP / REGON / nazwę) → „Wyszukaj” → „Wyświetl szczegółowe dane”. Strona pokazuje pełne imiona i nazwiska zarządu oraz sekcje „Wykreślenie z KRS”, „Zawieszenie / wznowienie”, „Postępowanie upadłościowe”.
- Tabela „Skład organu reprezentacji” pokazuje 5 osób na stronę — porównaj liczbę z API (2b) i przewijaj stronami. Skrypt zwraca osoby z bieżącej strony; z `next=true` najpierw klika „Następna strona”:
```js
const next=false; if(next){[...document.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')==='Następna strona').click();await new Promise(r=>setTimeout(r,800))}
const t=document.body.innerText,i=t.indexOf('Skład organu reprezentacji'),L=t.slice(i,t.indexOf('Siedziba i adres',i)).split('\n'),out=[];let c={};
for(let k=0;k<L.length;k++){const v=L[k+1];if(L[k]==='Nazwisko lub Nazwa')c={n:v};if(L[k]==='Nazwisko drugi człon'&&v!=='-')c.n+='-'+v;if(L[k]==='Imię pierwsze')c.i=v;if(L[k]==='Imię drugie'&&v!=='-')c.i+=' '+v;if(L[k]==='Funkcja')out.push(c.i+' '+c.n+' — '+v)}
JSON.stringify(out)
```
- Zrzut ekranu sekcji „Dane podmiotu”.
- Odpis: panel „Informacje aktualne” → „Pobierz PDF” (tam też „Informacje pełne”). Samodzielnie pobrany wydruk ma moc zrównaną z dokumentami Centralnej Informacji KRS (art. 4 ust. 4aa ustawy o KRS) — to jest dokument potwierdzający istnienie spółki.
- Przy dużych kwotach zajrzyj też do zakładki „Wyszukaj dłużnika” (Krajowy Rejestr Zadłużonych: upadłość, restrukturyzacja — także osób prowadzących JDG).

### 2d. CEIDG — jednoosobowe działalności i wspólnicy s.c.
- `https://www.biznes.gov.pl/pl/wyszukiwarka-firm/` → pole „NIP” → „Szukaj” → otwórz wpis. Weź: imię i nazwisko przedsiębiorcy, firmę, status (aktywny / zawieszony / wykreślony / oczekuje na rozpoczęcie), datę rozpoczęcia, adresy, PKD. Jeśli wpis ma opcję pobrania lub wydruku PDF — pobierz; wydruk z CEIDG jest jedną z form zaświadczenia o wpisie (art. 46 ustawy o CEIDG).
- Spółka cywilna nie ma wpisu jako całość — sprawdź każdego wspólnika w CEIDG, a NIP spółki na białej liście.
- Ta wyszukiwarka obejmuje też KRS — przydaje się, gdy znasz tylko nazwę.

### 2e. CRBR — beneficjenci rzeczywiści (odbiorcy końcowi)
- `https://crbr.podatki.gov.pl/adcrbr/#/wyszukaj` → zostaw „Wyszukiwanie podmiotu” → kliknij pole „NIP / identyfikator trustu” i wpisz NIP (albo pole „KRS”) → przycisk „Wyszukaj” jest pod formularzem (`find` → `scroll_to` → klik) → w wierszu wyniku przycisk rozwijający (`find` „ui-btn” w tabeli) → `get_page_text` zwraca sekcje „Beneficjenci” (imiona, nazwisko, PESEL, obywatelstwo, kraj zamieszkania, uprawnienia) i „Zgłaszający”.
- Zapisz „Identyfikator złożonego wniosku” i czas — to ID zapytania CRBR.
- Zanim zrobisz zrzut listy beneficjentów, zamaskuj PESEL-e na stronie (zmienia tylko widok w przeglądarce):
```js
const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode())n.nodeValue=n.nodeValue.replace(/\b(\d{2})\d{7}(\d{2})\b/g,'$1*******$2');'ok'
```
- „Pobierz plik PDF” → oficjalny wydruk (z pełnymi PESEL-ami — to dokument urzędowy, nie zmieniaj go); portal zaznacza, że dokument z CRBR nie wymaga dodatkowego podpisu. Lista beneficjentów otwiera się w oknie, które przykrywa przycisk — użyj skryptu pobierania z sekcji 0.
- Interpretacja:
  - Brak wpisu spółki handlowej (poza spółkami publicznymi), fundacji, stowarzyszenia rejestrowego lub spółdzielni → waga wysoka: zgłoszenie jest obowiązkowe, za brak grozi kara do 1 mln zł (art. 153 ustawy AML). JDG i s.c. nie zgłaszają — beneficjentem jest sam przedsiębiorca lub wspólnicy.
  - Beneficjent wskazany wyłącznie jako „osoba zajmująca wyższe stanowisko kierownicze” = spółka nie ustaliła właściciela będącego osobą fizyczną (typowe w grupach notowanych lub zagranicznych). Odnotuj to i porównaj ze wspólnikami z KRS; jeśli wspólnikiem jest spółka zagraniczna, idź łańcuchem (GLEIF, rejestr kraju wspólnika).
  - „Występują uwagi o rozbieżnościach: TAK” → uwaga.
  - Beneficjenci w CRBR niezgodni ze wspólnikami z KRS (np. wspólnik 100% to osoba fizyczna, a w CRBR jest ktoś inny) → uwaga.
- PESEL w raporcie maskuj (np. `76*******73`); pełny tylko na wyraźną prośbę użytkownika. Nie zapisuj PESEL-i w pamięci.
- Nie wyszukuj osób po PESEL lub nazwisku, chyba że użytkownik wyraźnie o to prosi.

### 2f. VIES — numer VAT UE
- `https://ec.europa.eu/taxation_customs/vies/rest-api/ms/{KOD_KRAJU}/vat/{NUMER_BEZ_PREFIKSU}` → `isValid`, `name`, `address`, `requestDate`.
- Polski NIP „nieaktywny” w VIES oznacza brak rejestracji do transakcji wewnątrzwspólnotowych, nie nieistnienie firmy. Niektóre kraje (np. DE, ES) nie zwracają nazwy ani adresu.

### 2g. Uzupełniająco
- GLEIF (globalny, bez klucza): otwórz `https://api.gleif.org/api/v1/lei-records?filter[entity.registeredAs]={KRS_lub_nr}&filter[entity.legalAddress.country]={KOD}` i na tej stronie uruchom (rodzice w jednym wywołaniu; `NON_PUBLIC` = spółka nie ujawnia rodzica):
```js
const d=JSON.parse(document.body.innerText).data[0],L=d.id,A='https://api.gleif.org/api/v1/lei-records/'+L,g=async s=>{const r=await fetch(A+s);return r.ok?(await r.json()).data:null},nm=x=>x&&(x.attributes.entity?{lei:x.id,name:x.attributes.entity.legalName.name,kraj:x.attributes.entity.legalAddress.country}:x.attributes.reason);
JSON.stringify({lei:L,nazwa:d.attributes.entity.legalName.name,status:d.attributes.entity.status,bezposredni:nm(await g('/direct-parent'))||nm(await g('/direct-parent-reporting-exception')),najwyzszy:nm(await g('/ultimate-parent'))||nm(await g('/ultimate-parent-reporting-exception'))})
```
  GLEIF pokazuje strukturę grupy (osoby prawne), nie osoby fizyczne.
- Sankcje — przy prośbie o AML/KYC albo gdy w łańcuchu jest podmiot spoza UE: lista MSWiA (`https://www.gov.pl/web/mswia/lista-osob-i-podmiotow-objetych-sankcjami`) i unijna mapa sankcji (`https://www.sanctionsmap.eu/`). Sprawdź firmę i beneficjentów.

## 3. Firmy zagraniczne

Rejestr spółek jest prawie zawsze publiczny, rejestr UBO w UE zwykle nie: po wyroku TSUE z 22.11.2022 większość państw zamknęła publiczny dostęp (zostaje „uzasadniony interes” lub dostęp dla instytucji obowiązanych). Nie obiecuj beneficjentów tam, gdzie rejestr jest zamknięty — napisz to w raporcie i podaj, co ustaliłeś zamiast tego (wspólnicy z rejestru spółek, łańcuch GLEIF).

| Kraj | Rejestr spółek (bezpłatny) | Beneficjenci |
|---|---|---|
| UK | Companies House `https://find-and-update.company-information.service.gov.uk/company/{numer}` + `/officers`, `/persons-with-significant-control`, `/filing-history` (PDF-y dokumentów za darmo); wyszukiwanie: `/search/companies?q=`. VIES nie obejmuje UK (poza Irlandią Płn., prefiks XI) | Publiczny rejestr PSC. Gdy PSC to spółka — przejdź do jej numeru i powtarzaj, aż dojdziesz do osoby fizycznej albo spółki notowanej (te są zwolnione z PSC; wtedy domknij łańcuch GLEIF-em) |
| DE | `https://www.handelsregister.de` → wyszukiwanie → dokument „AD” (aktueller Abdruck, darmowy PDF) | Transparenzregister — tylko z uzasadnionym interesem |
| FR | `https://annuaire-entreprises.data.gouv.fr` (SIREN, dirigeants, statut) | RBE (INPI) — ograniczony |
| CZ | `https://ares.gov.cz`, `https://or.justice.cz` | Zamknięty dla publiczności od 12.2025 |
| SK | `https://www.orsr.sk`; RPVS `https://rpvs.gov.sk` (tylko partnerzy sektora publicznego) | Ogólny rejestr zamknięty |
| EE | `https://ariregister.rik.ee` | Był publiczny — sprawdź, czy nadal |
| LV | `https://www.ur.gov.lv` | Publiczny |
| Inne UE | e-Justice „Znajdź spółkę” (BRIS) na e-justice.europa.eu + VIES + GLEIF | Zwykle ograniczony |

Dostęp do rejestrów UBO zmienia się wraz z wdrażaniem 6AMLD — gdy rejestr danego kraju jest kluczowy, sprawdź jego aktualny status wyszukiwarką. Dla innych krajów znajdź oficjalny rejestr wyszukiwarką i oznacz w raporcie, z czego skorzystałeś.

Szczegółowa metodyka AML/KYC (w tym procedura flagowania beneficjentów z Rosji i Białorusi oraz wzór oświadczenia UBO) znajduje się w pliku `00-metodyka.md`, a szczegółowe przewodniki dla poszczególnych jurysdykcji w katalogu `kraje/` (np. `kraje/DE-germany.md`, `kraje/US-united-states.md`, `kraje/HK-hong-kong.md`, `kraje/AE-united-arab-emirates.md`, `kraje/CY-cyprus.md`, `kraje/PL-poland.md`).

## 4. Porównanie i werdykt

Zestaw dane deklarowane z rejestrami. Waga rozbieżności:
- **wysoka**: brak podmiotu w rejestrach, wykreślenie, likwidacja, upadłość; NIP z dokumentu należy do innej firmy; rachunek „NIE” na białej liście przy kwocie powyżej 15 000 zł; status VAT niezarejestrowany na fakturze z VAT; podpisujący nie ma umocowania według sposobu reprezentacji; brak wpisu w CRBR tam, gdzie jest obowiązkowy; trafienie na liście sankcyjnej.
- **średnia**: adres inny niż siedziba (sprawdź `workingAddress` i adres do doręczeń); rachunek spoza listy przy mniejszej kwocie; spółka młodsza niż 6 miesięcy; świeże zmiany w zarządzie; uwagi o rozbieżnościach w CRBR; reprezentacja łączna, a podpisała jedna osoba.
- **niska**: różnice w zapisie nazwy (skróty, wielkość liter, „sp. z o.o.” vs pełna forma), literówka w kodzie pocztowym lub numerze lokalu.

Werdykt:
- `POTWIERDZONA` — istnieje, aktywna, dane zgodne, brak uwag wysokich i średnich.
- `POTWIERDZONA_Z_UWAGAMI` — istnieje i jest aktywna, ale są rozbieżności średnie albo luki (np. UBO niedostępne za granicą).
- `NIEPOTWIERDZONA` — nie znaleziono, nieaktywna albo jest choć jedna uwaga wysoka. Dotyczy też sytuacji „firma istnieje, ale dokument się z nią nie zgadza” — wtedy w `verdict_note` napisz to wprost (możliwe podszycie) i co zrobić: potwierdzić u firmy kanałem znanym z wcześniejszej współpracy, nie z danych z dokumentu.

Typowy obraz podszycia pod znaną firmę: prawdziwy NIP i KRS, ale „nowy rachunek” spoza białej listy, nieaktualny adres, podpis osoby spoza zarządu i prokury, nacisk na pilną płatność.

Nie łagodź werdyktu: fałszywy alarm z wyjaśnieniem kosztuje mniej niż przepuszczony oszust. Nie udzielaj porady prawnej — wskaż konsekwencje (np. próg 15 000 zł), decyzja należy do użytkownika.

## 5. Dowody: zrzuty ekranu i oficjalne PDF-y

- Zrzuty (do raportu): wynik białej listy (przy fakturze — wynik sprawdzenia rachunku), dane podmiotu z wyszukiwarki KRS / wpis CEIDG / strona Companies House, wynik CRBR z beneficjentami (PESEL zamaskowany). Każdy podpisz: źródło + data i godzina.
- Oficjalne PDF-y (odpis KRS, wydruk CRBR, wydruk CEIDG, AD z Handelsregister) pobierają się do folderu Pobrane na komputerze użytkownika. Pobranie pliku wymaga zgody: jeśli prośba użytkownika mówi o dokumentach, odpisach albo PDF-ach z rejestrów, to jest zgoda; w przeciwnym razie zapytaj raz, wymieniając pliki i źródła. Tych plików nie widzisz w sandboxie — wpisz je w raporcie do „Pobrane dokumenty urzędowe” z miejscem „folder Pobrane na Twoim komputerze”.

## 6. Raport PDF

Zapisz oba skrypty z sekcji 8 do katalogu roboczego, przygotuj `dane.json` i uruchom:
`python3 report.py dane.json Weryfikacja_{Nazwa}_{RRRR-MM-DD}.pdf`
Przed wysłaniem obejrzyj pierwszą stronę (np. `pdftoppm -png -r 60 -f 1 -l 1`), potem wyślij plik przez `SendUserFile`.

Schemat `dane.json` (pola bez danych pomiń):
```json
{
  "company": {"name": "", "legal_form": "", "country": "PL", "nip": "", "krs": "", "regon": "",
              "company_number": "", "vat_eu": "", "lei": "", "address": "", "registered_on": "",
              "status": "", "capital": "", "vat_status": ""},
  "verdict": "POTWIERDZONA | POTWIERDZONA_Z_UWAGAMI | NIEPOTWIERDZONA",
  "verdict_note": "jedno-dwa zdania uzasadnienia",
  "checked_at": "RRRR-MM-DD GG:MM",
  "input_source": "np. faktura FV/12/2026 z 10.11.2026 albo: NIP podany w czacie",
  "representation_method": "",
  "representatives": [{"name": "", "function": ""}],
  "shareholders": [{"name": "", "shares": ""}],
  "ubo_source": "CRBR, identyfikator wniosku …, RRRR-MM-DD GG:MM",
  "beneficial_owners": [{"name": "", "citizenship": "", "residence": "", "control": "", "pesel_masked": ""}],
  "ubo_note": "tekst, gdy brak beneficjentów lub rejestr niedostępny",
  "discrepancies": [{"field": "", "document": "", "registry": "", "severity": "wysoka | średnia | niska"}],
  "sources": [{"name": "", "status": "OK | UWAGA | BLAD | BRAK", "summary": "", "url": "",
               "request_id": "", "timestamp": ""}],
  "official_documents": [{"name": "", "where": ""}],
  "screenshots": [{"path": "/ścieżka/z/save_to_disk.jpg", "caption": "Źródło – data i godzina"}],
  "notes": [""]
}
```

## 7. Podsumowanie w czacie

Krótko, czytelnie na telefonie:
1. Werdykt jednym zdaniem (✅ / ⚠️ / ❌) z nazwą, NIP / KRS i statusem.
2. Trzy do sześciu punktów: status VAT i wynik sprawdzenia rachunku, data rejestracji, reprezentacja, beneficjenci (imię i nazwisko + charakter kontroli), najważniejsze rozbieżności.
3. Linki do źródeł z identyfikatorami zapytań oraz lista plików: raport (w czacie), oficjalne PDF-y (w folderze Pobrane).

## 8. Skrypty

`ids.py` — walidacja sum kontrolnych NIP, REGON, KRS i rachunku (bez sieci):
```python
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
```

`report.py` — raport PDF (reportlab + font DejaVu z polskimi znakami; gdy brak reportlab: `pip install reportlab --break-system-packages`):
```python
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
```