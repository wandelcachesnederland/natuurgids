# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1560, 'Buitenwaarden Wijhe', {
 'tags': ['Overijssel \u00b7 Olst-Wijhe', 'Uiterwaard \u00b7 open graslanden en plassen aan de IJssel', 'list 36 \u00b7 no. 279'],
 'loc': '\U0001f4cd Wijhe aan de IJssel \u00b7 Uiterwaard \u00b7 Middelgroot',
 'desc': 'De <b>Buitenwaarden</b> bij Wijhe zijn een open uiterwaard die \u2019s winters regelmatig <b>onder water staat</b>. Precies dat maakt ze zo waardevol voor vogels: overstroomd grasland is een gedekte tafel. Wormen en insecten worden door het stijgende water naar boven gedreven, en zodra het zakt blijft een <b>slikkige, voedselrijke bodem</b> achter waar duizenden <b>ganzen, smienten, kieviten en goudplevieren</b> op afkomen. De naam <b>buitenwaard</b> zegt het al: land dat <b>buiten de dijk</b> ligt en dus aan de rivier is prijsgegeven. Binnendijks land heet <b>binnenwaarts</b> en is beschermd. In de zomer broeden hier <b>grutto, tureluur en kwartelkoning</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Nov\u2013feb</b> (ganzen en watervogels), apr\u2013jun (weidevogels)<br>\n    <b>Beste tijd van de dag:</b> Ochtend en late middag \u2014 ganzen vliegen dan uit en in.',
 'why': ['Uiterwaard die \u2019s winters regelmatig <b>onder water staat</b>.',
         'Stijgend water drijft <b>wormen en insecten</b> naar boven.',
         'Bij zakkend water blijft een <b>slikkige, voedselrijke bodem</b> achter.',
         '<b>Buitenwaard</b> = land buiten de dijk, prijsgegeven aan de rivier.'],
 'phen': ['<span class="months">Nov\u2013Feb</span> \U0001f426 <b>Ganzen, smienten en goudplevieren</b> bij duizenden.',
          '<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Weidevogels</b> bezetten de graslanden.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Kwartelkoning</b> roept uit het hoge gras.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Libellen</b> boven de plassen.'],
 'wild': ['\U0001f426 Kolgans \u00b7 Smient \u00b7 Goudplevier \u00b7 Kievit', '\U0001f426 Grutto \u00b7 Tureluur \u00b7 Kwartelkoning in de zomer', '\U0001f985 Zeearend \u00b7 Slechtvalk \u00b7 Blauwe kiekendief', '\U0001f9ab Bever \u00b7 \U0001f98a Vos \u00b7 Haas', '\U0001f33e Grasland- en oeverflora'],
 'trail': ['Parkeren in <b>Wijhe</b>; het beste zicht heb je vanaf de <b>dijk</b>.',
           'Kom in <b>januari</b> voor de grootste aantallen ganzen.',
           'Verstoor foeragerende ganzen niet \u2014 blijf op de dijk.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f426 Wintervogelgebied \u00b7 \u26a0\ufe0f Hoogwaterrisico'
}, {
 'tags': ['Overijssel \u00b7 Olst-Wijhe', 'Floodplain \u00b7 open grasslands and pools on the IJssel', 'list 36 \u00b7 no. 279'],
 'loc': '\U0001f4cd Wijhe on the IJssel \u00b7 Floodplain \u00b7 Medium-sized',
 'desc': 'The <b>Buitenwaarden</b> at Wijhe are an open floodplain regularly <b>under water</b> in winter. That is exactly what makes them so valuable for birds: flooded grassland is a laid table. Worms and insects are driven upward by the rising water, and as soon as it falls a <b>muddy, nutrient-rich surface</b> remains, drawing thousands of <b>geese, wigeon, lapwings and golden plovers</b>. The name <b>buitenwaard</b> says it: land lying <b>outside the dyke</b> and thus surrendered to the river. Land inside the dyke is protected. In summer <b>black-tailed godwit, redshank and corncrake</b> breed here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Nov\u2013Feb</b> (geese and waterbirds), Apr\u2013Jun (meadow birds)<br>\n    <b>Best time of day:</b> Morning and late afternoon \u2014 geese fly out and in.',
 'why': ['A floodplain regularly <b>under water</b> in winter.',
         'Rising water drives <b>worms and insects</b> upward.',
         'Falling water leaves a <b>muddy, nutrient-rich surface</b>.',
         '<b>Buitenwaard</b> = land outside the dyke, surrendered to the river.'],
 'phen': ['<span class="months">Nov\u2013Feb</span> \U0001f426 <b>Geese, wigeon and golden plover</b> in thousands.',
          '<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Meadow birds</b> occupy the grasslands.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Corncrake</b> calls from the tall grass.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Dragonflies</b> above the pools.'],
 'wild': ['\U0001f426 White-fronted goose \u00b7 Wigeon \u00b7 Golden plover \u00b7 Lapwing', '\U0001f426 Black-tailed godwit \u00b7 Redshank \u00b7 Corncrake in summer', '\U0001f985 White-tailed eagle \u00b7 Peregrine \u00b7 Hen harrier', '\U0001f9ab Beaver \u00b7 \U0001f98a Fox \u00b7 Hare', '\U0001f33e Grassland and bankside flora'],
 'trail': ['Park in <b>Wijhe</b>; the best view is from the <b>dyke</b>.',
           'Come in <b>January</b> for the largest goose numbers.',
           'Do not disturb feeding geese \u2014 stay on the dyke.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f426 Winter bird area \u00b7 \u26a0\ufe0f Flood risk'
}, card_class='card water'))

