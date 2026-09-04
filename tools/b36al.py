# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1465, 'Zalk-Wilsum', {
 'tags': ['Overijssel \u00b7 Kampen', 'Uiterwaarden \u00b7 IJsseldorpen met rivierlandschap', 'list 36 \u00b7 no. 184'],
 'loc': '\U0001f4cd Tussen Zalk en Wilsum aan de IJssel \u00b7 Uiterwaarden \u00b7 Middelgroot',
 'desc': 'Tussen de dorpen <b>Zalk</b> en <b>Wilsum</b> ligt een van de gaafste stukken <b>IJssellandschap</b> van Overijssel. De rivier maakt hier brede bochten en heeft over eeuwen een reliëf achtergelaten dat je in de vlakke omgeving niet verwacht: <b>oeverwallen</b> waar het grovere zand bezonk bij overstromingen, en daarachter lager gelegen <b>komgronden</b> met zware klei. Op de oeverwallen liggen de dorpen en de boomgaarden \u2014 hoog en droog \u2014 en in de kommen de weilanden die \u2019s winters onderlopen. Dat is geen toeval maar het oudste ruimtelijke principe van het rivierengebied. De uiterwaarden zijn belangrijk voor <b>weidevogels en overwinterende ganzen</b>, en op de dijken en oeverwallen groeit <b>stroomdalflora</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (weidevogels en stroomdalflora), nov\u2013feb (ganzen en hoogwater)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 nevel over de uiterwaarden.',
 'why': ['Een van de <b>gaafste stukken IJssellandschap</b> van Overijssel.',
         '<b>Oeverwallen</b> van bezonken zand, daarachter zware <b>komgronden</b>.',
         'Dorpen en boomgaarden hoog, weilanden laag \u2014 het <b>oudste principe</b>.',
         'Belangrijk voor <b>weidevogels en overwinterende ganzen</b>.'],
 'phen': ['<span class="months">Mrt\u2013Mei</span> \U0001f426 <b>Grutto en kievit</b> in de uiterwaardweiden.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Stroomdalflora</b> op de dijken en oeverwallen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Kolganzen en smienten</b> in grote groepen.',
          '<span class="months">Dec\u2013Mrt</span> \U0001f30a <b>Hoogwater</b> zet de kommen onder.'],
 'wild': ['\U0001f426 Grutto \u00b7 Kievit \u00b7 Tureluur \u00b7 Scholekster', '\U0001f9a2 Kolgans \u00b7 Grauwe gans \u00b7 Smient \u00b7 Kleine zwaan', '\U0001f985 Buizerd \u00b7 Blauwe kiekendief (winter)', '\U0001f33c Kruisdistel \u00b7 Sikkelklaver \u00b7 Kleine ratelaar', '\U0001f98c Ree \u00b7 Haas \u00b7 \U0001f9ab Bever langs de IJssel'],
 'trail': ['Parkeren in <b>Zalk</b> of Wilsum; dijkpaden langs de IJssel.',
           'Loop de <b>dijk</b> \u2014 daar zie je oeverwal en kom naast elkaar.',
           'Winter voor de <b>ganzen</b>, voorjaar voor de weidevogels.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Hoogwater in de winter \u00b7 \U0001f6b6 Dijkroutes'
}, {
 'tags': ['Overijssel \u00b7 Kampen', 'Floodplains \u00b7 IJssel villages with river landscape', 'list 36 \u00b7 no. 184'],
 'loc': '\U0001f4cd Between Zalk and Wilsum on the IJssel \u00b7 Floodplains \u00b7 Medium-sized',
 'desc': 'Between the villages of <b>Zalk</b> and <b>Wilsum</b> lies one of the most intact stretches of <b>IJssel landscape</b> in Overijssel. The river makes broad bends here and over centuries has left a relief you would not expect in flat surroundings: <b>levees</b> where coarser sand settled during floods, and behind them lower <b>basin soils</b> of heavy clay. The villages and orchards stand on the levees \u2014 high and dry \u2014 and the basins hold the meadows that flood in winter. That is no accident but the oldest spatial principle of the river district. The floodplains matter for <b>meadow birds and wintering geese</b>, and <b>river-valley flora</b> grows on the dikes and levees.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (meadow birds and river flora), Nov\u2013Feb (geese and high water)<br>\n    <b>Best time of day:</b> Early morning \u2014 mist over the floodplains.',
 'why': ['One of the <b>most intact IJssel landscapes</b> in Overijssel.',
         '<b>Levees</b> of settled sand, behind them heavy <b>basin soils</b>.',
         'Villages and orchards high, meadows low \u2014 the <b>oldest principle</b>.',
         'Important for <b>meadow birds and wintering geese</b>.'],
 'phen': ['<span class="months">Mar\u2013May</span> \U0001f426 <b>Black-tailed godwit and lapwing</b> in the floodplain meadows.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>River-valley flora</b> on dikes and levees.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>White-fronted geese and wigeon</b> in large flocks.',
          '<span class="months">Dec\u2013Mar</span> \U0001f30a <b>High water</b> floods the basins.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Lapwing \u00b7 Redshank \u00b7 Oystercatcher', '\U0001f9a2 White-fronted goose \u00b7 Greylag \u00b7 Wigeon \u00b7 Bewick\u2019s swan', '\U0001f985 Buzzard \u00b7 Hen harrier (winter)', '\U0001f33c Field eryngo \u00b7 Sickle medick \u00b7 Yellow rattle', '\U0001f98c Roe deer \u00b7 Brown hare \u00b7 \U0001f9ab Beaver along the IJssel'],
 'trail': ['Park in <b>Zalk</b> or Wilsum; dike paths along the IJssel.',
           'Walk the <b>dike</b> \u2014 there you see levee and basin side by side.',
           'Winter for the <b>geese</b>, spring for the meadow birds.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f High water in winter \u00b7 \U0001f6b6 Dike routes'
}))

