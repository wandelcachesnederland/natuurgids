# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1345, 'Mantingerveld', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Heideveld \u00b7 heide, vennen en stuifzand', 'list 36 \u00b7 no. 64'],
 'loc': '\U0001f4cd Bij Mantinge en Balinge \u00b7 Heideveld \u00b7 Groot',
 'desc': 'Het <b>Mantingerveld</b> is een van de grootste heidegebieden van Midden-Drenthe en het resultaat van een van de ambitieuzere natuurherstelprojecten van het land. Wat hier gebeurde is instructief: in de jaren negentig lagen er nog losse heidesnippers tussen landbouwpercelen, en die snippers waren te klein om levensvatbaar te zijn. Kleine populaties sterven namelijk uit door <b>toeval</b> \u2014 een slechte zomer, een ziekte, en de laatste tien exemplaren zijn weg, zonder dat er nieuwe kunnen instromen. De oplossing was de tussenliggende akkers aankopen, de <b>bemeste bouwvoor afgraven</b> en de snippers zo aan elkaar te knopen tot \u00e9\u00e9n groot veld. Dat heeft gewerkt: <b>gladde slang, adder en levendbarende hagedis</b> hebben zich uitgebreid, en de <b>Schotse hooglanders</b> die er grazen houden de vergrassing tegen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Aug\u2013sep</b> (heidebloei), apr\u2013jun (reptielen en broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 reptielen zonnen zich dan langs de paden.',
 'why': ['Grootschalig <b>heideherstel</b> door snippers aan elkaar te knopen.',
         'Kleine populaties sterven uit door <b>toeval</b> \u2014 vandaar de vergroting.',
         'Bemeste bouwvoor werd <b>afgegraven</b> om schrale grond terug te krijgen.',
         '<b>Gladde slang en adder</b> hebben zich weer uitgebreid.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f40d <b>Adders</b> zonnen zich na de winterrust.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Boomleeuwerik en roodborsttapuit</b> broeden.',
          '<span class="months">Jul\u2013Aug</span> \U0001f338 <b>Dopheide</b> bloeit in de natte laagtes.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> kleurt het hele veld paars.'],
 'wild': ['\U0001f40d Adder \u00b7 Gladde slang \u00b7 Levendbarende hagedis', '\U0001f426 Boomleeuwerik \u00b7 Roodborsttapuit \u00b7 Veldleeuwerik', '\U0001f42e Schotse hooglanders (begrazing)', '\U0001f338 Struikheide \u00b7 Dopheide \u00b7 Jeneverbes', '\U0001f98b Heideblauwtje \u00b7 Heivlinder'],
 'trail': ['Parkeren bij <b>Mantinge</b>; gemarkeerde routes over het veld.',
           'Blijf op de paden \u2014 er lopen <b>adders</b>, en ze wijken alleen als je ze ziet aankomen.',
           'Combineer met het aangrenzende <b>Mantingerbos</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Adders aanwezig \u2014 blijf op de paden \u00b7 \U0001f42e Grote grazers \u00b7 \U0001f9ed Natuurmonumenten'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Heathland \u00b7 heath, pools and drift sand', 'list 36 \u00b7 no. 64'],
 'loc': '\U0001f4cd Near Mantinge and Balinge \u00b7 Heathland \u00b7 Large',
 'desc': 'The <b>Mantingerveld</b> is one of the largest heaths in Mid-Drenthe and the result of one of the more ambitious nature restoration projects in the country. What happened here is instructive: in the 1990s only scattered scraps of heath lay between farm fields, and those scraps were too small to be viable. Small populations die out through <b>chance</b> \u2014 a bad summer, a disease, and the last ten individuals are gone with no way for new ones to arrive. The solution was to buy the intervening fields, <b>strip off the fertilised topsoil</b> and tie the scraps together into one large heath. It worked: <b>smooth snake, adder and common lizard</b> have expanded, and the <b>Highland cattle</b> grazing there hold back grass encroachment.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Aug\u2013Sep</b> (heather), Apr\u2013Jun (reptiles and breeding birds)<br>\n    <b>Best time of day:</b> Morning \u2014 reptiles then bask along the paths.',
 'why': ['Large-scale <b>heath restoration</b> by tying scraps together.',
         'Small populations die out by <b>chance</b> \u2014 hence the enlargement.',
         'Fertilised topsoil was <b>stripped</b> to recover poor ground.',
         '<b>Smooth snake and adder</b> have expanded again.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f40d <b>Adders</b> bask after winter dormancy.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Woodlark and stonechat</b> breed.',
          '<span class="months">Jul\u2013Aug</span> \U0001f338 <b>Cross-leaved heath</b> flowers in the wet hollows.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Ling</b> turns the whole heath purple.'],
 'wild': ['\U0001f40d Adder \u00b7 Smooth snake \u00b7 Common lizard', '\U0001f426 Woodlark \u00b7 Stonechat \u00b7 Skylark', '\U0001f42e Highland cattle (grazing)', '\U0001f338 Ling \u00b7 Cross-leaved heath \u00b7 Juniper', '\U0001f98b Silver-studded blue \u00b7 Grayling'],
 'trail': ['Park at <b>Mantinge</b>; waymarked routes across the heath.',
           'Keep to the paths \u2014 there are <b>adders</b>, and they only move if they see you coming.',
           'Combine with the adjoining <b>Mantingerbos</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Adders present \u2014 keep to the paths \u00b7 \U0001f42e Large grazers \u00b7 \U0001f9ed Natuurmonumenten'
}, card_class='card dune'))

