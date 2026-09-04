# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1350, 'Boswachterij Sleenerzand', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Boswachterij \u00b7 naaldbos, heide en stuifzand', 'list 36 \u00b7 no. 69'],
 'loc': '\U0001f4cd Tussen Sleen, Schoonoord en Noord-Sleen \u00b7 Boswachterij \u00b7 Zeer groot',
 'desc': 'De <b>Boswachterij Sleenerzand</b> is een van de grote staatsbossen die in de jaren dertig zijn aangelegd door <b>werkverschaffing</b>: in de crisisjaren werden duizenden werklozen ingezet om heide en stuifzand te bebossen, met de schop en de kruiwagen. Dat verklaart de opvallende regelmaat van het bos \u2014 rechte vakken, gelijkjarige opstanden, een raster van brede brandgangen. Inmiddels wordt dat productiebos stap voor stap <b>omgevormd</b>: de dennen worden gedund, loofhout krijgt ruimte, en op sommige plekken is de heide weer teruggebracht door de bomen te kappen en de humuslaag te verwijderen. Het bijzonderste onderdeel is het <b>Sleenerzand</b> zelf, een restant actief stuifzand met <b>jeneverbesstruwelen</b>. In het bos leven <b>zwarte specht, havik en ree</b>, en de heide herbergt de <b>adder</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Aug\u2013sep</b> (heidebloei), sep\u2013nov (paddenstoelen), apr\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 grootste kans op ree en zwarte specht.',
 'why': ['Aangelegd door <b>werkverschaffing</b> in de crisisjaren dertig.',
         'Regelmatige vakken en brandgangen verraden de <b>industri\u00eble opzet</b>.',
         'Wordt stap voor stap <b>omgevormd</b> naar gevarieerder bos.',
         '<b>Jeneverbesstruwelen</b> op het resterende stuifzand.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Zwarte specht</b> roffelt door het bos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f40d <b>Adders</b> op de heidedelen.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heidebloei</b> op de herstelde velden.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelenrijkdom</b> onder de dennen.'],
 'wild': ['\U0001f426 Zwarte specht \u00b7 Havik \u00b7 Bosuil', '\U0001f40d Adder \u00b7 Levendbarende hagedis', '\U0001f98c Ree \u00b7 Vos \u00b7 Das', '\U0001f333 Jeneverbes \u00b7 Grove den \u00b7 Eik', '\U0001f344 Boleten \u00b7 Amanieten \u00b7 Russula\u2019s'],
 'trail': ['Parkeren bij <b>Sleen</b> of <b>Schoonoord</b>; uitgebreid routenetwerk.',
           'Zoek de <b>jeneverbesstruwelen</b> op het open zand.',
           'Kom in de <b>herfst</b> \u2014 dit is een topgebied voor paddenstoelen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Adders op de heide \u00b7 \U0001f9ed Staatsbosbeheer'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'State forest \u00b7 conifer wood, heath and drift sand', 'list 36 \u00b7 no. 69'],
 'loc': '\U0001f4cd Between Sleen, Schoonoord and Noord-Sleen \u00b7 State forest \u00b7 Very large',
 'desc': 'The <b>Boswachterij Sleenerzand</b> is one of the large state forests laid out in the 1930s through <b>work-relief schemes</b>: during the Depression thousands of unemployed men were set to afforest heath and drift sand, with spade and wheelbarrow. That explains the striking regularity of the wood \u2014 straight plots, even-aged stands, a grid of broad firebreaks. That production forest is now being <b>converted</b> step by step: the pines are thinned, broadleaves are given room, and in some places the heath has been restored by felling the trees and removing the humus layer. The most remarkable part is the <b>Sleenerzand</b> itself, a remnant of active drift sand with <b>juniper scrub</b>. <b>Black woodpecker, goshawk and roe deer</b> live in the wood, and the heath holds the <b>adder</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Aug\u2013Sep</b> (heather), Sep\u2013Nov (fungi), Apr\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Early morning \u2014 the best chance of roe deer and black woodpecker.',
 'why': ['Created by <b>work-relief schemes</b> in the Depression years.',
         'Regular plots and firebreaks betray the <b>industrial layout</b>.',
         'Being <b>converted</b> step by step into more varied woodland.',
         '<b>Juniper scrub</b> on the remaining drift sand.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Black woodpecker</b> drumming through the wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f40d <b>Adders</b> on the heath sections.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heather</b> on the restored fields.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Rich fungal flora</b> under the pines.'],
 'wild': ['\U0001f426 Black woodpecker \u00b7 Goshawk \u00b7 Tawny owl', '\U0001f40d Adder \u00b7 Common lizard', '\U0001f98c Roe deer \u00b7 Fox \u00b7 Badger', '\U0001f333 Juniper \u00b7 Scots pine \u00b7 Oak', '\U0001f344 Boletes \u00b7 Amanitas \u00b7 Brittlegills'],
 'trail': ['Park at <b>Sleen</b> or <b>Schoonoord</b>; extensive route network.',
           'Seek out the <b>juniper scrub</b> on the open sand.',
           'Come in <b>autumn</b> \u2014 this is a top area for fungi.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Adders on the heath \u00b7 \U0001f9ed Staatsbosbeheer'
}))

