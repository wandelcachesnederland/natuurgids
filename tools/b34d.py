# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1245, 'Sellinger Bossen', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Bosgebied \u00b7 ontginningsbos met vennen', 'list 34 \u00b7 no. 22'],
 'loc': '\U0001f4cd Bij Sellingen, Westerwolde \u00b7 Boscomplex \u00b7 Ruim 500 ha',
 'desc': 'De <b>Sellinger Bossen</b> vormen het grootste boscomplex van Groningen \u2014 een provincie die verder vrijwel boomloos is, wat dit gebied meteen bijzonder maakt. Het bos is in de jaren twintig en dertig aangeplant op afgegraven veen en arme zandgrond, opnieuw grotendeels als <b>werkverschaffing</b>. Wie er nu loopt merkt weinig van die strenge oorsprong: door decennia van omvormingsbeheer is een <b>gevarieerd loof- en naaldbos</b> ontstaan met open plekken, lanen van beuk en eik, en verspreide <b>vennen en poelen</b>. Juist die vennen zijn de parels: door hun voedselarme, zure water leven er <b>heikikker, kleine watersalamander en zeldzame libellen</b> als de venwitsnuitlibel. In het bos zelf broeden <b>havik, buizerd en zwarte specht</b>, en de boommarter is er inmiddels een vaste bewoner. Het gebied grenst naadloos aan de Braamberg en het Bourtangerveen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (libellen, amfibie\u00ebn en broedvogels), okt\u2013nov (paddenstoelen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Zonnige late ochtend bij de vennen voor libellen.',
 'why': ['Het <b>grootste boscomplex van Groningen</b> in een boomarme provincie.',
         'Verspreide <b>vennen</b> met venwitsnuitlibel en heikikker.',
         'Van strak <b>werkverschaffingsbos</b> naar gevarieerd gemengd bos.',
         '<b>Havik, zwarte specht en boommarter</b> als vaste broedvogels.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Heikikker</b> \u2014 blauwe mannetjes in de vennen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f9a0 <b>Venwitsnuitlibel</b> en andere zeldzame libellen boven het water.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Zwarte specht</b> roffelt in de oudere vakken.',
          '<span class="months">Okt\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> \u2014 een van de rijkste plekken van de provincie.'],
 'wild': ['\U0001f426 Havik \u00b7 Zwarte specht', '\U0001f9a1 Boommarter', '\U0001f438 Heikikker', '\U0001f9a0 Venwitsnuitlibel', '\U0001f33f Veenmos \u00b7 Pijpenstrootje'],
 'trail': ['Parkeren aan de <b>Sellingerbeetse</b> of bij het dorp <b>Sellingen</b>.',
           'Meerdere <b>gemarkeerde rondwandelingen</b> en een ruiterroutenetwerk.',
           'Combineer met de <b>Braamberg</b> en het <b>Bourtangerveen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Vennen kwetsbaar \u2014 blijf op de paden \u00b7 \U0001f6b6 Meerdere routes'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Woodland \u00b7 reclamation forest with pools', 'list 34 \u00b7 no. 22'],
 'loc': '\U0001f4cd Near Sellingen, Westerwolde \u00b7 Forest complex \u00b7 Over 500 ha',
 'desc': 'The <b>Sellinger Bossen</b> form the largest forest complex in Groningen \u2014 a province that is otherwise virtually treeless, which makes this area immediately remarkable. The wood was planted in the 1920s and 1930s on cut-over peat and poor sandy soil, again largely as a <b>relief work scheme</b>. Walking here now, you notice little of that severe origin: decades of conversion management have produced a <b>varied broadleaved and coniferous wood</b> with clearings, avenues of beech and oak, and scattered <b>pools and heath ponds</b>. Those pools are the jewels: their nutrient-poor, acid water supports <b>moor frog, smooth newt and rare dragonflies</b> such as the yellow-spotted whiteface. In the wood itself <b>goshawk, buzzard and black woodpecker</b> breed, and the pine marten is now a permanent resident. The area adjoins the Braamberg and the Bourtangerveen seamlessly.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (dragonflies, amphibians and breeding birds), Oct\u2013Nov (fungi and autumn colour)<br>\n    <b>Best time of day:</b> Sunny late morning at the pools for dragonflies.',
 'why': ['The <b>largest forest complex in Groningen</b>, in a province short of trees.',
         'Scattered <b>heath pools</b> with yellow-spotted whiteface and moor frog.',
         'From regimented <b>relief-scheme plantation</b> to varied mixed woodland.',
         '<b>Goshawk, black woodpecker and pine marten</b> as resident breeders.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Moor frog</b> \u2014 blue males in the pools.',
          '<span class="months">May\u2013Jul</span> \U0001f9a0 <b>Yellow-spotted whiteface</b> and other rare dragonflies over the water.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Black woodpecker</b> drumming in the older compartments.',
          '<span class="months">Oct\u2013Nov</span> \U0001f344 <b>Fungi</b> \u2014 one of the richest spots in the province.'],
 'wild': ['\U0001f426 Goshawk \u00b7 Black woodpecker', '\U0001f9a1 Pine marten', '\U0001f438 Moor frog', '\U0001f9a0 Yellow-spotted whiteface', '\U0001f33f Sphagnum \u00b7 Purple moor-grass'],
 'trail': ['Park at <b>Sellingerbeetse</b> or in the village of <b>Sellingen</b>.',
           'Several <b>waymarked circular walks</b> and a bridleway network.',
           'Combine with the <b>Braamberg</b> and the <b>Bourtangerveen</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Pools are fragile \u2014 keep to the paths \u00b7 \U0001f6b6 Several routes'
}))

