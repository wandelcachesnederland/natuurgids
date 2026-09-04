# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1241, 'Hondsrug Zuid', {
 'tags': ['Drenthe \u00b7 Borger-Odoorn', 'Stuwwal \u00b7 keileemrug met bos en heide', 'list 34 \u00b7 no. 18'],
 'loc': '\U0001f4cd Tussen Borger, Odoorn en Emmen \u00b7 Hondsrug \u00b7 Zeer groot gebied',
 'desc': 'De <b>Hondsrug</b> is de bekendste zandrug van Nederland en het zuidelijke deel toont hem op zijn duidelijkst. Anders dan bij een gewone stuwwal is de Hondsrug niet opgeduwd maar ontstaan onder een <b>bewegende ijskap</b>: in de voorlaatste ijstijd schoof het landijs in stroken over de ondergrond en liet een serie evenwijdige <b>keileemruggen</b> achter, met natte laagtes ertussen. Die combinatie \u2014 hoog en droog naast laag en nat, over tientallen kilometers \u2014 verklaart waarom de mens hier al <b>vijfduizend jaar</b> woont. De <b>hunebedden</b> liggen niet toevallig op deze rug: het keileem leverde de zwerfkeien \u00e9n de rug was de enige begaanbare noord-zuidroute door een land vol veen. Vandaag is Hondsrug Zuid een mozaa\u00efek van <b>oude eikenbossen, heideresten, essen en beekdalkoppen</b>, erkend als <b>UNESCO Global Geopark</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (voorjaarsflora en zang), aug\u2013sep (heidebloei), okt\u2013nov (herfstkleur en paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 ree\u00ebn en dassen op de open plekken; mist in de laagtes.',
 'why': ['Ontstaan onder een <b>bewegende ijskap</b>, niet opgeduwd \u2014 uniek in Europa.',
         '<b>Hunebedden</b> op de rug: keien \u00e9n de enige droge noord-zuidroute.',
         'Erkend als <b>UNESCO Global Geopark De Hondsrug</b>.',
         'Mozaa\u00efek van <b>oude eikenbossen, heide en essen</b> over tientallen kilometers.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33f <b>Bosanemoon en dalkruid</b> in de oude eikenbossen.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Wielewaal en zwarte specht</b> in het opgaand loofbos.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heidebloei</b> op de resterende heidevelden.',
          '<span class="months">Okt\u2013Nov</span> \U0001f344 <b>Paddenstoelenrijkdom</b> \u2014 vliegenzwam onder de berken.'],
 'wild': ['\U0001f98c Ree', '\U0001f9a1 Das', '\U0001f426 Zwarte specht \u00b7 Wielewaal', '\U0001f333 Oude zomereiken', '\U0001f33f Struikhei \u00b7 Bosanemoon'],
 'trail': ['Startpunten bij <b>Borger</b> (Hunebedcentrum), <b>Odoorn</b> en <b>Exloo</b>.',
           'Het <b>Hondsrugpad</b> loopt over de volle lengte van de rug.',
           'Fietsroutes verbinden de <b>hunebedden</b> als kralen aan een snoer.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Zeer uitgestrekt \u2014 kies vooraf een deelgebied \u00b7 \U0001f6b6 Vele routes'
}, {
 'tags': ['Drenthe \u00b7 Borger-Odoorn', 'Ice-pushed ridge \u00b7 boulder-clay ridge with wood and heath', 'list 34 \u00b7 no. 18'],
 'loc': '\U0001f4cd Between Borger, Odoorn and Emmen \u00b7 Hondsrug \u00b7 Very large area',
 'desc': 'The <b>Hondsrug</b> is the best-known sand ridge in the Netherlands and its southern section shows it at its clearest. Unlike an ordinary push moraine, the Hondsrug was not shoved up but formed beneath a <b>moving ice sheet</b>: during the penultimate glaciation the land ice slid over the subsoil in strips and left behind a series of parallel <b>boulder-clay ridges</b>, with wet hollows between them. That combination \u2014 high and dry beside low and wet, over tens of kilometres \u2014 explains why people have lived here for <b>five thousand years</b>. The <b>megalithic tombs</b> lie on this ridge for good reason: the boulder clay supplied the erratic boulders, and the ridge was the only passable north-south route through a land full of bog. Today Hondsrug Zuid is a mosaic of <b>old oak woods, heath remnants, open fields and brook-valley heads</b>, recognised as a <b>UNESCO Global Geopark</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (spring flora and song), Aug\u2013Sep (heather bloom), Oct\u2013Nov (autumn colour and fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 roe deer and badgers in the clearings; mist in the hollows.',
 'why': ['Formed beneath a <b>moving ice sheet</b>, not pushed up \u2014 unique in Europe.',
         '<b>Megalithic tombs</b> on the ridge: the boulders and the only dry north-south route.',
         'Recognised as <b>UNESCO Global Geopark De Hondsrug</b>.',
         'Mosaic of <b>old oak woods, heath and open fields</b> over tens of kilometres.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33f <b>Wood anemone and May lily</b> in the old oak woods.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Golden oriole and black woodpecker</b> in the high forest.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heather bloom</b> on the remaining heaths.',
          '<span class="months">Oct\u2013Nov</span> \U0001f344 <b>Rich fungi season</b> \u2014 fly agaric under the birches.'],
 'wild': ['\U0001f98c Roe deer', '\U0001f9a1 Badger', '\U0001f426 Black woodpecker \u00b7 Golden oriole', '\U0001f333 Old pedunculate oaks', '\U0001f33f Heather \u00b7 Wood anemone'],
 'trail': ['Starting points at <b>Borger</b> (Hunebedcentrum), <b>Odoorn</b> and <b>Exloo</b>.',
           'The <b>Hondsrugpad</b> long-distance path runs the full length of the ridge.',
           'Cycle routes link the <b>megalithic tombs</b> like beads on a string.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Very extensive \u2014 choose a section in advance \u00b7 \U0001f6b6 Many routes'
}))

