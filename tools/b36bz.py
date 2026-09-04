# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1665, 'De Rijndijk', {
 'tags': ['Zuid-Holland · Hazerswoude-Rijndijk', 'Rivierdijk · oude dijk en jaagpad langs de Oude Rijn', 'list 36 · no. 384'],
 'loc': '📍 Hazerswoude-Rijndijk/Koudekerk, gemeente Alphen aan den Rijn · Rivierdijk · Lang lint',
 'desc': 'De <b>Rijndijk</b> is de eeuwenoude dijk langs de <b>Oude Rijn</b>, tussen Leiden en Alphen aan den Rijn, met het langgerekte dorp <b>Hazerswoude-Rijndijk</b> dat er zijn naam aan dankt. Langs de rivier loopt het <b>jaagpad</b>, waar vroeger paarden de <b>trekschuiten</b> tussen Leiden en Utrecht voorttrokken; de paarden werden regelmatig \u2019ververst\u2019 en overgezet bij de Boerenschouw en de Prinsenschouw. Aan de dijk liggen oude boerderijen in karakteristieke lintbebouwing, en molens als de <b>Rijnenburgermolen</b> (1722), die de Rijnenburgerpolder tot 1965 bemaalde. Bij Koudekerk stond tot 1838 het overzetveer <b>\u2019de Olde Schouw\u2019</b>, dat werd vervangen door een stenen boogbrug; de huidige Koudekerkse brug dateert van 1929. Vanaf de dijk kijk je uit over de weidse polders van het Groene Hart.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr–sep</b> (jaagpad en molens), mrt–apr (weidevogels)<br>\n    <b>Beste tijd van de dag:</b> Ochtend — rust op het jaagpad langs de Rijn.',
 'why': ['De oude <b>dijk en het jaagpad</b> langs de Oude Rijn.', 'De <b>trekschuitroute</b> tussen Leiden en Utrecht.', 'De <b>Rijnenburgermolen</b> (1722) en andere poldermolens.', 'Lintbebouwing van boerderijen met uitzicht over de polders.'],
 'phen': ['<span class="months">Mrt–Apr</span> 🐦 <b>Weidevogels</b> in de polders achter de dijk.', '<span class="months">Mei–Jun</span> 🌼 <b>Bloeiende dijkflora</b> langs het jaagpad.', '<span class="months">Mei–Sep</span> 🌀 <b>Draaiende molens</b> op molendagen.', '<span class="months">Okt</span> 🍂 <b>Herfstkleur</b> langs de Oude Rijn.'],
 'wild': ['🐦 Grutto · Kievit · Boerenzwaluw', '🦢 Knobbelzwaan · Wilde eend · Meerkoet', '🦋 Dagpauwoog · Kleine vos · Citroenvlinder', '🌼 Margriet · Knoopkruid · Rode klaver', '🌳 Knotwilg · Els · Populier'],
 'trail': ['Wandel het <b>jaagpad</b> langs de Oude Rijn vanaf Hazerswoude-Rijndijk.', 'Steek bij de <b>Koudekerkse brug</b> over naar Koudekerk aan den Rijn.', 'Fiets of wandel langs de <b>Rijnenburgermolen</b> aan de oostzijde.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · ⚠️ Fietsers op het jaagpad · 🚶/🚲 Dijk en jaagpad'
}, {
 'tags': ['Zuid-Holland · Hazerswoude-Rijndijk', 'River dike · old dike and towpath along the Oude Rijn', 'list 36 · no. 384'],
 'loc': '📍 Hazerswoude-Rijndijk/Koudekerk, Alphen aan den Rijn municipality · River dike · Long ribbon',
 'desc': 'The <b>Rijndijk</b> is the age-old dike along the <b>Oude Rijn</b>, between Leiden and Alphen aan den Rijn, with the elongated village of <b>Hazerswoude-Rijndijk</b> that takes its name from it. Along the river runs the <b>towpath</b>, where horses once pulled the <b>trekschuiten</b> (passenger barges) between Leiden and Utrecht; the horses were regularly \u2019refreshed\u2019 and ferried across at the Boerenschouw and the Prinsenschouw. Along the dike lie old farmhouses in characteristic ribbon development, and mills such as the <b>Rijnenburgermolen</b> (1722), which drained the Rijnenburgerpolder until 1965. At Koudekerk stood the ferry <b>\u2019de Olde Schouw\u2019</b> until 1838, replaced by a stone arch bridge; the present Koudekerkse brug dates from 1929. From the dike you look out over the wide polders of the Groene Hart.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr–Sep</b> (towpath and mills), Mar–Apr (meadow birds)<br>\n    <b>Best time of day:</b> Morning — quiet on the towpath along the Rijn.',
 'why': ['The old <b>dike and towpath</b> along the Oude Rijn.', 'The <b>trekschuit route</b> between Leiden and Utrecht.', 'The <b>Rijnenburgermolen</b> (1722) and other polder mills.', 'Ribbon development of farms with views over the polders.'],
 'phen': ['<span class="months">Mar–Apr</span> 🐦 <b>Meadow birds</b> in the polders behind the dike.', '<span class="months">May–Jun</span> 🌼 <b>Flowering dike flora</b> along the towpath.', '<span class="months">May–Sep</span> 🌀 <b>Turning mills</b> on mill days.', '<span class="months">Oct</span> 🍂 <b>Autumn colour</b> along the Oude Rijn.'],
 'wild': ['🐦 Black-tailed godwit · Lapwing · Barn swallow', '🦢 Mute swan · Mallard · Coot', '🦋 Peacock · Small tortoiseshell · Brimstone', '🌼 Oxeye daisy · Brown knapweed · Red clover', '🌳 Pollard willow · Alder · Poplar'],
 'trail': ['Walk the <b>towpath</b> along the Oude Rijn from Hazerswoude-Rijndijk.', 'Cross at the <b>Koudekerkse brug</b> to Koudekerk aan den Rijn.', 'Cycle or walk past the <b>Rijnenburgermolen</b> on the east side.'],
 'foot': '🐕 Dogs on lead · 💶 Free · ⚠️ Cyclists on the towpath · 🚶/🚲 Dike and towpath'
}))