C.append(mk.card(1351, 'Boswachterij Gees', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Boswachterij \u00b7 gemengd bos en heideveldjes', 'list 36 \u00b7 no. 70'],
 'loc': '\U0001f4cd Bij Gees en Oosterhesselen \u00b7 Boswachterij \u00b7 Groot',
 'desc': 'De <b>Boswachterij Gees</b> is een gemengd bos op de flank van de Hondsrug, aangelegd op voormalige heidegrond. Wat dit bos onderscheidt van veel andere boswachterijen is de <b>bodemvariatie</b>: de ondergrond bestaat hier deels uit <b>keileem</b> uit de voorlaatste ijstijd, en keileem houdt water vast waar zand het doorlaat. Het gevolg is dat er binnen \u00e9\u00e9n bos droge dennenvakken op zandkoppen liggen naast vochtige eiken-berkenbossen op de leem, en zelfs enkele <b>vennetjes</b> op plekken waar de leemlaag ondiep zit. Die variatie vertaalt zich in een rijke <b>paddenstoelenflora</b> \u2014 mycologen komen hier speciaal voor \u2014 en in een gevarieerde vogelbevolking met <b>zwarte specht, havik, appelvink en bosuil</b>. In de heideveldjes tussen de bosvakken leven reptielen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Sep\u2013nov</b> (paddenstoelen), apr\u2013jun (broedvogels), aug\u2013sep (heideveldjes)<br>\n    <b>Beste tijd van de dag:</b> Ochtend na een natte nacht \u2014 optimaal voor paddenstoelen.',
 'why': ['<b>Keileem</b> in de ondergrond houdt water vast waar zand het doorlaat.',
         'Droge dennenvakken en <b>vochtige eiken-berkenbossen</b> naast elkaar.',
         'Enkele <b>vennetjes</b> waar de leemlaag ondiep zit.',
         'Rijke <b>paddenstoelenflora</b> \u2014 een bekende mycologenbestemming.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Zwarte specht</b> roffelt in de oude opstanden.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Appelvink</b> in de loofhoutvakken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heideveldjes</b> in bloei tussen het bos.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelenpiek</b> op de gevarieerde bodem.'],
 'wild': ['\U0001f344 Boleten \u00b7 Amanieten \u00b7 Stekelzwammen', '\U0001f426 Zwarte specht \u00b7 Havik \u00b7 Appelvink \u00b7 Bosuil', '\U0001f98e Levendbarende hagedis', '\U0001f333 Grove den \u00b7 Eik \u00b7 Berk \u00b7 Beuk', '\U0001f98c Ree \u00b7 Vos'],
 'trail': ['Parkeren bij <b>Gees</b>; gemarkeerde routes door de vakken.',
           'Let op de overgang van <b>zandkop naar leemlaagte</b> \u2014 het bos verandert erdoor.',
           'Kom in <b>oktober</b> voor de paddenstoelen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Paddenstoelen niet plukken \u00b7 \U0001f9ed Staatsbosbeheer'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'State forest \u00b7 mixed woodland and small heaths', 'list 36 \u00b7 no. 70'],
 'loc': '\U0001f4cd Near Gees and Oosterhesselen \u00b7 State forest \u00b7 Large',
 'desc': 'The <b>Boswachterij Gees</b> is a mixed wood on the flank of the Hondsrug, planted on former heathland. What distinguishes this wood from many other state forests is its <b>soil variation</b>: the subsoil here consists partly of <b>boulder clay</b> from the penultimate ice age, and boulder clay holds water where sand lets it through. The result is that within one wood, dry pine plots on sand knolls lie beside damp oak-birch woods on the clay, and even a few <b>small pools</b> where the clay layer is shallow. That variation translates into a rich <b>fungal flora</b> \u2014 mycologists come here specially \u2014 and a varied bird community with <b>black woodpecker, goshawk, hawfinch and tawny owl</b>. Reptiles live in the small heaths between the plots.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Sep\u2013Nov</b> (fungi), Apr\u2013Jun (breeding birds), Aug\u2013Sep (small heaths)<br>\n    <b>Best time of day:</b> Morning after a wet night \u2014 optimal for fungi.',
 'why': ['<b>Boulder clay</b> in the subsoil holds water where sand drains it.',
         'Dry pine plots and <b>damp oak-birch woods</b> side by side.',
         'A few <b>small pools</b> where the clay layer lies shallow.',
         'Rich <b>fungal flora</b> \u2014 a known destination for mycologists.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Black woodpecker</b> drumming in the old stands.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Hawfinch</b> in the broadleaf plots.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Small heaths</b> in flower between the woods.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungal peak</b> on the varied soil.'],
 'wild': ['\U0001f344 Boletes \u00b7 Amanitas \u00b7 Tooth fungi', '\U0001f426 Black woodpecker \u00b7 Goshawk \u00b7 Hawfinch \u00b7 Tawny owl', '\U0001f98e Common lizard', '\U0001f333 Scots pine \u00b7 Oak \u00b7 Birch \u00b7 Beech', '\U0001f98c Roe deer \u00b7 Fox'],
 'trail': ['Park at <b>Gees</b>; waymarked routes through the plots.',
           'Note the shift from <b>sand knoll to clay hollow</b> \u2014 the wood changes with it.',
           'Come in <b>October</b> for the fungi.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Do not pick fungi \u00b7 \U0001f9ed Staatsbosbeheer'
}))