C.append(mk.card(1561, "'t Nijenhuis en 't Rozendael", {
 'tags': ['Overijssel \u00b7 Heino', 'Landgoed \u00b7 kasteel met parkbos en lanen', 'list 36 \u00b7 no. 280'],
 'loc': '\U0001f4cd Heino bij Zwolle \u00b7 Landgoed \u00b7 Middelgroot',
 'desc': '<b>\u2019t Nijenhuis</b> bij Heino is een havezate met een omgracht kasteel, tegenwoordig bekend als <b>museum met kunstcollectie</b>, met daarnaast het landgoed <b>\u2019t Rozendael</b>. Kenmerkend voor deze Salland-landgoederen is de <b>gracht</b>: die had zelden nog een militaire functie, maar diende als statussymbool, als afscheiding van het vee en \u2014 heel praktisch \u2014 als visvijver en waterreservoir. Grachten zijn bovendien ecologisch waardevol: het permanente, beschutte water herbergt <b>amfibieën, libellen en waterplanten</b>, en de oude bomen eromheen bieden <b>holtes voor uilen en vleermuizen</b>. Er broeden <b>bosuil, ijsvogel en boomklever</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang en amfibieën), okt\u2013nov (herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 spiegeling in de gracht en vogelzang.',
 'why': ['Een <b>havezate</b> met omgracht kasteel, nu ook museum.',
         'De <b>gracht</b> was zelden militair maar vooral statussymbool.',
         'Ook praktisch: <b>visvijver, veekering en waterreservoir</b>.',
         'Het permanente water herbergt <b>amfibieën, libellen en waterplanten</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Amfibieën</b> trekken naar de gracht.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en bosuil</b> broeden in de oude bomen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> jagen boven het water.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> in de beukenlanen.'],
 'wild': ['\U0001f426 IJsvogel \u00b7 Boomklever \u00b7 Grote bonte specht', '\U0001f989 Bosuil \u00b7 Ransuil \u00b7 \U0001f985 Buizerd', '\U0001f987 Vleermuizen in kelders en boomholtes', '\U0001f438 Amfibieën en libellen in de gracht', '\U0001f333 Oude beuk \u00b7 Eik \u00b7 Linde'],
 'trail': ['Parkeren bij <b>\u2019t Nijenhuis</b> in Heino; lanen door het park.',
           'Loop rond de <b>gracht</b> voor ijsvogel en amfibieën.',
           'Combineer het landgoed met het <b>museum</b> in het kasteel.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Park gratis \u00b7 \U0001f3f0 Havezate en museum \u00b7 \U0001f6b6 Vlakke lanen'
}, {
 'tags': ['Overijssel \u00b7 Heino', 'Country estate \u00b7 castle with park woodland and avenues', 'list 36 \u00b7 no. 280'],
 'loc': '\U0001f4cd Heino near Zwolle \u00b7 Country estate \u00b7 Medium-sized',
 'desc': '<b>\u2019t Nijenhuis</b> near Heino is a havezate with a moated castle, today known as a <b>museum with an art collection</b>, alongside the estate of <b>\u2019t Rozendael</b>. Characteristic of these Salland estates is the <b>moat</b>: it rarely served a military purpose any more but functioned as a status symbol, a barrier against livestock and \u2014 very practically \u2014 as a fish pond and water reservoir. Moats are moreover ecologically valuable: the permanent, sheltered water holds <b>amphibians, dragonflies and water plants</b>, and the old trees around offer <b>cavities for owls and bats</b>. <b>Tawny owl, kingfisher and nuthatch</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song and amphibians), Oct\u2013Nov (autumn colour)<br>\n    <b>Best time of day:</b> Morning \u2014 reflections in the moat and birdsong.',
 'why': ['A <b>havezate</b> with moated castle, now also a museum.',
         'The <b>moat</b> was rarely military but chiefly a status symbol.',
         'Also practical: <b>fish pond, stock barrier and water reservoir</b>.',
         'The permanent water holds <b>amphibians, dragonflies and water plants</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Amphibians</b> migrate to the moat.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and tawny owl</b> breed in the old trees.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> hunt above the water.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> in the beech avenues.'],
 'wild': ['\U0001f426 Kingfisher \u00b7 Nuthatch \u00b7 Great spotted woodpecker', '\U0001f989 Tawny owl \u00b7 Long-eared owl \u00b7 \U0001f985 Buzzard', '\U0001f987 Bats in cellars and tree cavities', '\U0001f438 Amphibians and dragonflies in the moat', '\U0001f333 Old beech \u00b7 Oak \u00b7 Lime'],
 'trail': ['Park at <b>\u2019t Nijenhuis</b> in Heino; avenues cross the park.',
           'Walk around the <b>moat</b> for kingfisher and amphibians.',
           'Combine the estate with the <b>museum</b> in the castle.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Park free \u00b7 \U0001f3f0 Havezate and museum \u00b7 \U0001f6b6 Level avenues'
}))

C.append(mk.card(1562, 'Luttenbergerven', {
 'tags': ['Overijssel \u00b7 Raalte', 'Ven en heide \u00b7 hoogveenrestant met blauwgrasland', 'list 36 \u00b7 no. 281'],
 'loc': '\U0001f4cd Luttenberg bij Raalte \u00b7 Ven en heide \u00b7 Klein',
 'desc': 'Het <b>Luttenbergerven</b> is een klein maar botanisch beroemd terrein in Salland, met een venachtige laagte, natte heide en fragmenten <b>blauwgrasland</b>. Dat laatste vegetatietype is een van de zeldzaamste van Nederland: het ontstaat alleen op <b>natte, voedselarme, licht basische grond</b> die eeuwenlang jaarlijks werd gemaaid en waar het maaisel telkens werd afgevoerd, zodat er nooit voedsel ophoopte. De naam komt van de blauwgrijze gloed die de <b>zeggen en pijpenstrootjes</b> in de zomer over het land leggen. Herstelbeheer bestaat hier uit <b>maaien en plaggen</b>. Er groeien <b>klokjesgentiaan, spaanse ruiter en orchideeën</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (blauwgraslandflora en gentiaan)<br>\n    <b>Beste tijd van de dag:</b> Late ochtend \u2014 vlinders actief boven de natte heide.',
 'why': ['Fragmenten <b>blauwgrasland</b>, een van de zeldzaamste vegetaties van Nederland.',
         'Ontstaat alleen op <b>natte, voedselarme, licht basische grond</b>.',
         'Vereist eeuwenlang <b>maaien en het maaisel afvoeren</b>.',
         'De naam komt van de <b>blauwgrijze gloed</b> van zeggen in de zomer.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33a <b>Orchideeën</b> in het blauwgrasland.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33f <b>Spaanse ruiter</b> en zeggen in bloei.',
          '<span class="months">Aug\u2013Sep</span> \U0001f499 <b>Klokjesgentiaan</b> \u2014 waardplant van het gentiaanblauwtje.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Dophei</b> kleurt de natte heide.'],
 'wild': ['\U0001f499 Klokjesgentiaan \u00b7 Spaanse ruiter \u00b7 Orchideeën', '\U0001f98b Gentiaanblauwtje \u00b7 Heidevlinders', '\U0001f426 Roodborsttapuit \u00b7 Boompieper \u00b7 Watersnip', '\U0001f438 Heikikker \u00b7 \U0001f98e Levendbarende hagedis \u00b7 Adder', '\U0001f33f Zonnedauw \u00b7 Veenpluis \u00b7 Dophei'],
 'trail': ['Parkeren bij <b>Luttenberg</b>; smalle paden langs het ven.',
           'Augustus voor de <b>klokjesgentiaan</b> en het gentiaanblauwtje.',
           'Blijf strikt op de paden \u2014 blauwgrasland is <b>uiterst kwetsbaar</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f33a Botanisch topgebied \u00b7 \u26a0\ufe0f Zeer kwetsbaar'
}, {
 'tags': ['Overijssel \u00b7 Raalte', 'Fen and heath \u00b7 bog remnant with fen meadow', 'list 36 \u00b7 no. 281'],
 'loc': '\U0001f4cd Luttenberg near Raalte \u00b7 Fen and heath \u00b7 Small',
 'desc': 'The <b>Luttenbergerven</b> is a small but botanically famous site in Salland, with a fen-like hollow, wet heath and fragments of <b>blauwgrasland</b> (fen meadow). That vegetation type is among the rarest in the Netherlands: it arises only on <b>wet, nutrient-poor, slightly alkaline ground</b> that was mown annually for centuries with the cuttings always carted off, so that nutrients never accumulated. The name comes from the blue-grey sheen the <b>sedges and purple moor-grass</b> lay over the land in summer. Restoration here means <b>mowing and sod-cutting</b>. <b>Marsh gentian, meadow thistle and orchids</b> grow here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (fen meadow flora and gentian)<br>\n    <b>Best time of day:</b> Late morning \u2014 butterflies active above the wet heath.',
 'why': ['Fragments of <b>fen meadow</b>, among the rarest vegetation in the Netherlands.',
         'It arises only on <b>wet, nutrient-poor, slightly alkaline ground</b>.',
         'It requires centuries of <b>mowing and removing the cuttings</b>.',
         'The name comes from the <b>blue-grey sheen</b> of sedges in summer.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33a <b>Orchids</b> in the fen meadow.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33f <b>Meadow thistle</b> and sedges in flower.',
          '<span class="months">Aug\u2013Sep</span> \U0001f499 <b>Marsh gentian</b> \u2014 host plant of the alcon blue.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Cross-leaved heath</b> colours the wet heath.'],
 'wild': ['\U0001f499 Marsh gentian \u00b7 Meadow thistle \u00b7 Orchids', '\U0001f98b Alcon blue \u00b7 Heath butterflies', '\U0001f426 Stonechat \u00b7 Tree pipit \u00b7 Snipe', '\U0001f438 Moor frog \u00b7 \U0001f98e Viviparous lizard \u00b7 Adder', '\U0001f33f Sundew \u00b7 Cottongrass \u00b7 Cross-leaved heath'],
 'trail': ['Park at <b>Luttenberg</b>; narrow paths skirt the fen.',
           'August for the <b>marsh gentian</b> and the alcon blue.',
           'Keep strictly to the paths \u2014 fen meadow is <b>extremely fragile</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f33a Botanical hotspot \u00b7 \u26a0\ufe0f Highly fragile'
}, card_class='card heath'))

C.append(mk.card(1563, 'Heideblok Heino', {
 'tags': ['Overijssel \u00b7 Raalte', 'Heiderestant \u00b7 droge heide met bosjes in Salland', 'list 36 \u00b7 no. 282'],
 'loc': '\U0001f4cd Heino bij Raalte \u00b7 Heiderestant \u00b7 Klein',
 'desc': 'Het <b>Heideblok</b> bij Heino is een van de laatste heiderestanten van Salland. Dat er zo weinig over is heeft een precieze oorzaak: de uitvinding van <b>kunstmest</b> rond 1900. Zolang boeren afhankelijk waren van heideplaggen en schapenmest, was uitgestrekte heide een economische noodzaak \u2014 men rekende soms tien hectare heide per hectare akker. Toen kunstmest die functie overnam, was de heide van de ene generatie op de andere waardeloos en werd ze massaal ontgonnen tot landbouwgrond of bebost. Van de honderdduizenden hectaren resteren nu snippers zoals deze. Er leven <b>levendbarende hagedis, boompieper en heidevlinders</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Aug\u2013sep</b> (heidebloei), apr\u2013jun (zang)<br>\n    <b>Beste tijd van de dag:</b> Warme ochtend \u2014 hagedissen zonnen op de paden.',
 'why': ['Een van de laatste <b>heiderestanten van Salland</b>.',
         'De oorzaak van het verdwijnen: <b>kunstmest</b> rond 1900.',
         'Daarvoor rekende men soms <b>tien hectare heide per hectare akker</b>.',
         'Toen die functie wegviel werd heide massaal <b>ontgonnen of bebost</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boompieper en roodborsttapuit</b> zingen.',
          '<span class="months">Mei\u2013Aug</span> \U0001f98e <b>Hagedissen</b> zonnen op de zandpaden.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heidebloei</b> \u2014 het veld kleurt paars.',
          '<span class="months">Sep\u2013Okt</span> \U0001f41d <b>Heidebijen</b> op de late bloei.'],
 'wild': ['\U0001f98e Levendbarende hagedis \u00b7 Adder \u00b7 Hazelworm', '\U0001f426 Boompieper \u00b7 Roodborsttapuit \u00b7 Geelgors', '\U0001f98b Heidevlinder \u00b7 Kleine vuurvlinder \u00b7 \U0001f41d Heidebijen', '\U0001f98c Ree \u00b7 \U0001f98a Vos \u00b7 Haas', '\U0001f49c Struikhei \u00b7 Buntgras \u00b7 Jeneverbes'],
 'trail': ['Parkeren bij <b>Heino</b>; korte paden over het heideblok.',
           'Kom op een <b>warme ochtend</b> voor de hagedissen.',
           'Augustus\u2013september voor de <b>heidebloei</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Korte routes \u00b7 \u26a0\ufe0f Kwetsbaar heiderestant'
}, {
 'tags': ['Overijssel \u00b7 Raalte', 'Heath remnant \u00b7 dry heath with copses in Salland', 'list 36 \u00b7 no. 282'],
 'loc': '\U0001f4cd Heino near Raalte \u00b7 Heath remnant \u00b7 Small',
 'desc': 'The <b>Heideblok</b> near Heino is one of the last heath remnants of Salland. That so little survives has a precise cause: the invention of <b>artificial fertiliser</b> around 1900. As long as farmers depended on heath sods and sheep manure, extensive heath was an economic necessity \u2014 sometimes ten hectares of heath were reckoned per hectare of arable. When fertiliser took over that function, heath became worthless from one generation to the next and was reclaimed wholesale into farmland or planted with trees. Of hundreds of thousands of hectares only scraps like this remain. <b>Viviparous lizard, tree pipit and heath butterflies</b> live here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Aug\u2013Sep</b> (heather bloom), Apr\u2013Jun (song)<br>\n    <b>Best time of day:</b> Warm morning \u2014 lizards basking on the paths.',
 'why': ['One of the last <b>heath remnants of Salland</b>.',
         'The cause of its disappearance: <b>artificial fertiliser</b> around 1900.',
         'Before that, <b>ten hectares of heath per hectare of arable</b> were reckoned.',
         'Once that function vanished, heath was <b>reclaimed or afforested</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tree pipit and stonechat</b> sing.',
          '<span class="months">May\u2013Aug</span> \U0001f98e <b>Lizards</b> bask on the sandy paths.',
          '<span class="months">Aug\u2013Sep</span> \U0001f49c <b>Heather bloom</b> \u2014 the field turns purple.',
          '<span class="months">Sep\u2013Oct</span> \U0001f41d <b>Heath bees</b> on the late flowers.'],
 'wild': ['\U0001f98e Viviparous lizard \u00b7 Adder \u00b7 Slow worm', '\U0001f426 Tree pipit \u00b7 Stonechat \u00b7 Yellowhammer', '\U0001f98b Grayling \u00b7 Small copper \u00b7 \U0001f41d Heath bees', '\U0001f98c Roe deer \u00b7 \U0001f98a Fox \u00b7 Hare', '\U0001f49c Heather \u00b7 Grey hair-grass \u00b7 Juniper'],
 'trail': ['Park at <b>Heino</b>; short paths cross the heath block.',
           'Come on a <b>warm morning</b> for the lizards.',
           'August\u2013September for the <b>heather bloom</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Short routes \u00b7 \u26a0\ufe0f Fragile heath remnant'
}, card_class='card heath'))

C.append(mk.card(1564, 'Raalterwoold', {
 'tags': ['Overijssel \u00b7 Raalte', 'Wooldlandschap \u00b7 oud broekbos en houtwallen', 'list 36 \u00b7 no. 283'],
 'loc': '\U0001f4cd Raalte, Salland \u00b7 Wooldlandschap \u00b7 Middelgroot',
 'desc': 'Het <b>Raalterwoold</b> draagt het oude woord <b>woold</b> of <b>wold</b>, dat verwant is aan het Engelse <i>wold</i> en het Duitse <i>Wald</i> en oorspronkelijk <b>moerasbos</b> betekende \u2014 niet het droge bos dat wij nu voor ogen hebben. In heel Noord- en Oost-Nederland duikt het op: Woldberg, Oldenzaal, Wolvega, Nieuwkoopse Wold. Die woldgebieden waren voor de ontginning drassige elzen- en berkenbossen op veen, en werden vanaf de middeleeuwen systematisch ontgonnen in lange, smalle stroken haaks op een ontginningsas \u2014 het <b>slagenlandschap</b>. Rond Raalte zijn nog <b>houtwallen, singels en natte bosjes</b> over, met <b>das, ree, groene specht en houtsnip</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 das en houtsnip actief.',
 'why': ['<b>Woold</b> betekende oorspronkelijk <b>moerasbos</b>, geen droog bos.',
         'Verwant aan het Engelse <i>wold</i> en het Duitse <i>Wald</i>.',
         'Woldgebieden waren drassige <b>elzen- en berkenbossen op veen</b>.',
         'Ze werden ontgonnen in smalle stroken: het <b>slagenlandschap</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Voorjaarsflora</b> in de vochtige bosjes.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Groene specht en zangvogels</b> in de wallen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> langs de singels.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in de oude houtwallen.'],
 'wild': ['\U0001f98c Das \u00b7 Ree \u00b7 \U0001f98a Vos \u00b7 Haas', '\U0001f426 Groene specht \u00b7 Houtsnip \u00b7 Geelgors', '\U0001f989 Bosuil \u00b7 Steenuil \u00b7 \U0001f985 Buizerd', '\U0001f344 Paddenstoelen op oud hout', '\U0001f333 Els \u00b7 Berk \u00b7 Eik \u00b7 Hazelaar'],
 'trail': ['Parkeren bij <b>Raalte</b>; zandwegen tussen de percelen.',
           'Let op het <b>slagenpatroon</b>: lange smalle kavels haaks op de weg.',
           'Schemer voor <b>das en houtsnip</b>; blijf stil en op afstand.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3fa Ontginningslandschap \u00b7 \u26a0\ufe0f Natte paden'
}, {
 'tags': ['Overijssel \u00b7 Raalte', 'Woold landscape \u00b7 old carr woodland and hedge banks', 'list 36 \u00b7 no. 283'],
 'loc': '\U0001f4cd Raalte, Salland \u00b7 Woold landscape \u00b7 Medium-sized',
 'desc': 'The <b>Raalterwoold</b> carries the old word <b>woold</b> or <b>wold</b>, cognate with English <i>wold</i> and German <i>Wald</i>, originally meaning <b>swamp forest</b> \u2014 not the dry woodland we picture today. It crops up all over northern and eastern Netherlands: Woldberg, Oldenzaal, Wolvega, Nieuwkoopse Wold. Before reclamation those wold areas were boggy alder and birch woods on peat, systematically reclaimed from the Middle Ages in long narrow strips at right angles to a reclamation axis \u2014 the <b>strip landscape</b>. Around Raalte, <b>hedge banks, shelterbelts and damp copses</b> survive, with <b>badger, roe deer, green woodpecker and woodcock</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Dusk \u2014 badger and woodcock active.',
 'why': ['<b>Woold</b> originally meant <b>swamp forest</b>, not dry woodland.',
         'Cognate with English <i>wold</i> and German <i>Wald</i>.',
         'Wold areas were boggy <b>alder and birch woods on peat</b>.',
         'They were reclaimed in narrow strips: the <b>strip landscape</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Spring flora</b> in the damp copses.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Green woodpecker and songbirds</b> in the banks.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> along the shelterbelts.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> in the old hedge banks.'],
 'wild': ['\U0001f98c Badger \u00b7 Roe deer \u00b7 \U0001f98a Fox \u00b7 Hare', '\U0001f426 Green woodpecker \u00b7 Woodcock \u00b7 Yellowhammer', '\U0001f989 Tawny owl \u00b7 Little owl \u00b7 \U0001f985 Buzzard', '\U0001f344 Fungi on old wood', '\U0001f333 Alder \u00b7 Birch \u00b7 Oak \u00b7 Hazel'],
 'trail': ['Park at <b>Raalte</b>; sand tracks run between the parcels.',
           'Note the <b>strip pattern</b>: long narrow plots at right angles to the road.',
           'Dusk for <b>badger and woodcock</b>; stay quiet and at a distance.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3fa Reclamation landscape \u00b7 \u26a0\ufe0f Wet paths'
}))

mk.insert(C, '1559')
mk.progress(1564)
mk.check()
