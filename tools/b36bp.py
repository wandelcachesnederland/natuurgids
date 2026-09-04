# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1615, 'Roderveld', {
 'tags': ['Overijssel · Dinkelland', 'Bos · gemengd bos met heide en vennen bij het Everlo', 'list 36 · no. 334'],
 'loc': '📍 Rossum/Volthe, gemeente Dinkelland · Natuurgebied · ca. 87 ha',
 'desc': 'Het <b>Roderveld</b> is een natuurgebied van zo’n 87 hectare bij Rossum, gelegen nabij havezate <b>Het Everlo</b>. De naam verraadt het verleden: <b>roden</b> betekent rooien — een <b>veld</b> was hier ooit gemeenschappelijk, schraal gebruikt land. Nu is het een afwisseling van <b>gemengd bos, heide en enkele vennetjes</b>, in beheer bij Natuurmonumenten. De laatste jaren verdwijnen de naaldbomen geleidelijk, zodat loofhout en bodemflora — <b>klaverzuring, heksenkruid en varens</b> — meer licht krijgen, en dood hout blijft liggen voor <b>bosuil, zwarte specht en paddenstoelen</b>. In de kruinen zingen vuurgoudhaantje, tjiftjaf en fitis.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr–jun</b> (zang), aug–sep (heide), okt (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend — het bos is dan op zijn levendigst.',
 'why': ['De naam <b>roderveld</b> = gerooid, gemeenschappelijk veld.',
         '87 ha <b>gemengd bos, heide en vennetjes</b> bij het Everlo.',
         'Natuurmonumenten vervangt <b>naald- door loofhout</b>.',
         'Dood hout blijft liggen — goed voor <b>bosuil en zwarte specht</b>.'],
 'phen': ['<span class="months">Apr–Jun</span> 🐦 <b>Vuurgoudhaantje, tjiftjaf en fitis</b> in de kruinen.',
          '<span class="months">Mei–Jun</span> 🌼 <b>Klaverzuring en heksenkruid</b> op de bosbodem.',
          '<span class="months">Aug–Sep</span> 🌸 <b>Heide</b> kleurt de open plekken.',
          '<span class="months">Okt</span> 🍄 <b>Paddenstoelen</b> op dood hout.'],
 'wild': ['🐦 Vuurgoudhaantje · Tjiftjaf · Fitis', '🦉 Bosuil · Zwarte specht', '🦇 Vleermuizen in de oude bomen', '🌼 Klaverzuring · Heksenkruid · Varens', '🌳 Zomereik · Beuk · Grove den'],
 'trail': ['Parkeren bij havezathe <b>Het Everlo</b> (Everlostraat 16, Rossum).',
           'Twee gemarkeerde routes starten er — onderdeel van het <b>Wandelnetwerk Regio Twente</b>.',
           'Luister in april naar het <b>zangconcert</b> in de kruinen.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · 🌳 Bos en heide · 🚶 Wandelnetwerk'
}, {
 'tags': ['Overijssel · Dinkelland', 'Wood · mixed woodland with heath and fens by the Everlo', 'list 36 · no. 334'],
 'loc': '📍 Rossum/Volthe, Dinkelland municipality · Nature area · c. 87 ha',
 'desc': 'The <b>Roderveld</b> is a nature area of some 87 hectares near Rossum, close to the havezate <b>Het Everlo</b>. The name betrays its past: <b>roden</b> means to clear — a <b>veld</b> was once common, meagrely used land. Today it is a patchwork of <b>mixed woodland, heath and a few small fens</b>, managed by Natuurmonumenten. In recent years the conifers have gradually gone, so broadleaf trees and the ground flora — <b>wood sorrel, enchanter\'s nightshade and ferns</b> — get more light, and dead wood stays put for <b>tawny owl, black woodpecker and fungi</b>. In the canopy sing firecrest, chiffchaff and willow warbler.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr–Jun</b> (song), Aug–Sep (heath), Oct (fungi)<br>\n    <b>Best time of day:</b> Morning — the wood is at its liveliest.',
 'why': ['The name <b>roderveld</b> = cleared, common field.',
         '87 ha of <b>mixed woodland, heath and fens</b> by the Everlo.',
         'Natuurmonumenten replaces <b>conifer with broadleaf</b>.',
         'Dead wood stays put — good for <b>tawny owl and black woodpecker</b>.'],
 'phen': ['<span class="months">Apr–Jun</span> 🐦 <b>Firecrest, chiffchaff and willow warbler</b> in the canopy.',
          '<span class="months">May–Jun</span> 🌼 <b>Wood sorrel and enchanter\'s nightshade</b> on the floor.',
          '<span class="months">Aug–Sep</span> 🌸 <b>Heath</b> colours the clearings.',
          '<span class="months">Oct</span> 🍄 <b>Fungi</b> on dead wood.'],
 'wild': ['🐦 Firecrest · Chiffchaff · Willow warbler', '🦉 Tawny owl · Black woodpecker', '🦇 Bats in the old trees', '🌼 Wood sorrel · Enchanter\'s nightshade · Ferns', '🌳 Pedunculate oak · Beech · Scots pine'],
 'trail': ['Park at havezate <b>Het Everlo</b> (Everlostraat 16, Rossum).',
           'Two marked routes start there — part of the <b>Wandelnetwerk Regio Twente</b>.',
           'Listen in April for the <b>song concert</b> in the canopy.'],
 'foot': '🐕 Dogs on lead · 💶 Free · 🌳 Wood and heath · 🚶 Walking network'
}))

