# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1375, 'Emmerdennen en Valtherbos', {
 'tags': ['Drenthe \u00b7 Emmen', 'Bos \u00b7 oude dennenaanplant op keileem en zand', 'list 36 \u00b7 no. 94'],
 'loc': '\U0001f4cd Direct ten oosten en noorden van Emmen \u00b7 Naaldbos \u00b7 Groot',
 'desc': 'De <b>Emmerdennen</b> en het aangrenzende <b>Valtherbos</b> vormen samen een van de oudste dennenaanplanten van Drenthe: al rond 1880 werd hier op de kale Emmer heide grove den gezaaid, bedoeld als <b>mijnhout</b> voor de Limburgse kolenmijnen. Dat de bomen nu monumentaal zijn, komt doordat de mijnbouwvraag wegviel voordat het bos geoogst werd. Wandelen tussen die anderhalve eeuw oude dennen is een bijzondere ervaring: hoge, kaarsrechte stammen met roodbruine schors en een open kroondak waardoor het licht in banen naar beneden valt. In het bos liggen bovendien <b>grafheuvels en een hunebed</b>, want deze zandrug werd al in het neolithicum bewoond. Er broeden <b>zwarte specht, havik en boomklever</b>, en in de herfst is het paddenstoelenrijk.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Sep\u2013nov</b> (paddenstoelen en herfstlicht), mrt\u2013mei (zang en baltsende haviken)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 zonnestralen tussen de hoge stammen.',
 'why': ['Rond <b>1880</b> gezaaid als <b>mijnhout</b> voor de kolenmijnen.',
         'Nooit geoogst \u2014 daardoor <b>monumentale, anderhalve eeuw oude dennen</b>.',
         '<b>Grafheuvels en een hunebed</b> in het bos.',
         'Rijk paddenstoelenbos in de herfst.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f985 <b>Havik</b> baltst boven het kroondak.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Zwarte specht</b> roffelt op de dikste stammen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in grote soortenrijkdom.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstlicht</b> tussen de roodbruine stammen.'],
 'wild': ['\U0001f426 Zwarte specht \u00b7 Boomklever \u00b7 Goudhaan', '\U0001f985 Havik \u00b7 Buizerd \u00b7 Bosuil', '\U0001f344 Boleten \u00b7 Russula\u2019s \u00b7 Amanieten', '\U0001f98c Ree \u00b7 Eekhoorn \u00b7 Das', '\U0001f333 Grove den (ca. 1880) \u00b7 Beuk \u00b7 Eik'],
 'trail': ['Parkeren aan de <b>oostrand van Emmen</b>; uitgebreid padennet.',
           'Zoek het <b>hunebed</b> en de grafheuvels op de zandrug.',
           'Beste licht in de <b>vroege ochtend</b> tussen de hoge dennen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Hunebed en grafheuvels \u00b7 \U0001f6b6 Uitgebreid padennet'
}, {
 'tags': ['Drenthe \u00b7 Emmen', 'Woodland \u00b7 old pine plantation on boulder clay and sand', 'list 36 \u00b7 no. 94'],
 'loc': '\U0001f4cd Directly east and north of Emmen \u00b7 Coniferous woodland \u00b7 Large',
 'desc': 'The <b>Emmerdennen</b> and the adjoining <b>Valtherbos</b> together form one of the oldest pine plantations in Drenthe: as early as around 1880 Scots pine was sown here on the bare Emmen heath, intended as <b>pit props</b> for the Limburg coal mines. That the trees are now monumental is because mining demand fell away before the wood was harvested. Walking among those century-and-a-half-old pines is a special experience: tall, ramrod-straight trunks with red-brown bark and an open canopy through which light falls in shafts. The wood also contains <b>burial mounds and a dolmen</b>, for this sand ridge was already inhabited in the Neolithic. <b>Black woodpecker, goshawk and nuthatch</b> breed here, and in autumn it is rich in fungi.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Sep\u2013Nov</b> (fungi and autumn light), Mar\u2013May (song and displaying goshawks)<br>\n    <b>Best time of day:</b> Early morning \u2014 sunbeams between the tall trunks.',
 'why': ['Sown around <b>1880</b> as <b>pit props</b> for the coal mines.',
         'Never harvested \u2014 hence <b>monumental pines of 150 years old</b>.',
         '<b>Burial mounds and a dolmen</b> within the wood.',
         'Rich fungus woodland in autumn.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f985 <b>Goshawk</b> displays above the canopy.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Black woodpecker</b> drums on the thickest trunks.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> in great diversity.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn light</b> among the red-brown trunks.'],
 'wild': ['\U0001f426 Black woodpecker \u00b7 Nuthatch \u00b7 Goldcrest', '\U0001f985 Goshawk \u00b7 Buzzard \u00b7 Tawny owl', '\U0001f344 Boletes \u00b7 Russulas \u00b7 Amanitas', '\U0001f98c Roe deer \u00b7 Red squirrel \u00b7 Badger', '\U0001f333 Scots pine (c. 1880) \u00b7 Beech \u00b7 Oak'],
 'trail': ['Park at the <b>eastern edge of Emmen</b>; extensive path network.',
           'Seek out the <b>dolmen</b> and burial mounds on the sand ridge.',
           'Best light in the <b>early morning</b> among the tall pines.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Dolmen and burial mounds \u00b7 \U0001f6b6 Extensive path network'
}))