C.append(mk.card(1466, 'Larserbos', {
 'tags': ['Flevoland \u00b7 Lelystad', 'Polderbos \u00b7 productiebos met open plekken', 'list 36 \u00b7 no. 185'],
 'loc': '\U0001f4cd Ten zuiden van Lelystad \u00b7 Polderbos \u00b7 Groot',
 'desc': 'Het <b>Larserbos</b> is een van de grote bossen van Zuidelijk Flevoland, aangeplant in de jaren zeventig toen de polder net droog was. De aanplant volgde een principe dat in Flevoland overal terugkeert: eerst snelgroeiende <b>populier en wilg</b> als <b>pioniersgewas</b>, want die verdragen de natte, zoute jonge bodem, en pas onder hun beschutting konden <b>es, esdoorn en eik</b> volgen. Zo werd in dertig jaar een bos gemaakt waar de natuur er duizenden jaren over zou doen. Inmiddels is het gelaagd genoeg voor <b>havik, boomvalk en zwarte specht</b>. Op de open plekken en langs de bosranden bloeien in juni <b>orchideeën</b> op de kalkrijke zeeklei \u2014 een verrassing in een aangeplant bos.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jun</b> (orchideeën), apr\u2013jun (zang), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 havik en specht boven de kruinen.',
 'why': ['Groot polderbos, aangeplant toen de bodem <b>net droog</b> was.',
         'Eerst <b>populier en wilg</b> als pioniers op natte, zoute grond.',
         'Onder hun beschutting volgden <b>es, esdoorn en eik</b>.',
         '<b>Orchideeën</b> op de kalkrijke zeeklei van de open plekken.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f985 <b>Havik</b> baltst boven het bos.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33a <b>Orchideeën</b> op de open plekken.',
          '<span class="months">Jun\u2013Aug</span> \U0001f985 <b>Boomvalk</b> jaagt op libellen boven de open plekken.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in het loofbos.'],
 'wild': ['\U0001f985 Havik \u00b7 Boomvalk \u00b7 Buizerd', '\U0001f426 Zwarte specht \u00b7 Boomklever \u00b7 Wielewaal', '\U0001f33a Rietorchis \u00b7 Bijenorchis \u00b7 Moeraswespenorchis', '\U0001f98c Ree \u00b7 Vos \u00b7 \U0001f43f\ufe0f Eekhoorn', '\U0001f333 Populier \u00b7 Es \u00b7 Esdoorn \u00b7 Eik'],
 'trail': ['Parkeren aan de <b>Larserweg</b> bij Lelystad; ruim padennet.',
           'Zoek in juni de <b>open plekken</b> voor de orchideeën.',
           'Let op de <b>populierenlagen</b> \u2014 het pionierstadium is nog zichtbaar.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f333 Groot bos \u00b7 \U0001f6b4 Fietspaden'
}, {
 'tags': ['Flevoland \u00b7 Lelystad', 'Polder wood \u00b7 production wood with glades', 'list 36 \u00b7 no. 185'],
 'loc': '\U0001f4cd South of Lelystad \u00b7 Polder wood \u00b7 Large',
 'desc': 'The <b>Larserbos</b> is one of the large woods of Southern Flevoland, planted in the 1970s when the polder had only just fallen dry. The planting followed a principle repeated all over Flevoland: first fast-growing <b>poplar and willow</b> as a <b>pioneer crop</b>, since they tolerate the wet, salty young soil, and only under their shelter could <b>ash, maple and oak</b> follow. Thus in thirty years a wood was made that nature would have taken thousands of years to build. It is now layered enough for <b>goshawk, hobby and black woodpecker</b>. In the glades and along the woodland edges <b>orchids</b> flower in June on the lime-rich marine clay \u2014 a surprise in a planted wood.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jun</b> (orchids), Apr\u2013Jun (song), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 goshawk and woodpecker above the canopy.',
 'why': ['A large polder wood, planted when the soil had <b>just dried</b>.',
         'First <b>poplar and willow</b> as pioneers on wet, salty ground.',
         'Under their shelter followed <b>ash, maple and oak</b>.',
         '<b>Orchids</b> on the lime-rich marine clay of the glades.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f985 <b>Goshawk</b> displays above the wood.',
          '<span class="months">May\u2013Jun</span> \U0001f33a <b>Orchids</b> in the glades.',
          '<span class="months">Jun\u2013Aug</span> \U0001f985 <b>Hobby</b> hunts dragonflies over the glades.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> in the broadleaf wood.'],
 'wild': ['\U0001f985 Goshawk \u00b7 Hobby \u00b7 Buzzard', '\U0001f426 Black woodpecker \u00b7 Nuthatch \u00b7 Golden oriole', '\U0001f33a Marsh orchid \u00b7 Bee orchid \u00b7 Marsh helleborine', '\U0001f98c Roe deer \u00b7 Fox \u00b7 \U0001f43f\ufe0f Red squirrel', '\U0001f333 Poplar \u00b7 Ash \u00b7 Maple \u00b7 Oak'],
 'trail': ['Park on the <b>Larserweg</b> near Lelystad; an extensive path network.',
           'Seek out the <b>glades</b> in June for the orchids.',
           'Note the <b>poplar layers</b> \u2014 the pioneer stage is still visible.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f333 Large wood \u00b7 \U0001f6b4 Cycle paths'
}))

C.append(mk.card(1467, 'Biddingbos', {
 'tags': ['Flevoland \u00b7 Dronten', 'Polderbos \u00b7 loofbos met waterpartijen', 'list 36 \u00b7 no. 186'],
 'loc': '\U0001f4cd Bij Biddinghuizen, Oostelijk Flevoland \u00b7 Polderbos \u00b7 Middelgroot',
 'desc': 'Het <b>Biddingbos</b> ligt tussen Biddinghuizen en het Veluwemeer, en het is een van de bossen waar de <b>bodemverschillen</b> van de polder goed zichtbaar zijn. Onder Oostelijk Flevoland liggen naast elkaar zware <b>zeeklei</b>, oude <b>veenlagen</b> en zandige ruggen \u2014 restanten van het landschap dat vóór de Zuiderzee bestond. Waar de klei zwaar is groeit het bos traag en blijft het open; op de zandiger plekken staat het dichter. Dat mozaïek geeft variatie die de aanplanters niet hebben ontworpen maar die de ondergrond hun oplegde. Er broeden <b>havik, bosuil en grote bonte specht</b>, en langs de waterpartijen jaagt de <b>ijsvogel</b>. In de herfst is het bos rijk aan <b>paddenstoelen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang), sep\u2013nov (paddenstoelen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig langs de waterpartijen.',
 'why': ['De <b>bodemverschillen</b> van de polder zijn hier goed zichtbaar.',
         'Zeeklei, oude <b>veenlagen</b> en zandruggen liggen naast elkaar.',
         'Op zware klei groeit het bos traag en <b>open</b>, op zand dichter.',
         'Een mozaïek dat de <b>ondergrond</b> oplegde, niet de aanplanter.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Bosuil</b> roept in de late winter.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Spechten en zangvogels</b> in het loofbos.',
          '<span class="months">Jun\u2013Aug</span> \U0001f426 <b>IJsvogel</b> bij de waterpartijen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op klei en zand.'],
 'wild': ['\U0001f985 Havik \u00b7 Buizerd \u00b7 \U0001f989 Bosuil', '\U0001f426 Grote bonte specht \u00b7 Boomklever \u00b7 IJsvogel', '\U0001f98c Ree \u00b7 Vos \u00b7 \U0001f43f\ufe0f Eekhoorn', '\U0001f344 Boleten \u00b7 Russula\u2019s \u00b7 Houtzwammen', '\U0001f333 Es \u00b7 Populier \u00b7 Eik \u00b7 Wilg'],
 'trail': ['Parkeren bij <b>Biddinghuizen</b>; paden door het bos naar het Veluwemeer.',
           'Let op waar het bos <b>opener</b> wordt \u2014 daar ligt de zware klei.',
           'Herfst voor de <b>paddenstoelen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Bospaden \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Flevoland \u00b7 Dronten', 'Polder wood \u00b7 broadleaf wood with pools', 'list 36 \u00b7 no. 186'],
 'loc': '\U0001f4cd Near Biddinghuizen, Eastern Flevoland \u00b7 Polder wood \u00b7 Medium-sized',
 'desc': 'The <b>Biddingbos</b> lies between Biddinghuizen and the Veluwemeer, and is one of the woods where the polder\u2019s <b>soil differences</b> are clearly visible. Beneath Eastern Flevoland lie heavy <b>marine clay</b>, old <b>peat layers</b> and sandy ridges side by side \u2014 remnants of the landscape that existed before the Zuiderzee. Where the clay is heavy the wood grows slowly and stays open; on the sandier spots it stands denser. That mosaic gives a variation the planters never designed but which the subsoil imposed on them. <b>Goshawk, tawny owl and great spotted woodpecker</b> breed, and the <b>kingfisher</b> hunts along the pools. In autumn the wood is rich in <b>fungi</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song), Sep\u2013Nov (fungi and autumn colour)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet along the pools.',
 'why': ['The polder\u2019s <b>soil differences</b> are clearly visible here.',
         'Marine clay, old <b>peat layers</b> and sand ridges lie side by side.',
         'On heavy clay the wood grows slowly and <b>open</b>; on sand, denser.',
         'A mosaic imposed by the <b>subsoil</b>, not by the planter.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Tawny owl</b> calls in late winter.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Woodpeckers and songbirds</b> in the broadleaf wood.',
          '<span class="months">Jun\u2013Aug</span> \U0001f426 <b>Kingfisher</b> at the pools.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on clay and sand.'],
 'wild': ['\U0001f985 Goshawk \u00b7 Buzzard \u00b7 \U0001f989 Tawny owl', '\U0001f426 Great spotted woodpecker \u00b7 Nuthatch \u00b7 Kingfisher', '\U0001f98c Roe deer \u00b7 Fox \u00b7 \U0001f43f\ufe0f Red squirrel', '\U0001f344 Boletes \u00b7 Brittlegills \u00b7 Bracket fungi', '\U0001f333 Ash \u00b7 Poplar \u00b7 Oak \u00b7 Willow'],
 'trail': ['Park at <b>Biddinghuizen</b>; paths through the wood to the Veluwemeer.',
           'Note where the wood grows <b>more open</b> \u2014 that is the heavy clay.',
           'Autumn for the <b>fungi</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Woodland paths \u00b7 \U0001f6b4 Cycle route'
}))

C.append(mk.card(1468, 'Dorpsbossen Biddinghuizen', {
 'tags': ['Flevoland \u00b7 Dronten', 'Dorpsbos \u00b7 groene mantel rond een polderdorp', 'list 36 \u00b7 no. 187'],
 'loc': '\U0001f4cd Rond Biddinghuizen \u00b7 Dorpsbos \u00b7 Klein',
 'desc': 'Rond <b>Biddinghuizen</b> ligt de gebruikelijke groene mantel van de polderdorpen, maar hier heeft die een extra functie gekregen. Het dorp ligt naast <b>Walibi</b> en het evenemententerrein waar jaarlijks grote festivals worden gehouden; het bos vormt daarmee ook een <b>geluidsbuffer</b> en visueel scherm tussen dorp en drukte. Ecologisch werken de dorpsbossen zoals elders in Flevoland: ze zijn een halve eeuw oud, hebben inmiddels dood hout en struiklagen, en verbinden de grotere polderbossen met elkaar. Er broeden <b>groene specht, boomklever en bosuil</b>, en de bosranden zijn goed voor <b>vlinders en wilde bijen</b>. Voor het dorp zelf zijn het de dagelijkse wandelrondjes.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang), jun\u2013aug (vlinders op de bosranden)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 stil, ook in festivalseizoen.',
 'why': ['De gebruikelijke <b>groene mantel</b> van de polderdorpen.',
         'Hier ook een <b>geluidsbuffer</b> tussen dorp en evenemententerrein.',
         'Een halve eeuw oud: <b>dood hout en struiklagen</b>.',
         'Verbindt de grotere polderbossen met elkaar.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Spechten</b> roffelen in de mantel.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en zwartkop</b> zingen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Vlinders</b> op de bloemrijke bosranden.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> langs de paden.'],
 'wild': ['\U0001f426 Groene specht \u00b7 Boomklever \u00b7 Zwartkop', '\U0001f989 Bosuil \u00b7 \U0001f985 Buizerd', '\U0001f98b Vlinders \u00b7 \U0001f41d Wilde bijen op de randen', '\U0001f43f\ufe0f Eekhoorn \u00b7 Egel \u00b7 \U0001f98a Vos', '\U0001f333 Es \u00b7 Esdoorn \u00b7 Els \u00b7 Wilg'],
 'trail': ['Parkeren in <b>Biddinghuizen</b>; de bossen liggen op loopafstand.',
           'Loop de <b>mantel</b> rond \u2014 dan zie je de bufferfunctie.',
           'Combineer met het <b>Biddingbos</b> even verderop.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Korte ommetjes \u00b7 \U0001f9d2 Gezinsvriendelijk'
}, {
 'tags': ['Flevoland \u00b7 Dronten', 'Village wood \u00b7 green mantle around a polder village', 'list 36 \u00b7 no. 187'],
 'loc': '\U0001f4cd Around Biddinghuizen \u00b7 Village wood \u00b7 Small',
 'desc': 'Around <b>Biddinghuizen</b> lies the usual green mantle of the polder villages, but here it has acquired an extra function. The village adjoins <b>Walibi</b> and the events ground where large festivals are held each year; the wood therefore also serves as a <b>noise buffer</b> and visual screen between village and bustle. Ecologically the village woods work as elsewhere in Flevoland: half a century old, now with dead wood and shrub layers, and linking the larger polder woods together. <b>Green woodpecker, nuthatch and tawny owl</b> breed, and the woodland edges are good for <b>butterflies and wild bees</b>. For the village itself they are the daily walking round.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song), Jun\u2013Aug (butterflies on the edges)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet, even in festival season.',
 'why': ['The usual <b>green mantle</b> of the polder villages.',
         'Here also a <b>noise buffer</b> between village and events ground.',
         'Half a century old: <b>dead wood and shrub layers</b>.',
         'Links the larger polder woods together.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Woodpeckers</b> drum in the mantle.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and blackcap</b> sing.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Butterflies</b> on the flowery woodland edges.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> along the paths.'],
 'wild': ['\U0001f426 Green woodpecker \u00b7 Nuthatch \u00b7 Blackcap', '\U0001f989 Tawny owl \u00b7 \U0001f985 Buzzard', '\U0001f98b Butterflies \u00b7 \U0001f41d Wild bees on the edges', '\U0001f43f\ufe0f Red squirrel \u00b7 Hedgehog \u00b7 \U0001f98a Fox', '\U0001f333 Ash \u00b7 Maple \u00b7 Alder \u00b7 Willow'],
 'trail': ['Park in <b>Biddinghuizen</b>; the woods are within walking distance.',
           'Walk the <b>mantle</b> round \u2014 the buffer function becomes clear.',
           'Combine with the <b>Biddingbos</b> a little further on.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Short strolls \u00b7 \U0001f9d2 Family-friendly'
}))

C.append(mk.card(1469, 'Flevoland landschapselementen', {
 'tags': ['Flevoland \u00b7 provinciebreed', 'Landschapselementen \u00b7 singels, bosjes en bermen in de polder', 'list 36 \u00b7 no. 188'],
 'loc': '\U0001f4cd Verspreid over Flevoland \u00b7 Kleine elementen \u00b7 Verspreid',
 'desc': 'Verspreid over heel Flevoland ligt een fijnmazig net van <b>landschapselementen</b>: erfbeplantingen, houtsingels, bermen, tochtoevers en kleine bosjes. Ze zijn bij de inrichting van de polder ontworpen door landschapsarchitecten van de <b>Rijksdienst voor de IJsselmeerpolders</b>, die als een van de eersten ter wereld natuur en landschap systematisch in een landbouwplan opnamen. Het resultaat is opvallend: een van de meest grootschalige landbouwgebieden van Nederland bezit tegelijk een verrassend dicht netwerk van kleine natuur. Juist die kleine elementen dragen de <b>biodiversiteit</b> van het boerenland \u2014 <b>steenuil, geelgors, patrijs, wilde bijen en vlinders</b> zijn er van afhankelijk, en ze verbinden de grote bossen en moerassen met elkaar.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (zang, bloei en insecten), okt\u2013nov (bessen en trek)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 steenuil en vleermuizen langs de singels.',
 'why': ['Ontworpen door de <b>Rijksdienst voor de IJsselmeerpolders</b>.',
         'Een van de eerste plannen ter wereld met natuur <b>systematisch ingebouwd</b>.',
         'Grootschalige landbouw met een <b>dicht netwerk kleine natuur</b>.',
         'Dragers van de <b>biodiversiteit</b> van het boerenland.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Geelgors en patrijs</b> in de singels.',
          '<span class="months">Mei\u2013Jul</span> \U0001f41d <b>Wilde bijen en vlinders</b> op de bermen.',
          '<span class="months">Mei\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> gebruiken de singels als vliegroute.',
          '<span class="months">Okt\u2013Nov</span> \U0001fad0 <b>Bessen</b> trekken lijsters en pestvogels.'],
 'wild': ['\U0001f989 Steenuil \u00b7 \U0001f426 Geelgors \u00b7 Patrijs \u00b7 Grasmus', '\U0001f41d Wilde bijen \u00b7 \U0001f98b Vlinders op de bermen', '\U0001f987 Vleermuizen langs de singels', '\U0001f98c Haas \u00b7 Ree \u00b7 \U0001f98a Vos', '\U0001f333 Meidoorn \u00b7 Sleedoorn \u00b7 Els \u00b7 Wilg'],
 'trail': ['Fiets door het <b>buitengebied</b> \u2014 het netwerk zie je pas onderweg.',
           'Kijk naar <b>erfbeplantingen</b>: elk boerenerf is een klein bos.',
           'Schemer voor <b>steenuil</b> op paaltjes en in knotbomen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Respecteer erven en akkers \u00b7 \U0001f6b4 Fietsroutes'
}, {
 'tags': ['Flevoland \u00b7 province-wide', 'Landscape elements \u00b7 tree lines, copses and verges in the polder', 'list 36 \u00b7 no. 188'],
 'loc': '\U0001f4cd Scattered across Flevoland \u00b7 Small elements \u00b7 Scattered',
 'desc': 'Scattered across the whole of Flevoland lies a fine-meshed net of <b>landscape elements</b>: farmyard plantings, tree lines, verges, ditch banks and small copses. They were designed when the polder was laid out by landscape architects of the <b>IJsselmeer Polders Development Authority</b>, among the first in the world to incorporate nature and landscape systematically into an agricultural plan. The result is striking: one of the most large-scale farming regions in the Netherlands also possesses a surprisingly dense network of small-scale nature. It is precisely those small elements that carry the <b>biodiversity</b> of the farmland \u2014 <b>little owl, yellowhammer, grey partridge, wild bees and butterflies</b> depend on them, and they link the large woods and marshes together.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (song, flowering and insects), Oct\u2013Nov (berries and migration)<br>\n    <b>Best time of day:</b> Dusk \u2014 little owl and bats along the tree lines.',
 'why': ['Designed by the <b>IJsselmeer Polders Development Authority</b>.',
         'One of the first plans worldwide with nature <b>systematically built in</b>.',
         'Large-scale farming with a <b>dense network of small nature</b>.',
         'The carriers of farmland <b>biodiversity</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Yellowhammer and grey partridge</b> in the tree lines.',
          '<span class="months">May\u2013Jul</span> \U0001f41d <b>Wild bees and butterflies</b> on the verges.',
          '<span class="months">May\u2013Aug</span> \U0001f987 <b>Bats</b> use the lines as flight routes.',
          '<span class="months">Oct\u2013Nov</span> \U0001fad0 <b>Berries</b> attract thrushes and waxwings.'],
 'wild': ['\U0001f989 Little owl \u00b7 \U0001f426 Yellowhammer \u00b7 Grey partridge \u00b7 Whitethroat', '\U0001f41d Wild bees \u00b7 \U0001f98b Butterflies on the verges', '\U0001f987 Bats along the tree lines', '\U0001f98c Brown hare \u00b7 Roe deer \u00b7 \U0001f98a Fox', '\U0001f333 Hawthorn \u00b7 Blackthorn \u00b7 Alder \u00b7 Willow'],
 'trail': ['Cycle through the <b>countryside</b> \u2014 the network only shows en route.',
           'Look at the <b>farmyard plantings</b>: every farm is a small wood.',
           'Dusk for <b>little owls</b> on posts and in pollarded trees.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Respect farmyards and fields \u00b7 \U0001f6b4 Cycle routes'
}))

mk.insert(C, '1464')
mk.progress(1469)
mk.check()