C.append(mk.card(1246, 'Bourtangerveen', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Hoogveenrestant \u00b7 grensoverschrijdend', 'list 34 \u00b7 no. 23'],
 'loc': '\U0001f4cd Bij Sellingen en de Duitse grens \u00b7 Hoogveenrelict \u00b7 Grensoverschrijdend gebied',
 'desc': 'Het <b>Bourtangerveen</b> was ooit het grootste aaneengesloten hoogveen van Noordwest-Europa: een veenkussen van zeker <b>duizend vierkante kilometer</b> dat zich uitstrekte van Groningen en Drenthe diep in Nedersaksen. Het was een ondoordringbare wildernis die eeuwenlang als natuurlijke grens en verdedigingslinie functioneerde \u2014 vandaar Bourtange. Van dat immense veen is minder dan een procent over. De Nederlandse resten bij Sellingen zijn klein maar cruciaal, en samen met het veel grotere Duitse <b>Bargerveen-Emsland</b>-complex vormen ze een grensoverschrijdend herstelproject. Het werk bestaat vooral uit <b>vernatten</b>: dammen aanleggen, sloten dempen, regenwater vasthouden. Waar dat lukt keert de <b>veenmoslaag</b> terug, en met haar <b>lavendelhei, veenbes en kleine veenbes</b>. Hoogveen groeit ongeveer \u00e9\u00e9n millimeter per jaar \u2014 herstel is hier een project van eeuwen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (veenflora en libellen), sep\u2013okt (kleuring van het veen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 nevel boven het veen en de meeste vogelactiviteit.',
 'why': ['Restant van het <b>grootste hoogveen van Noordwest-Europa</b>.',
         'Historische <b>natuurlijke grens</b> \u2014 vandaar de vesting Bourtange.',
         '<b>Grensoverschrijdend herstelproject</b> met Duitsland.',
         'Terugkerende <b>veenmoslaag</b> met lavendelhei en veenbes.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Geoorde fuut</b> op de vernatte plassen.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Lavendelhei</b> bloeit \u2014 kenmerkende roze belletjes.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Hoogveenglanslibel en venwitsnuitlibel</b> boven de slenken.',
          '<span class="months">Sep\u2013Okt</span> \U0001f341 <b>Veenkleuren</b> \u2014 rood veenmos en koperen pijpenstrootje.'],
 'wild': ['\U0001f426 Geoorde fuut \u00b7 Watersnip', '\U0001f9a0 Hoogveenglanslibel', '\U0001f438 Heikikker', '\U0001f33f Veenmos \u00b7 Lavendelhei \u00b7 Kleine veenbes', '\U0001f33e Eenarig wollegras'],
 'trail': ['Parkeren bij <b>Sellingen</b>; het veen ligt richting de Duitse grens.',
           '<b>Vlonderpaden</b> op de kwetsbaarste delen \u2014 verlaat ze niet.',
           'Aan Duitse zijde sluit het <b>Emsland-veencomplex</b> naadloos aan.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Zeer kwetsbaar hoogveen \u00b7 \U0001f97e Nat \u2014 laarzen'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Raised-bog remnant \u00b7 cross-border', 'list 34 \u00b7 no. 23'],
 'loc': '\U0001f4cd Near Sellingen and the German border \u00b7 Raised-bog relic \u00b7 Cross-border area',
 'desc': 'The <b>Bourtangerveen</b> was once the largest continuous raised bog in north-western Europe: a peat cushion of at least <b>a thousand square kilometres</b> stretching from Groningen and Drenthe deep into Lower Saxony. It was an impenetrable wilderness that for centuries served as a natural border and defensive line \u2014 hence Bourtange. Less than one per cent of that immense bog survives. The Dutch remnants near Sellingen are small but crucial, and together with the far larger German <b>Bargerveen-Emsland</b> complex they form a cross-border restoration project. The work consists mainly of <b>rewetting</b>: building dams, filling in ditches, holding rainwater. Where that succeeds the <b>sphagnum layer</b> returns, and with it <b>bog rosemary and cranberry</b>. Raised bog grows about <b>one millimetre a year</b> \u2014 restoration here is a project measured in centuries.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (bog flora and dragonflies), Sep\u2013Oct (autumn colouring of the bog)<br>\n    <b>Best time of day:</b> Early morning \u2014 mist over the bog and peak bird activity.',
 'why': ['Remnant of the <b>largest raised bog in north-western Europe</b>.',
         'Historic <b>natural frontier</b> \u2014 hence the fortress of Bourtange.',
         '<b>Cross-border restoration project</b> with Germany.',
         'Returning <b>sphagnum layer</b> with bog rosemary and cranberry.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f426 <b>Black-necked grebe</b> on the rewetted pools.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Bog rosemary</b> in flower \u2014 distinctive pink bells.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Bog hawker and whiteface dragonflies</b> above the hollows.',
          '<span class="months">Sep\u2013Oct</span> \U0001f341 <b>Bog colours</b> \u2014 red sphagnum and copper moor-grass.'],
 'wild': ['\U0001f426 Black-necked grebe \u00b7 Snipe', '\U0001f9a0 Bog dragonflies', '\U0001f438 Moor frog', '\U0001f33f Sphagnum \u00b7 Bog rosemary \u00b7 Small cranberry', '\U0001f33e Hare\u2019s-tail cottongrass'],
 'trail': ['Park at <b>Sellingen</b>; the bog lies towards the German border.',
           '<b>Boardwalks</b> on the most fragile sections \u2014 do not leave them.',
           'On the German side the <b>Emsland bog complex</b> adjoins seamlessly.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Very fragile raised bog \u00b7 \U0001f97e Wet \u2014 boots'
}, card_class='card water'))

C.append(mk.card(1247, 'Ter Apel', {
 'tags': ['Groningen \u00b7 Westerwolde', 'Kloosterlandschap \u00b7 oud bos en tuinen', 'list 34 \u00b7 no. 24'],
 'loc': '\U0001f4cd Ter Apel, Westerwolde \u00b7 Klooster met bos en tuinen \u00b7 Middelgroot',
 'desc': 'Het <b>klooster van Ter Apel</b>, gesticht in 1465 door de kruisheren, is het enige middeleeuwse plattelandsklooster in Nederland dat de beeldenstorm en de eeuwen daarna vrijwel gaaf heeft doorstaan. Het staat op een <b>zandrug midden in het veen</b> \u2014 een eiland van beschaving in een moeras, bereikbaar via \u00e9\u00e9n veenweg. Voor de natuurliefhebber is niet alleen het gebouw interessant maar vooral het omringende <b>kloosterbos</b>: omdat het al meer dan vijfhonderd jaar bos is, zonder ontginningsonderbreking, heeft het een <b>bodemflora</b> die je in aangeplante bossen nooit vindt. Hier groeien <b>eenbes, bosanemoon, gele dovenetel en daslook</b> \u2014 stuk voor stuk trage soorten die zich maar enkele meters per eeuw verspreiden en dus als <b>oud-bosindicatoren</b> gelden. De <b>kruidentuinen</b> bij het klooster zijn gereconstrueerd naar middeleeuws model, en de eeuwenoude <b>beuken en eiken</b> op het terrein herbergen vleermuizen en holenbroeders.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (voorjaarsflora op zijn mooist), jun\u2013aug (kloostertuinen in bloei)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend in april \u2014 stil bos, volle vogelzang, licht door het jonge blad.',
 'why': ['Enig gaaf bewaard <b>middeleeuws plattelandsklooster</b> (1465) van Nederland.',
         'Meer dan <b>vijfhonderd jaar boscontinu\u00efteit</b> \u2014 zeldzaam in Nederland.',
         '<b>Oud-bosindicatoren</b>: eenbes, daslook, gele dovenetel.',
         'Gereconstrueerde <b>middeleeuwse kruidentuinen</b>.'],
 'phen': ['<span class="months">Apr</span> \U0001f33c <b>Bosanemoon en daslook</b> \u2014 tapijten op de bosbodem.',
          '<span class="months">Apr\u2013Mei</span> \U0001f33f <b>Eenbes</b> bloeit, onopvallend maar veelzeggend.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Holenbroeders</b> in de oude beuken rond het klooster.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Kruidentuinen</b> op hun hoogtepunt.'],
 'wild': ['\U0001f987 Vleermuizen in kloostergebouwen', '\U0001f426 Boomklever \u00b7 Bosuil', '\U0001f33f Eenbes \u00b7 Daslook', '\U0001f33f Gele dovenetel \u00b7 Bosanemoon', '\U0001f333 Eeuwenoude beuken en eiken'],
 'trail': ['Parkeren bij het <b>Klooster Ter Apel</b> (museum, entree voor het gebouw).',
           'Het <b>kloosterbos en de tuinen</b> zijn vrij toegankelijk.',
           'Sluit aan op wandelroutes richting <b>Pagebos</b> en de Ruiten Aa.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Bos gratis, museum betaald \u00b7 \u26a0\ufe0f Kwetsbare voorjaarsflora \u2014 op de paden blijven \u00b7 \U0001f6b6 Kort'
}, {
 'tags': ['Groningen \u00b7 Westerwolde', 'Monastic landscape \u00b7 ancient woodland and gardens', 'list 34 \u00b7 no. 24'],
 'loc': '\U0001f4cd Ter Apel, Westerwolde \u00b7 Monastery with woodland and gardens \u00b7 Medium-sized',
 'desc': 'The <b>monastery of Ter Apel</b>, founded in 1465 by the Crosier friars, is the only medieval rural monastery in the Netherlands to have survived the iconoclasm and the following centuries almost intact. It stands on a <b>sand ridge in the middle of the bog</b> \u2014 an island of civilisation in a marsh, reached by a single peat road. For the naturalist it is not only the building that matters but above all the surrounding <b>monastery wood</b>: because it has been woodland for more than five hundred years, with no interruption for reclamation, it has a <b>ground flora</b> you never find in planted forests. Here grow <b>herb Paris, wood anemone, yellow archangel and ramsons</b> \u2014 all slow species that spread only a few metres per century and therefore count as <b>ancient woodland indicators</b>. The <b>herb gardens</b> by the monastery have been reconstructed on a medieval model, and the centuries-old <b>beeches and oaks</b> on the grounds shelter bats and hole-nesting birds.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (spring flora at its finest), Jun\u2013Aug (monastery gardens in flower)<br>\n    <b>Best time of day:</b> Early morning in April \u2014 quiet wood, full birdsong, light through the young leaves.',
 'why': ['The only intact <b>medieval rural monastery</b> (1465) in the Netherlands.',
         'More than <b>five hundred years of woodland continuity</b> \u2014 rare in this country.',
         '<b>Ancient woodland indicators</b>: herb Paris, ramsons, yellow archangel.',
         'Reconstructed <b>medieval herb gardens</b>.'],
 'phen': ['<span class="months">Apr</span> \U0001f33c <b>Wood anemone and ramsons</b> \u2014 carpets on the woodland floor.',
          '<span class="months">Apr\u2013May</span> \U0001f33f <b>Herb Paris</b> flowers, inconspicuous but telling.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Hole-nesting birds</b> in the old beeches around the monastery.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Herb gardens</b> at their peak.'],
 'wild': ['\U0001f987 Bats in the monastery buildings', '\U0001f426 Nuthatch \u00b7 Tawny owl', '\U0001f33f Herb Paris \u00b7 Ramsons', '\U0001f33f Yellow archangel \u00b7 Wood anemone', '\U0001f333 Centuries-old beeches and oaks'],
 'trail': ['Park at <b>Klooster Ter Apel</b> (museum, admission charged for the building).',
           'The <b>monastery wood and gardens</b> are freely accessible.',
           'Links to walking routes towards the <b>Pagebos</b> and the Ruiten Aa.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Woodland free, museum paid \u00b7 \u26a0\ufe0f Fragile spring flora \u2014 keep to the paths \u00b7 \U0001f6b6 Short'
}, card_class='card estate'))

mk.insert(C, '1244')
mk.progress(1247)
mk.check()