C.append(mk.card(1666, 'Kruiskade', {
 'tags': ['Zuid-Holland · Hazerswoude-Rijndijk', 'Polderkade · oude waterscheiding met spookverlaat', 'list 36 · no. 385'],
 'loc': '📍 Hazerswoude-Rijndijk, gemeente Alphen aan den Rijn · Polderkade · ca. 1,3 km',
 'desc': 'De <b>Kruiskade</b> ligt aan de noordkant van de voormalige <b>Rietveldse polder</b>, in het gebied dat tegenwoordig het <b>Spookverlaat</b> wordt genoemd. De kade werd in <b>1470</b> aangelegd voor de drooglegging van de Hoornse polder aan de Rijn; na 1648 vormde hij de waterscheiding tussen de Hoornse en de Rietveldse polder, die elk hun eigen peil en molens hadden. In 1659 werd in de Dwarswetering een <b>verlaat</b> (sluisje) gebouwd, dat in de negentiende eeuw vanwege een legende <b>\u2019spookverlaat\u2019</b> ging heten; het werd in 1960 gesloopt. Sinds een ruilverkaveling kreeg de omgeving een groenbestemming met bosaanplant en waterpartijen. De ruim 1300 meter lange kade ligt tussen de <b>Compierekade</b> en de Papenvaart.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr–sep</b> (kade en waterpartijen), mrt–mei (weidevogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend — stilte langs de oude kade.',
 'why': ['Een <b>waterscheiding</b> uit 1470 tussen twee polders.', 'De naam <b>Spookverlaat</b> en de legende erachter.', 'Ruim <b>1300 meter</b> oude kade tussen Compierekade en Papenvaart.', 'Na ruilverkaveling ingericht als <b>groen en water</b>.'],
 'phen': ['<span class="months">Mrt–Mei</span> 🐦 <b>Weidevogels</b> in de Riethoornse polder.', '<span class="months">Mei–Jul</span> 🌼 <b>Bloeiende kade</b> en waterplanten.', '<span class="months">Jun–Aug</span> 🦋 <b>Vlinders en libellen</b> bij de waterpartijen.', '<span class="months">Sep–Okt</span> 🍂 <b>Herfst</b> in de aangeplante bosjes.'],
 'wild': ['🐦 Kievit · Grutto · Rietgors', '🦢 Meerkoet · Wilde eend · Blauwe reiger', '🦋 Dagpauwoog · Kleine vos · Atalanta', '🌼 Echte koekoeksbloem · Dotterbloem · Gele lis', '🌳 Zwarte els · Wilg · Meidoorn'],
 'trail': ['Wandel de <b>Kruiskade</b> tussen de Compierekade en de Papenvaart.', 'Combineer met het <b>Spookverlaat</b> en het Oostvaartpad.', 'Start bij Hazerswoude-Rijndijk of het Rietveldsepad.'],
 'foot': '🐕 Honden aan de lijn · 💶 Gratis · ⚠️ Soms drassig · 🚶 Kade en graspaden'
}, {
 'tags': ['Zuid-Holland · Hazerswoude-Rijndijk', 'Polder bank · old water divide with a \u2019ghost\u2019 lock', 'list 36 · no. 385'],
 'loc': '📍 Hazerswoude-Rijndijk, Alphen aan den Rijn municipality · Polder bank · c. 1.3 km',
 'desc': 'The <b>Kruiskade</b> lies on the north side of the former <b>Rietveldse polder</b>, in the area nowadays called the <b>Spookverlaat</b>. The bank was laid out in <b>1470</b> for the reclamation of the Hoornse polder on the Rijn; after 1648 it formed the water divide between the Hoornse and the Rietveldse polders, each with its own water level and mills. In 1659 a <b>verlaat</b> (small lock) was built in the Dwarswetering, which in the nineteenth century came to be called <b>\u2019spookverlaat\u2019</b> (\u2019ghost lock\u2019) after a legend; it was demolished in 1960. After a land consolidation the surroundings were given a green purpose with tree planting and ponds. The more than 1300-metre-long bank lies between the <b>Compierekade</b> and the Papenvaart.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr–Sep</b> (bank and ponds), Mar–May (meadow birds)<br>\n    <b>Best time of day:</b> Early morning — quiet along the old bank.',
 'why': ['A <b>water divide</b> of 1470 between two polders.', 'The name <b>Spookverlaat</b> and the legend behind it.', 'Over <b>1300 metres</b> of old bank between Compierekade and Papenvaart.', 'Laid out as <b>green space and water</b> after land consolidation.'],
 'phen': ['<span class="months">Mar–May</span> 🐦 <b>Meadow birds</b> in the Riethoornse polder.', '<span class="months">May–Jul</span> 🌼 <b>Flowering bank</b> and water plants.', '<span class="months">Jun–Aug</span> 🦋 <b>Butterflies and dragonflies</b> at the ponds.', '<span class="months">Sep–Oct</span> 🍂 <b>Autumn</b> in the planted copses.'],
 'wild': ['🐦 Lapwing · Godwit · Reed bunting', '🦢 Coot · Mallard · Grey heron', '🦋 Peacock · Small tortoiseshell · Red admiral', '🌼 Ragged robin · Marsh marigold · Yellow iris', '🌳 Black alder · Willow · Hawthorn'],
 'trail': ['Walk the <b>Kruiskade</b> between the Compierekade and the Papenvaart.', 'Combine with the <b>Spookverlaat</b> and the Oostvaartpad.', 'Start from Hazerswoude-Rijndijk or the Rietveldsepad.'],
 'foot': '🐕 Dogs on lead · 💶 Free · ⚠️ Sometimes soggy · 🚶 Bank and grass paths'
}))