C.append(mk.card(1352, 'Mepperdennen', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Dennenbos \u00b7 grove den op stuifzand', 'list 36 \u00b7 no. 71'],
 'loc': '\U0001f4cd Bij Meppen en Zweeloo \u00b7 Dennenbos \u00b7 Klein',
 'desc': 'De <b>Mepperdennen</b> zijn een oud grove-dennenbos bij het gehucht Meppen, aangeplant om stuifzand vast te leggen. Dennenbossen hebben een slechte reputatie als \u2018groene woestijn\u2019, maar dat oordeel klopt vooral voor jonge, dichte aanplant. Zodra een dennenbos <b>oud genoeg</b> wordt \u2014 en dat is hier het geval \u2014 verandert de zaak: de kronen gaan uit elkaar staan, er valt licht op de bodem, oude bomen ontwikkelen dikke schors en de eerste dode stammen blijven liggen. Precies dat maakt een dennenbos waardevol. Hier profiteren <b>boomkruiper, kuifmees en zwarte specht</b> ervan, en de dikke schorsplaten bieden schuilplaats aan insecten en <b>vleermuizen</b>. De zure, schrale bodem levert bovendien een karakteristieke paddenstoelenflora op met <b>boleten en stekelzwammen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Sep\u2013nov</b> (paddenstoelen), mrt\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 dan roffelt de zwarte specht.',
 'why': ['Oud dennenbos \u2014 <b>niet te vergelijken</b> met jonge dichte aanplant.',
         'Kronen uit elkaar, licht op de bodem, eerste <b>dode stammen</b>.',
         'Dikke <b>schorsplaten</b> als schuilplaats voor insecten en vleermuizen.',
         'Karakteristieke paddenstoelen: <b>boleten en stekelzwammen</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Zwarte specht</b> roffelt op dode stammen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kuifmees en goudhaan</b> in de kronen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> achter losse schorsplaten.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Boleten en stekelzwammen</b> op de zure bodem.'],
 'wild': ['\U0001f426 Zwarte specht \u00b7 Kuifmees \u00b7 Goudhaan \u00b7 Boomkruiper', '\U0001f344 Boleten \u00b7 Stekelzwammen \u00b7 Vliegenzwam', '\U0001f987 Vleermuizen achter schors', '\U0001f333 Oude grove dennen', '\U0001f98c Ree'],
 'trail': ['Parkeren bij <b>Meppen</b>; paden door het bos.',
           'Kijk naar de <b>losse schorsplaten</b> op de oudste stammen.',
           'Klein bos \u2014 combineer met <b>Wezup</b> of <b>De Palmen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f9ed Staatsbosbeheer'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Pine wood \u00b7 Scots pine on drift sand', 'list 36 \u00b7 no. 71'],
 'loc': '\U0001f4cd Near Meppen and Zweeloo \u00b7 Pine wood \u00b7 Small',
 'desc': 'The <b>Mepperdennen</b> is an old Scots pine wood by the hamlet of Meppen, planted to fix drift sand. Pine woods have a poor reputation as \u2018green deserts\u2019, but that judgement applies mainly to young, dense plantations. Once a pine wood becomes <b>old enough</b> \u2014 as is the case here \u2014 things change: the crowns separate, light reaches the floor, old trees develop thick bark and the first dead trunks are left lying. That is precisely what makes a pine wood valuable. <b>Treecreeper, crested tit and black woodpecker</b> benefit here, and the thick bark plates shelter insects and <b>bats</b>. The acid, poor soil also produces a characteristic fungal flora with <b>boletes and tooth fungi</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Sep\u2013Nov</b> (fungi), Mar\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Early morning \u2014 when the black woodpecker drums.',
 'why': ['Old pine wood \u2014 <b>not comparable</b> to young dense plantation.',
         'Crowns apart, light on the floor, first <b>dead trunks</b>.',
         'Thick <b>bark plates</b> as shelter for insects and bats.',
         'Characteristic fungi: <b>boletes and tooth fungi</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Black woodpecker</b> drums on dead trunks.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Crested tit and goldcrest</b> in the crowns.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> behind loose bark plates.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Boletes and tooth fungi</b> on the acid soil.'],
 'wild': ['\U0001f426 Black woodpecker \u00b7 Crested tit \u00b7 Goldcrest \u00b7 Treecreeper', '\U0001f344 Boletes \u00b7 Tooth fungi \u00b7 Fly agaric', '\U0001f987 Bats behind bark', '\U0001f333 Old Scots pines', '\U0001f98c Roe deer'],
 'trail': ['Park at <b>Meppen</b>; paths through the wood.',
           'Look at the <b>loose bark plates</b> on the oldest trunks.',
           'Small wood \u2014 combine with <b>Wezup</b> or <b>De Palmen</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f9ed Staatsbosbeheer'
}))

C.append(mk.card(1353, 'De Palmen', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Natte laagte \u00b7 elzenbroek en moerasje', 'list 36 \u00b7 no. 72'],
 'loc': '\U0001f4cd Bij Zweeloo en Aalden \u00b7 Elzenbroek \u00b7 Klein',
 'desc': '<b>De Palmen</b> is een klein elzenbroekbos in een natte laagte bij Zweeloo. Elzenbroek is een van de meest ondergewaardeerde bostypen van Nederland, waarschijnlijk omdat het er het grootste deel van het jaar ontoegankelijk en rommelig uitziet. Maar juist die <b>ontoegankelijkheid</b> is de kracht: er wordt niet gewandeld, niet gekapt en niet gemaaid, en dat maakt het tot een van de rustigste plekken in het landschap. De zwarte els heeft bovendien een truc \u2014 hij leeft in symbiose met <b>stikstofbindende bacteri\u00ebn</b> in wortelknolletjes, waardoor hij op voedselarme natte grond kan groeien waar andere bomen het opgeven. Onder de elzen staan <b>elzenzegge, moerasvaren en dotterbloem</b>, en het bos is broedplaats voor <b>houtsnip, matkop en zwarte specht</b>. Ook de <b>ijsvogel</b> jaagt er langs de greppels.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels en voorjaarsflora), okt\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig en het beste moment voor de matkop.',
 'why': ['<b>Elzenbroek</b>: ondergewaardeerd, maar juist door ontoegankelijkheid rijk.',
         'Zwarte els leeft in symbiose met <b>stikstofbindende bacteri\u00ebn</b>.',
         'Groeit daardoor waar andere bomen het <b>opgeven</b>.',
         'Broedplaats van <b>houtsnip, matkop en zwarte specht</b>.'],
 'phen': ['<span class="months">Feb\u2013Mrt</span> \U0001f33e <b>Elzenkatjes</b> bloeien \u2014 vroegste stuifmeelbron.',
          '<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dotterbloem</b> in de natte delen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Matkop en houtsnip</b> broeden.',
          '<span class="months">Okt\u2013Nov</span> \U0001f344 <b>Elzenspecifieke paddenstoelen</b>.'],
 'wild': ['\U0001f426 Houtsnip \u00b7 Matkop \u00b7 Zwarte specht \u00b7 IJsvogel', '\U0001f33c Dotterbloem \u00b7 Elzenzegge \u00b7 Moerasvaren', '\U0001f333 Zwarte els \u00b7 Wilg', '\U0001f438 Amfibie\u00ebn in de greppels', '\U0001f344 Elzenpaddenstoelen'],
 'trail': ['Parkeren bij <b>Aalden</b>; het bos is grotendeels alleen van de <b>rand</b> te bekijken.',
           'Betreden is meestal onmogelijk \u2014 dat hoort bij dit bostype.',
           'Luister vanaf de rand naar de <b>matkop</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Drassig en niet toegankelijk \u00b7 \U0001f97e Laarzen bij de rand'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Wet hollow \u00b7 alder carr and small marsh', 'list 36 \u00b7 no. 72'],
 'loc': '\U0001f4cd Near Zweeloo and Aalden \u00b7 Alder carr \u00b7 Small',
 'desc': '<b>De Palmen</b> is a small alder carr in a wet hollow near Zweeloo. Alder carr is one of the most undervalued woodland types in the Netherlands, probably because for most of the year it looks impenetrable and untidy. But that <b>inaccessibility</b> is precisely its strength: nobody walks, fells or mows there, which makes it one of the quietest places in the landscape. The black alder also has a trick \u2014 it lives in symbiosis with <b>nitrogen-fixing bacteria</b> in root nodules, allowing it to grow on nutrient-poor wet ground where other trees give up. Beneath the alders stand <b>tufted sedge, marsh fern and marsh marigold</b>, and the wood is a breeding site for <b>woodcock, willow tit and black woodpecker</b>. The <b>kingfisher</b> also hunts along the ditches.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds and spring flora), Oct\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet, and the best moment for the willow tit.',
 'why': ['<b>Alder carr</b>: undervalued, but rich precisely through inaccessibility.',
         'Black alder lives in symbiosis with <b>nitrogen-fixing bacteria</b>.',
         'It therefore grows where other trees <b>give up</b>.',
         'Breeding site for <b>woodcock, willow tit and black woodpecker</b>.'],
 'phen': ['<span class="months">Feb\u2013Mar</span> \U0001f33e <b>Alder catkins</b> flower \u2014 the earliest pollen source.',
          '<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh marigold</b> in the wet parts.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Willow tit and woodcock</b> breed.',
          '<span class="months">Oct\u2013Nov</span> \U0001f344 <b>Alder-specific fungi</b>.'],
 'wild': ['\U0001f426 Woodcock \u00b7 Willow tit \u00b7 Black woodpecker \u00b7 Kingfisher', '\U0001f33c Marsh marigold \u00b7 Tufted sedge \u00b7 Marsh fern', '\U0001f333 Black alder \u00b7 Willow', '\U0001f438 Amphibians in the ditches', '\U0001f344 Alder fungi'],
 'trail': ['Park at <b>Aalden</b>; the wood is largely viewable only from the <b>edge</b>.',
           'Entering is usually impossible \u2014 that is part of this woodland type.',
           'Listen from the edge for the <b>willow tit</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Boggy and not accessible \u00b7 \U0001f97e Boots at the edge'
}, card_class='card water'))

C.append(mk.card(1354, 'Geeserstroom', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Beekherstel \u00b7 hermeanderde beek en natte graslanden', 'list 36 \u00b7 no. 73'],
 'loc': '\U0001f4cd Tussen Gees, Oosterhesselen en Zweeloo \u00b7 Beekdal \u00b7 Groot',
 'desc': 'De <b>Geeserstroom</b> is een van de meest geslaagde <b>beekherstelprojecten</b> van Nederland en daarmee een leerzaam gebied. De beek was in de twintigste eeuw rechtgetrokken tot een kaarsrechte sloot, met als doel het water zo snel mogelijk af te voeren. Dat werkte \u2014 te goed: het beekdal verdroogde, de karakteristieke vegetatie verdween, en stroomafwaarts kwam het water in \u00e9\u00e9n golf aan met wateroverlast als gevolg. Rond 2000 is het roer omgegooid: de beek kreeg zijn <b>meanders terug</b>, de landbouwgronden eromheen werden aangekocht en de voedselrijke bouwvoor afgegraven. Het gebied houdt nu water vast in plaats van het af te voeren \u2014 een <b>spons</b> in plaats van een goot. Het resultaat kwam sneller dan verwacht: er broeden <b>kraanvogels</b>, en verder grutto, watersnip, roodborsttapuit en paapje.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (kraanvogels en weidevogels), aug\u2013okt (doortrek)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 kraanvogels roepen bij zonsopkomst.',
 'why': ['Geslaagd <b>beekherstel</b>: de meanders zijn teruggebracht.',
         'Bouwvoor <b>afgegraven</b> en landbouwgrond omgezet in natuur.',
         'Het gebied werkt nu als <b>spons</b> in plaats van als goot.',
         'Broedende <b>kraanvogels</b> \u2014 een van de weinige plekken in Nederland.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Kraanvogels</b> beginnen te baltsen \u2014 trompetterende roep.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Grutto, watersnip en paapje</b> broeden.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Beekdalflora</b> op de vernatte percelen.',
          '<span class="months">Aug\u2013Okt</span> \U0001f426 <b>Doortrekkende steltlopers</b> op de plas-drasdelen.'],
 'wild': ['\U0001f426 Kraanvogel', '\U0001f426 Grutto \u00b7 Watersnip \u00b7 Paapje \u00b7 Roodborsttapuit', '\U0001f985 Bruine kiekendief \u00b7 Blauwe kiekendief', '\U0001f42e Grote grazers (begrazing)', '\U0001f33c Beekdalflora \u00b7 Zeggen'],
 'trail': ['Parkeren bij <b>Gees</b>; uitkijkpunten en paden langs de rand.',
           'Blijf op <b>ruime afstand</b> van broedende kraanvogels \u2014 ze zijn zeer gevoelig.',
           'Neem een <b>telescoop</b> mee; het gebied is groot en open.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kraanvogels niet verstoren \u2014 blijf op de paden \u00b7 \U0001f52d Telescoop aanbevolen'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Brook restoration \u00b7 remeandered brook and wet grasslands', 'list 36 \u00b7 no. 73'],
 'loc': '\U0001f4cd Between Gees, Oosterhesselen and Zweeloo \u00b7 Brook valley \u00b7 Large',
 'desc': 'The <b>Geeserstroom</b> is one of the most successful <b>brook restoration projects</b> in the Netherlands and therefore an instructive site. In the twentieth century the brook was straightened into a dead-straight ditch, with the aim of discharging water as fast as possible. That worked \u2014 too well: the valley dried out, the characteristic vegetation vanished, and downstream the water arrived in a single surge, causing flooding. Around 2000 the approach was reversed: the brook got its <b>meanders back</b>, the surrounding farmland was bought up and the nutrient-rich topsoil stripped. The area now retains water instead of discharging it \u2014 a <b>sponge</b> rather than a gutter. The result came faster than expected: <b>cranes</b> breed here, along with godwit, snipe, stonechat and whinchat.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (cranes and meadow birds), Aug\u2013Oct (passage)<br>\n    <b>Best time of day:</b> Early morning \u2014 cranes call at sunrise.',
 'why': ['Successful <b>brook restoration</b>: the meanders have been returned.',
         'Topsoil <b>stripped</b> and farmland converted to nature.',
         'The area now works as a <b>sponge</b> instead of a gutter.',
         'Breeding <b>cranes</b> \u2014 one of the few sites in the Netherlands.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Cranes</b> begin displaying \u2014 trumpeting calls.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Godwit, snipe and whinchat</b> breed.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Brook-valley flora</b> on the rewetted parcels.',
          '<span class="months">Aug\u2013Oct</span> \U0001f426 <b>Passage waders</b> on the shallow flooded parts.'],
 'wild': ['\U0001f426 Common crane', '\U0001f426 Black-tailed godwit \u00b7 Snipe \u00b7 Whinchat \u00b7 Stonechat', '\U0001f985 Marsh harrier \u00b7 Hen harrier', '\U0001f42e Large grazers', '\U0001f33c Brook-valley flora \u00b7 Sedges'],
 'trail': ['Park at <b>Gees</b>; viewpoints and paths along the edge.',
           'Keep a <b>wide distance</b> from breeding cranes \u2014 they are highly sensitive.',
           'Bring a <b>telescope</b>; the area is large and open.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Do not disturb cranes \u2014 keep to the paths \u00b7 \U0001f52d Telescope recommended'
}, card_class='card water'))

mk.insert(C, '1349')
mk.progress(1354)
mk.check()