C.append(mk.card(1376, 'Noordbargerbos', {
 'tags': ['Drenthe \u00b7 Emmen', 'Stadsbos \u00b7 gemengd bos aan de rand van Emmen', 'list 36 \u00b7 no. 95'],
 'loc': '\U0001f4cd Zuidwestrand van Emmen \u00b7 Gemengd bos \u00b7 Middelgroot',
 'desc': 'Het <b>Noordbargerbos</b> hoort bij het buurtschap <b>Noordbarge</b>, en die naam is een van de oudste van de streek: <b>Barge</b> gaat terug op <i>berg</i> in de oude betekenis van een <b>hoogte in het landschap</b>, hier de zandrug waarop Emmen is gebouwd. De rug loopt van noord naar zuid en droeg oorspronkelijk drie esdorpen: Noordbarge, Zuidbarge en Westenesch. Het bos werd in de twintigste eeuw aangelegd op de voormalige heidegronden bij het dorp en is inmiddels een volwassen <b>gemengd bos</b> met eik, beuk en den, doorsneden door lanen. Voor de stad Emmen is het het belangrijkste uitloopgebied. Ecologisch draait het om de <b>oude bomen en dood hout</b>, met <b>grote bonte specht, boomklever, bosuil</b> en in de herfst een rijk paddenstoelenbestand.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (voorjaarszang), sep\u2013nov (paddenstoelen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 voor de wandelaars uit de stad arriveren.',
 'why': ['<b>Barge</b> = berg, de zandrug waarop Emmen ligt.',
         'De rug droeg drie esdorpen: <b>Noordbarge, Zuidbarge, Westenesch</b>.',
         'Volwassen gemengd bos op voormalige <b>heidegrond</b>.',
         'Rijk aan <b>oude bomen en dood hout</b>.'],
 'phen': ['<span class="months">Mrt\u2013Mei</span> \U0001f426 <b>Grote bonte specht</b> roffelt.',
          '<span class="months">Apr\u2013Mei</span> \U0001f3b6 <b>Voorjaarskoor</b> in de lanen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op dood hout.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> van beuk en eik.'],
 'wild': ['\U0001f426 Grote bonte specht \u00b7 Boomklever \u00b7 Glanskop', '\U0001f989 Bosuil \u00b7 Ransuil', '\U0001f344 Zwavelkop \u00b7 Elfenbankje \u00b7 Boleten', '\U0001f98c Ree \u00b7 Eekhoorn \u00b7 Vos', '\U0001f333 Eik \u00b7 Beuk \u00b7 Grove den'],
 'trail': ['Parkeren bij de <b>zuidwestrand van Emmen</b>; verharde en zandpaden.',
           'Bezoek het bos <b>vroeg</b> \u2014 later is het druk met stadswandelaars.',
           'Let op de <b>dode stammen</b>, vol spechtengaten.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Goed toegankelijk \u00b7 \U0001f68c Bereikbaar vanuit Emmen'
}, {
 'tags': ['Drenthe \u00b7 Emmen', 'City wood \u00b7 mixed woodland on the edge of Emmen', 'list 36 \u00b7 no. 95'],
 'loc': '\U0001f4cd South-western edge of Emmen \u00b7 Mixed woodland \u00b7 Medium-sized',
 'desc': 'The <b>Noordbargerbos</b> belongs to the hamlet of <b>Noordbarge</b>, and that name is one of the oldest in the district: <b>Barge</b> goes back to <i>berg</i> in the old sense of a <b>rise in the landscape</b>, here the sand ridge on which Emmen is built. The ridge runs north to south and originally carried three esdorpen: Noordbarge, Zuidbarge and Westenesch. The wood was planted in the twentieth century on former heathland beside the village and is now a mature <b>mixed woodland</b> of oak, beech and pine, cut through by avenues. For the town of Emmen it is the main recreational green space. Ecologically it turns on the <b>old trees and dead wood</b>, with <b>great spotted woodpecker, nuthatch, tawny owl</b> and a rich fungus flora in autumn.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (spring song), Sep\u2013Nov (fungi and autumn colour)<br>\n    <b>Best time of day:</b> Early morning \u2014 before the walkers arrive from town.',
 'why': ['<b>Barge</b> = hill, the sand ridge on which Emmen stands.',
         'The ridge carried three esdorpen: <b>Noordbarge, Zuidbarge, Westenesch</b>.',
         'Mature mixed woodland on former <b>heathland</b>.',
         'Rich in <b>old trees and dead wood</b>.'],
 'phen': ['<span class="months">Mar\u2013May</span> \U0001f426 <b>Great spotted woodpecker</b> drums.',
          '<span class="months">Apr\u2013May</span> \U0001f3b6 <b>Spring chorus</b> in the avenues.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on dead wood.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> of beech and oak.'],
 'wild': ['\U0001f426 Great spotted woodpecker \u00b7 Nuthatch \u00b7 Marsh tit', '\U0001f989 Tawny owl \u00b7 Long-eared owl', '\U0001f344 Sulphur tuft \u00b7 Turkeytail \u00b7 Boletes', '\U0001f98c Roe deer \u00b7 Red squirrel \u00b7 Fox', '\U0001f333 Oak \u00b7 Beech \u00b7 Scots pine'],
 'trail': ['Park at the <b>south-western edge of Emmen</b>; paved and sandy paths.',
           'Visit the wood <b>early</b> \u2014 later it is busy with town walkers.',
           'Note the <b>dead trunks</b>, full of woodpecker holes.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Easily accessible \u00b7 \U0001f68c Reachable from Emmen'
}))

C.append(mk.card(1377, 'Oosterbos en Emmerschans', {
 'tags': ['Drenthe \u00b7 Emmen', 'Bos en schans \u00b7 aardwerk uit de Tachtigjarige Oorlog', 'list 36 \u00b7 no. 96'],
 'loc': '\U0001f4cd Noordoostrand van Emmen \u00b7 Bos met historisch aardwerk \u00b7 Middelgroot',
 'desc': 'In het <b>Oosterbos</b> bij Emmen ligt de <b>Emmerschans</b>, een vierkant aardwerk met wallen en grachten dat in de <b>Tachtigjarige Oorlog</b> werd opgeworpen. Zulke schansen bewaakten de smalle, begaanbare zandruggen door het veen \u2014 de enige plekken waar legers zich konden verplaatsen. Wie de schans bezette, controleerde de doorgang. Toen het veen werd afgegraven verloor de schans haar functie, maar het aardwerk bleef als reli\u00ebf bewaard en werd later door bos overgroeid. De <b>wallen en de gracht</b> zijn nog goed zichtbaar en vormen nu een eigen microhabitat: de gracht houdt water vast, de wal is droog en warm. Er broeden <b>bosuil, boomklever en gekraagde roodstaart</b>, en op de vochtige gracht vliegen libellen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Okt\u2013mrt</b> (aardwerk zichtbaar zonder blad), apr\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Winterse ochtend \u2014 laag licht toont het reli\u00ebf van de wallen.',
 'why': ['<b>Emmerschans</b> \u2014 vierkant aardwerk uit de Tachtigjarige Oorlog.',
         'Bewaakte de <b>begaanbare zandrug</b> door het veen.',
         'Wallen en gracht nog als <b>reli\u00ebf</b> bewaard onder het bos.',
         'Gracht en wal vormen een <b>eigen microhabitat</b>.'],
 'phen': ['<span class="months">Okt\u2013Mrt</span> \U0001f3db\ufe0f <b>Aardwerk</b> het best zichtbaar zonder blad.',
          '<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Bosuil</b> roept in het schemer.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Gekraagde roodstaart</b> in de oude bomen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven de gracht.'],
 'wild': ['\U0001f989 Bosuil \u00b7 \U0001f426 Boomklever \u00b7 Gekraagde roodstaart', '\U0001f9a0 Libellen \u00b7 Waterjuffers in de gracht', '\U0001f98c Ree \u00b7 Eekhoorn \u00b7 Vos', '\U0001f344 Paddenstoelen op de wal', '\U0001f333 Eik \u00b7 Beuk \u00b7 Den'],
 'trail': ['Parkeren aan de <b>noordoostrand van Emmen</b>; bospaden naar de schans.',
           'Bezoek in de <b>winter</b>: het aardwerk is dan zonder blad goed leesbaar.',
           'Loop <b>om de gracht heen</b> om de vierkante vorm te vatten.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Archeologisch monument \u2014 niet graven'
}, {
 'tags': ['Drenthe \u00b7 Emmen', 'Wood and sconce \u00b7 earthwork from the Eighty Years War', 'list 36 \u00b7 no. 96'],
 'loc': '\U0001f4cd North-eastern edge of Emmen \u00b7 Woodland with historic earthwork \u00b7 Medium-sized',
 'desc': 'In the <b>Oosterbos</b> near Emmen lies the <b>Emmerschans</b>, a square earthwork with ramparts and a moat thrown up during the <b>Eighty Years War</b>. Such sconces guarded the narrow passable sand ridges through the bog \u2014 the only places where armies could move. Whoever held the sconce controlled the crossing. When the peat was dug away the sconce lost its function, but the earthwork survived as relief and was later overgrown by woodland. The <b>ramparts and moat</b> are still clearly visible and now form a microhabitat of their own: the moat holds water, the rampart is dry and warm. <b>Tawny owl, nuthatch and redstart</b> breed here, and dragonflies fly over the damp moat.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Oct\u2013Mar</b> (earthwork visible without leaves), Apr\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Winter morning \u2014 low light reveals the relief of the ramparts.',
 'why': ['<b>Emmerschans</b> \u2014 square earthwork from the Eighty Years War.',
         'Guarded the <b>passable sand ridge</b> through the bog.',
         'Ramparts and moat preserved as <b>relief</b> beneath the wood.',
         'Moat and rampart form a <b>microhabitat of their own</b>.'],
 'phen': ['<span class="months">Oct\u2013Mar</span> \U0001f3db\ufe0f <b>Earthwork</b> best visible without leaves.',
          '<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Tawny owl</b> calls at dusk.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redstart</b> among the old trees.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the moat.'],
 'wild': ['\U0001f989 Tawny owl \u00b7 \U0001f426 Nuthatch \u00b7 Redstart', '\U0001f9a0 Dragonflies \u00b7 Damselflies in the moat', '\U0001f98c Roe deer \u00b7 Red squirrel \u00b7 Fox', '\U0001f344 Fungi on the rampart', '\U0001f333 Oak \u00b7 Beech \u00b7 Pine'],
 'trail': ['Park at the <b>north-eastern edge of Emmen</b>; forest paths to the sconce.',
           'Visit in <b>winter</b>: the earthwork then reads clearly without leaves.',
           'Walk <b>around the moat</b> to grasp the square plan.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Archaeological monument \u2014 no digging'
}))

C.append(mk.card(1378, 'Berkenrode', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Ontginningsbos \u00b7 berkenbos op oude rodegrond', 'list 36 \u00b7 no. 97'],
 'loc': '\U0001f4cd Bij Dalen en Erm \u00b7 Berken- en gemengd bos \u00b7 Klein',
 'desc': '<b>Berkenrode</b> combineert twee landschapswoorden tot een compleet verhaal: <b>berken</b>, de pionierboom die als eerste op verlaten grond verschijnt, en <b>rode</b>, van <i>roden</i> \u2014 het rooien of ontginnen van bos. De naam beschrijft dus grond die ooit werd gerooid en waarop vervolgens weer berken opsloegen; de vegetatie neemt haar eigen naam terug. Berk is daar bij uitstek geschikt voor: het zaad is licht als stof, waait kilometers ver en kiemt op vrijwel elke kale bodem. Een berkenbos is daarom bijna altijd een <b>jong bos</b> op verstoorde grond, en het maakt op termijn plaats voor eik en beuk. Hier is dat proces halverwege, met lichte berkenopstanden en al opkomend eikenhout. Er broeden <b>fitis, boompieper en matkop</b>, en er staan veel <b>berkenzwammen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang in het lichte bos), sep\u2013nov (berkenzwammen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 het lichte berkenblad filtert dan mooi.',
 'why': ['<b>Berken + rode</b>: gerooide grond waarop berk terugkwam.',
         'Berkenzaad is <b>licht als stof</b> en waait kilometers ver.',
         'Berkenbos is bijna altijd <b>jong bos op verstoorde grond</b>.',
         'Successie halverwege: berk maakt plaats voor <b>eik</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33f <b>Berken lopen uit</b> \u2014 lichtgroen waas.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Fitis en boompieper</b> zingen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Berkenzwam</b> op de stammen.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Goudgele herfstkleur</b> van de berken.'],
 'wild': ['\U0001f426 Fitis \u00b7 Boompieper \u00b7 Matkop', '\U0001f344 Berkenzwam \u00b7 Vliegenzwam', '\U0001f333 Ruwe berk \u00b7 Zachte berk \u00b7 Jonge eik', '\U0001f98c Ree \u00b7 Haas', '\U0001f41d Insecten op berkensap'],
 'trail': ['Parkeren bij <b>Dalen</b>; smalle paden door het bos.',
           'Let op de <b>vliegenzwam</b> \u2014 vaste partner van de berk.',
           'In oktober is de <b>goudgele kleur</b> op zijn mooist.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Kort rondje'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Reclamation wood \u00b7 birch wood on old cleared ground', 'list 36 \u00b7 no. 97'],
 'loc': '\U0001f4cd Near Dalen and Erm \u00b7 Birch and mixed woodland \u00b7 Small',
 'desc': '<b>Berkenrode</b> combines two landscape words into a complete story: <b>berken</b>, the birch, the pioneer tree that is first to appear on abandoned ground, and <b>rode</b>, from <i>roden</i> \u2014 to clear or grub out woodland. The name thus describes ground that was once cleared and on which birch then seeded back in; the vegetation reclaims its own name. Birch is ideally suited to that: its seed is light as dust, blows for kilometres and germinates on almost any bare soil. A birch wood is therefore nearly always a <b>young wood</b> on disturbed ground, and in time it gives way to oak and beech. Here that process is half-way, with light birch stands and oak already coming through. <b>Willow warbler, tree pipit and marsh tit</b> breed here, and <b>birch polypores</b> abound.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song in the light wood), Sep\u2013Nov (birch polypores and autumn colour)<br>\n    <b>Best time of day:</b> Morning \u2014 the light birch foliage filters beautifully then.',
 'why': ['<b>Birch + rode</b>: cleared ground on which birch returned.',
         'Birch seed is <b>light as dust</b> and blows for kilometres.',
         'Birch wood is nearly always <b>young wood on disturbed ground</b>.',
         'Succession half-way: birch giving way to <b>oak</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33f <b>Birches flush</b> \u2014 a pale green haze.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Willow warbler and tree pipit</b> sing.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Birch polypore</b> on the trunks.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Golden autumn colour</b> of the birches.'],
 'wild': ['\U0001f426 Willow warbler \u00b7 Tree pipit \u00b7 Marsh tit', '\U0001f344 Birch polypore \u00b7 Fly agaric', '\U0001f333 Silver birch \u00b7 Downy birch \u00b7 Young oak', '\U0001f98c Roe deer \u00b7 Brown hare', '\U0001f41d Insects on birch sap'],
 'trail': ['Park at <b>Dalen</b>; narrow paths through the wood.',
           'Look for the <b>fly agaric</b> \u2014 the birch\u2019s constant partner.',
           'In October the <b>golden colour</b> is at its finest.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Short circuit'
}))

C.append(mk.card(1379, 'Ermerzand', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Zandwinplas \u00b7 recreatieplas met natuuroevers', 'list 36 \u00b7 no. 98'],
 'loc': '\U0001f4cd Bij Erm, ten noorden van Coevorden \u00b7 Zandwinplas \u00b7 Middelgroot',
 'desc': 'Het <b>Ermerzand</b> is een diepe plas die ontstond door <b>zandwinning</b> voor de aanleg van de rijkswegen in de regio, en het is een leerzaam voorbeeld van hoe zulke gaten een tweede leven krijgen. Een zandwinplas is aanvankelijk ecologisch bijna leeg: steile oevers, groot doorzicht, weinig waterplanten en geen geleidelijke overgangszone. Pas als de oevers worden verflauwd en er ondiepe zones ontstaan, komt het leven op gang. Bij het Ermerzand is dat gebeurd: naast het recreatiestrand liggen nu <b>natuurvriendelijke oevers</b> met riet en waterplanten. Het diepe, heldere water trekt <b>fuut, dodaars en aalscholver</b>, in de winter <b>brilduiker en nonnetje</b>. De ondiepe hoeken zijn belangrijk voor libellen en <b>amfibie\u00ebn</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Nov\u2013mrt</b> (duikeenden op het diepe water), jun\u2013aug (libellen aan de oevers)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig water v\u00f3\u00f3r de recreanten.',
 'why': ['Ontstaan door <b>zandwinning</b> voor de rijkswegen.',
         'Zandwinplassen zijn aanvankelijk <b>ecologisch bijna leeg</b>.',
         'Verflauwde oevers brachten <b>riet en waterplanten</b>.',
         'Diep, helder water met <b>brilduiker en nonnetje</b> in de winter.'],
 'phen': ['<span class="months">Nov\u2013Mrt</span> \U0001f986 <b>Brilduiker en nonnetje</b> op het diepe water.',
          '<span class="months">Mrt\u2013Mei</span> \U0001f438 <b>Amfibie\u00ebn</b> planten zich voort in de ondiepe hoeken.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> langs de natuuroevers.',
          '<span class="months">Aug\u2013Okt</span> \U0001f426 <b>Doortrekkers</b> rusten op de plas.'],
 'wild': ['\U0001f986 Fuut \u00b7 Dodaars \u00b7 Aalscholver \u00b7 Brilduiker \u00b7 Nonnetje', '\U0001f9a0 Libellen \u00b7 Juffers', '\U0001f438 Kikkers \u00b7 Padden \u00b7 Watersalamander', '\U0001f33e Riet \u00b7 Lisdodde \u00b7 Waterplanten', '\U0001f41f Baars \u00b7 Snoek'],
 'trail': ['Parkeren bij het <b>recreatieterrein</b>; rondje om de plas.',
           'Kijk vanaf de <b>natuuroeverzijde</b>, weg van het strand.',
           'Winter is het <b>beste vogelseizoen</b> \u2014 en dan is het er stil.'],
 'foot': '\U0001f436 Honden beperkt \u00b7 \U0001f4b6 Parkeergeld in seizoen \u00b7 \U0001f3ca Zwemwater \u00b7 \U0001f6b4 Rondje mogelijk'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Sand-extraction lake \u00b7 recreation lake with natural banks', 'list 36 \u00b7 no. 98'],
 'loc': '\U0001f4cd Near Erm, north of Coevorden \u00b7 Sand-extraction lake \u00b7 Medium-sized',
 'desc': 'The <b>Ermerzand</b> is a deep lake created by <b>sand extraction</b> for building the region\u2019s motorways, and it is an instructive example of how such holes gain a second life. A sand-extraction lake is at first almost ecologically empty: steep banks, great clarity, few water plants and no gradual transition zone. Only when the banks are gently graded and shallow zones appear does life get going. At the Ermerzand that has happened: beside the recreational beach there are now <b>nature-friendly banks</b> with reed and water plants. The deep, clear water attracts <b>great crested grebe, little grebe and cormorant</b>, and in winter <b>goldeneye and smew</b>. The shallow corners matter for dragonflies and <b>amphibians</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Nov\u2013Mar</b> (diving ducks on the deep water), Jun\u2013Aug (dragonflies at the banks)<br>\n    <b>Best time of day:</b> Early morning \u2014 calm water before the visitors.',
 'why': ['Created by <b>sand extraction</b> for the motorways.',
         'Sand-extraction lakes are at first <b>almost ecologically empty</b>.',
         'Graded banks brought <b>reed and water plants</b>.',
         'Deep, clear water with <b>goldeneye and smew</b> in winter.'],
 'phen': ['<span class="months">Nov\u2013Mar</span> \U0001f986 <b>Goldeneye and smew</b> on the deep water.',
          '<span class="months">Mar\u2013May</span> \U0001f438 <b>Amphibians</b> breed in the shallow corners.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> along the natural banks.',
          '<span class="months">Aug\u2013Oct</span> \U0001f426 <b>Migrants</b> rest on the lake.'],
 'wild': ['\U0001f986 Great crested grebe \u00b7 Little grebe \u00b7 Cormorant \u00b7 Goldeneye \u00b7 Smew', '\U0001f9a0 Dragonflies \u00b7 Damselflies', '\U0001f438 Frogs \u00b7 Toads \u00b7 Newts', '\U0001f33e Reed \u00b7 Bulrush \u00b7 Water plants', '\U0001f41f Perch \u00b7 Pike'],
 'trail': ['Park at the <b>recreation area</b>; a circuit runs round the lake.',
           'Watch from the <b>natural-bank side</b>, away from the beach.',
           'Winter is the <b>best bird season</b> \u2014 and it is quiet then.'],
 'foot': '\U0001f436 Dogs restricted \u00b7 \U0001f4b6 Parking fee in season \u00b7 \U0001f3ca Swimming water \u00b7 \U0001f6b4 Circuit possible'
}, card_class='card water'))

mk.insert(C, '1374')
mk.progress(1379)
mk.check()