C.append(mk.card(1346, 'Mantingerbos en -weiden', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Oud bos \u00b7 hakhout, jeneverbes en schrale weiden', 'list 36 \u00b7 no. 65'],
 'loc': '\U0001f4cd Bij Mantinge \u00b7 Oud loofbos met weiden \u00b7 Klein',
 'desc': 'Het <b>Mantingerbos</b> is een van de weinige stukken <b>oud bos</b> van Drenthe \u2014 een provincie die eeuwenlang vrijwel boomloos was. Het bos overleefde als <b>markebos</b>: gemeenschappelijk bezit van de boermarke, waar hakhout werd gewonnen voor gereedschap, omheiningen en brandhout. Omdat de grond nooit is geploegd of bemest, staat er een bosbodemflora die elders is verdwenen \u2014 met <b>dalkruid, lelietje-van-dalen en witte klaverzuring</b>. Die soorten verspreiden zich extreem traag, vaak maar enkele meters per eeuw, en zijn daarom betrouwbare indicatoren van bosbodems die eeuwenlang ongestoord bleven. In het bos staan bovendien oude <b>jeneverbessen</b>, en de aangrenzende <b>Mantingerweiden</b> zijn schrale graslanden die nooit zijn omgeploegd \u2014 met orchidee\u00ebn en een rijke insectenfauna.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (bosbodemflora), mei\u2013jul (orchidee\u00ebn in de weiden), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 in mei is de bosbodem op zijn mooist.',
 'why': ['Zeldzaam <b>oud bos</b> in een van oudsher boomloze provincie.',
         'Overleefde als <b>markebos</b>: gemeenschappelijk hakhout.',
         'Bosbodemflora verspreidt zich <b>enkele meters per eeuw</b> \u2014 een indicator.',
         'Oude <b>jeneverbessen</b> en nooit omgeploegde schrale weiden.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dalkruid en lelietje-van-dalen</b> bloeien.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Orchidee\u00ebn</b> in de Mantingerweiden.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Insecten</b> op de schrale graslanden.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de oude bosbodem.'],
 'wild': ['\U0001f33c Dalkruid \u00b7 Lelietje-van-dalen \u00b7 Witte klaverzuring', '\U0001f333 Jeneverbes \u00b7 Eikenhakhout \u00b7 Hulst', '\U0001f426 Boomklever \u00b7 Bosuil \u00b7 Appelvink', '\U0001f33c Orchidee\u00ebn in de weiden', '\U0001f344 Zeldzame bospaddenstoelen'],
 'trail': ['Parkeren bij <b>Mantinge</b>; paden door bos en weiden.',
           'Kom in <b>mei</b> \u2014 de bosbodemflora is dan op zijn hoogtepunt.',
           'Blijf op de paden: de <b>bosbodem</b> herstelt niet van betreding.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbare oude bosbodem \u00b7 \U0001f9ed Natuurmonumenten'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Ancient woodland \u00b7 coppice, juniper and poor meadows', 'list 36 \u00b7 no. 65'],
 'loc': '\U0001f4cd Near Mantinge \u00b7 Ancient broadleaf wood with meadows \u00b7 Small',
 'desc': 'The <b>Mantingerbos</b> is one of the few pieces of <b>ancient woodland</b> in Drenthe \u2014 a province that was virtually treeless for centuries. The wood survived as a <b>marke wood</b>: common property of the village commons association, where coppice was cut for tools, fencing and firewood. Because the ground was never ploughed or fertilised, it carries a woodland-floor flora that has vanished elsewhere \u2014 with <b>May lily, lily-of-the-valley and wood sorrel</b>. Those species spread extremely slowly, often only a few metres per century, and are therefore reliable indicators of woodland soils that remained undisturbed for centuries. Old <b>junipers</b> also stand in the wood, and the adjoining <b>Mantingerweiden</b> are poor grasslands never ploughed up \u2014 with orchids and a rich insect fauna.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (woodland-floor flora), May\u2013Jul (orchids in the meadows), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Morning \u2014 in May the woodland floor is at its finest.',
 'why': ['Rare <b>ancient woodland</b> in a historically treeless province.',
         'Survived as a <b>marke wood</b>: communal coppice.',
         'Woodland-floor flora spreads <b>a few metres per century</b> \u2014 an indicator.',
         'Old <b>junipers</b> and never-ploughed poor meadows.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>May lily and lily-of-the-valley</b> in flower.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Orchids</b> in the Mantingerweiden.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Insects</b> on the poor grasslands.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the ancient woodland floor.'],
 'wild': ['\U0001f33c May lily \u00b7 Lily-of-the-valley \u00b7 Wood sorrel', '\U0001f333 Juniper \u00b7 Oak coppice \u00b7 Holly', '\U0001f426 Nuthatch \u00b7 Tawny owl \u00b7 Hawfinch', '\U0001f33c Orchids in the meadows', '\U0001f344 Rare woodland fungi'],
 'trail': ['Park at <b>Mantinge</b>; paths through wood and meadows.',
           'Come in <b>May</b> \u2014 the woodland-floor flora is then at its peak.',
           'Keep to the paths: the <b>woodland floor</b> does not recover from trampling.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile ancient woodland floor \u00b7 \U0001f9ed Natuurmonumenten'
}, card_class='card estate'))

C.append(mk.card(1347, 'Broekstreek', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Ontginningslandschap \u00b7 natte graslanden en houtwallen', 'list 36 \u00b7 no. 66'],
 'loc': '\U0001f4cd Rond Balinge, Mantinge en Bruntinge \u00b7 Broekontginning \u00b7 Groot',
 'desc': 'De <b>Broekstreek</b> is de naam voor het gebied rond Balinge, Mantinge en Bruntinge, en <b>broek</b> betekent \u2014 zoals vaker in deze gids \u2014 moerassig laagland. Dit was het natte tegendeel van de hoge essen: land dat pas laat is ontgonnen omdat het simpelweg te drassig was om iets mee te doen. Die late ontginning is een geluk gebleken, want er zijn veel meer <b>landschapselementen</b> bewaard gebleven dan in gebieden die de volle negentiende-eeuwse ontginningsdrift over zich heen kregen. Er liggen nog kilometers <b>houtwallen en elzensingels</b>, oude sloten en kleine bosjes, en het geheel vormt een dicht netwerk. Hier broeden nog <b>steenuil, geelgors en grutto</b> in relatief hoge dichtheden, en de <b>das</b> vindt er zowel burchtplaatsen in de wallen als voedsel in de weides.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels en zang), okt\u2013nov (herfstkleur in de singels)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 steenuil, das en vleermuizen worden dan actief.',
 'why': ['<b>Broek</b> = moerassig laagland \u2014 het natte tegendeel van de es.',
         '<b>Laat ontgonnen</b>, en daardoor rijk aan bewaarde landschapselementen.',
         'Kilometers <b>houtwallen en elzensingels</b> in een dicht netwerk.',
         'Hoge dichtheden <b>steenuil, geelgors en grutto</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f989 <b>Steenuil</b> roept vanaf de knotbomen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Grutto en kievit</b> in de natte graslanden.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors</b> zingt vanaf de houtwallen.',
          '<span class="months">Okt\u2013Nov</span> \U0001f341 <b>Herfstkleur</b> maakt het singelnetwerk zichtbaar.'],
 'wild': ['\U0001f989 Steenuil \u00b7 Kerkuil', '\U0001f426 Grutto \u00b7 Kievit \u00b7 Geelgors', '\U0001f9a1 Das \u00b7 Steenmarter', '\U0001f987 Vleermuizen langs de singels', '\U0001f333 Els \u00b7 Eik \u00b7 Knotwilg'],
 'trail': ['Parkeren in <b>Balinge</b> of <b>Bruntinge</b>; landweggetjes verbinden alles.',
           'Ideaal per <b>fiets</b> \u2014 het netwerk is uitgestrekt.',
           'Kom bij <b>schemer</b> voor uilen en das.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Veel particulier land \u2014 blijf op de wegen \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Reclamation landscape \u00b7 wet grasslands and hedgebanks', 'list 36 \u00b7 no. 66'],
 'loc': '\U0001f4cd Around Balinge, Mantinge and Bruntinge \u00b7 Marsh reclamation \u00b7 Large',
 'desc': 'The <b>Broekstreek</b> is the name for the area around Balinge, Mantinge and Bruntinge, and <b>broek</b> means \u2014 as often in this guide \u2014 marshy lowland. This was the wet opposite of the high open fields: land reclaimed only late because it was simply too boggy to do anything with. That late reclamation has proved fortunate, because far more <b>landscape elements</b> have survived here than in areas that took the full force of nineteenth-century reclamation. Kilometres of <b>hedgebanks and alder lines</b>, old ditches and small copses remain, and together they form a dense network. <b>Little owl, yellowhammer and black-tailed godwit</b> still breed here at relatively high densities, and the <b>badger</b> finds both sett sites in the banks and food in the pastures.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds and song), Oct\u2013Nov (autumn colour in the tree lines)<br>\n    <b>Best time of day:</b> Dusk \u2014 little owl, badger and bats then become active.',
 'why': ['<b>Broek</b> = marshy lowland \u2014 the wet opposite of the es.',
         '<b>Reclaimed late</b>, and therefore rich in surviving landscape elements.',
         'Kilometres of <b>hedgebanks and alder lines</b> in a dense network.',
         'High densities of <b>little owl, yellowhammer and godwit</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f989 <b>Little owl</b> calls from the pollards.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Godwit and lapwing</b> in the wet grasslands.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer</b> sings from the hedgebanks.',
          '<span class="months">Oct\u2013Nov</span> \U0001f341 <b>Autumn colour</b> reveals the network of tree lines.'],
 'wild': ['\U0001f989 Little owl \u00b7 Barn owl', '\U0001f426 Black-tailed godwit \u00b7 Lapwing \u00b7 Yellowhammer', '\U0001f9a1 Badger \u00b7 Stone marten', '\U0001f987 Bats along the tree lines', '\U0001f333 Alder \u00b7 Oak \u00b7 Pollard willow'],
 'trail': ['Park in <b>Balinge</b> or <b>Bruntinge</b>; country lanes connect everything.',
           'Ideal <b>by bicycle</b> \u2014 the network is extensive.',
           'Come at <b>dusk</b> for owls and badger.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Much private land \u2014 keep to the roads \u00b7 \U0001f6b4 Cycle route'
}))

C.append(mk.card(1348, 'Sniphorsten', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Bosje \u00b7 houtwallen en natte laagtes', 'list 36 \u00b7 no. 67'],
 'loc': '\U0001f4cd Bij Wezup en Zweeloo \u00b7 Kleinschalig bos \u00b7 Klein',
 'desc': 'De <b>Sniphorsten</b> is een klein natuurgebiedje waarvan de naam twee landschapstermen combineert: <b>snip</b> verwijst naar de watersnip, en een <b>horst</b> is een hogere, drogere plek in nat terrein. Samen beschrijft de naam dus precies wat het gebied is \u2014 een reeks kleine zandkoppen die als eilanden in een drassige omgeving liggen. Zulke <b>micro-reli\u00ebfverschillen</b> van soms maar een halve meter zijn in Drenthe bepalend: ze scheiden droge eikenbosjes van natte elzenbroekjes, vaak binnen \u00e9\u00e9n oogopslag. Die afwisseling op kleine schaal levert een groot aantal <b>overgangsmilieus</b> op, en daar zit de soortenrijkdom. Op de horsten groeien eik en berk, in de laagtes els en wilg, en er broeden <b>houtsnip, bosuil en boomkruiper</b>. In het natte deel paaien amfibie\u00ebn.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (amfibie\u00ebn en broedvogels), okt\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 houtsnippen maken dan hun baltsvluchten boven het bos.',
 'why': ['Naam combineert <b>snip</b> en <b>horst</b>: hoogtes in nat terrein.',
         '<b>Micro-reli\u00ebf</b> van een halve meter scheidt droog van nat.',
         'Veel <b>overgangsmilieus</b> op kleine schaal.',
         'Baltsende <b>houtsnippen</b> boven het bos in het voorjaar.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Amfibie\u00ebn</b> paaien in de natte laagtes.',
          '<span class="months">Mrt\u2013Mei</span> \U0001f426 <b>Houtsnip</b> baltst bij schemer boven het bos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Bosuil en boomkruiper</b> broeden.',
          '<span class="months">Okt\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de vochtige bosbodem.'],
 'wild': ['\U0001f426 Houtsnip \u00b7 Bosuil \u00b7 Boomkruiper', '\U0001f438 Bruine kikker \u00b7 Kleine watersalamander', '\U0001f333 Eik \u00b7 Berk \u00b7 Els \u00b7 Wilg', '\U0001f344 Vochtminnende paddenstoelen', '\U0001f98c Ree'],
 'trail': ['Parkeren bij <b>Wezup</b>; smalle paden door het gebiedje.',
           'Let op het <b>hoogteverschil</b>: een halve meter verandert alles.',
           'Kom bij <b>schemer in maart</b> voor de baltsende houtsnip.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Nat in de laagtes \u00b7 \u26a0\ufe0f Klein gebied, snel verstoord'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Copse \u00b7 hedgebanks and wet hollows', 'list 36 \u00b7 no. 67'],
 'loc': '\U0001f4cd Near Wezup and Zweeloo \u00b7 Small-scale woodland \u00b7 Small',
 'desc': 'The <b>Sniphorsten</b> is a small reserve whose name combines two landscape terms: <b>snip</b> refers to the snipe, and a <b>horst</b> is a higher, drier spot in wet terrain. Together the name describes exactly what the area is \u2014 a series of small sand knolls lying like islands in boggy surroundings. Such <b>micro-relief differences</b> of sometimes only half a metre are decisive in Drenthe: they separate dry oak copses from wet alder carr, often within a single glance. That small-scale alternation produces a large number of <b>transitional habitats</b>, and that is where the species richness lies. Oak and birch grow on the knolls, alder and willow in the hollows, and <b>woodcock, tawny owl and treecreeper</b> breed. Amphibians spawn in the wet part.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (amphibians and breeding birds), Oct\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Dusk \u2014 woodcock then make their roding flights above the wood.',
 'why': ['Name combines <b>snipe</b> and <b>horst</b>: rises in wet terrain.',
         '<b>Micro-relief</b> of half a metre separates dry from wet.',
         'Many <b>transitional habitats</b> on a small scale.',
         'Roding <b>woodcock</b> above the wood in spring.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Amphibians</b> spawn in the wet hollows.',
          '<span class="months">Mar\u2013May</span> \U0001f426 <b>Woodcock</b> roding at dusk above the wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tawny owl and treecreeper</b> breed.',
          '<span class="months">Oct\u2013Nov</span> \U0001f344 <b>Fungi</b> on the damp woodland floor.'],
 'wild': ['\U0001f426 Woodcock \u00b7 Tawny owl \u00b7 Treecreeper', '\U0001f438 Common frog \u00b7 Smooth newt', '\U0001f333 Oak \u00b7 Birch \u00b7 Alder \u00b7 Willow', '\U0001f344 Moisture-loving fungi', '\U0001f98c Roe deer'],
 'trail': ['Park at <b>Wezup</b>; narrow paths through the site.',
           'Note the <b>height difference</b>: half a metre changes everything.',
           'Come at <b>dusk in March</b> for the roding woodcock.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Wet in the hollows \u00b7 \u26a0\ufe0f Small site, easily disturbed'
}))

C.append(mk.card(1349, 'Wezup', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Esdorp \u00b7 brink, essen en houtwallen', 'list 36 \u00b7 no. 68'],
 'loc': '\U0001f4cd Het dorp Wezup bij Zweeloo \u00b7 Esdorp \u00b7 Klein',
 'desc': '<b>Wezup</b> is een klein esdorp met een gaaf bewaarde <b>brink</b> \u2014 de open, met eiken beplante ruimte in het hart van het dorp. De brink is misschien wel het meest onbegrepen onderdeel van het Drentse dorp: het was geen dorpsplein voor de gezelligheid maar een <b>functionele veeruimte</b>, waar het vee \u2019s ochtends werd verzameld voordat de herder het naar de heide dreef, en waar het \u2019s avonds terugkeerde. De eiken die er staan waren daarbij geen versiering maar leverden <b>schaduw voor het vee</b> en eikels als varkensvoer. Rond het dorp liggen de es, houtwallen en enkele natte laagtes. In de eeuwenoude brinkeiken \u2014 vaak de dikste bomen van de wijde omgeving \u2014 broeden <b>holenduif, spreeuw en boomklever</b>, en er leven <b>vleermuizen</b> in de holtes.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (broedvogels in de brinkeiken), okt\u2013nov (herfstkleur en eikels)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 vleermuizen komen dan uit de brinkeiken.',
 'why': ['Gaaf bewaarde <b>brink</b> in het hart van het dorp.',
         'De brink was een <b>functionele veeruimte</b>, geen dorpsplein.',
         'Brinkeiken leverden <b>schaduw en eikels</b>, geen versiering.',
         'Eeuwenoude eiken met <b>holenduif, spreeuw en vleermuizen</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Holenduif en spreeuw</b> in de boomholtes.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Boomklever</b> roept vanaf de brinkeiken.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> verlaten de holtes bij schemer.',
          '<span class="months">Okt\u2013Nov</span> \U0001f330 <b>Eikels</b> vallen \u2014 gaaien leggen voorraden aan.'],
 'wild': ['\U0001f426 Holenduif \u00b7 Spreeuw \u00b7 Boomklever', '\U0001f987 Gewone dwergvleermuis \u00b7 Rosse vleermuis', '\U0001f426 Gaai \u00b7 Grote bonte specht', '\U0001f333 Eeuwenoude brinkeiken', '\U0001f989 Steenuil'],
 'trail': ['Parkeren aan de <b>brink</b> van Wezup; zandwegen naar de es.',
           'Bekijk de <b>brinkeiken</b> \u2014 let op holtes en spechtengaten.',
           'Combineer met de <b>Sniphorsten</b> vlakbij.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historische brink \u00b7 \u26a0\ufe0f Particulier erf respecteren'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Es village \u00b7 village green, open fields and hedgebanks', 'list 36 \u00b7 no. 68'],
 'loc': '\U0001f4cd The village of Wezup near Zweeloo \u00b7 Es village \u00b7 Small',
 'desc': '<b>Wezup</b> is a small es village with a well-preserved <b>brink</b> \u2014 the open, oak-planted space at the heart of the village. The brink may be the most misunderstood element of the Drenthe village: it was not a square for socialising but a <b>functional livestock space</b>, where cattle were gathered in the morning before the herdsman drove them to the heath, and where they returned in the evening. The oaks standing there were no decoration but provided <b>shade for the livestock</b> and acorns as pig fodder. Around the village lie the es, hedgebanks and a few wet hollows. In the centuries-old brink oaks \u2014 often the thickest trees for miles \u2014 <b>stock dove, starling and nuthatch</b> breed, and <b>bats</b> live in the cavities.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (birds breeding in the brink oaks), Oct\u2013Nov (autumn colour and acorns)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats then emerge from the brink oaks.',
 'why': ['Well-preserved <b>brink</b> at the heart of the village.',
         'The brink was a <b>functional livestock space</b>, not a village square.',
         'Brink oaks provided <b>shade and acorns</b>, not decoration.',
         'Centuries-old oaks with <b>stock dove, starling and bats</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Stock dove and starling</b> in the tree cavities.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Nuthatch</b> calls from the brink oaks.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> leave the cavities at dusk.',
          '<span class="months">Oct\u2013Nov</span> \U0001f330 <b>Acorns</b> fall \u2014 jays lay in stores.'],
 'wild': ['\U0001f426 Stock dove \u00b7 Starling \u00b7 Nuthatch', '\U0001f987 Common pipistrelle \u00b7 Noctule', '\U0001f426 Jay \u00b7 Great spotted woodpecker', '\U0001f333 Centuries-old brink oaks', '\U0001f989 Little owl'],
 'trail': ['Park on the <b>brink</b> of Wezup; sandy tracks to the es.',
           'Study the <b>brink oaks</b> \u2014 look for cavities and woodpecker holes.',
           'Combine with the nearby <b>Sniphorsten</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic village green \u00b7 \u26a0\ufe0f Respect private yards'
}))

mk.insert(C, '1344')
mk.progress(1349)
mk.check()
