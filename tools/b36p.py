# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1355, 'De Stroeten', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Beekdal \u00b7 natte graslanden en houtwallen', 'list 36 \u00b7 no. 74'],
 'loc': '\U0001f4cd Bij Oosterhesselen \u00b7 Beekdalgraslanden \u00b7 Middelgroot',
 'desc': '<b>De Stroeten</b> is een beekdalgebied bij Oosterhesselen, en de naam is een oude meervoudsvorm van <b>stroet</b> \u2014 een streekwoord voor moerassig, met struweel begroeid laagland. Zulke woorden zijn zelf al informatie: waar een gebied een naam draagt die \u2018drassig struikgebied\u2019 betekent, weet je dat het nooit goed bruikbaar bouwland is geweest. Het dal is doorsneden met <b>houtwallen en elzensingels</b> die de percelen scheidden, en het beheer is er nu op gericht het water langer vast te houden. Waar dat lukt, verschijnen de karakteristieke soorten van natte schraallanden weer: <b>echte koekoeksbloem, blauwe knoop en gevlekte orchis</b>. In de singels broeden <b>geelgors en grasmus</b>, en boven het dal jaagt de <b>bruine kiekendief</b> die in de ruigere delen nestelt.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (schraallandflora), apr\u2013jun (weidevogels en zang)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 en let op de kiekendief boven het dal.',
 'why': ['<b>Stroet</b> = drassig struikgebied \u2014 de naam verraadt de bodem.',
         'Nooit bruikbaar als bouwland, en daardoor <b>bewaard</b>.',
         'Doorsneden met <b>houtwallen en elzensingels</b>.',
         'Vernatting brengt <b>blauwe knoop en gevlekte orchis</b> terug.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Echte koekoeksbloem</b> in de natte percelen.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Gevlekte orchis</b> bloeit.',
          '<span class="months">Mei\u2013Jul</span> \U0001f985 <b>Bruine kiekendief</b> jaagt boven het dal.',
          '<span class="months">Aug\u2013Sep</span> \U0001f33c <b>Blauwe knoop</b> trekt late vlinders.'],
 'wild': ['\U0001f33c Echte koekoeksbloem \u00b7 Blauwe knoop \u00b7 Gevlekte orchis', '\U0001f985 Bruine kiekendief \u00b7 Torenvalk', '\U0001f426 Geelgors \u00b7 Grasmus \u00b7 Watersnip', '\U0001f98b Vlinders op blauwe knoop', '\U0001f333 Els \u00b7 Eik \u00b7 Wilg'],
 'trail': ['Parkeren bij <b>Oosterhesselen</b>; paden langs de singels.',
           'Combineer met de <b>Geeserstroom</b> in dezelfde streek.',
           'Draag <b>waterdicht schoeisel</b> \u2014 het dal is nat.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Nat \u00b7 \u26a0\ufe0f Broedgebied \u2014 blijf op de paden'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Brook valley \u00b7 wet grasslands and hedgebanks', 'list 36 \u00b7 no. 74'],
 'loc': '\U0001f4cd Near Oosterhesselen \u00b7 Brook-valley grasslands \u00b7 Medium-sized',
 'desc': '<b>De Stroeten</b> is a brook-valley area near Oosterhesselen, and the name is an old plural of <b>stroet</b> \u2014 a regional word for boggy lowland grown over with scrub. Such words are information in themselves: where an area bears a name meaning \u2018boggy scrubland\u2019, you know it was never usable arable. The valley is cut through with <b>hedgebanks and alder lines</b> that separated the plots, and management now aims to hold water longer. Where that succeeds, the characteristic species of wet poor grassland reappear: <b>ragged robin, devil\u2019s-bit scabious and heath spotted orchid</b>. <b>Yellowhammer and whitethroat</b> breed in the tree lines, and the <b>marsh harrier</b> that nests in the rougher parts hunts above the valley.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (poor-grassland flora), Apr\u2013Jun (meadow birds and song)<br>\n    <b>Best time of day:</b> Early morning \u2014 and watch for the harrier above the valley.',
 'why': ['<b>Stroet</b> = boggy scrubland \u2014 the name betrays the soil.',
         'Never usable as arable, and therefore <b>preserved</b>.',
         'Cut through with <b>hedgebanks and alder lines</b>.',
         'Rewetting brings back <b>devil\u2019s-bit scabious and spotted orchid</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Ragged robin</b> in the wet parcels.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Heath spotted orchid</b> in flower.',
          '<span class="months">May\u2013Jul</span> \U0001f985 <b>Marsh harrier</b> hunts above the valley.',
          '<span class="months">Aug\u2013Sep</span> \U0001f33c <b>Devil\u2019s-bit scabious</b> draws late butterflies.'],
 'wild': ['\U0001f33c Ragged robin \u00b7 Devil\u2019s-bit scabious \u00b7 Heath spotted orchid', '\U0001f985 Marsh harrier \u00b7 Kestrel', '\U0001f426 Yellowhammer \u00b7 Whitethroat \u00b7 Snipe', '\U0001f98b Butterflies on scabious', '\U0001f333 Alder \u00b7 Oak \u00b7 Willow'],
 'trail': ['Park at <b>Oosterhesselen</b>; paths along the tree lines.',
           'Combine with the <b>Geeserstroom</b> in the same district.',
           'Wear <b>waterproof footwear</b> \u2014 the valley is wet.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Wet \u00b7 \u26a0\ufe0f Breeding ground \u2014 keep to the paths'
}, card_class='card water'))

