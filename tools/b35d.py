# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1262, 'Amstelmeer', {
 'tags': ['Noord-Holland \u00b7 Hollands Kroon', 'Binnenmeer \u00b7 restant Zuiderzee-inham', 'list 35 \u00b7 no. 15'],
 'loc': '\U0001f4cd Bij Van Ewijcksluis en Wieringen \u00b7 Ondiep binnenmeer \u00b7 Groot wateroppervlak',
 'desc': 'Het <b>Amstelmeer</b> is een merkwaardig overblijfsel: tot 1924 was dit een open zeearm tussen het eiland <b>Wieringen</b> en de vaste wal, onderdeel van de <b>Zuiderzee</b>. Toen de Amsteldiepdijk \u2014 het eerste, kleine proefstuk van de Afsluitdijk \u2014 werd gelegd, viel het water erachter stil en verzoette het langzaam. Wat overbleef is een ondiep, luw meer met <b>brakke restinvloeden</b> in de bodem, en juist die tussentoestand maakt het waardevol. Er groeien nog <b>ruppia en zannichellia</b>, waterplanten van zwak brak water, en de oevers dragen <b>riet, biezen en zilte graslandjes</b>. Voor vogels is het meer vooral in de winter belangrijk: het bevriest laat en biedt dan een toevluchtsoord voor duizenden <b>kuifeenden, toppers, brilduikers en futen</b>. In de zomer broeden er <b>visdief, bruine kiekendief en baardman</b> in de rietzomen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Nov\u2013feb</b> (grote aantallen duikeenden), mei\u2013jul (broedvogels in de rietzomen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend bij windstil weer \u2014 dan is het water spiegelglad en zijn de eenden goed te tellen.',
 'why': ['Restant van een <b>Zuiderzee-inham</b>, afgesloten in 1924.',
         'De <b>Amsteldiepdijk</b> was het proefstuk voor de Afsluitdijk.',
         'Zwak <b>brakke waterplanten</b> als ruppia en zannichellia.',
         'Winterse concentraties <b>kuifeend, topper en brilduiker</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Visdief</b> jaagt boven het open water.',
          '<span class="months">Mei\u2013Jul</span> \U0001f985 <b>Bruine kiekendief en baardman</b> in de rietzomen.',
          '<span class="months">Okt\u2013Nov</span> \U0001f986 <b>Aankomst</b> van de eerste duikeenden.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Duizenden kuifeenden en toppers</b> op het meer.'],
 'wild': ['\U0001f986 Kuifeend \u00b7 Topper \u00b7 Brilduiker', '\U0001f426 Visdief \u00b7 Fuut', '\U0001f985 Bruine kiekendief', '\U0001f426 Baardman', '\U0001f33f Ruppia \u00b7 Riet \u00b7 Zilte graslandjes'],
 'trail': ['Parkeren bij <b>Van Ewijcksluis</b> of langs de dijk richting Wieringen.',
           'De <b>dijken rond het meer</b> geven het beste zicht op het water.',
           'Neem een <b>telescoop</b> mee voor de duikeenden ver op het meer.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Open en winderig; watersport in de zomer \u00b7 \U0001f52d Telescoop nuttig'
}, {
 'tags': ['North Holland \u00b7 Hollands Kroon', 'Inland lake \u00b7 former Zuiderzee inlet', 'list 35 \u00b7 no. 15'],
 'loc': '\U0001f4cd Near Van Ewijcksluis and Wieringen \u00b7 Shallow inland lake \u00b7 Large water surface',
 'desc': 'The <b>Amstelmeer</b> is a curious survival: until 1924 this was an open sea arm between the island of <b>Wieringen</b> and the mainland, part of the <b>Zuiderzee</b>. When the Amsteldiepdijk \u2014 the first small trial section of the Afsluitdijk \u2014 was laid, the water behind it fell still and slowly freshened. What remains is a shallow, sheltered lake with <b>residual brackish influence</b> in the bed, and it is precisely that in-between state that makes it valuable. <b>Beaked tasselweed and horned pondweed</b> still grow here, water plants of slightly brackish water, and the shores carry <b>reed, club-rush and small saline grasslands</b>. For birds the lake matters most in winter: it freezes late and then offers refuge to thousands of <b>tufted duck, scaup, goldeneye and great crested grebe</b>. In summer <b>common tern, marsh harrier and bearded reedling</b> breed in the reed fringes.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Nov\u2013Feb</b> (large numbers of diving ducks), May\u2013Jul (breeding birds in the reed fringes)<br>\n    <b>Best time of day:</b> Morning in calm weather \u2014 the water is mirror-still and the ducks easy to count.',
 'why': ['Remnant of a <b>Zuiderzee inlet</b>, closed off in 1924.',
         'The <b>Amsteldiepdijk</b> was the trial section for the Afsluitdijk.',
         'Slightly <b>brackish water plants</b> such as tasselweed and horned pondweed.',
         'Winter concentrations of <b>tufted duck, scaup and goldeneye</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Common tern</b> hunting over the open water.',
          '<span class="months">May\u2013Jul</span> \U0001f985 <b>Marsh harrier and bearded reedling</b> in the reed fringes.',
          '<span class="months">Oct\u2013Nov</span> \U0001f986 <b>Arrival</b> of the first diving ducks.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Thousands of tufted duck and scaup</b> on the lake.'],
 'wild': ['\U0001f986 Tufted duck \u00b7 Scaup \u00b7 Goldeneye', '\U0001f426 Common tern \u00b7 Great crested grebe', '\U0001f985 Marsh harrier', '\U0001f426 Bearded reedling', '\U0001f33f Tasselweed \u00b7 Reed \u00b7 Saline grassland'],
 'trail': ['Park at <b>Van Ewijcksluis</b> or along the dike towards Wieringen.',
           'The <b>dikes around the lake</b> give the best view over the water.',
           'Bring a <b>telescope</b> for the diving ducks far out on the lake.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Open and windy; watersports in summer \u00b7 \U0001f52d Telescope useful'
}, card_class='card water'))