C.append(mk.card(1667, 'Spijkerboorsekade en Coppierenkade', {
 'tags': ['Zuid-Holland · Alphen aan den Rijn/Hazerswoude', 'Polderkades · houtwallen en knotbomen tussen Alphen en de kwekerijen', 'list 36 · no. 386'],
 'loc': '📍 Hazerswoude-Dorp/Alphen aan den Rijn · Polderkades · ca. 7 ha',
 'desc': 'De <b>Spijkerboorsekade</b> en de <b>Coppierenkade</b> liggen ten zuiden van Alphen aan den Rijn, op de grens van het veenweidelandschap en de <b>Boskoopse kwekerijen</b>. De Spijkerboorse Kade (7 hectare, Zuid-Hollands Landschap) was van oudsher een kade met een <b>houtwal</b>, waarschijnlijk aangelegd om de kwetsbare kwekerijen tegen de wind te beschermen. Langs het smalle onverharde pad staan <b>knotbomen</b>, een historisch hakhoutbosje van zwarte els en es, en een <b>poel</b> vol amfibieën en libellen. In het schone slootwater groeit <b>krabbenscheer</b>, een veeleisende drijfplant, en langs de oevers bloeien echte koekoeksbloem en <b>watermunt</b> met zijn frisse pepermuntgeur. Bij de Coppierenkade stond al vóór 1615 de Rietveldse (Behoude Kost)molen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei–jun</b> (krabbenscheer en koekoeksbloem), apr–sep (vlinders)<br>\n    <b>Beste tijd van de dag:</b> Ochtend — libellen boven de poel.',
 'why': ['Een <b>houtwal</b> die de Boskoopse kwekerijen beschermde.', '<b>Knotbomen</b> en een hakhoutbosje van zwarte els en es.', '<b>Krabbenscheer</b> in de schone sloten.', 'Een <b>poel</b> vol amfibieën en libellen.'],
 'phen': ['<span class="months">Mei–Jun</span> 🌼 <b>Krabbenscheer</b> en echte koekoeksbloem.', '<span class="months">Mei–Aug</span> 🦋 <b>Vlinders en libellen</b> boven de poel.', '<span class="months">Jul–Aug</span> 🌸 <b>Watermunt</b> verspreidt zijn pepermuntgeur.', '<span class="months">Sep</span> 🪵 <b>Knotwerk</b> door de knotploeg.'],
 'wild': ['🐦 Kleine karekiet · Rietgors · IJsvogel', '🦢 Wilde eend · Meerkoet · Waterhoen', '🦋 Groene glazenmaker · Vuurjuffer · Weidebeekjuffer', '🌼 Krabbenscheer · Echte koekoeksbloem · Watermunt', '🌳 Knotwilg · Zwarte els · Es'],
 'trail': ['Wandel het onverharde pad langs de <b>Spijkerboorsche Wetering</b>.', 'De doorgaande route loopt tussen de <b>Compierekade</b> en het Bedelaarsbos.', 'Bereikbaar vanaf de <b>Kooiweg</b> en het Rietveldsepad.'],
 'foot': '🐕 Honden aangelijnd · 💶 Gratis · ⚠️ Nat in de winter · 🚶 Smalle graspaden'
}, {
 'tags': ['Zuid-Holland · Alphen aan den Rijn/Hazerswoude', 'Polder banks · wood banks and pollards between Alphen and the nurseries', 'list 36 · no. 386'],
 'loc': '📍 Hazerswoude-Dorp/Alphen aan den Rijn · Polder banks · c. 7 ha',
 'desc': 'The <b>Spijkerboorsekade</b> and the <b>Coppierenkade</b> lie south of Alphen aan den Rijn, on the border of the peat meadow country and the <b>Boskoop nurseries</b>. The Spijkerboorse Kade (7 hectares, Zuid-Hollands Landschap) was traditionally a bank with a <b>wood bank</b>, probably laid out to shelter the vulnerable nurseries from the wind. Along the narrow unpaved path stand <b>pollards</b>, a historic coppice of black alder and ash, and a <b>pool</b> full of amphibians and dragonflies. In the clean ditch water grows <b>water soldier</b> (krabbenscheer), a demanding floating plant, and along the banks flower ragged robin and <b>water mint</b> with its fresh peppermint scent. Near the Coppierenkade stood the Rietveldse (Behoude Kost) mill already before 1615.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May–Jun</b> (water soldier and ragged robin), Apr–Sep (butterflies)<br>\n    <b>Best time of day:</b> Morning — dragonflies above the pool.',
 'why': ['A <b>wood bank</b> that sheltered the Boskoop nurseries.', '<b>Pollards</b> and a coppice of black alder and ash.', '<b>Water soldier</b> in the clean ditches.', 'A <b>pool</b> full of amphibians and dragonflies.'],
 'phen': ['<span class="months">May–Jun</span> 🌼 <b>Water soldier</b> and ragged robin.', '<span class="months">May–Aug</span> 🦋 <b>Butterflies and dragonflies</b> above the pool.', '<span class="months">Jul–Aug</span> 🌸 <b>Water mint</b> spreads its peppermint scent.', '<span class="months">Sep</span> 🪵 <b>Pollarding</b> by the volunteer team.'],
 'wild': ['🐦 Reed warbler · Reed bunting · Kingfisher', '🦢 Mallard · Coot · Moorhen', '🦋 Green hawker · Common blue damselfly · Beautiful demoiselle', '🌼 Water soldier · Ragged robin · Water mint', '🌳 Pollard willow · Black alder · Ash'],
 'trail': ['Walk the unpaved path along the <b>Spijkerboorsche Wetering</b>.', 'The through route runs between the <b>Compierekade</b> and the Bedelaarsbos.', 'Reachable from the <b>Kooiweg</b> and the Rietveldsepad.'],
 'foot': '🐕 Dogs on lead · 💶 Free · ⚠️ Wet in winter · 🚶 Narrow grass paths'
}))