C.append(mk.card(1616, 'Hakenberg', {
 'tags': ['Overijssel · Losser', 'Landgoed · stuwwalheuvel met park in landschapsstijl', 'list 36 · no. 335'],
 'loc': '📍 Beuningen/De Lutte, gemeente Losser · Landgoed · 54,4 m',
 'desc': 'De <b>Hakenberg</b> is een 54,4 meter hoge heuvel ten zuidwesten van Beuningen, de zuidelijke uitloper van het <b>stuwwalcomplex Enschede-Oldenzaal</b> — in het illustere rijtje van Tankenberg en Paasberg. In 1927 verrees op de top een houten villa; het landgoed is nu van <b>Natuurmonumenten</b>. Uniek is de combinatie van oud <b>boerenland</b> — akkers met biologisch geteelde <b>winterrogge</b>, korenbloemen en akkerviooltjes — en een park in <b>Engelse landschapsstijl</b> met witte hekken, waar de zeldzame <b>grote keverorchis</b> groeit. Over de westflank loopt de Roelinksbeek.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei–jul</b> (orchidee en akkerbloemen), okt (herfst)<br>\n    <b>Beste tijd van de dag:</b> Late middag over de glooiende velden.',
 'why': ['Heuvel van <b>54,4 meter</b> — uitloper van de stuwwal Oldenzaal.',
         'Villa uit <b>1927</b> op de top; landgoed van Natuurmonumenten.',
         '<b>Winterrogge</b>, korenbloem en akkerviooltje op de akkers.',
         'Zeldzame <b>grote keverorchis</b> in het landschapspark.'],
 'phen': ['<span class="months">Mei–Jun</span> 🌸 <b>Korenbloemen</b> in de roggeakkers.',
          '<span class="months">Jun–Jul</span> 🌼 <b>Grote keverorchis</b> in het park.',
          '<span class="months">Apr–Jun</span> 🐦 <b>Geelgors en kneu</b> langs de velden.',
          '<span class="months">Okt</span> 🍂 <b>Herfstkleur</b> in de lanen.'],
 'wild': ['🐦 Geelgors · Kneu · Torenvalk', '🦌 Ree · Haas · Egel', '🦋 Atalanta · Dagpauwoog', '🌼 Grote keverorchis · Korenbloem · Akkerviooltje', '🌳 Zomereik · Beuk · Winterlinde'],
 'trail': ['Parkeren bij <b>Beuningen</b> (Hakenbergweg); wandelnetwerk Oost.',
           'Loop door de <b>witte landgoedhekken</b> langs boomgaard en boerenschuur.',
           'Zoek in juni de <b>grote keverorchis</b> in het park.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · 🌾 Akkers en landschapspark · 🚶 Wandelnetwerk'
}, {
 'tags': ['Overijssel · Losser', 'Estate · ice-pushed hill with landscape-style park', 'list 36 · no. 335'],
 'loc': '📍 Beuningen/De Lutte, Losser municipality · Estate · 54.4 m',
 'desc': 'The <b>Hakenberg</b> is a 54.4-metre hill south-west of Beuningen, the southern outrunner of the <b>Enschede-Oldenzaal ice-pushed ridge</b> — in the illustrious company of Tankenberg and Paasberg. In 1927 a wooden villa rose on the summit; the estate now belongs to <b>Natuurmonumenten</b>. Unique is the combination of old <b>farmland</b> — fields of organically grown <b>winter rye</b>, cornflowers and field pansies — and a park in <b>English landscape style</b> with white gates, where the rare <b>broad-leaved helleborine</b> grows. The Roelinksbeek runs along the west flank.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May–Jul</b> (orchid and field flowers), Oct (autumn)<br>\n    <b>Best time of day:</b> Late afternoon over the rolling fields.',
 'why': ['A hill of <b>54.4 metres</b> — outrunner of the Oldenzaal ridge.',
         'Villa of <b>1927</b> on the summit; Natuurmonumenten estate.',
         '<b>Winter rye</b>, cornflower and field pansy on the fields.',
         'Rare <b>broad-leaved helleborine</b> in the landscape park.'],
 'phen': ['<span class="months">May–Jun</span> 🌸 <b>Cornflowers</b> in the rye fields.',
          '<span class="months">Jun–Jul</span> 🌼 <b>Broad-leaved helleborine</b> in the park.',
          '<span class="months">Apr–Jun</span> 🐦 <b>Yellowhammer and linnet</b> along the fields.',
          '<span class="months">Oct</span> 🍂 <b>Autumn colour</b> in the avenues.'],
 'wild': ['🐦 Yellowhammer · Linnet · Kestrel', '🦌 Roe deer · Hare · Hedgehog', '🦋 Red admiral · Peacock', '🌼 Broad-leaved helleborine · Cornflower · Field pansy', '🌳 Pedunculate oak · Beech · Small-leaved lime'],
 'trail': ['Park at <b>Beuningen</b> (Hakenbergweg); walking network East.',
           'Pass through the <b>white estate gates</b> past orchard and farm barn.',
           'Look for the <b>broad-leaved helleborine</b> in the park in June.'],
 'foot': '🐕 Dogs on lead · 💶 Free · 🌾 Fields and landscape park · 🚶 Walking network'
}))

C.append(mk.card(1617, 'Egheria', {
 'tags': ['Overijssel · Losser', 'Landgoed · de Tankenberg, hoogste punt van Overijssel', 'list 36 · no. 336'],
 'loc': '📍 De Lutte/Oldenzaal, gemeente Losser · Landgoed · 85 m',
 'desc': 'Landgoed <b>Egheria</b> strekt zich uit op en rond de <b>Tankenberg</b>, met zo’n 85 meter het hoogste punt van Overijssel. Op de top staat een <b>koepel</b>, omgeven door sagen: volgens een van de verhalen stond hier aan het begin van de jaartelling een tempel gewijd aan de Germaanse vruchtbaarheidsgodin <b>Tanfana</b>. Bij helder weer kijk je ver Duitsland in. Het landgoed zelf is een bijna onaangetast <b>Twents hoevenlandschap</b>: oude boerderijen omgeven door akkers, weilanden, houtwallen en bossen — een omgeving die bijzonder geschikt is voor <b>reeën</b>. Natuurmonumenten beheert het geheel.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Heel jaar</b> (uitzicht), apr–jun (zang), okt (herfst)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend — reeën langs de bosranden.',
 'why': ['De <b>Tankenberg</b> is het hoogste punt van Overijssel (±85 m).',
         'De <b>koepel</b> is omgeven door de Tanfana-legende.',
         'Bij helder weer kijk je <b>ver Duitsland</b> in.',
         'Bijna onaangetast <b>hoevenlandschap</b> — domein van reeën.'],
 'phen': ['<span class="months">Mrt–Apr</span> 🌼 <b>Voorjaarsbloei</b> in de houtwallen.',
          '<span class="months">Apr–Jun</span> 🐦 <b>Geelgors en boomleeuwerik</b> op de akkers.',
          '<span class="months">Mei–Jul</span> 🦌 <b>Reeën</b> grazen langs de bosranden.',
          '<span class="months">Okt</span> 🍂 <b>Herfstkleur</b> en vér uitzicht.'],
 'wild': ['🦌 Ree · Haas · Das', '🐦 Geelgors · Boomleeuwerik · Buizerd', '🦋 Atalanta · Koevinkje', '🌼 Gewone margriet · Knoopkruid', '🌳 Zomereik · Beuk · Meidoorn'],
 'trail': ['Parkeren bij de <b>koepel</b> (Tankenbergweg 4, De Lutte).',
           'Beklim de top voor het <b>uitzicht tot in Duitsland</b>.',
           'Wandel het <b>hoevenlandschap</b> rond de boerderijen af.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · 🔭 Hoogste punt Overijssel · 🚶 Wandelpaden'
}, {
 'tags': ['Overijssel · Losser', 'Estate · the Tankenberg, highest point of Overijssel', 'list 36 · no. 336'],
 'loc': '📍 De Lutte/Oldenzaal, Losser municipality · Estate · 85 m',
 'desc': 'The <b>Egheria</b> estate stretches over and around the <b>Tankenberg</b>, at about 85 metres the highest point of Overijssel. On the summit stands a <b>cupola</b>, wrapped in legend: according to one tale a temple to the Germanic fertility goddess <b>Tanfana</b> stood here at the start of the common era. On clear days you look far into Germany. The estate itself is an almost untouched <b>Twente farmstead landscape</b>: old farms ringed by fields, meadows, hedge banks and woods — country ideally suited to <b>roe deer</b>. Natuurmonumenten manages it all.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Year-round</b> (views), Apr–Jun (song), Oct (autumn)<br>\n    <b>Best time of day:</b> Early morning — roe deer along the wood edges.',
 'why': ['The <b>Tankenberg</b> is the highest point of Overijssel (±85 m).',
         'The <b>cupola</b> is wrapped in the Tanfana legend.',
         'On clear days you look <b>far into Germany</b>.',
         'Almost untouched <b>farmstead landscape</b> — domain of roe deer.'],
 'phen': ['<span class="months">Mar–Apr</span> 🌼 <b>Spring blossom</b> in the hedge banks.',
          '<span class="months">Apr–Jun</span> 🐦 <b>Yellowhammer and woodlark</b> on the fields.',
          '<span class="months">May–Jul</span> 🦌 <b>Roe deer</b> graze along the wood edges.',
          '<span class="months">Oct</span> 🍂 <b>Autumn colour</b> and far views.'],
 'wild': ['🦌 Roe deer · Hare · Badger', '🐦 Yellowhammer · Woodlark · Buzzard', '🦋 Red admiral · Meadow brown', '🌼 Oxeye daisy · Brown knapweed', '🌳 Pedunculate oak · Beech · Hawthorn'],
 'trail': ['Park at the <b>cupola</b> (Tankenbergweg 4, De Lutte).',
           'Climb the summit for the <b>view into Germany</b>.',
           'Walk the <b>farmstead landscape</b> around the farms.'],
 'foot': '🐕 Dogs on lead · 💶 Free · 🔭 Highest point of Overijssel · 🚶 Footpaths'
}))

C.append(mk.card(1618, "'t Hanhof", {
 'tags': ['Overijssel · Losser', 'Erf · buitengoedje aan de voet van de Kribberug', 'list 36 · no. 337'],
 'loc': '📍 De Lutte, gemeente Losser · Erf · Klein',
 'desc': 'Over <b>’t Hanhof</b> is weinig meer te vinden dan wat de oude gidsen erover melden — en dat is precies zijn waarde. De <i>Gids voor Twente</i> van 1917 schrijft: “Noordwaarts, door het dal van Harbert, komt men bij de belvedère op een hoogte nabij het aardige buitentje Duivendaal. Van hier zou men over ’t Hanhof de Kribberug en daarachter het woeste duinlandschap Lutterzand kunnen bereiken.” Het was dus een <b>doorgangsplek</b> op de route naar het Lutterzand: een erf aan de voet van de <b>Kribberug</b>, waar het kleinschalige hoevenland van De Lutte overgaat in bos en stuifzand. Een naamkaart, meer dan een reservaat.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr–jul</b> (zang), sep–okt (herfst)<br>\n    <b>Beste tijd van de dag:</b> Ochtend langs de zandwegen.',
 'why': ['De <b>1917-gids</b> noemt ’t Hanhof als doorgang naar het Lutterzand.',
         'Gelegen aan de voet van de <b>Kribberug</b>.',
         'Overgang van <b>hoevenland naar bos en stuifzand</b>.',
         'Een <b>naamkaart</b> — dun gedocumenteerd, niet afgebakend.'],
 'phen': ['<span class="months">Mrt–Apr</span> 🌼 <b>Meidoorn</b> bloeit in de wallen.',
          '<span class="months">Apr–Jul</span> 🐦 <b>Geelgors en kneu</b> langs de zandwegen.',
          '<span class="months">Jun–Aug</span> 🦋 <b>Vlinders</b> op de erfranden.',
          '<span class="months">Sep–Okt</span> 🍂 <b>Herfstkleur</b> richting het Lutterzand.'],
 'wild': ['🐦 Geelgors · Kneu · Grasmus', '🦌 Ree · Haas · Egel', '🦋 Dagpauwoog · Atalanta', '🌳 Zomereik · Meidoorn · Hazelaar', '🌼 Gewone margriet · Knoopkruid'],
 'trail': ['Parkeren in <b>De Lutte</b>; zandwegen richting de Kribberug.',
           'Volg de oude route van de <b>1917-gids</b> naar het Lutterzand.',
           'Verwacht <b>geen bebording</b> — het is een naam, geen park.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · ⚠️ Naamkaart — geen afgebakend gebied · 🚶 Zandwegen'
}, {
 'tags': ['Overijssel · Losser', 'Farmstead · small country place at the foot of the Kribberug', 'list 36 · no. 337'],
 'loc': '📍 De Lutte, Losser municipality · Farmstead · Small',
 'desc': 'About <b>’t Hanhof</b> little more can be found than what the old guidebooks record — and that is precisely its value. The 1917 <i>Gids voor Twente</i> writes: “Northward, through the Harbert valley, one reaches the belvedere on a height near the charming little country place Duivendaal. From here one could reach, via ’t Hanhof, the Kribberug and behind it the wild dune landscape of the Lutterzand.” It was, then, a <b>waypoint</b> on the route to the Lutterzand: a farmstead at the foot of the <b>Kribberug</b>, where the small-scale farmland of De Lutte grades into wood and drift sand. A name-entry, more than a reserve.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr–Jul</b> (song), Sep–Oct (autumn)<br>\n    <b>Best time of day:</b> Morning along the sandy lanes.',
 'why': ['The <b>1917 guide</b> names ’t Hanhof as the way to the Lutterzand.',
         'Lies at the foot of the <b>Kribberug</b>.',
         'Transition from <b>farmland to wood and drift sand</b>.',
         'A <b>name-entry</b> — thinly documented, not demarcated.'],
 'phen': ['<span class="months">Mar–Apr</span> 🌼 <b>Hawthorn</b> flowers in the banks.',
          '<span class="months">Apr–Jul</span> 🐦 <b>Yellowhammer and linnet</b> along the sandy lanes.',
          '<span class="months">Jun–Aug</span> 🦋 <b>Butterflies</b> on the yard edges.',
          '<span class="months">Sep–Oct</span> 🍂 <b>Autumn colour</b> towards the Lutterzand.'],
 'wild': ['🐦 Yellowhammer · Linnet · Whitethroat', '🦌 Roe deer · Hare · Hedgehog', '🦋 Peacock · Red admiral', '🌳 Pedunculate oak · Hawthorn · Hazel', '🌼 Oxeye daisy · Brown knapweed'],
 'trail': ['Park in <b>De Lutte</b>; sandy lanes towards the Kribberug.',
           'Follow the old <b>1917-guide</b> route to the Lutterzand.',
           'Expect <b>no signposts</b> — it is a name, not a park.'],
 'foot': '🐕 Dogs on lead · 💶 Free · ⚠️ Name-entry — no demarcated area · 🚶 Sandy lanes'
}))

C.append(mk.card(1619, 'Molterheurne', {
 'tags': ['Overijssel · Losser', 'Es · oude es met winterrogge bij De Lutte', 'list 36 · no. 338'],
 'loc': '📍 De Lutte, gemeente Losser · Natuurgebied · ca. 6 ha',
 'desc': 'De marke <b>De Lutte</b> was ooit de machtigste en rijkste van Twente, zo groot dat ze in vier <b>heurnes</b> was verdeeld: Rooderheurne, Molterheurne, Elfterheurne en Hengelheurne. De <b>Molterheurne</b> is een oude <b>es</b> van zo’n zes hectare, waar Natuurmonumenten jaarlijks <b>winterrogge</b> inzaait — biologisch, zodat <b>klaproos en korenbloem</b> tussen het gewas bloeien. In juni en juli pikken <b>patrijs, ree en haas</b> graag een graantje mee, en in de avond klinkt de <b>bramensprinkhaan</b>. Het veldje vormt bovendien een buffer langs de <b>Bloemenbeek</b>, waar goudveil en dotterbloem groeien.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun–jul</b> (goudgele rogge), apr–jun (beekflora)<br>\n    <b>Beste tijd van de dag:</b> Namiddag en avond — dan klinkt de bramensprinkhaan.',
 'why': ['Een van de vier <b>heurnes</b> van de oude marke De Lutte.',
         'Natuurmonumenten zaait er <b>winterrogge</b>, biologisch.',
         '<b>Klaproos en korenbloem</b> bloeien tussen het gewas.',
         'Buffer voor de <b>Bloemenbeek</b> met goudveil en dotterbloem.'],
 'phen': ['<span class="months">Jun–Jul</span> 🌾 <b>Goudgele rogge</b> — patrijs, ree en haas pikken mee.',
          '<span class="months">Jun–Aug</span> 🌸 <b>Klaproos en korenbloem</b> in de akker.',
          '<span class="months">Apr–Jun</span> 🌼 <b>Goudveil en dotterbloem</b> langs de Bloemenbeek.',
          '<span class="months">Jul–Sep</span> 🦗 <b>Bramensprinkhaan</b> klinkt in de avond.'],
 'wild': ['🐦 Patrijs · Geelgors · Kneu', '🦌 Ree · Haas · Egel', '🦗 Bramensprinkhaan · Groene zandloopkever', '🌼 Klaproos · Korenbloem · Goudveil', '🌾 Winterrogge · Zomereik'],
 'trail': ['Kijken vanaf de <b>Bentheimerstraat</b> ten noorden van De Lutte.',
           'Het veld is <b>niet toegankelijk</b> — het landschap is goed te overzien.',
           'Kom in juli voor de <b>goudgele rogge</b>.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · ⚠️ Niet toegankelijk — kijken vanaf de weg · 🌾 Winterrogge-es'
}, {
 'tags': ['Overijssel · Losser', 'Es · old es with winter rye near De Lutte', 'list 36 · no. 338'],
 'loc': '📍 De Lutte, Losser municipality · Nature area · c. 6 ha',
 'desc': 'The marke of <b>De Lutte</b> was once the mightiest and richest in Twente, so large that it was divided into four <b>heurnes</b>: Rooderheurne, Molterheurne, Elfterheurne and Hengelheurne. The <b>Molterheurne</b> is an old <b>es</b> of about six hectares, where Natuurmonumenten sows <b>winter rye</b> each year — organically, so that <b>poppy and cornflower</b> flower among the crop. In June and July <b>partridge, roe deer and hare</b> gladly take a grain, and in the evening the <b>bramble cricket</b> sounds. The little field also forms a buffer along the <b>Bloemenbeek</b>, where golden saxifrage and marsh marigold grow.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun–Jul</b> (golden rye), Apr–Jun (brook flora)<br>\n    <b>Best time of day:</b> Late afternoon and evening — the bramble cricket calls.',
 'why': ['One of the four <b>heurnes</b> of the old marke of De Lutte.',
         'Natuurmonumenten sows <b>winter rye</b>, organically.',
         '<b>Poppy and cornflower</b> flower among the crop.',
         'A buffer for the <b>Bloemenbeek</b> with golden saxifrage and marigold.'],
 'phen': ['<span class="months">Jun–Jul</span> 🌾 <b>Golden rye</b> — partridge, roe deer and hare help themselves.',
          '<span class="months">Jun–Aug</span> 🌸 <b>Poppy and cornflower</b> in the field.',
          '<span class="months">Apr–Jun</span> 🌼 <b>Golden saxifrage and marsh marigold</b> by the Bloemenbeek.',
          '<span class="months">Jul–Sep</span> 🦗 <b>Bramble cricket</b> sounds in the evening.'],
 'wild': ['🐦 Partridge · Yellowhammer · Linnet', '🦌 Roe deer · Hare · Hedgehog', '🦗 Bramble cricket · Green tiger beetle', '🌼 Poppy · Cornflower · Golden saxifrage', '🌾 Winter rye · Pedunculate oak'],
 'trail': ['View from the <b>Bentheimerstraat</b> north of De Lutte.',
           'The field is <b>not accessible</b> — the landscape is easily surveyed.',
           'Come in July for the <b>golden rye</b>.'],
 'foot': '🐕 Dogs on lead · 💶 Free · ⚠️ Not accessible — view from the road · 🌾 Winter-rye es'
}))

mk.insert(C, '1614')
mk.progress(1619)
mk.check()