C.append(mk.card(1356, 'De Klencke', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Landgoed \u00b7 havezate, lanen en oud bos', 'list 36 \u00b7 no. 75'],
 'loc': '\U0001f4cd Bij Oosterhesselen \u00b7 Landgoed met havezate \u00b7 Groot',
 'desc': '<b>De Klencke</b> is een van de weinige Drentse <b>havezaten</b> die nog met hun landgoed intact zijn. Een havezate was in Drenthe en Overijssel een adellijk huis waarvan de eigenaar recht had op een zetel in de <b>Ridderschap</b>, het adellijke bestuurscollege van de provincie \u2014 een status die aan het huis kleefde, niet aan de persoon. Om die reden werden havezaten zorgvuldig in stand gehouden en niet zomaar verkocht of gesloopt, en dat verklaart waarom hier nog eeuwenoude <b>beukenlanen</b> en oud loofbos staan. Ecologisch is het landgoed waardevol door zijn <b>oude bomen</b>: die ontwikkelen holtes, losse schors en dood hout, en dat trekt vleermuizen, holenbroeders en houtkevers aan. Er broeden <b>bosuil, boomklever en appelvink</b>, en in de kelders van bijgebouwen overwinteren <b>vleermuizen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (stinzenflora en zang), sep\u2013nov (paddenstoelen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Ochtend voor vogels; schemer voor vleermuizen langs de lanen.',
 'why': ['Zeldzame intacte <b>havezate</b> met bijbehorend landgoed.',
         'Havezate-status gaf recht op een zetel in de <b>Ridderschap</b>.',
         'Daardoor eeuwenlang <b>zorgvuldig in stand gehouden</b>.',
         '<b>Oude bomen</b> met holtes, losse schors en dood hout.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Stinzenflora</b> onder de oude bomen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Bosuil en appelvink</b> broeden.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> jagen langs de beukenlanen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op dood beukenhout.'],
 'wild': ['\U0001f426 Bosuil \u00b7 Boomklever \u00b7 Appelvink', '\U0001f987 Rosse vleermuis \u00b7 Watervleermuis \u00b7 Grootoorvleermuis', '\U0001f333 Eeuwenoude beuken en eiken', '\U0001f33c Stinzenflora \u00b7 Bosanemoon', '\U0001f344 Zwavelzwam \u00b7 Tonderzwam'],
 'trail': ['Parkeren bij <b>De Klencke</b>; lanen en bospaden zijn opengesteld.',
           'Volg de <b>beukenlanen</b> \u2014 daar zitten de oudste bomen.',
           'Het <b>huis zelf</b> is particulier; respecteer de afzettingen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3f0 Historische havezate \u00b7 \U0001f9ed Natuurmonumenten'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Estate \u00b7 manor, avenues and ancient woodland', 'list 36 \u00b7 no. 75'],
 'loc': '\U0001f4cd Near Oosterhesselen \u00b7 Estate with manor house \u00b7 Large',
 'desc': '<b>De Klencke</b> is one of the few Drenthe <b>havezaten</b> still intact with its estate. In Drenthe and Overijssel a havezate was a noble house whose owner had the right to a seat in the <b>Ridderschap</b>, the province\u2019s noble governing body \u2014 a status attached to the house, not to the person. For that reason havezaten were carefully maintained and not casually sold or demolished, which explains why centuries-old <b>beech avenues</b> and ancient broadleaf woodland still stand here. Ecologically the estate is valuable for its <b>old trees</b>: they develop cavities, loose bark and deadwood, and that attracts bats, hole-nesters and wood beetles. <b>Tawny owl, nuthatch and hawfinch</b> breed here, and <b>bats</b> hibernate in the cellars of the outbuildings.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (stinzen flora and song), Sep\u2013Nov (fungi and autumn colour)<br>\n    <b>Best time of day:</b> Morning for birds; dusk for bats along the avenues.',
 'why': ['Rare intact <b>havezate</b> with its accompanying estate.',
         'Havezate status conferred a seat in the <b>Ridderschap</b>.',
         'It was therefore <b>carefully maintained</b> for centuries.',
         '<b>Old trees</b> with cavities, loose bark and deadwood.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Stinzen flora</b> beneath the old trees.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tawny owl and hawfinch</b> breed.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> hunt along the beech avenues.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on dead beech wood.'],
 'wild': ['\U0001f426 Tawny owl \u00b7 Nuthatch \u00b7 Hawfinch', '\U0001f987 Noctule \u00b7 Daubenton\u2019s bat \u00b7 Brown long-eared bat', '\U0001f333 Centuries-old beeches and oaks', '\U0001f33c Stinzen flora \u00b7 Wood anemone', '\U0001f344 Chicken-of-the-woods \u00b7 Tinder fungus'],
 'trail': ['Park at <b>De Klencke</b>; avenues and woodland paths are open.',
           'Follow the <b>beech avenues</b> \u2014 the oldest trees stand there.',
           'The <b>house itself</b> is private; respect the barriers.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3f0 Historic manor \u00b7 \U0001f9ed Natuurmonumenten'
}, card_class='card estate'))

C.append(mk.card(1357, 'Lage Veen', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Veenrestant \u00b7 natte heide en veenmos', 'list 36 \u00b7 no. 76'],
 'loc': '\U0001f4cd Bij Dalen en Wachtum \u00b7 Veenrestant \u00b7 Klein',
 'desc': 'Het <b>Lage Veen</b> is een klein restant van het hoogveen dat ooit grote delen van Zuidoost-Drenthe bedekte. Het contrast met de omgeving is scherp: rondom liggen de <b>veenkoloni\u00ebn</b>, waar het veen tot op de zandondergrond is afgegraven en waar nu akkerbouw op de resterende dalgrond plaatsvindt. Hier bleef een stukje liggen, meestal omdat het te nat, te afgelegen of eigendomsrechtelijk te ingewikkeld was. Het herstel van zo\u2019n restant is moeilijk, want hoogveen groeit alleen bij een <b>permanent hoge waterstand</b> die uitsluitend uit regenwater bestaat \u2014 en een klein restant tussen ontwaterde akkers lekt aan alle kanten. Met dammen en peilverhoging lukt het hier toch: <b>veenmos, veenpluis en kleine veenbes</b> groeien weer, en er leven <b>heikikker en veenmosorchis</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (veenvegetatie en libellen), apr (heikikkers)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 dauw op het veenmos maakt de structuur zichtbaar.',
 'why': ['Klein <b>hoogveenrestant</b> midden tussen de veenkoloni\u00ebn.',
         'Hoogveen groeit alleen bij een waterstand van <b>puur regenwater</b>.',
         'Kleine restanten <b>lekken</b> naar de ontwaterde omgeving.',
         'Herstel met dammen: <b>veenmos en kleine veenbes</b> keren terug.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Heikikkers</b> paaien in de slenken.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33f <b>Veenpluis</b> met witte pluizen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Veenlibellen</b> boven de slenken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Dopheide</b> bloeit op de bulten.'],
 'wild': ['\U0001f438 Heikikker', '\U0001f33f Veenmos \u00b7 Veenpluis \u00b7 Kleine veenbes', '\U0001f33c Veenmosorchis \u00b7 Ronde zonnedauw', '\U0001f9a0 Venwitsnuitlibel \u00b7 Noordse witsnuitlibel', '\U0001f338 Dopheide'],
 'trail': ['Parkeren bij <b>Dalen</b>; smal pad langs de rand van het veen.',
           'Betreed het <b>veenmos niet</b> \u2014 het is drijvend en breekbaar.',
           'Klein gebied \u2014 combineer met <b>Wachtum</b> en <b>Dalerpeel</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Drijvend veenmos \u2014 nooit betreden \u00b7 \U0001f97e Nat'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Bog remnant \u00b7 wet heath and sphagnum', 'list 36 \u00b7 no. 76'],
 'loc': '\U0001f4cd Near Dalen and Wachtum \u00b7 Bog remnant \u00b7 Small',
 'desc': 'The <b>Lage Veen</b> is a small remnant of the raised bog that once covered large parts of south-east Drenthe. The contrast with the surroundings is sharp: all around lie the <b>peat colonies</b>, where the peat was dug down to the sandy subsoil and arable farming now takes place on the residual soil. Here a fragment survived, usually because it was too wet, too remote or too complicated in terms of ownership. Restoring such a remnant is difficult, because raised bog grows only with a <b>permanently high water table</b> consisting exclusively of rainwater \u2014 and a small remnant amid drained fields leaks on all sides. With dams and raised levels it nevertheless works here: <b>sphagnum, cottongrass and small cranberry</b> grow again, and <b>moor frog and fen orchid</b> live here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (bog vegetation and dragonflies), Apr (moor frogs)<br>\n    <b>Best time of day:</b> Morning \u2014 dew on the sphagnum reveals its structure.',
 'why': ['Small <b>raised-bog remnant</b> amid the peat colonies.',
         'Raised bog grows only on a water table of <b>pure rainwater</b>.',
         'Small remnants <b>leak</b> into the drained surroundings.',
         'Restoration with dams: <b>sphagnum and small cranberry</b> return.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Moor frogs</b> spawn in the hollows.',
          '<span class="months">May\u2013Jun</span> \U0001f33f <b>Cottongrass</b> with white tufts.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Bog dragonflies</b> above the hollows.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Cross-leaved heath</b> flowers on the hummocks.'],
 'wild': ['\U0001f438 Moor frog', '\U0001f33f Sphagnum \u00b7 Cottongrass \u00b7 Small cranberry', '\U0001f33c Fen orchid \u00b7 Round-leaved sundew', '\U0001f9a0 White-faced darter \u00b7 Dark whiteface', '\U0001f338 Cross-leaved heath'],
 'trail': ['Park at <b>Dalen</b>; a narrow path along the edge of the bog.',
           '<b>Do not walk on the sphagnum</b> \u2014 it floats and breaks.',
           'Small site \u2014 combine with <b>Wachtum</b> and <b>Dalerpeel</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Floating sphagnum \u2014 never walk on it \u00b7 \U0001f97e Wet'
}, card_class='card water'))

C.append(mk.card(1358, 'Falieberg', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Zandrug \u00b7 bos en heiderestant', 'list 36 \u00b7 no. 77'],
 'loc': '\U0001f4cd Bij Dalen \u00b7 Zandrug met bos \u00b7 Klein',
 'desc': 'De <b>Falieberg</b> is een dekzandrug bij Dalen met een naam die tot de verbeelding spreekt: <i>falie</i> was een lange sluier of doek die vrouwen vroeger over hoofd en schouders droegen, en de naam zou verwijzen naar de vorm van de rug of naar het mistgordijn dat er in de ochtend overheen ligt. Zulke ruggen zijn ontstaan in de laatste ijstijd, toen de wind over een <b>vegetatieloze toendra</b> vrij spel had en zand in langgerekte banen afzette. Ze zijn zelden hoger dan een paar meter, maar bepalen wel volledig waar het droog is en waar niet \u2014 en dus waar men vroeger bouwde en boerde. De rug is nu begroeid met bos en draagt een klein heiderestant op de top. Er broeden <b>boomleeuwerik en gekraagde roodstaart</b>, en op de zandige plekken graven <b>bijen en wespen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels en graafbijen), aug\u2013sep (heiderestant in bloei)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 bij mist zie je waar de naam vandaan komt.',
 'why': ['<b>Dekzandrug</b> uit de laatste ijstijd, gevormd op vegetatieloze toendra.',
         'Enkele meters hoog, maar bepalend voor <b>waar het droog is</b>.',
         'Klein <b>heiderestant</b> op de top.',
         'Zandige plekken met <b>graafbijen en wespen</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Boomleeuwerik</b> zingt boven de rug.',
          '<span class="months">Mei\u2013Jul</span> \U0001f41d <b>Graafbijen</b> nestelen in het open zand.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> op de top.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> onder de bomen.'],
 'wild': ['\U0001f426 Boomleeuwerik \u00b7 Gekraagde roodstaart', '\U0001f41d Graafbijen \u00b7 Graafwespen', '\U0001f98e Levendbarende hagedis', '\U0001f338 Struikheide \u00b7 Buntgras', '\U0001f333 Eik \u00b7 Berk \u00b7 Grove den'],
 'trail': ['Parkeren bij <b>Dalen</b>; paden over de rug.',
           'Kom bij <b>ochtendmist</b> \u2014 dan verklaart de naam zichzelf.',
           'Klein gebied \u2014 combineer met <b>Lage Veen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbaar heiderestant \u2014 blijf op de paden'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Sand ridge \u00b7 woodland and heath remnant', 'list 36 \u00b7 no. 77'],
 'loc': '\U0001f4cd Near Dalen \u00b7 Sand ridge with woodland \u00b7 Small',
 'desc': 'The <b>Falieberg</b> is a cover-sand ridge near Dalen with an evocative name: a <i>falie</i> was a long veil or cloth that women once wore over head and shoulders, and the name is said to refer to the shape of the ridge or to the curtain of mist that lies over it in the morning. Such ridges formed in the last ice age, when the wind had free rein over a <b>vegetationless tundra</b> and deposited sand in elongated bands. They are seldom more than a few metres high, yet they entirely determine where the ground is dry and where it is not \u2014 and hence where people once built and farmed. The ridge is now wooded and carries a small heath remnant on top. <b>Woodlark and redstart</b> breed here, and <b>bees and wasps</b> burrow in the sandy patches.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds and mining bees), Aug\u2013Sep (heath remnant in flower)<br>\n    <b>Best time of day:</b> Early morning \u2014 in mist you see where the name comes from.',
 'why': ['<b>Cover-sand ridge</b> from the last ice age, formed on vegetationless tundra.',
         'A few metres high, yet decisive for <b>where the ground is dry</b>.',
         'Small <b>heath remnant</b> on the summit.',
         'Sandy patches with <b>mining bees and wasps</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f426 <b>Woodlark</b> sings above the ridge.',
          '<span class="months">May\u2013Jul</span> \U0001f41d <b>Mining bees</b> nest in the open sand.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Ling</b> on the summit.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> beneath the trees.'],
 'wild': ['\U0001f426 Woodlark \u00b7 Redstart', '\U0001f41d Mining bees \u00b7 Digger wasps', '\U0001f98e Common lizard', '\U0001f338 Ling \u00b7 Grey hair-grass', '\U0001f333 Oak \u00b7 Birch \u00b7 Scots pine'],
 'trail': ['Park at <b>Dalen</b>; paths over the ridge.',
           'Come in <b>morning mist</b> \u2014 the name then explains itself.',
           'Small site \u2014 combine with <b>Lage Veen</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile heath remnant \u2014 keep to the paths'
}, card_class='card dune'))

C.append(mk.card(1359, 'Steenberger Oosterveld', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Heideveld \u00b7 natte heide en vennen', 'list 36 \u00b7 no. 78'],
 'loc': '\U0001f4cd Bij Dalerveen en Steenbergen \u00b7 Heideveld \u00b7 Middelgroot',
 'desc': 'Het <b>Steenberger Oosterveld</b> is een heideveld ten oosten van het dorp Steenbergen \u2014 de naam volgt de oude, praktische logica waarmee marken hun gronden benoemden: het <i>oosterveld</i> was simpelweg het gemeenschappelijke veld aan de oostkant van het dorp. Zulke namen komen door heel Drenthe voor en vormen samen een soort kaart in woorden. Het veld bestaat uit <b>vochtige en droge heide</b> met enkele vennen, en het is grotendeels bewaard gebleven omdat de bodem er te nat en te leemhoudend was voor rendabele ontginning. Op de natte delen groeit <b>klokjesgentiaan</b>, en daarmee vliegt er het <b>gentiaanblauwtje</b> \u2014 een vlinder die zijn rupsen door <b>knoopmieren</b> laat grootbrengen, die de rups voor eigen broed aanzien en hem in het nest voeren.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jul\u2013aug</b> (klokjesgentiaan en gentiaanblauwtje), aug\u2013sep (heidebloei)<br>\n    <b>Beste tijd van de dag:</b> Warme ochtend in juli \u2014 het gentiaanblauwtje vliegt dan.',
 'why': ['Naam volgt de oude <b>markelogica</b>: het veld ten oosten van het dorp.',
         'Bewaard omdat de bodem <b>te nat en leemhoudend</b> was.',
         '<b>Klokjesgentiaan</b> op de vochtige delen.',
         '<b>Gentiaanblauwtje</b>: rupsen worden door knoopmieren grootgebracht.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Roodborsttapuit</b> en boomleeuwerik broeden.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33c <b>Klokjesgentiaan</b> bloeit diepblauw.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Gentiaanblauwtje</b> legt eitjes op de knoppen.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> kleurt het veld paars.'],
 'wild': ['\U0001f98b Gentiaanblauwtje \u00b7 Heideblauwtje', '\U0001f41c Knoopmieren (gastheer van de rupsen)', '\U0001f33c Klokjesgentiaan \u00b7 Beenbreek', '\U0001f426 Roodborsttapuit \u00b7 Boomleeuwerik', '\U0001f338 Struikheide \u00b7 Dopheide'],
 'trail': ['Parkeren bij <b>Steenbergen</b>; paden over het veld.',
           'Zoek in juli de <b>vochtige laagtes</b> voor gentiaan en vlinder.',
           'Combineer met <b>Dalerpeel</b> en <b>Lage Veen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbare natte heide \u2014 blijf op de paden'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Heathland \u00b7 wet heath and pools', 'list 36 \u00b7 no. 78'],
 'loc': '\U0001f4cd Near Dalerveen and Steenbergen \u00b7 Heathland \u00b7 Medium-sized',
 'desc': 'The <b>Steenberger Oosterveld</b> is a heath east of the village of Steenbergen \u2014 the name follows the old, practical logic with which commons associations named their grounds: the <i>oosterveld</i> was simply the common field on the east side of the village. Such names occur throughout Drenthe and together form a kind of map in words. The field consists of <b>wet and dry heath</b> with a few pools, and it has largely survived because the soil was too wet and too loamy for profitable reclamation. <b>Marsh gentian</b> grows on the wet parts, and with it flies the <b>alcon blue</b> \u2014 a butterfly that has its caterpillars raised by <b>Myrmica ants</b>, which mistake the caterpillar for their own brood and feed it in the nest.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jul\u2013Aug</b> (marsh gentian and alcon blue), Aug\u2013Sep (heather)<br>\n    <b>Best time of day:</b> Warm morning in July \u2014 when the alcon blue flies.',
 'why': ['Name follows the old <b>commons logic</b>: the field east of the village.',
         'Survived because the soil was <b>too wet and loamy</b>.',
         '<b>Marsh gentian</b> on the damp parts.',
         '<b>Alcon blue</b>: caterpillars are raised by Myrmica ants.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Stonechat</b> and woodlark breed.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33c <b>Marsh gentian</b> flowers deep blue.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Alcon blue</b> lays eggs on the buds.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Ling</b> turns the field purple.'],
 'wild': ['\U0001f98b Alcon blue \u00b7 Silver-studded blue', '\U0001f41c Myrmica ants (host of the caterpillars)', '\U0001f33c Marsh gentian \u00b7 Bog asphodel', '\U0001f426 Stonechat \u00b7 Woodlark', '\U0001f338 Ling \u00b7 Cross-leaved heath'],
 'trail': ['Park at <b>Steenbergen</b>; paths across the heath.',
           'In July seek the <b>damp hollows</b> for gentian and butterfly.',
           'Combine with <b>Dalerpeel</b> and <b>Lage Veen</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile wet heath \u2014 keep to the paths'
}, card_class='card dune'))

mk.insert(C, '1354')
mk.progress(1359)
mk.check()