C.append(mk.card(1668, 'De Haaglanden', {
 'tags': ['Zuid-Holland · Delft/Nootdorp', 'Recreatiebos · groene buffer tussen de snelwegen bij Delft', 'list 36 · no. 387'],
 'loc': '📍 Delft/Nootdorp, tussen de A13 en A12 · Recreatiebos · Rijksbufferzone',
 'desc': '<b>De Haaglanden</b> is een recreatiebos in de <b>Randstadgroenstructuur</b>, aangelegd in de buffer tussen de stedelijke agglomeraties van Den Haag, Delft en Rotterdam. Het bos ligt ten noordoosten van Delft, tussen de <b>A13 en de A12</b>, en wordt beheerd door Staatsbosbeheer. Wandelaars vinden er bossen met lanen, bospaden en weggetjes langs landbouwgronden, met <b>geriefbosjes</b> en ruige, bloemrijke bermen. Het sluit aan op de <b>Delftse Hout</b>, het bekende recreatiegebied met het NME-centrum <b>De Papaver</b> en een arboretum/heemtuin. Vooral vlinders en vogels profiteren van de afwisseling tussen bos, ruigte en weiland.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr–sep</b> (vlinders en bloemen), okt (herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Ochtend — rust voordat het recreatieverkeer komt.',
 'why': ['Recreatiebos in de <b>Randstadgroenstructuur</b>.', 'Groene buffer tussen <b>Den Haag, Delft en Rotterdam</b>.', 'Aansluitend op de <b>Delftse Hout</b> met NME-centrum De Papaver.', 'Bossen met lanen, <b>geriefbosjes</b> en ruige bermen.'],
 'phen': ['<span class="months">Apr–Mei</span> 🌼 <b>Bloeiende ruigten</b> en bosranden.', '<span class="months">Mei–Aug</span> 🦋 <b>Vlinders</b> langs de bospaden en heggen.', '<span class="months">Jun–Sep</span> 🌿 <b>Ruige graslanden</b> met koninginnekruid en valeriaan.', '<span class="months">Okt</span> 🍂 <b>Herfstkleur</b> in de aangeplante bossen.'],
 'wild': ['🐦 Buizerd · Grote bonte specht · Zanglijster', '🦌 Ree · Egel · Eekhoorn', '🦋 Dagpauwoog · Atalanta · Kleine vos', '🌼 Koninginnekruid · Valeriaan · Kattenstaart', '🌳 Zomereik · Beuk · Berk'],
 'trail': ['Parkeer bij de <b>Delftse Hout</b> (Kanaalweg/Korftlaan) of langs de Olof Palmenlaan.', 'Wandel of fiets de lanen tussen de <b>A13 en A12</b>.', 'Bezoek het <b>arboretum/heemtuin</b> bij NME-centrum De Papaver.'],
 'foot': '🐕 Honden aangelijnd · 💶 Gratis · ⚠️ Snelwegen in de omgeving · 🚶/🚲 Lanen en bospaden'
}, {
 'tags': ['Zuid-Holland · Delft/Nootdorp', 'Recreation woodland · green buffer between the motorways near Delft', 'list 36 · no. 387'],
 'loc': '📍 Delft/Nootdorp, between the A13 and A12 · Recreation woodland · National buffer zone',
 'desc': '<b>De Haaglanden</b> is a recreation woodland in the <b>Randstad green structure</b>, laid out in the buffer between the urban agglomerations of The Hague, Delft and Rotterdam. The wood lies north-east of Delft, between the <b>A13 and the A12</b>, and is managed by Staatsbosbeheer. Walkers find woods with lanes, forest paths and tracks along farmland, with <b>coppice stands</b> and rough, flower-rich verges. It adjoins the <b>Delftse Hout</b>, the well-known recreation area with the <b>De Papaver</b> nature-education centre and an arboretum/nature garden. Above all butterflies and birds benefit from the mix of woodland, rough growth and meadow.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr–Sep</b> (butterflies and flowers), Oct (autumn colour)<br>\n    <b>Best time of day:</b> Morning — calm before the recreational traffic arrives.',
 'why': ['Recreation woodland in the <b>Randstad green structure</b>.', 'A green buffer between <b>The Hague, Delft and Rotterdam</b>.', 'Adjoining the <b>Delftse Hout</b> with the De Papaver centre.', 'Woods with lanes, <b>coppice stands</b> and rough verges.'],
 'phen': ['<span class="months">Apr–May</span> 🌼 <b>Flowering rough growth</b> and woodland edges.', '<span class="months">May–Aug</span> 🦋 <b>Butterflies</b> along the forest paths and hedges.', '<span class="months">Jun–Sep</span> 🌿 <b>Rough grassland</b> with hemp agrimony and valerian.', '<span class="months">Oct</span> 🍂 <b>Autumn colour</b> in the planted woods.'],
 'wild': ['🐦 Buzzard · Great spotted woodpecker · Song thrush', '🦌 Roe deer · Hedgehog · Squirrel', '🦋 Peacock · Red admiral · Small tortoiseshell', '🌼 Hemp agrimony · Valerian · Purple loosestrife', '🌳 Pedunculate oak · Beech · Birch'],
 'trail': ['Park at the <b>Delftse Hout</b> (Kanaalweg/Korftlaan) or along the Olof Palmenlaan.', 'Walk or cycle the lanes between the <b>A13 and A12</b>.', 'Visit the <b>arboretum/nature garden</b> at the De Papaver centre.'],
 'foot': '🐕 Dogs on lead · 💶 Free · ⚠️ Motorways nearby · 🚶/🚲 Lanes and forest paths'
}))