C.append(mk.card(1242, 'Boswachterij Odoorn', {
 'tags': ['Drenthe \u00b7 Borger-Odoorn', 'Productiebos \u00b7 omvorming naar gemengd bos', 'list 34 \u00b7 no. 19'],
 'loc': '\U0001f4cd Bij Odoorn en Valthe \u00b7 Boswachterij \u00b7 Ruim 1.000 ha',
 'desc': 'De <b>Boswachterij Odoorn</b> is aangelegd in de jaren dertig, toen werklozen in de <b>werkverschaffing</b> de laatste woeste heidegronden van de Hondsrug omspitten en beplantten met grove den. Het doel was <b>mijnhout</b> voor de Limburgse kolenmijnen \u2014 een economisch project dat als bos vermomd ging. Die herkomst is nog zichtbaar in de <b>kaarsrechte lanen en gelijkjarige vakken</b>, maar het bos van nu is een ander bos. Al decennia werkt Staatsbosbeheer aan <b>omvorming</b>: naaldhout dunnen, loofhout inbrengen, dood hout laten liggen en oude heidekernen weer openkappen. Het resultaat is een steeds gevarieerder bos met <b>zwarte specht, havik en boommarter</b>, en op de open plekken keren <b>heideblauwtje en zandhagedis</b> terug. Op de vroegere brandsingels liggen nu <b>vennetjes en heidecorridors</b> die de vakken onderling verbinden.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (baltsende roofvogels en zang), aug\u2013sep (heideplekken), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 boommarter en havik het best waarneembaar.',
 'why': ['Aangelegd in de <b>werkverschaffing</b> voor mijnhout \u2014 zichtbare geschiedenis.',
         'Grootschalige <b>omvorming</b> van naaldhout naar gemengd bos.',
         '<b>Zwarte specht, havik en boommarter</b> in de oudere vakken.',
         'Heropende <b>heidekernen en vennetjes</b> tussen de bosvakken.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f985 <b>Havik baltst</b> boven het kronendak.',
          '<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Zwarte specht</b> roffelt \u2014 ver hoorbaar in de stille vakken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heidebloei</b> op de heropende plekken.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op het achtergelaten dode hout.'],
 'wild': ['\U0001f426 Zwarte specht', '\U0001f985 Havik', '\U0001f9a1 Boommarter', '\U0001f98e Zandhagedis', '\U0001f33f Struikhei \u00b7 Bochtige smele'],
 'trail': ['Parkeren bij <b>Odoorn</b> of aan de weg naar <b>Valthe</b>.',
           'Gemarkeerde <b>wandel- en mountainbikeroutes</b> door de vakken.',
           'Uitgestrekt en rustig \u2014 ook bij druk weer vind je hier <b>stilte</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Houtoogst mogelijk \u2014 let op afzettingen \u00b7 \U0001f6b4 MTB-routes'
}, {
 'tags': ['Drenthe \u00b7 Borger-Odoorn', 'Production forest \u00b7 conversion to mixed woodland', 'list 34 \u00b7 no. 19'],
 'loc': '\U0001f4cd Near Odoorn and Valthe \u00b7 State forest \u00b7 Over 1,000 ha',
 'desc': 'The <b>Boswachterij Odoorn</b> was planted in the 1930s, when unemployed men on <b>relief work schemes</b> dug over the last waste heaths of the Hondsrug and planted them with Scots pine. The aim was <b>pit props</b> for the Limburg coal mines \u2014 an economic project disguised as a forest. That origin is still visible in the <b>ruler-straight rides and even-aged compartments</b>, but the wood of today is a different wood. For decades the State Forestry Service has been working on <b>conversion</b>: thinning conifers, introducing broadleaves, leaving deadwood and reopening old heath cores. The result is an increasingly varied forest with <b>black woodpecker, goshawk and pine marten</b>, while <b>silver-studded blue and sand lizard</b> return to the clearings. The former firebreaks now hold <b>small pools and heath corridors</b> that link the compartments together.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (displaying raptors and birdsong), Aug\u2013Sep (heath patches), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Morning \u2014 pine marten and goshawk are easiest to see.',
 'why': ['Planted under <b>relief work schemes</b> for pit props \u2014 visible history.',
         'Large-scale <b>conversion</b> from conifer plantation to mixed woodland.',
         '<b>Black woodpecker, goshawk and pine marten</b> in the older compartments.',
         'Reopened <b>heath cores and pools</b> between the forest blocks.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f985 <b>Goshawk display</b> above the canopy.',
          '<span class="months">Apr\u2013May</span> \U0001f426 <b>Black woodpecker</b> drumming \u2014 audible far across the quiet blocks.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heather bloom</b> in the reopened clearings.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the deadwood left in place.'],
 'wild': ['\U0001f426 Black woodpecker', '\U0001f985 Goshawk', '\U0001f9a1 Pine marten', '\U0001f98e Sand lizard', '\U0001f33f Heather \u00b7 Wavy hair-grass'],
 'trail': ['Park at <b>Odoorn</b> or along the road to <b>Valthe</b>.',
           'Waymarked <b>walking and mountain-bike routes</b> through the compartments.',
           'Extensive and quiet \u2014 even in busy weather you will find <b>silence</b> here.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Timber harvesting possible \u2014 heed closures \u00b7 \U0001f6b4 MTB routes'
}))

C.append(mk.card(1243, 'Veenstreek', {
 'tags': ['Groningen \u00b7 Veenkoloni\u00ebn', 'Veenontginning \u00b7 restveen en dalgrond', 'list 34 \u00b7 no. 20'],
 'loc': '\U0001f4cd Rond Stadskanaal en Musselkanaal \u00b7 Ontginningslandschap \u00b7 Groot gebied',
 'desc': 'De <b>Veenstreek</b> is de strook langs het Stadskanaal waar de vervening het langst doorging en waar de sporen daarvan het scherpst zijn. Hier zie je alle stadia naast elkaar: percelen die al in de achttiende eeuw op <b>dalgrond</b> kwamen, en plekken waar pas na de Tweede Wereldoorlog de laatste turf werd gestoken. Het <b>Stadskanaal</b> zelf, in 1765 begonnen door de stad Groningen, is de ruggengraat \u2014 ruim veertig kilometer kaarsrecht, met aan weerszijden lintbebouwing die de hele economie van de streek droeg. Wat het gebied natuurlijk interessant maakt zijn de <b>restveenpakketten</b>: op enkele plaatsen is het veen nooit helemaal weggehaald, en daar liggen nu <b>natte heiderelicten, veenputjes en pijpenstrootjevelden</b>. In die restanten broeden <b>watersnip en paapje</b>, en groeit hier en daar nog echte <b>veenmoslaag</b> \u2014 het levende begin van hoogveen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (broedvogels en veenflora), sep\u2013okt (herfstkleuren van pijpenstrootje)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 watersnip baltst boven de natte laagtes.',
 'why': ['Alle stadia van <b>vervening</b> naast elkaar zichtbaar.',
         'Het <b>Stadskanaal</b> (1765): veertig kilometer kaarsrechte ruggengraat.',
         '<b>Restveenpakketten</b> met natte heide en levend veenmos.',
         'Broedplaats van <b>watersnip en paapje</b> in de natte relicten.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Watersnip</b> \u2014 baltsvlucht met blatend staartgeluid.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Paapje</b> op de ruige perceelsranden.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33f <b>Veenpluis en zonnedauw</b> in de restveenplekken.',
          '<span class="months">Sep\u2013Okt</span> \U0001f33e <b>Pijpenstrootje</b> kleurt de laagtes koperbruin.'],
 'wild': ['\U0001f426 Watersnip', '\U0001f426 Paapje', '\U0001f98b Veenbesblauwtje (zeldzaam)', '\U0001f33f Veenpluis \u00b7 Ronde zonnedauw', '\U0001f33e Pijpenstrootje'],
 'trail': ['Startpunten in <b>Stadskanaal</b> en <b>Musselkanaal</b>.',
           'Volg het kanaal per <b>fiets</b>; de restveenplekken liggen in de zijlussen.',
           'Natte delen \u2014 <b>laarzen</b> aanbevolen buiten de verharde paden.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Deels nat en particulier \u00b7 \U0001f6b4 Kanaalroutes'
}, {
 'tags': ['Groningen \u00b7 Peat Colonies', 'Peat reclamation \u00b7 residual bog and cut-over soil', 'list 34 \u00b7 no. 20'],
 'loc': '\U0001f4cd Around Stadskanaal and Musselkanaal \u00b7 Reclamation landscape \u00b7 Large area',
 'desc': 'The <b>Veenstreek</b> is the strip along the Stadskanaal where peat cutting continued longest and where its traces are sharpest. Here you see every stage side by side: plots that were already turned into <b>dalgrond</b> (cut-over soil) in the eighteenth century, and places where the last peat was cut only after the Second World War. The <b>Stadskanaal</b> itself, begun by the city of Groningen in 1765, is the backbone \u2014 more than forty kilometres dead straight, lined on both sides by ribbon settlement that carried the entire economy of the region. What makes the area interesting for nature are the <b>residual peat bodies</b>: in a few places the peat was never entirely removed, and there you now find <b>wet heath relics, peat pools and purple moor-grass fields</b>. In those remnants <b>snipe and whinchat</b> breed, and here and there a genuine <b>sphagnum layer</b> still grows \u2014 the living beginning of raised bog.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (breeding birds and bog flora), Sep\u2013Oct (autumn colours of purple moor-grass)<br>\n    <b>Best time of day:</b> Early morning \u2014 snipe drumming above the wet hollows.',
 'why': ['All stages of <b>peat cutting</b> visible side by side.',
         'The <b>Stadskanaal</b> (1765): forty kilometres of dead-straight backbone.',
         '<b>Residual peat bodies</b> with wet heath and living sphagnum.',
         'Breeding site for <b>snipe and whinchat</b> in the wet relics.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f426 <b>Snipe</b> \u2014 display flight with bleating tail sound.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Whinchat</b> on the rough field margins.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33f <b>Cotton-grass and sundew</b> in the residual peat patches.',
          '<span class="months">Sep\u2013Oct</span> \U0001f33e <b>Purple moor-grass</b> turns the hollows copper-brown.'],
 'wild': ['\U0001f426 Snipe', '\U0001f426 Whinchat', '\U0001f98b Cranberry blue (rare)', '\U0001f33f Cotton-grass \u00b7 Round-leaved sundew', '\U0001f33e Purple moor-grass'],
 'trail': ['Starting points in <b>Stadskanaal</b> and <b>Musselkanaal</b>.',
           'Follow the canal by <b>bike</b>; the residual peat patches lie in the side loops.',
           'Wet in places \u2014 <b>boots</b> recommended off the surfaced paths.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Partly wet and private \u00b7 \U0001f6b4 Canal routes'
}))

C.append(mk.card(1244, 'Braamberg', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Zandopduiking \u00b7 bos en heiderelict', 'list 34 \u00b7 no. 21'],
 'loc': '\U0001f4cd Bij Sellingen, Westerwolde \u00b7 Bos- en heuvelgebied \u00b7 Middelgroot',
 'desc': 'De <b>Braamberg</b> bij Sellingen is een van die bescheiden Nederlandse \u2018bergen\u2019 die je pas waardeert als je weet wat eronder ligt. Het is een <b>dekzandopduiking</b> uit het einde van de laatste ijstijd: toen hier poolwoestijn lag, blies de wind zand op tot ruggen en koppen, en de Braamberg is er daarvan een. Enkele meters hoogteverschil, meer is het niet \u2014 maar in Westerwolde is dat genoeg om een compleet ander <b>bodemleven</b> te dragen. De top is droog en voedselarm, met <b>oude eiken, grove dennen en heiderelicten</b>; de flanken zijn rijker en dragen loofbos; de voet is vochtig met <b>elzen en berken</b>. Die gradi\u00ebnt in het klein maakt het gebied verrassend soortenrijk. Er broeden <b>boomleeuwerik en gekraagde roodstaart</b>, en op zonnige zandplekken zonnen <b>levendbarende hagedissen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang en zonnende reptielen), aug\u2013sep (heide), okt (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend voor de boomleeuwerik; midden op de dag voor hagedissen.',
 'why': ['<b>Dekzandopduiking</b> uit de laatste ijstijd \u2014 poolwoestijn als vormgever.',
         'Complete <b>gradi\u00ebnt</b> van droge top naar vochtige voet in enkele meters.',
         '<b>Boomleeuwerik en gekraagde roodstaart</b> in de oude eiken.',
         'Zonnige zandplekken met <b>levendbarende hagedis</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Boomleeuwerik</b> zingt in cirkelende zangvlucht.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Gekraagde roodstaart</b> in de holtes van oude eiken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heiderelicten</b> in bloei op de top.',
          '<span class="months">Okt</span> \U0001f344 <b>Paddenstoelen</b> op de arme zandbodem.'],
 'wild': ['\U0001f426 Boomleeuwerik', '\U0001f426 Gekraagde roodstaart', '\U0001f98e Levendbarende hagedis', '\U0001f98c Ree', '\U0001f33f Struikhei \u00b7 Schapenzuring'],
 'trail': ['Parkeren bij <b>Sellingen</b>; het gebied grenst aan de Sellinger Bossen.',
           'Korte <b>rondwandelingen</b> over de kop en langs de flanken.',
           'Goed te combineren met de <b>Sellinger Bossen</b> tot een halve dag.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Los zand op de hellingen \u00b7 \U0001f6b6 Korte routes'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Sand rise \u00b7 woodland and heath relic', 'list 34 \u00b7 no. 21'],
 'loc': '\U0001f4cd Near Sellingen, Westerwolde \u00b7 Woodland and hill area \u00b7 Medium-sized',
 'desc': 'The <b>Braamberg</b> near Sellingen is one of those modest Dutch \u2018mountains\u2019 you only appreciate once you know what lies beneath. It is a <b>cover-sand rise</b> from the end of the last glaciation: when polar desert lay here, the wind piled sand into ridges and knolls, and the Braamberg is one of them. A few metres of height difference, no more \u2014 but in Westerwolde that is enough to carry a completely different <b>soil life</b>. The summit is dry and nutrient-poor, with <b>old oaks, Scots pines and heath relics</b>; the flanks are richer and carry broadleaved woodland; the foot is damp with <b>alder and birch</b>. That gradient in miniature makes the area surprisingly rich in species. <b>Woodlark and common redstart</b> breed here, and <b>viviparous lizards</b> bask on sunny sandy patches.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song and basking reptiles), Aug\u2013Sep (heather), Oct (fungi)<br>\n    <b>Best time of day:</b> Morning for the woodlark; midday for lizards.',
 'why': ['<b>Cover-sand rise</b> from the last glaciation \u2014 shaped by polar desert.',
         'Complete <b>gradient</b> from dry summit to damp foot within a few metres.',
         '<b>Woodlark and common redstart</b> in the old oaks.',
         'Sunny sandy patches with <b>viviparous lizard</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Woodlark</b> sings in circling song flight.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Common redstart</b> in the holes of old oaks.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heath relics</b> in flower on the summit.',
          '<span class="months">Oct</span> \U0001f344 <b>Fungi</b> on the poor sandy soil.'],
 'wild': ['\U0001f426 Woodlark', '\U0001f426 Common redstart', '\U0001f98e Viviparous lizard', '\U0001f98c Roe deer', '\U0001f33f Heather \u00b7 Sheep\u2019s sorrel'],
 'trail': ['Park at <b>Sellingen</b>; the area adjoins the Sellinger Bossen.',
           'Short <b>circular walks</b> over the knoll and along the flanks.',
           'Easily combined with the <b>Sellinger Bossen</b> for a half day.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Loose sand on the slopes \u00b7 \U0001f6b6 Short routes'
}))

mk.insert(C, '1240')
mk.progress(1244)
mk.check()
