# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

C = []

C.append(mk.card(1236, 'Westerwoldsche A Zuid', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Beekdal \u00b7 hermeanderde laaglandbeek', 'list 34 \u00b7 no. 13'],
 'loc': '\U0001f4cd Tussen Wedde en Blijham \u00b7 Beekdallandschap \u00b7 Lange noord-zuidcorridor',
 'desc': 'De <b>Westerwoldsche A</b> ontstaat waar de Ruiten Aa en de Mussel Aa samenkomen en voert het water van heel Westerwolde noordwaarts naar het Oldambt. Het zuidelijke deel is de afgelopen decennia ingrijpend <b>hermeanderd</b>: de kaarsrechte kanaalbedding uit de ruilverkaveling is verlaten en de beek slingert weer door zijn eigen dal. Dat is meer dan cosmetiek. Een meanderende beek stroomt <b>trager</b>, houdt water langer vast in het landschap en biedt een afwisseling van <b>diepe buitenbochten en ondiepe grindbanken</b> waar vissen paaien. Langs de oevers ontstaan opnieuw <b>ruigtes, natte hooilanden en elzensingels</b>. Het dal is bovendien een <b>ecologische verbindingszone</b> van formaat: otter en bever trekken hier tussen Duitsland en het Groninger achterland. In de winter loopt het dal bewust onder \u2014 de zogeheten <b>waterberging</b> \u2014 en dan is het een glinsterende vlakte vol <b>smienten, wintertalingen en kieviten</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (beekvegetatie en vogels), nov\u2013feb (waterberging en watervogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend en late avond \u2014 otter en bever zijn schemeractief.',
 'why': ['Grootschalig <b>hermeanderd</b> beekdal \u2014 herstel in plaats van kanalisatie.',
         'Belangrijke <b>ecologische verbindingszone</b> met otter en bever.',
         'Winterse <b>waterberging</b> trekt duizenden eenden en steltlopers.',
         'Natte hooilanden en <b>elzensingels</b> langs de oevers.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f41f <b>Vissen trekken stroomopwaarts</b> over de nieuwe ondiepten.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel en oeverzwaluw</b> broeden in de steile buitenbochten.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Ruigtes in bloei</b> \u2014 moerasspirea, koninginnenkruid en valeriaan.',
          '<span class="months">Nov\u2013Feb</span> \U0001f4a7 <b>Waterberging</b> \u2014 het dal loopt onder en vult zich met watervogels.'],
 'wild': ['\U0001f9a6 Otter', '\U0001f9ab Bever', '\U0001f426 IJsvogel \u00b7 Oeverzwaluw', '\U0001f986 Smient \u00b7 Wintertaling', '\U0001f33f Moerasspirea \u00b7 Dotterbloem'],
 'trail': ['Startpunten bij <b>Wedde</b> en <b>Blijham</b>; het dal is over grote lengte begaanbaar.',
           'Het <b>fietspad langs de beek</b> geeft het beste overzicht van de meanders.',
           'Bij hoogwater kunnen delen van de paden <b>onder water staan</b> \u2014 laarzen aanbevolen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kan \u2019s winters overstromen \u00b7 \U0001f6b4 Goed per fiets'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Brook valley \u00b7 remeandered lowland stream', 'list 34 \u00b7 no. 13'],
 'loc': '\U0001f4cd Between Wedde and Blijham \u00b7 Brook-valley landscape \u00b7 Long north-south corridor',
 'desc': 'The <b>Westerwoldsche A</b> forms where the Ruiten Aa and the Mussel Aa meet and carries the water of the whole of Westerwolde northwards to the Oldambt. Its southern stretch has been thoroughly <b>remeandered</b> in recent decades: the ruler-straight channel of the land consolidation era has been abandoned and the brook again winds through its own valley. That is more than cosmetic. A meandering brook flows <b>more slowly</b>, holds water in the landscape for longer and offers an alternation of <b>deep outer bends and shallow gravel bars</b> where fish spawn. Along the banks, <b>tall-herb fringes, wet hay meadows and alder rows</b> are returning. The valley is also a major <b>ecological corridor</b>: otter and beaver move along it between Germany and the Groningen hinterland. In winter the valley is deliberately allowed to flood \u2014 so-called <b>water storage</b> \u2014 and then it becomes a glittering plain full of <b>wigeon, teal and lapwing</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (brook vegetation and birds), Nov\u2013Feb (water storage and waterfowl)<br>\n    <b>Best time of day:</b> Early morning and late evening \u2014 otter and beaver are active at dusk.',
 'why': ['Large-scale <b>remeandered</b> brook valley \u2014 restoration instead of canalisation.',
         'Important <b>ecological corridor</b> with otter and beaver.',
         'Winter <b>water storage</b> attracts thousands of ducks and waders.',
         'Wet hay meadows and <b>alder rows</b> along the banks.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f41f <b>Fish migrate upstream</b> across the new shallows.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher and sand martin</b> breed in the steep outer bends.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Tall herbs in flower</b> \u2014 meadowsweet, hemp-agrimony and valerian.',
          '<span class="months">Nov\u2013Feb</span> \U0001f4a7 <b>Water storage</b> \u2014 the valley floods and fills with waterfowl.'],
 'wild': ['\U0001f9a6 Otter', '\U0001f9ab Beaver', '\U0001f426 Kingfisher \u00b7 Sand martin', '\U0001f986 Wigeon \u00b7 Teal', '\U0001f33f Meadowsweet \u00b7 Marsh marigold'],
 'trail': ['Access points at <b>Wedde</b> and <b>Blijham</b>; the valley is walkable over long stretches.',
           'The <b>cycle path along the brook</b> gives the best overview of the meanders.',
           'At high water parts of the paths may be <b>flooded</b> \u2014 boots recommended.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f May flood in winter \u00b7 \U0001f6b4 Good by bike'
}, card_class='card water'))

C.append(mk.card(1237, 'Bouten', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Kleinschalig cultuurlandschap \u00b7 houtwallen', 'list 34 \u00b7 no. 14'],
 'loc': '\U0001f4cd Bij Vlagtwedde, Westerwolde \u00b7 Esdorpenlandschap \u00b7 Klein gebied',
 'desc': 'De <b>Bouten</b> is een van die kleine Westerwoldse terreinen die je op geen enkele toeristische kaart vindt en die juist daarom zo\u2019n zuiver beeld geven van hoe het <b>oude zandlandschap</b> functioneerde. Het is een mozaa\u00efek van <b>bouwlandkampen, houtwallen en vochtige laagtes</b>, precies op de overgang van de hoge es naar het beekdal. De naam verwijst naar <i>bouwland</i>: dit waren de akkers die eeuwenlang met <b>plaggenmest</b> werden opgehoogd, waardoor de bodem letterlijk decimeters is gegroeid. De omringende <b>houtwallen</b> waren geen decoratie maar functioneel \u2014 ze hielden vee binnen, leverden geriefhout en beschermden het gewas tegen wind. Vandaag zijn diezelfde wallen <b>lijnvormige natuurreservaatjes</b>: broedplaats voor geelgors en grauwe klauwier, jachtgebied voor vleermuizen en corridor voor das en marterachtigen. In het voorjaar bloeien er <b>sleedoorn en meidoorn</b>, in het najaar hangt het vol <b>bessen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (broedvogels en bloei), sep\u2013okt (bessen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 geelgors en grauwe klauwier zingen en jagen vanaf de wallen.',
 'why': ['Gaaf <b>kleinschalig zandlandschap</b> van kampen en houtwallen.',
         '<b>Plaggendek</b> heeft de akkers eeuwenlang letterlijk opgehoogd.',
         'Houtwallen als <b>lijnvormige leefgebieden</b> voor vogels en zoogdieren.',
         'Zeldzame combinatie van <b>geelgors en grauwe klauwier</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Sleedoorn en meidoorn</b> in volle bloei op de wallen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Grauwe klauwier</b> jaagt vanaf uitkijkposten; prooien op doorns geprikt.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Vlinders</b> langs de zonnige wallenkanten.',
          '<span class="months">Sep\u2013Okt</span> \U0001f347 <b>Bessendracht</b> \u2014 lijsters en zanglijsters strijken massaal neer.'],
 'wild': ['\U0001f426 Geelgors', '\U0001f426 Grauwe klauwier', '\U0001f987 Vleermuizen', '\U0001f9a1 Das', '\U0001f33f Sleedoorn \u00b7 Meidoorn \u00b7 Hazelaar'],
 'trail': ['Parkeren in <b>Vlagtwedde</b>; het gebied ligt aan lokale zandwegen.',
           'Volg de <b>wandelroutes van Westerwolde</b> die de houtwallen aandoen.',
           'Klein terrein \u2014 goed te combineren met het dal van de Ruiten Aa.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Deels particulier bouwland \u00b7 \U0001f6b6 Kort rondje'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Small-scale farmed landscape \u00b7 hedgebanks', 'list 34 \u00b7 no. 14'],
 'loc': '\U0001f4cd Near Vlagtwedde, Westerwolde \u00b7 Es-village landscape \u00b7 Small area',
 'desc': 'The <b>Bouten</b> is one of those small Westerwolde sites that appears on no tourist map and precisely for that reason gives such a pure picture of how the <b>old sandy landscape</b> worked. It is a mosaic of <b>arable enclosures, hedgebanks and damp hollows</b>, exactly on the transition from the high open field to the brook valley. The name refers to <i>bouwland</i>, arable land: these were the fields raised for centuries with <b>sod manure</b>, so that the soil literally grew by decimetres. The surrounding <b>hedgebanks</b> were not decoration but functional \u2014 they kept livestock in, supplied usable wood and sheltered the crop from wind. Today those same banks are <b>linear nature reserves</b>: breeding sites for yellowhammer and red-backed shrike, hunting grounds for bats and corridors for badger and mustelids. In spring <b>blackthorn and hawthorn</b> flower here; in autumn the banks hang full of <b>berries</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (breeding birds and blossom), Sep\u2013Oct (berries and autumn colour)<br>\n    <b>Best time of day:</b> Morning \u2014 yellowhammer and red-backed shrike sing and hunt from the banks.',
 'why': ['Intact <b>small-scale sandy landscape</b> of enclosures and hedgebanks.',
         '<b>Sod-manure layer</b> literally raised the fields over centuries.',
         'Hedgebanks as <b>linear habitats</b> for birds and mammals.',
         'Rare combination of <b>yellowhammer and red-backed shrike</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Blackthorn and hawthorn</b> in full flower on the banks.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Red-backed shrike</b> hunts from perches; prey impaled on thorns.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Butterflies</b> along the sunny edges of the banks.',
          '<span class="months">Sep\u2013Oct</span> \U0001f347 <b>Berry crop</b> \u2014 thrushes and redwings descend in numbers.'],
 'wild': ['\U0001f426 Yellowhammer', '\U0001f426 Red-backed shrike', '\U0001f987 Bats', '\U0001f9a1 Badger', '\U0001f33f Blackthorn \u00b7 Hawthorn \u00b7 Hazel'],
 'trail': ['Park in <b>Vlagtwedde</b>; the area lies along local sand tracks.',
           'Follow the <b>Westerwolde walking routes</b> that take in the hedgebanks.',
           'Small site \u2014 easily combined with the valley of the Ruiten Aa.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Partly private arable land \u00b7 \U0001f6b6 Short circuit'
}))

C.append(mk.card(1238, 'Veenkoloni\u00ebn', {
 'tags': ['Groningen \u00b7 Veenkoloni\u00ebn', 'Ontginningslandschap \u00b7 kanalen en wijken', 'list 34 \u00b7 no. 15'],
 'loc': '\U0001f4cd Tussen Hoogezand, Veendam, Stadskanaal en Ter Apel \u00b7 Cultuurlandschap \u00b7 Zeer groot gebied',
 'desc': 'De <b>Veenkoloni\u00ebn</b> zijn geen natuurgebied maar een <b>landschap dat je moet begrijpen</b> om de rest van Oost-Groningen te kunnen lezen. Hier lag ooit het immense <b>Bourtanger Moor</b>, een hoogveenkussen van meters dik dat zich uitstrekte tot ver in Duitsland. Vanaf de zeventiende eeuw is het door de stad Groningen systematisch afgegraven: eerst een <b>hoofddiep</b> graven, dan haaks daarop de <b>wijken</b>, het veen laten uitdrogen, de turf steken en per schip afvoeren. Wat overbleef was de <b>dalgrond</b>, het zandige restant onderin, dat met stadsmest tot akkerland werd gemaakt. Het resultaat is een landschap van <b>meetkundige strengheid</b>: rechte kanalen, lintdorpen, eindeloze horizonten. Ecologisch is de winst pas recent \u2014 in <b>natuurontwikkelingsprojecten</b> worden oude wijken verbreed en petgaten uitgegraven, waardoor <b>roerdomp, blauwborst en otter</b> terugkeren in wat generaties lang louter productielandschap was.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Hele jaar</b>; apr\u2013jun (moerasvogels in de nieuwe natuur), nov\u2013feb (ganzen en open horizonten)<br>\n    <b>Beste tijd van de dag:</b> Late middag \u2014 het strijklicht toont het lijnenspel van kanalen en wijken op zijn best.',
 'why': ['Sleutel tot het begrip van het <b>Oost-Groninger landschap</b>.',
         'Restant van het immense <b>Bourtanger Moor</b>, systematisch afgegraven.',
         '<b>Hoofddiepen en wijken</b> als meetkundig ontginningspatroon.',
         'Nieuwe natuur brengt <b>roerdomp, blauwborst en otter</b> terug.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Blauwborst en rietzanger</b> in de verbrede wijken.',
          '<span class="months">Mei\u2013Jul</span> \U0001f4a8 <b>Roerdomp</b> hoorbaar in de nieuwe rietmoerassen.',
          '<span class="months">Aug\u2013Sep</span> \U0001f33e <b>Oogsttijd</b> \u2014 aardappelen, suikerbieten en granen op de dalgrond.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Ganzen en zwanen</b> op de open akkers.'],
 'wild': ['\U0001f426 Blauwborst \u00b7 Rietzanger', '\U0001f426 Roerdomp', '\U0001f9a6 Otter', '\U0001f9a2 Kolgans \u00b7 Wilde zwaan', '\U0001f33f Riet \u00b7 Lisdodde in de wijken'],
 'trail': ['Startpunten in <b>Veendam</b>, <b>Stadskanaal</b> en <b>Ter Apel</b>.',
           'Het <b>Veenkoloniaal Museum</b> in Veendam verklaart het hele systeem.',
           'Bij uitstek een landschap voor de <b>fiets</b> \u2014 volg de kanalen kilometerslang.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Grotendeels particulier akkerland \u00b7 \U0001f6b4 Fietslandschap bij uitstek'
}, {
 'tags': ['Groningen \u00b7 Peat Colonies', 'Reclamation landscape \u00b7 canals and side canals', 'list 34 \u00b7 no. 15'],
 'loc': '\U0001f4cd Between Hoogezand, Veendam, Stadskanaal and Ter Apel \u00b7 Cultural landscape \u00b7 Very large area',
 'desc': 'The <b>Veenkoloni\u00ebn</b> (Peat Colonies) are not a nature reserve but a <b>landscape you must understand</b> in order to read the rest of eastern Groningen. Here once lay the immense <b>Bourtanger Moor</b>, a raised-bog cushion metres thick that stretched far into Germany. From the seventeenth century the city of Groningen dug it away systematically: first cut a <b>main canal</b>, then the <b>side canals</b> at right angles to it, let the bog dry out, cut the peat and ship it away. What remained was the <b>dalgrond</b>, the sandy residue at the bottom, turned into arable land with city manure. The result is a landscape of <b>geometric severity</b>: straight canals, ribbon villages, endless horizons. The ecological gain is only recent \u2014 in <b>nature development projects</b> old side canals are widened and pools dug out, so that <b>bittern, bluethroat and otter</b> are returning to what was purely production land for generations.',
 'meta': '<b>Best season &amp; peak months:</b> <b>All year</b>; Apr\u2013Jun (marsh birds in the new nature areas), Nov\u2013Feb (geese and open horizons)<br>\n    <b>Best time of day:</b> Late afternoon \u2014 raking light shows the geometry of canals and side canals at its best.',
 'why': ['Key to understanding the <b>eastern Groningen landscape</b>.',
         'Remnant of the immense <b>Bourtanger Moor</b>, systematically dug away.',
         '<b>Main and side canals</b> as a geometric reclamation pattern.',
         'New nature brings back <b>bittern, bluethroat and otter</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Bluethroat and sedge warbler</b> in the widened side canals.',
          '<span class="months">May\u2013Jul</span> \U0001f4a8 <b>Bittern</b> audible in the new reed marshes.',
          '<span class="months">Aug\u2013Sep</span> \U0001f33e <b>Harvest time</b> \u2014 potatoes, sugar beet and grain on the cut-over soil.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Geese and swans</b> on the open fields.'],
 'wild': ['\U0001f426 Bluethroat \u00b7 Sedge warbler', '\U0001f426 Bittern', '\U0001f9a6 Otter', '\U0001f9a2 White-fronted goose \u00b7 Whooper swan', '\U0001f33f Reed \u00b7 Bulrush in the side canals'],
 'trail': ['Starting points in <b>Veendam</b>, <b>Stadskanaal</b> and <b>Ter Apel</b>.',
           'The <b>Veenkoloniaal Museum</b> in Veendam explains the whole system.',
           'Above all a landscape for the <b>bicycle</b> \u2014 follow the canals for kilometres.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Largely private arable land \u00b7 \U0001f6b4 Ideal cycling landscape'
}))

C.append(mk.card(1239, 'Vledderhuizen landschapselementen', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Landschapselementen \u00b7 houtwallen en poelen', 'list 34 \u00b7 no. 16'],
 'loc': '\U0001f4cd Bij Onstwedde en Vledderhuizen \u00b7 Verspreide landschapselementen \u00b7 Klein oppervlak',
 'desc': 'Bij <b>Vledderhuizen</b> beheert Staatsbosbeheer geen aaneengesloten reservaat maar een verzameling <b>losse landschapselementen</b>: houtwallen, singels, poelen, bosjes en perceelsrandjes verspreid door het boerenland. Dat klinkt bescheiden, maar juist deze snippers bepalen of een agrarisch landschap <b>leeft of leeg</b> is. Een <b>poel</b> van tien bij tien meter kan de enige voortplantingsplek voor kamsalamander en heikikker in de wijde omtrek zijn. Een <b>houtwal</b> van tweehonderd meter verbindt twee bosjes en maakt het verschil tussen een ge\u00efsoleerde en een levensvatbare populatie. De elementen bij Vledderhuizen zijn bovendien <b>historisch</b>: veel wallen staan al op negentiende-eeuwse kaarten en de <b>eikenstoven</b> erop zijn generaties lang afgezet, waardoor ze een veel hogere leeftijd hebben dan hun dunne stammen doen vermoeden. Het beheer is arbeidsintensief \u2014 om de zoveel jaar afzetten, poelen uitbaggeren \u2014 en gebeurt deels met vrijwilligers.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (amfibie\u00ebn en broedvogels), okt\u2013nov (herfstkleur en bessen)<br>\n    <b>Beste tijd van de dag:</b> Schemer in het voorjaar \u2014 dan roepen de kikkers bij de poelen.',
 'why': ['Netwerk van <b>historische houtwallen</b> met eeuwenoude eikenstoven.',
         '<b>Poelen</b> als onmisbare voortplantingsplek voor kamsalamander en heikikker.',
         'Toont hoe <b>kleine elementen</b> een heel agrarisch landschap dragen.',
         'Beheer deels door <b>vrijwilligers</b> \u2014 levend cultuurhistorisch onderhoud.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Heikikker</b> \u2014 mannetjes kleuren enkele dagen fel blauw.',
          '<span class="months">Apr\u2013Mei</span> \U0001f98e <b>Kamsalamander</b> baltst in de poelen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors en braamsluiper</b> in de wallen.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Afzetten van hakhout</b> \u2014 traditioneel wallenbeheer zichtbaar.'],
 'wild': ['\U0001f98e Kamsalamander', '\U0001f438 Heikikker', '\U0001f426 Geelgors \u00b7 Braamsluiper', '\U0001f987 Vleermuizen', '\U0001f333 Zomereik \u00b7 Hazelaar \u00b7 Lijsterbes'],
 'trail': ['Parkeren in <b>Onstwedde</b>; de elementen liggen langs openbare zandwegen.',
           'Geen gemarkeerde route \u2014 <b>combineer met de wandelpaden rond Onstwedde</b>.',
           'Respecteer <b>particuliere percelen</b>: de elementen zijn vanaf de weg te bekijken.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Verspreide elementen, geen aaneengesloten terrein \u00b7 \U0001f6b6 Vanaf de weg'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Landscape features \u00b7 hedgebanks and ponds', 'list 34 \u00b7 no. 16'],
 'loc': '\U0001f4cd Near Onstwedde and Vledderhuizen \u00b7 Scattered landscape features \u00b7 Small area',
 'desc': 'At <b>Vledderhuizen</b> the State Forestry Service manages not a single continuous reserve but a collection of <b>separate landscape features</b>: hedgebanks, tree rows, ponds, copses and field margins scattered through the farmland. That sounds modest, but it is exactly these fragments that decide whether an agricultural landscape is <b>alive or empty</b>. A <b>pond</b> ten metres square may be the only breeding site for great crested newt and moor frog for miles around. A <b>hedgebank</b> two hundred metres long links two copses and makes the difference between an isolated and a viable population. The features at Vledderhuizen are also <b>historic</b>: many banks already appear on nineteenth-century maps, and the <b>oak stools</b> on them have been coppiced for generations, giving them a far greater age than their slender stems suggest. Management is labour-intensive \u2014 coppicing every few years, dredging out ponds \u2014 and is partly done by volunteers.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (amphibians and breeding birds), Oct\u2013Nov (autumn colour and berries)<br>\n    <b>Best time of day:</b> Dusk in spring \u2014 when the frogs call at the ponds.',
 'why': ['Network of <b>historic hedgebanks</b> with centuries-old oak stools.',
         '<b>Ponds</b> as indispensable breeding sites for great crested newt and moor frog.',
         'Shows how <b>small features</b> carry an entire farmed landscape.',
         'Management partly by <b>volunteers</b> \u2014 living heritage maintenance.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Moor frog</b> \u2014 males turn bright blue for a few days.',
          '<span class="months">Apr\u2013May</span> \U0001f98e <b>Great crested newt</b> displays in the ponds.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer and lesser whitethroat</b> in the banks.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Coppicing</b> \u2014 traditional hedgebank management on view.'],
 'wild': ['\U0001f98e Great crested newt', '\U0001f438 Moor frog', '\U0001f426 Yellowhammer \u00b7 Lesser whitethroat', '\U0001f987 Bats', '\U0001f333 Pedunculate oak \u00b7 Hazel \u00b7 Rowan'],
 'trail': ['Park in <b>Onstwedde</b>; the features lie along public sand tracks.',
           'No waymarked route \u2014 <b>combine with the footpaths around Onstwedde</b>.',
           'Respect <b>private plots</b>: the features can be viewed from the road.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Scattered features, not a continuous site \u00b7 \U0001f6b6 View from the road'
}))

C.append(mk.card(1240, 'Vlagtwedde landschapselementen', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Landschapselementen \u00b7 essen en wallen', 'list 34 \u00b7 no. 17'],
 'loc': '\U0001f4cd Rond Vlagtwedde \u00b7 Verspreide landschapselementen \u00b7 Klein oppervlak',
 'desc': 'Rond het dorp <b>Vlagtwedde</b> ligt een tweede reeks beschermde <b>landschapselementen</b>, en samen met die van Vledderhuizen vormen ze het geraamte van het Westerwoldse cultuurlandschap. Vlagtwedde was van oudsher een <b>esdorp</b>: het dorp op de rand van de hoge zandkop, de gemeenschappelijke <b>es</b> ernaast, de <b>madelanden</b> in het beekdal en daarachter de woeste gronden. Die viertrapsindeling is nog altijd afleesbaar, en de bewaarde <b>houtwallen, singels, steilranden en solitaire eiken</b> markeren de grenzen ertussen. Bijzonder zijn de <b>steilranden</b>: door eeuwenlange ophoging met plaggenmest ligt de es soms een meter hoger dan het aangrenzende land, en die abrupte overgang is een landschappelijk archief op zich. Voor de natuur betekenen deze elementen <b>zoom en mantel</b> \u2014 de warme, bloemrijke overgangszones waar insecten, reptielen en zangvogels van afhankelijk zijn.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013aug</b> (bloei, insecten en zangvogels), okt\u2013nov (herfst en beheerwerk)<br>\n    <b>Beste tijd van de dag:</b> Zonnige ochtend \u2014 dan zijn de zoomvegetaties het levendigst.',
 'why': ['<b>Steilranden</b> tonen hoe hoog de es door plaggenbemesting is opgehoogd.',
         'Complete <b>esdorpstructuur</b> nog afleesbaar rond het dorp.',
         '<b>Zoom- en mantelvegetaties</b> als hotspot voor insecten en zangvogels.',
         'Monumentale <b>solitaire eiken</b> als bakens in het akkerland.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Bloeiende wallen</b> \u2014 sleedoorn, meidoorn en look-zonder-look.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors</b> zingt vanaf de wallen; \u2018een beetje bro-o-od\u2019.',
          '<span class="months">Jun\u2013Aug</span> \U0001f41d <b>Wilde bijen</b> op de warme zuidkanten van de steilranden.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> van eik, hazelaar en lijsterbes.'],
 'wild': ['\U0001f426 Geelgors \u00b7 Grasmus', '\U0001f41d Wilde bijen', '\U0001f98e Levendbarende hagedis', '\U0001f333 Monumentale zomereiken', '\U0001f33f Look-zonder-look \u00b7 Dagkoekoeksbloem'],
 'trail': ['Parkeren in het centrum van <b>Vlagtwedde</b>.',
           'De <b>dorpsommetjes</b> voeren langs de belangrijkste wallen en steilranden.',
           'Combineer met <b>De Bouten</b> en het dal van de Ruiten Aa voor een volle dag.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Verspreide elementen in boerenland \u00b7 \U0001f6b6 Dorpsommetje'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Landscape features \u00b7 open fields and banks', 'list 34 \u00b7 no. 17'],
 'loc': '\U0001f4cd Around Vlagtwedde \u00b7 Scattered landscape features \u00b7 Small area',
 'desc': 'Around the village of <b>Vlagtwedde</b> lies a second series of protected <b>landscape features</b>, and together with those at Vledderhuizen they form the skeleton of the Westerwolde cultural landscape. Vlagtwedde was traditionally an <b>es village</b>: the village on the edge of the high sandy rise, the communal <b>open field</b> beside it, the <b>hay lands</b> in the brook valley and beyond them the waste grounds. That four-tier arrangement can still be read, and the surviving <b>hedgebanks, tree rows, escarpments and solitary oaks</b> mark the boundaries between them. The <b>escarpments</b> are especially striking: centuries of raising the soil with sod manure have left the open field sometimes a metre higher than the adjoining land, and that abrupt step is an archive in itself. For nature these features mean <b>fringe and mantle</b> \u2014 the warm, flower-rich transition zones on which insects, reptiles and songbirds depend.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Aug</b> (flowering, insects and songbirds), Oct\u2013Nov (autumn and management work)<br>\n    <b>Best time of day:</b> Sunny morning \u2014 when the fringe vegetation is liveliest.',
 'why': ['<b>Escarpments</b> show how high the open field was raised by sod manuring.',
         'Complete <b>es-village structure</b> still legible around the village.',
         '<b>Fringe and mantle vegetation</b> as a hotspot for insects and songbirds.',
         'Monumental <b>solitary oaks</b> as landmarks in the arable land.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Flowering banks</b> \u2014 blackthorn, hawthorn and garlic mustard.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer</b> sings from the banks: \u2018a little bit of bread and no cheese\u2019.',
          '<span class="months">Jun\u2013Aug</span> \U0001f41d <b>Wild bees</b> on the warm south faces of the escarpments.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> of oak, hazel and rowan.'],
 'wild': ['\U0001f426 Yellowhammer \u00b7 Whitethroat', '\U0001f41d Wild bees', '\U0001f98e Viviparous lizard', '\U0001f333 Monumental pedunculate oaks', '\U0001f33f Garlic mustard \u00b7 Red campion'],
 'trail': ['Park in the centre of <b>Vlagtwedde</b>.',
           'The <b>village circular walks</b> pass the main banks and escarpments.',
           'Combine with <b>De Bouten</b> and the Ruiten Aa valley for a full day.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Scattered features in farmland \u00b7 \U0001f6b6 Village circuit'
}))

mk.insert(C, '1235')
mk.progress(1240)
mk.check()