C.append(mk.card(1669, 'Noorderhout', {
 'tags': ['Zuid-Holland · Gouda', 'Stadsnatuur · geluidswal van puin tot bloemrijk groen', 'list 36 · no. 388'],
 'loc': '📍 Gouda, gemeente Gouda · Stadsnatuur · Geluidswal langs de A12',
 'desc': 'Het <b>Noorderhout</b> ligt aan de noordrand van Gouda, nabij de wijk <b>Plaswijck</b>, en vormt een groene <b>geluidswal</b> langs de A12. De wal is opgebouwd uit grote hoeveelheden puin; deze <b>puinstort</b> werd in de jaren zeventig afgedekt met een dikke laag aarde en beplant. Inmiddels is het uitgegroeid tot een verrassend rijk <b>natuurgebied</b> met een gevarieerde flora en fauna, waar konijnen talrijk zijn en in mei de bloemen uitbundig bloeien. Er is een <b>natuurspeeltuin</b> en een dicht net van wandelpaden; bij nat weer kan het drassig zijn. De KNNV organiseert er plantenexcursies (onder meer <b>moerasandoorn</b>), en het ligt vlak bij de Reeuwijkse Plassen en de Goudse Hout.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei–jun</b> (bloei), apr–sep (vlinders en insecten)<br>\n    <b>Beste tijd van de dag:</b> Ochtend — konijnen en zingende vogels.',
 'why': ['Van <b>puinstort</b> tot bloemrijk natuurgebied.', 'Een <b>geluidswal</b> die de A12 afschermt.', 'Rijke <b>flora en fauna</b> vlak bij de stad.', '<b>Natuurspeeltuin</b> en wandelpaden voor iedereen.'],
 'phen': ['<span class="months">Apr–Mei</span> 🌼 <b>Bloeiende kruiden</b> op de wal.', '<span class="months">Mei–Jul</span> 🦋 <b>Vlinders en insecten</b> tussen de planten.', '<span class="months">Mei–Aug</span> 🌸 <b>Moerasandoorn</b> langs de vochtige randen.', '<span class="months">Sep–Okt</span> 🍂 <b>Herfstkleur</b> over de heesters.'],
 'wild': ['🐦 Groenling · Zanglijster · Winterkoning', '🐇 Konijn · Egel · Veldmuis', '🦋 Dagpauwoog · Kleine vos · Atalanta', '🌼 Moerasandoorn · Wilde peen · Sint-Janskruid', '🌳 Meidoorn · Sleedoorn · Berk'],
 'trail': ['Bereikbaar vanuit de wijk <b>Plaswijck</b> of vanaf de Bloemendaalseweg.', 'Wandel het padennet <b>bovenlangs of onderlangs</b> de wal.', 'Combineer met de <b>Goudse Hout</b> of de Reeuwijkse Plassen.'],
 'foot': '🐕 Honden deels losloopgebied · 💶 Gratis · ⚠️ Bij nat weer drassig · 🚶 Wandelpaden'
}, {
 'tags': ['Zuid-Holland · Gouda', 'Urban nature · a noise barrier from rubble to flower-rich green', 'list 36 · no. 388'],
 'loc': '📍 Gouda, Gouda municipality · Urban nature · Noise barrier along the A12',
 'desc': 'The <b>Noorderhout</b> lies on the northern edge of Gouda, near the <b>Plaswijck</b> district, and forms a green <b>noise barrier</b> along the A12. The wall was built from large quantities of rubble; this <b>rubble dump</b> was covered in the 1970s with a thick layer of earth and planted. Since then it has grown into a surprisingly rich <b>nature area</b> with a varied flora and fauna, where rabbits are plentiful and in May the flowers bloom profusely. There is a <b>nature playground</b> and a dense network of footpaths; in wet weather it can be soggy. The KNNV organises plant excursions there (among others for <b>marsh woundwort</b>), and it lies close to the Reeuwijkse Plassen and the Goudse Hout.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May–Jun</b> (flowering), Apr–Sep (butterflies and insects)<br>\n    <b>Best time of day:</b> Morning — rabbits and singing birds.',
 'why': ['From <b>rubble dump</b> to flower-rich nature area.', 'A <b>noise barrier</b> screening off the A12.', 'Rich <b>flora and fauna</b> close to the city.', 'A <b>nature playground</b> and paths for everyone.'],
 'phen': ['<span class="months">Apr–May</span> 🌼 <b>Flowering herbs</b> on the wall.', '<span class="months">May–Jul</span> 🦋 <b>Butterflies and insects</b> among the plants.', '<span class="months">May–Aug</span> 🌸 <b>Marsh woundwort</b> along the damp edges.', '<span class="months">Sep–Oct</span> 🍂 <b>Autumn colour</b> over the shrubs.'],
 'wild': ['🐦 Greenfinch · Song thrush · Wren', '🐇 Rabbit · Hedgehog · Field vole', '🦋 Peacock · Small tortoiseshell · Red admiral', '🌼 Marsh woundwort · Wild carrot · St John\u2019s wort', '🌳 Hawthorn · Blackthorn · Birch'],
 'trail': ['Reachable from the <b>Plaswijck</b> district or from the Bloemendaalseweg.', 'Walk the path network <b>along the top or the foot</b> of the wall.', 'Combine with the <b>Goudse Hout</b> or the Reeuwijkse Plassen.'],
 'foot': '🐕 Dogs partly off-lead · 💶 Free · ⚠️ Soggy in wet weather · 🚶 Footpaths'
}))

mk.insert(C, '1664')
mk.progress(1669)
mk.check()