C.append(mk.card(1263, 'Eendenkooi \u2019t Zand', {
 'tags': ['Noord-Holland \u00b7 Schagen', 'Eendenkooi \u00b7 kooibos in polderland', 'list 35 \u00b7 no. 16'],
 'loc': '\U0001f4cd Bij \u2019t Zand, Zijpe \u00b7 Eendenkooi met bos \u00b7 Zeer klein',
 'desc': 'De <b>Eendenkooi \u2019t Zand</b> ligt in de Zijpepolder, een van de oudste droogmakerijen van Noord-Holland (1597), en is een van de weinige kooien in dit vlakke, open land die nog compleet zijn. Wie er komt ziet meteen waarom kooien zo herkenbaar zijn in het landschap: een <b>vierkant bosje</b> midden in het weiland, van veraf zichtbaar als een donkere vlek. Binnenin ligt de <b>kooiplas</b> met vier gebogen <b>vangpijpen</b>, elk in een andere windrichting, zodat er altijd een pijp is waar de eenden met de wind mee in vliegen. Het <b>kooibos</b> eromheen bestaat uit <b>els, es en meidoorn</b>, dicht genoeg om alle beweging aan het zicht te onttrekken. Doordat het bosje al eeuwen ongemoeid blijft, is het een eiland van biodiversiteit in intensief boerenland: <b>ransuil, sperwer en grote bonte specht</b> broeden er, en het is een vaste rustplaats voor <b>vleermuizen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Okt\u2013mrt</b> (eenden op de kooiplas), apr\u2013jun (broedvogels in het kooibos)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 dan vliegen de eenden in en jagen de uilen.',
 'why': ['Compleet bewaarde <b>eendenkooi</b> met vier vangpijpen.',
         'Vierkant <b>kooibos</b> als herkenbaar baken in de open Zijpepolder.',
         'Pijpen in <b>vier windrichtingen</b> \u2014 altijd \u00e9\u00e9n met de wind mee.',
         'Eeuwenlange rust maakt het tot een <b>biodiversiteitseiland</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f989 <b>Ransuil</b> broedt in oude kraaiennesten.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Grote bonte specht en sperwer</b> in het kooibos.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Vleermuizen</b> jagen boven de kooiplas.',
          '<span class="months">Okt\u2013Mrt</span> \U0001f986 <b>Eenden</b> verzamelen zich op de plas.'],
 'wild': ['\U0001f989 Ransuil', '\U0001f426 Sperwer \u00b7 Grote bonte specht', '\U0001f987 Vleermuizen', '\U0001f986 Wilde eend \u00b7 Wintertaling', '\U0001f333 Zwarte els \u00b7 Es \u00b7 Meidoorn'],
 'trail': ['De kooi ligt in <b>particulier polderland</b> bij \u2019t Zand \u2014 van buitenaf zichtbaar.',
           '<b>Kooirust</b>: niet betreden zonder toestemming van de kooiker.',
           'Soms <b>rondleidingen</b> \u2014 informeer bij het Hoogheemraadschap of de beheerder.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Alleen vanaf de weg \u00b7 \u26a0\ufe0f Kooirust \u2014 stilte en afstand \u00b7 \U0001f9ed Op afspraak'
}, {
 'tags': ['North Holland \u00b7 Schagen', 'Duck decoy \u00b7 decoy wood in polder land', 'list 35 \u00b7 no. 16'],
 'loc': '\U0001f4cd Near \u2019t Zand, Zijpe \u00b7 Duck decoy with wood \u00b7 Very small',
 'desc': 'The <b>Eendenkooi \u2019t Zand</b> lies in the Zijpe polder, one of the oldest reclamations in North Holland (1597), and is one of the few decoys in this flat, open land that are still complete. Anyone visiting immediately sees why decoys are so recognisable in the landscape: a <b>square copse</b> in the middle of the meadows, visible from afar as a dark patch. Inside lies the <b>decoy pond</b> with four curved <b>catching pipes</b>, each facing a different quarter, so that there is always a pipe the ducks can fly into downwind. The surrounding <b>decoy wood</b> consists of <b>alder, ash and hawthorn</b>, dense enough to hide all movement. Because the copse has been left undisturbed for centuries, it is an island of biodiversity in intensive farmland: <b>long-eared owl, sparrowhawk and great spotted woodpecker</b> breed here, and it is a regular roost for <b>bats</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Oct\u2013Mar</b> (ducks on the decoy pond), Apr\u2013Jun (breeding birds in the decoy wood)<br>\n    <b>Best time of day:</b> Dusk \u2014 when the ducks fly in and the owls hunt.',
 'why': ['Completely preserved <b>duck decoy</b> with four catching pipes.',
         'Square <b>decoy wood</b> as a landmark in the open Zijpe polder.',
         'Pipes facing <b>four quarters</b> \u2014 always one to fly into downwind.',
         'Centuries of quiet make it an <b>island of biodiversity</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f989 <b>Long-eared owl</b> breeds in old crow nests.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Great spotted woodpecker and sparrowhawk</b> in the decoy wood.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Bats</b> hunt over the decoy pond.',
          '<span class="months">Oct\u2013Mar</span> \U0001f986 <b>Ducks</b> gather on the pond.'],
 'wild': ['\U0001f989 Long-eared owl', '\U0001f426 Sparrowhawk \u00b7 Great spotted woodpecker', '\U0001f987 Bats', '\U0001f986 Mallard \u00b7 Teal', '\U0001f333 Black alder \u00b7 Ash \u00b7 Hawthorn'],
 'trail': ['The decoy lies in <b>private polder land</b> near \u2019t Zand \u2014 visible from outside.',
           '<b>Decoy peace</b>: do not enter without the decoyman\u2019s permission.',
           'Occasional <b>guided tours</b> \u2014 enquire with the water board or the manager.'],
 'foot': '\U0001f436 No dogs \u00b7 \U0001f4b6 View from the road only \u00b7 \u26a0\ufe0f Decoy peace \u2014 silence and distance \u00b7 \U0001f9ed By appointment'
}))

C.append(mk.card(1264, 'De Pikster', {
 'tags': ['Noord-Holland \u00b7 Hollands Kroon', 'Poldernatuur \u00b7 nat grasland en rietland', 'list 35 \u00b7 no. 17'],
 'loc': '\U0001f4cd Bij Winkel en Nieuwe Niedorp \u00b7 Nat grasland met rietzomen \u00b7 Klein gebied',
 'desc': '<b>De Pikster</b> is een klein natuurterrein in het polderland van de Niedorpen, waar het waterschap en de terreinbeheerder een aantal percelen bewust <b>nat en schraal</b> houden. In een landschap dat vrijwel volledig uit ontwaterd, bemest grasland bestaat, is dat een radicale ingreep: door het <b>peil hoog</b> te zetten en het maaisel af te voeren keert er in enkele jaren een compleet ander systeem terug. Waar het water tot in het voorjaar op het maaiveld blijft staan, ontstaat <b>dotterbloemgrasland</b> met <b>echte koekoeksbloem, grote ratelaar en pinksterbloem</b> \u2014 planten die vroeger overal langs de sloten stonden. Weidevogels profiteren direct: <b>grutto, tureluur en slobeend</b> vinden hier de zachte, doorprikbare bodem die ze nodig hebben. In de rietzomen langs de sloten broeden <b>rietzanger en kleine karekiet</b>, en de kikkerpopulaties trekken \u2019s zomers <b>purperreiger en lepelaar</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels en bloeiend nat grasland), jul\u2013aug (reigers op de kikkers)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 weidevogels alarmeren en het grasland ligt in de dauw.',
 'why': ['<b>Hoog waterpeil</b> in een verder volledig ontwaterd polderlandschap.',
         'Terugkeer van <b>dotterbloemgrasland</b> met koekoeksbloem en ratelaar.',
         'Zachte, <b>doorprikbare bodem</b> voor grutto en tureluur.',
         'Zomerse <b>purperreigers en lepelaars</b> op de kikkerrijkdom.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Grutto\u2019s keren terug</b> uit West-Afrika en Iberi\u00eb.',
          '<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Pinksterbloem en dotterbloem</b> in bloei.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Kuikens</b> in het lange gras; maaien wordt uitgesteld.',
          '<span class="months">Jul\u2013Aug</span> \U0001f426 <b>Purperreiger en lepelaar</b> foerageren in de natte laagtes.'],
 'wild': ['\U0001f426 Grutto \u00b7 Tureluur', '\U0001f986 Slobeend \u00b7 Zomertaling', '\U0001f426 Purperreiger \u00b7 Lepelaar', '\U0001f33c Dotterbloem \u00b7 Echte koekoeksbloem', '\U0001f426 Rietzanger \u00b7 Kleine karekiet'],
 'trail': ['Parkeren in <b>Winkel</b> of <b>Nieuwe Niedorp</b>.',
           'Bekijken vanaf de <b>polderwegen</b>; het terrein zelf is broedgebied.',
           'In het <b>broedseizoen (mrt\u2013jun)</b> extra afstand houden.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Broedgebied \u2014 niet betreden mrt\u2013jun \u00b7 \U0001f52d Verrekijker'
}, {
 'tags': ['North Holland \u00b7 Hollands Kroon', 'Polder nature \u00b7 wet grassland and reedland', 'list 35 \u00b7 no. 17'],
 'loc': '\U0001f4cd Near Winkel and Nieuwe Niedorp \u00b7 Wet grassland with reed fringes \u00b7 Small area',
 'desc': '<b>De Pikster</b> is a small nature site in the polder land of the Niedorpen, where the water board and the site manager deliberately keep a number of parcels <b>wet and nutrient-poor</b>. In a landscape consisting almost entirely of drained, fertilised grassland, that is a radical intervention: by raising the <b>water level</b> and carting off the cuttings, a completely different system returns within a few years. Where water stands at the surface into spring, <b>marsh-marigold grassland</b> develops with <b>ragged robin, yellow rattle and cuckooflower</b> \u2014 plants that once lined every ditch. Meadow birds benefit immediately: <b>black-tailed godwit, redshank and shoveler</b> find here the soft, probeable soil they need. In the reed fringes along the ditches <b>sedge warbler and reed warbler</b> breed, and the frog populations draw in <b>purple heron and spoonbill</b> in summer.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds and flowering wet grassland), Jul\u2013Aug (herons after the frogs)<br>\n    <b>Best time of day:</b> Early morning \u2014 meadow birds calling and the grassland still in dew.',
 'why': ['<b>High water level</b> in an otherwise completely drained polder landscape.',
         'Return of <b>marsh-marigold grassland</b> with ragged robin and yellow rattle.',
         'Soft, <b>probeable soil</b> for godwit and redshank.',
         'Summer <b>purple herons and spoonbills</b> drawn by the abundance of frogs.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Godwits return</b> from West Africa and Iberia.',
          '<span class="months">Apr\u2013May</span> \U0001f33c <b>Cuckooflower and marsh marigold</b> in bloom.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Chicks</b> in the long grass; mowing is postponed.',
          '<span class="months">Jul\u2013Aug</span> \U0001f426 <b>Purple heron and spoonbill</b> feed in the wet hollows.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Redshank', '\U0001f986 Shoveler \u00b7 Garganey', '\U0001f426 Purple heron \u00b7 Spoonbill', '\U0001f33c Marsh marigold \u00b7 Ragged robin', '\U0001f426 Sedge warbler \u00b7 Reed warbler'],
 'trail': ['Park in <b>Winkel</b> or <b>Nieuwe Niedorp</b>.',
           'View from the <b>polder roads</b>; the site itself is breeding ground.',
           'Keep extra distance during the <b>breeding season (Mar\u2013Jun)</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Breeding ground \u2014 do not enter Mar\u2013Jun \u00b7 \U0001f52d Binoculars'
}, card_class='card water'))

C.append(mk.card(1265, 'Eendenkooi De Hoop', {
 'tags': ['Noord-Holland \u00b7 Hollands Kroon', 'Eendenkooi \u00b7 ringstation', 'list 35 \u00b7 no. 18'],
 'loc': '\U0001f4cd In de Wieringermeer of Niedorper polders \u00b7 Eendenkooi \u00b7 Zeer klein',
 'desc': 'Waar de meeste eendenkooien in Nederland zijn verdwenen \u2014 van ruim <b>duizend</b> rond 1800 naar iets meer dan <b>honderd</b> nu \u2014 is <b>De Hoop</b> een van de kooien die een tweede leven kregen. De vangst voor de poelier stopte, maar de installatie bleek ideaal voor <b>wetenschappelijk ringonderzoek</b>: eenden worden nog altijd in de pijpen gelokt, maar nu gemeten, geringd en weer losgelaten. Dat levert gegevens op over <b>trekroutes, overleving en plaatstrouw</b> die op geen andere manier te verzamelen zijn; Nederlandse kooien leveren zo al decennialang een groot deel van de Europese kennis over eendentrek. De <b>kooiker</b> beheert daarnaast het bos: hakhout afzetten, rietkragen maaien, de pijpen onderhouden met traditionele <b>rietschermen</b>. Het kooibos zelf, met zijn <b>elzen en essen</b>, is een van de weinige opgaande begroeiingen in de kale polder en trekt daardoor uilen, spechten en doortrekkende zangvogels.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Sep\u2013mrt</b> (vangst- en ringseizoen), apr\u2013jun (broedvogels in het kooibos)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 het ringwerk gebeurt bij daglicht, kort na zonsopkomst.',
 'why': ['Van vangstinstallatie naar <b>ringstation</b> voor wetenschappelijk onderzoek.',
         'Levert data over <b>trekroutes, overleving en plaatstrouw</b>.',
         'Traditioneel onderhoud met <b>rietschermen</b> en hakhoutbeheer.',
         'Zeldzaam <b>opgaand bos</b> in een kale polder.'],
 'phen': ['<span class="months">Sep\u2013Nov</span> \U0001f426 <b>Najaarsvangst</b> \u2014 het drukste ringseizoen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Wintertaling en smient</b> in de pijpen.',
          '<span class="months">Mrt\u2013Apr</span> \U0001f989 <b>Ransuil en bosuil</b> broeden in het kooibos.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Hakhoutbeheer</b> \u2014 de kooiker zet het bos af.'],
 'wild': ['\U0001f986 Wintertaling \u00b7 Smient \u00b7 Krakeend', '\U0001f989 Ransuil \u00b7 Bosuil', '\U0001f426 Doortrekkende zangvogels', '\U0001f987 Vleermuizen', '\U0001f333 Zwarte els \u00b7 Es \u00b7 Wilg'],
 'trail': ['Ligt in <b>particulier polderland</b> \u2014 alleen toegankelijk met de kooiker.',
           '<b>Excursies</b> worden soms georganiseerd buiten het vangseizoen.',
           'Van buitenaf herkenbaar als <b>vierkant bosje</b> in de polder.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Alleen op afspraak \u00b7 \u26a0\ufe0f Kooirust \u2014 absolute stilte vereist \u00b7 \U0001f9ed Ringstation'
}, {
 'tags': ['North Holland \u00b7 Hollands Kroon', 'Duck decoy \u00b7 ringing station', 'list 35 \u00b7 no. 18'],
 'loc': '\U0001f4cd In the Wieringermeer or Niedorp polders \u00b7 Duck decoy \u00b7 Very small',
 'desc': 'Where most duck decoys in the Netherlands have disappeared \u2014 from over <b>a thousand</b> around 1800 to little more than <b>a hundred</b> today \u2014 <b>De Hoop</b> is one of those that found a second life. Catching for the poulterer stopped, but the installation proved ideal for <b>scientific ringing research</b>: ducks are still lured into the pipes, but now measured, ringed and released. That yields data on <b>migration routes, survival and site fidelity</b> obtainable in no other way; for decades Dutch decoys have supplied a large share of European knowledge about duck migration. The <b>decoyman</b> also manages the wood: coppicing, mowing reed fringes, maintaining the pipes with traditional <b>reed screens</b>. The decoy wood itself, with its <b>alder and ash</b>, is one of the few stands of tall vegetation in the bare polder and therefore attracts owls, woodpeckers and passing songbirds.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Sep\u2013Mar</b> (catching and ringing season), Apr\u2013Jun (breeding birds in the decoy wood)<br>\n    <b>Best time of day:</b> Early morning \u2014 ringing work is done in daylight, shortly after sunrise.',
 'why': ['From catching installation to <b>ringing station</b> for scientific research.',
         'Supplies data on <b>migration routes, survival and site fidelity</b>.',
         'Traditional maintenance with <b>reed screens</b> and coppicing.',
         'Rare stand of <b>tall woodland</b> in a bare polder.'],
 'phen': ['<span class="months">Sep\u2013Nov</span> \U0001f426 <b>Autumn catching</b> \u2014 the busiest ringing season.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Teal and wigeon</b> in the pipes.',
          '<span class="months">Mar\u2013Apr</span> \U0001f989 <b>Long-eared and tawny owl</b> breed in the decoy wood.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Coppicing</b> \u2014 the decoyman cuts back the wood.'],
 'wild': ['\U0001f986 Teal \u00b7 Wigeon \u00b7 Gadwall', '\U0001f989 Long-eared owl \u00b7 Tawny owl', '\U0001f426 Passing songbirds', '\U0001f987 Bats', '\U0001f333 Black alder \u00b7 Ash \u00b7 Willow'],
 'trail': ['Lies in <b>private polder land</b> \u2014 accessible only with the decoyman.',
           '<b>Excursions</b> are occasionally organised outside the catching season.',
           'Recognisable from outside as a <b>square copse</b> in the polder.'],
 'foot': '\U0001f436 No dogs \u00b7 \U0001f4b6 By appointment only \u00b7 \u26a0\ufe0f Decoy peace \u2014 absolute silence required \u00b7 \U0001f9ed Ringing station'
}))

C.append(mk.card(1266, 'Schagerwad en Weerepolder', {
 'tags': ['Noord-Holland \u00b7 Schagen', 'Weidevogelgebied \u00b7 nat poldergrasland', 'list 35 \u00b7 no. 19'],
 'loc': '\U0001f4cd Bij Schagen \u00b7 Open poldergrasland \u00b7 Middelgroot',
 'desc': 'De naam <b>Schagerwad</b> verraadt de oorsprong: hier lag ooit werkelijk <b>wad</b>, een getijdengebied dat via de Zijpe met de Zuiderzee in verbinding stond, tot het in de zestiende en zeventiende eeuw werd bedijkt. Wat overbleef is een laag, nat stuk polder waar het oude <b>krekenpatroon</b> nog altijd zichtbaar is in de bochtige sloten en de flauwe hoogteverschillen. Samen met de aangrenzende <b>Weerepolder</b> vormt het een van de betere <b>weidevogelgebieden</b> van de kop van Noord-Holland. Het beheer is nauwkeurig getimed: <b>plas-dras</b> zetten in maart zodat terugkerende grutto\u2019s meteen voedsel vinden, <b>uitgesteld maaien</b> tot half juni, en <b>predatiebeheer</b> rond de kolonies. Het resultaat zijn dichtheden van <b>grutto, kievit, tureluur en scholekster</b> die elders zeldzaam zijn geworden, met <b>veldleeuwerik en gele kwikstaart</b> op de drogere delen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> \u2014 het weidevogelseizoen; maart voor plas-dras, mei\u2013jun voor kuikens<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 hoogste activiteit en de baltsvluchten van grutto en tureluur.',
 'why': ['Voormalig <b>getijdengebied</b> \u2014 het krekenpatroon is nog afleesbaar.',
         'Een van de beste <b>weidevogelgebieden</b> van Noord-Holland.',
         'Beheer met <b>plas-dras, uitgesteld maaien en predatiebeheer</b>.',
         'Hoge dichtheden <b>grutto, tureluur en scholekster</b>.'],
 'phen': ['<span class="months">Mrt</span> \U0001f4a7 <b>Plas-dras</b> \u2014 ondergelopen percelen trekken de eerste grutto\u2019s.',
          '<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Baltsvluchten</b> van grutto, tureluur en kievit.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Kuikentijd</b> \u2014 maaien uitgesteld tot de jongen vliegvlug zijn.',
          '<span class="months">Jul\u2013Aug</span> \U0001f426 <b>Verzameling</b> voor de trek naar het zuiden.'],
 'wild': ['\U0001f426 Grutto \u00b7 Tureluur', '\U0001f426 Kievit \u00b7 Scholekster', '\U0001f426 Veldleeuwerik \u00b7 Gele kwikstaart', '\U0001f986 Slobeend \u00b7 Zomertaling', '\U0001f33c Pinksterbloem \u00b7 Echte koekoeksbloem'],
 'trail': ['Parkeren in <b>Schagen</b>; bekijken vanaf de polderwegen en dijkjes.',
           '<b>Niet betreden</b> in het broedseizoen \u2014 nesten liggen open in het gras.',
           'Neem een <b>verrekijker</b>: de vogels blijven op afstand.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Weidevogelgebied \u2014 niet betreden mrt\u2013jun \u00b7 \U0001f52d Verrekijker'
}, {
 'tags': ['North Holland \u00b7 Schagen', 'Meadow bird area \u00b7 wet polder grassland', 'list 35 \u00b7 no. 19'],
 'loc': '\U0001f4cd Near Schagen \u00b7 Open polder grassland \u00b7 Medium-sized',
 'desc': 'The name <b>Schagerwad</b> betrays its origin: real <b>tidal flats</b> once lay here, a tidal area connected to the Zuiderzee via the Zijpe, until it was diked in during the sixteenth and seventeenth centuries. What remains is a low, wet stretch of polder where the old <b>creek pattern</b> is still visible in the winding ditches and gentle differences in level. Together with the adjoining <b>Weerepolder</b> it forms one of the better <b>meadow bird areas</b> in the north of North Holland. Management is precisely timed: creating <b>shallow flooded plots</b> in March so returning godwits find food at once, <b>delayed mowing</b> until mid-June, and <b>predator management</b> around the colonies. The result is densities of <b>black-tailed godwit, lapwing, redshank and oystercatcher</b> that have become rare elsewhere, with <b>skylark and yellow wagtail</b> on the drier parts.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> \u2014 the meadow bird season; March for the flooded plots, May\u2013Jun for chicks<br>\n    <b>Best time of day:</b> Early morning \u2014 peak activity and the display flights of godwit and redshank.',
 'why': ['Former <b>tidal area</b> \u2014 the creek pattern can still be read.',
         'One of the best <b>meadow bird areas</b> in North Holland.',
         'Management with <b>shallow flooding, delayed mowing and predator control</b>.',
         'High densities of <b>godwit, redshank and oystercatcher</b>.'],
 'phen': ['<span class="months">Mar</span> \U0001f4a7 <b>Shallow flooding</b> \u2014 inundated plots draw the first godwits.',
          '<span class="months">Apr\u2013May</span> \U0001f426 <b>Display flights</b> of godwit, redshank and lapwing.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Chick season</b> \u2014 mowing delayed until the young can fly.',
          '<span class="months">Jul\u2013Aug</span> \U0001f426 <b>Gathering</b> for the migration south.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Redshank', '\U0001f426 Lapwing \u00b7 Oystercatcher', '\U0001f426 Skylark \u00b7 Yellow wagtail', '\U0001f986 Shoveler \u00b7 Garganey', '\U0001f33c Cuckooflower \u00b7 Ragged robin'],
 'trail': ['Park in <b>Schagen</b>; view from the polder roads and small dikes.',
           '<b>Do not enter</b> during the breeding season \u2014 nests lie open in the grass.',
           'Bring <b>binoculars</b>: the birds keep their distance.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Meadow bird area \u2014 do not enter Mar\u2013Jun \u00b7 \U0001f52d Binoculars'
}))

mk.insert(C, '1261')
mk.progress(1266)
mk.check()
