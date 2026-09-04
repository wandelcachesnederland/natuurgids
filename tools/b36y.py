# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1400, 'Ham en Crommenije', {
 'tags': ['Noord-Holland \u00b7 Zaanstad', 'Veenweide \u00b7 moerasland en petgaten', 'list 36 \u00b7 no. 119'],
 'loc': '\U0001f4cd Tussen Krommenie en Uitgeest \u00b7 Veenweide met moeras \u00b7 Groot',
 'desc': '<b>Ham en Crommenije</b> is een uitgestrekt veenweidegebied met twee sprekende namen. <b>Ham</b> is een oud landschapswoord voor een <b>bocht of hoek land in een waterloop</b> \u2014 hetzelfde woord dat in Engelse plaatsnamen op <i>-ham</i> zit. <b>Crommenije</b> is samengesteld uit <i>krom</i> en <i>IJ</i>: de kromme arm van het IJ die hier ooit landinwaarts reikte. Beide namen beschrijven dus water dat er niet meer is. Wat bleef is een van de grootste aaneengesloten <b>veenweidegebieden</b> van Noord-Holland, met natte graslanden, petgaten en rietkragen die deels als moerasnatuur worden beheerd. Het is een van de belangrijkste weidevogelgebieden van de provincie, met <b>grutto, tureluur, kemphaan en watersnip</b>, en in de rietzones broeden <b>bruine kiekendief en snor</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (weidevogels), nov\u2013feb (ganzen en smienten)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 weidevogelkoor boven de open polder.',
 'why': ['<b>Ham</b> = bocht of hoek land in een waterloop, als in Engelse <i>-ham</i>.',
         '<b>Crommenije</b> = de kromme arm van het IJ die hier landinwaarts reikte.',
         'Een van de grootste <b>veenweidegebieden</b> van Noord-Holland.',
         'Topgebied voor <b>grutto, tureluur en kemphaan</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Grutto\u2019s</b> arriveren massaal.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tureluur en watersnip</b> broeden.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33e <b>Snor</b> snort in de rietkragen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Ganzen en smienten</b> in grote aantallen.'],
 'wild': ['\U0001f426 Grutto \u00b7 Tureluur \u00b7 Kemphaan \u00b7 Watersnip', '\U0001f33e Snor \u00b7 Rietzanger \u00b7 Rietgors', '\U0001f985 Bruine kiekendief \u00b7 Blauwe kiekendief (winter)', '\U0001f9a2 Kolgans \u00b7 Grauwe gans \u00b7 Smient', '\U0001f33f Krabbenscheer \u00b7 Waterviolier'],
 'trail': ['Parkeren bij <b>Krommenie</b> of <b>Uitgeest</b>; kijk vanaf dijken en paden.',
           'Blijf in het broedseizoen <b>op de paden</b> \u2014 topweidevogelgebied.',
           'April is de <b>beste maand</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Weidevogelgebied mrt\u2013jun \u00b7 \U0001f97e Nat'
}, {
 'tags': ['North Holland \u00b7 Zaanstad', 'Peat meadow \u00b7 marshland and turf pits', 'list 36 \u00b7 no. 119'],
 'loc': '\U0001f4cd Between Krommenie and Uitgeest \u00b7 Peat meadow with marsh \u00b7 Large',
 'desc': '<b>Ham en Crommenije</b> is an extensive peat-meadow area with two eloquent names. <b>Ham</b> is an old landscape word for a <b>bend or corner of land in a watercourse</b> \u2014 the same word found in English place names ending in <i>-ham</i>. <b>Crommenije</b> is compounded from <i>krom</i>, crooked, and <i>IJ</i>: the crooked arm of the IJ that once reached inland here. Both names therefore describe water that is no longer there. What remains is one of the largest continuous <b>peat-meadow areas</b> in North Holland, with wet grasslands, turf pits and reed fringes partly managed as marsh nature. It is one of the province\u2019s most important meadow-bird areas, with <b>godwit, redshank, ruff and snipe</b>, while <b>marsh harrier and Savi\u2019s warbler</b> breed in the reed zones.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (meadow birds), Nov\u2013Feb (geese and wigeon)<br>\n    <b>Best time of day:</b> Early morning \u2014 meadow-bird chorus over the open polder.',
 'why': ['<b>Ham</b> = bend or corner of land in a watercourse, as in English <i>-ham</i>.',
         '<b>Crommenije</b> = the crooked arm of the IJ that reached inland here.',
         'One of the largest <b>peat-meadow areas</b> in North Holland.',
         'Prime area for <b>godwit, redshank and ruff</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Godwits</b> arrive in numbers.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redshank and snipe</b> breed.',
          '<span class="months">May\u2013Jul</span> \U0001f33e <b>Savi\u2019s warbler</b> reels in the reed fringes.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Geese and wigeon</b> in large numbers.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Redshank \u00b7 Ruff \u00b7 Snipe', '\U0001f33e Savi\u2019s warbler \u00b7 Sedge warbler \u00b7 Reed bunting', '\U0001f985 Marsh harrier \u00b7 Hen harrier (winter)', '\U0001f9a2 White-fronted goose \u00b7 Greylag \u00b7 Wigeon', '\U0001f33f Water soldier \u00b7 Water violet'],
 'trail': ['Park at <b>Krommenie</b> or <b>Uitgeest</b>; watch from dikes and paths.',
           'In the breeding season stay <b>on the paths</b> \u2014 prime meadow-bird ground.',
           'April is the <b>best month</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Meadow-bird area Mar\u2013Jun \u00b7 \U0001f97e Wet'
}, card_class='card water'))

C.append(mk.card(1401, 'Westerhout', {
 'tags': ['Noord-Holland \u00b7 Beverwijk', 'Stadspark \u00b7 oud hakhoutbos op de strandwal', 'list 36 \u00b7 no. 120'],
 'loc': '\U0001f4cd Beverwijk \u00b7 Historisch bos en park \u00b7 Klein',
 'desc': '<b>Westerhout</b> in Beverwijk is een van de oudste bosjes van Kennemerland, en het woord <b>hout</b> in de naam is veelzeggend: in het Middelnederlands betekende <i>hout</i> gewoon <b>bos</b>, en het duikt op in tientallen namen van Haarlemmerhout tot \u2019s-Gravenhout. Die oude houtbossen op de strandwallen werden als <b>hakhout</b> beheerd: elke acht tot vijftien jaar werden de stobben afgezet, waarna ze weer uitliepen \u2014 een oogstsysteem dat brandhout en geriefhout leverde zonder de boom te doden, en dat stobben eeuwenoud kan maken. Westerhout werd in de negentiende eeuw tot <b>wandelpark</b> omgevormd, maar de oude bodem bleef. Daardoor groeit er een rijke <b>voorjaarsflora</b> met boshyacint en daslook, en broeden er <b>boomklever, bosuil en grote bonte specht</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (voorjaarsflora en zang), okt\u2013nov (herfstkleur en paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 stil voordat de stad wakker is.',
 'why': ['<b>Hout</b> = bos in het Middelnederlands, als in Haarlemmerhout.',
         'Beheerd als <b>hakhout</b>: stobben elke 8\u201315 jaar afgezet.',
         'Dat systeem maakt stobben <b>eeuwenoud</b> zonder de boom te doden.',
         'Oude bosbodem \u2192 rijke <b>voorjaarsflora</b> met daslook.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Boshyacint en daslook</b> bedekken de bodem.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever</b> zingt in de oude bomen.',
          '<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Bosuil</b> roept in het park.',
          '<span class="months">Okt\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de oude stobben.'],
 'wild': ['\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Boomkruiper', '\U0001f989 Bosuil \u00b7 Ransuil', '\U0001f33c Boshyacint \u00b7 Daslook \u00b7 Speenkruid', '\U0001f344 Elfenbankje \u00b7 Zwavelkop', '\U0001f333 Oude hakhoutstobben \u00b7 Beuk \u00b7 Eik'],
 'trail': ['Parkeren in <b>Beverwijk</b>; het park ligt in de stad.',
           'Zoek de <b>meerstammige stobben</b> \u2014 sporen van hakhoutbeheer.',
           'April is de maand van de <b>boshyacint</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historisch park \u00b7 \U0001f6b6 Verharde paden'
}, {
 'tags': ['North Holland \u00b7 Beverwijk', 'City park \u00b7 old coppice wood on the beach ridge', 'list 36 \u00b7 no. 120'],
 'loc': '\U0001f4cd Beverwijk \u00b7 Historic wood and park \u00b7 Small',
 'desc': '<b>Westerhout</b> in Beverwijk is one of the oldest woods in Kennemerland, and the word <b>hout</b> in the name is telling: in Middle Dutch <i>hout</i> simply meant <b>wood</b>, and it appears in dozens of names from Haarlemmerhout to \u2019s-Gravenhout. Those old woods on the beach ridges were managed as <b>coppice</b>: every eight to fifteen years the stools were cut back, after which they resprouted \u2014 a harvesting system that yielded firewood and utility wood without killing the tree, and which can make stools centuries old. Westerhout was converted into a <b>public park</b> in the nineteenth century, but the ancient soil remained. As a result a rich <b>spring flora</b> of bluebell and ramsons grows there, and <b>nuthatch, tawny owl and great spotted woodpecker</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (spring flora and song), Oct\u2013Nov (autumn colour and fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet before the town wakes.',
 'why': ['<b>Hout</b> = wood in Middle Dutch, as in Haarlemmerhout.',
         'Managed as <b>coppice</b>: stools cut every 8\u201315 years.',
         'That system makes stools <b>centuries old</b> without killing the tree.',
         'Ancient woodland soil \u2192 rich <b>spring flora</b> with ramsons.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Bluebell and ramsons</b> carpet the floor.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch</b> sings in the old trees.',
          '<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Tawny owl</b> calls in the park.',
          '<span class="months">Oct\u2013Nov</span> \U0001f344 <b>Fungi</b> on the old stools.'],
 'wild': ['\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Treecreeper', '\U0001f989 Tawny owl \u00b7 Long-eared owl', '\U0001f33c Bluebell \u00b7 Ramsons \u00b7 Lesser celandine', '\U0001f344 Turkeytail \u00b7 Sulphur tuft', '\U0001f333 Old coppice stools \u00b7 Beech \u00b7 Oak'],
 'trail': ['Park in <b>Beverwijk</b>; the park lies within the town.',
           'Look for the <b>multi-stemmed stools</b> \u2014 traces of coppice management.',
           'April is the month of the <b>bluebell</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic park \u00b7 \U0001f6b6 Paved paths'
}))

C.append(mk.card(1402, 'Lunetten', {
 'tags': ['Noord-Holland \u00b7 Beverwijk', 'Verdedigingswerk \u00b7 aarden lunetten met gracht', 'list 36 \u00b7 no. 121'],
 'loc': '\U0001f4cd Bij Beverwijk \u00b7 Historische aardwerken \u00b7 Klein',
 'desc': 'De <b>Lunetten</b> bij Beverwijk zijn kleine, zelfstandige verdedigingswerken met een karakteristieke vorm: een <b>lunet</b> heeft twee naar voren gerichte punten en een open achterzijde, waardoor de plattegrond op een halve maan lijkt \u2014 vandaar de naam, van het Franse <i>lune</i>. Ze werden in de negentiende eeuw aangelegd als onderdeel van de verdediging van het Noordzeekanaalgebied, om de toegang tot de <b>Stelling van Amsterdam</b> te dekken. Anders dan de latere betonnen forten bestaan lunetten volledig uit <b>aarde en gras</b>: wallen, grachten en glooiingen. Juist dat maakt ze ecologisch aantrekkelijk, want de <b>steile, nooit bemeste taluds</b> dragen een schrale vegetatie met veel bloemen. Er vliegen <b>vlinders en wilde bijen</b>, en in de grachten leven <b>amfibie\u00ebn</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (taludbloei en insecten), okt\u2013mrt (aardwerken zichtbaar zonder blad)<br>\n    <b>Beste tijd van de dag:</b> Warme middag \u2014 insecten actief op de zuidtaluds.',
 'why': ['<b>Lunet</b> = halvemaanvormig werk, van het Franse <i>lune</i>.',
         'Aangelegd om de toegang tot de <b>Stelling van Amsterdam</b> te dekken.',
         'Volledig uit <b>aarde en gras</b>, anders dan de betonnen forten.',
         '<b>Nooit bemeste taluds</b> dragen een schrale, bloemrijke vegetatie.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Taludbloei</b> begint op de zuidhellingen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Vlinders en wilde bijen</b> op de wallen.',
          '<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Amfibie\u00ebn</b> planten zich voort in de gracht.',
          '<span class="months">Okt\u2013Mrt</span> \U0001f3db\ufe0f <b>Aardwerken</b> goed leesbaar zonder blad.'],
 'wild': ['\U0001f33c Knoopkruid \u00b7 Margriet \u00b7 Duizendblad', '\U0001f98b Vlinders \u00b7 \U0001f41d Wilde bijen \u00b7 Zweefvliegen', '\U0001f438 Kikkers \u00b7 Padden \u00b7 Watersalamander', '\U0001f426 Grasmus \u00b7 Roodborsttapuit', '\U0001f997 Sprinkhanen op de taluds'],
 'trail': ['Parkeren bij <b>Beverwijk</b>; paden over en om de wallen.',
           'Loop de <b>halvemaanvorm</b> af om het ontwerp te begrijpen.',
           'De <b>zuidtaluds</b> zijn het bloemrijkst.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Militair erfgoed \u00b7 \u26a0\ufe0f Blijf van de steile taluds'
}, {
 'tags': ['North Holland \u00b7 Beverwijk', 'Defence work \u00b7 earthen lunettes with moat', 'list 36 \u00b7 no. 121'],
 'loc': '\U0001f4cd Near Beverwijk \u00b7 Historic earthworks \u00b7 Small',
 'desc': 'The <b>Lunetten</b> near Beverwijk are small, self-contained defence works with a characteristic shape: a <b>lunette</b> has two forward-facing points and an open rear, giving a plan resembling a half-moon \u2014 hence the name, from the French <i>lune</i>. They were built in the nineteenth century as part of the defence of the North Sea Canal area, to cover the approach to the <b>Defence Line of Amsterdam</b>. Unlike the later concrete forts, lunettes consist entirely of <b>earth and grass</b>: ramparts, moats and slopes. That is exactly what makes them ecologically attractive, for the <b>steep, never-fertilised banks</b> carry a poor vegetation rich in flowers. <b>Butterflies and wild bees</b> fly here, and <b>amphibians</b> live in the moats.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (bank flowering and insects), Oct\u2013Mar (earthworks visible without leaves)<br>\n    <b>Best time of day:</b> Warm afternoon \u2014 insects active on the south-facing banks.',
 'why': ['<b>Lunette</b> = half-moon shaped work, from the French <i>lune</i>.',
         'Built to cover the approach to the <b>Defence Line of Amsterdam</b>.',
         'Entirely of <b>earth and grass</b>, unlike the concrete forts.',
         '<b>Never-fertilised banks</b> carry a poor, flower-rich vegetation.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33c <b>Bank flowering</b> begins on the south slopes.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Butterflies and wild bees</b> on the ramparts.',
          '<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Amphibians</b> breed in the moat.',
          '<span class="months">Oct\u2013Mar</span> \U0001f3db\ufe0f <b>Earthworks</b> clearly readable without leaves.'],
 'wild': ['\U0001f33c Knapweed \u00b7 Oxeye daisy \u00b7 Yarrow', '\U0001f98b Butterflies \u00b7 \U0001f41d Wild bees \u00b7 Hoverflies', '\U0001f438 Frogs \u00b7 Toads \u00b7 Newts', '\U0001f426 Whitethroat \u00b7 Stonechat', '\U0001f997 Grasshoppers on the banks'],
 'trail': ['Park at <b>Beverwijk</b>; paths over and around the ramparts.',
           'Walk the <b>half-moon shape</b> to understand the design.',
           'The <b>south-facing banks</b> are the most flowery.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Military heritage \u00b7 \u26a0\ufe0f Stay off the steep banks'
}))

C.append(mk.card(1403, 'Fort Veldhuis', {
 'tags': ['Noord-Holland \u00b7 Heemskerk', 'Stelling van Amsterdam \u00b7 fort met museum en fortgracht', 'list 36 \u00b7 no. 122'],
 'loc': '\U0001f4cd Bij Heemskerk, aan de Stelling van Amsterdam \u00b7 Fortterrein \u00b7 Klein',
 'desc': '<b>Fort Veldhuis</b> is een van de forten van de Stelling van Amsterdam en herbergt tegenwoordig een museum over de <b>luchtoorlog boven Noord-Holland</b>. Dat past bij de plek, want de forten van de Stelling raakten al v\u00f3\u00f3r hun voltooiing verouderd: rond 1920 was duidelijk dat vliegtuigen en zware artillerie een waterlinie eenvoudig konden passeren. De hele ring was daarmee een <b>defensief systeem dat nooit heeft gewerkt</b> \u2014 en juist daardoor gaaf bewaard bleef. Het fortterrein bestaat uit een betonnen hoofdgebouw, een <b>gracht</b> en een dichte beplanting die ooit als camouflage diende. Die combinatie levert nu een rijke stadsrandnatuur: <b>vleermuizen</b> in de kelders, <b>ijsvogel</b> aan de gracht, en <b>boomkruiper, groene specht en gekraagde roodstaart</b> in het fortbos.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels), okt\u2013mrt (overwinterende vleermuizen)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 uitvliegende vleermuizen boven de gracht.',
 'why': ['Forten van de Stelling waren <b>bij voltooiing al verouderd</b>.',
         'Vliegtuigen konden een waterlinie eenvoudig <b>passeren</b>.',
         'Een systeem dat nooit werkte \u2014 en daardoor <b>gaaf bewaard</b> bleef.',
         'Camouflagebeplanting werd <b>fortbos</b> vol vogels.'],
 'phen': ['<span class="months">Okt\u2013Mrt</span> \U0001f987 <b>Vleermuizen</b> overwinteren in de fortkelders.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Groene specht</b> roept in het fortbos.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>IJsvogel</b> jaagt boven de gracht.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Zwermende vleermuizen</b> bij de ingangen.'],
 'wild': ['\U0001f987 Watervleermuis \u00b7 Baardvleermuis \u00b7 Grootoorvleermuis', '\U0001f426 IJsvogel \u00b7 Groene specht \u00b7 Boomkruiper \u00b7 Gekraagde roodstaart', '\U0001f33f Muurvarens op het beton', '\U0001f438 Amfibie\u00ebn in de gracht', '\U0001f333 Es \u00b7 Iep \u00b7 Meidoorn'],
 'trail': ['Parkeren bij het <b>museum</b>; terrein en gracht te belopen.',
           'Combineer het <b>luchtoorlogmuseum</b> met een rondje om de gracht.',
           'Kom in de <b>schemer</b> voor uitvliegende vleermuizen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Museum entree \u00b7 \U0001f3db\ufe0f UNESCO-werelderfgoed \u00b7 \u26a0\ufe0f Vleermuisverblijf'
}, {
 'tags': ['North Holland \u00b7 Heemskerk', 'Defence Line of Amsterdam \u00b7 fort with museum and moat', 'list 36 \u00b7 no. 122'],
 'loc': '\U0001f4cd Near Heemskerk, on the Defence Line of Amsterdam \u00b7 Fort grounds \u00b7 Small',
 'desc': '<b>Fort Veldhuis</b> is one of the forts of the Defence Line of Amsterdam and today houses a museum about the <b>air war over North Holland</b>. That suits the place, for the Line\u2019s forts were obsolete even before they were finished: by around 1920 it was clear that aircraft and heavy artillery could simply pass over a water line. The entire ring was thus a <b>defensive system that never worked</b> \u2014 and precisely for that reason survived intact. The fort grounds consist of a concrete main building, a <b>moat</b> and dense planting that once served as camouflage. That combination now yields rich urban-fringe nature: <b>bats</b> in the cellars, <b>kingfisher</b> at the moat, and <b>treecreeper, green woodpecker and redstart</b> in the fort wood.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds), Oct\u2013Mar (hibernating bats)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats emerging over the moat.',
 'why': ['The Line\u2019s forts were <b>obsolete on completion</b>.',
         'Aircraft could simply <b>pass over</b> a water line.',
         'A system that never worked \u2014 and so survived <b>intact</b>.',
         'Camouflage planting became a <b>fort wood</b> full of birds.'],
 'phen': ['<span class="months">Oct\u2013Mar</span> \U0001f987 <b>Bats</b> hibernate in the fort cellars.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Green woodpecker</b> calls in the fort wood.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Kingfisher</b> hunts over the moat.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Swarming bats</b> at the entrances.'],
 'wild': ['\U0001f987 Daubenton\u2019s bat \u00b7 Whiskered bat \u00b7 Brown long-eared bat', '\U0001f426 Kingfisher \u00b7 Green woodpecker \u00b7 Treecreeper \u00b7 Redstart', '\U0001f33f Wall ferns on the concrete', '\U0001f438 Amphibians in the moat', '\U0001f333 Ash \u00b7 Elm \u00b7 Hawthorn'],
 'trail': ['Park at the <b>museum</b>; grounds and moat can be walked.',
           'Combine the <b>air war museum</b> with a circuit of the moat.',
           'Come at <b>dusk</b> for emerging bats.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Museum entry fee \u00b7 \U0001f3db\ufe0f UNESCO World Heritage \u00b7 \u26a0\ufe0f Bat roost'
}))

C.append(mk.card(1404, 'Liniedijken', {
 'tags': ['Noord-Holland \u00b7 Beverwijk', 'Dijkenstelsel \u00b7 bloemrijke bermen van de Stelling', 'list 36 \u00b7 no. 123'],
 'loc': '\U0001f4cd Tussen de forten van de Stelling van Amsterdam \u00b7 Dijklinten \u00b7 Middelgroot',
 'desc': 'De <b>Liniedijken</b> zijn de aarden verbindingen tussen de forten van de Stelling van Amsterdam, en ze vervulden een dubbele rol: ze hielden het <b>inundatiewater</b> op de juiste hoogte en dienden als beschutte aanvoerroute voor troepen en materieel. Het waterbeheer was daarbij verrassend fijnzinnig \u2014 om het gewenste peil van dertig tot veertig centimeter te bereiken moest het water in <b>compartimenten</b> worden gehouden, elk met eigen sluizen en dammen. Precies daarom loopt het dijkenstelsel zo grillig door het landschap. Ecologisch zijn de dijken nu <b>lange lijnvormige landschapselementen</b>: schrale, nooit bemeste bermen die als corridor werken tussen de fortbossen. Er bloeien <b>knoopkruid, wilde marjolein en bevertjes</b>, en er vliegen veel <b>vlinders, bijen en sprinkhanen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (bermbloei en insecten), sep\u2013okt (trekvogels langs de linten)<br>\n    <b>Beste tijd van de dag:</b> Warme middag \u2014 insecten op de zonnige dijkhellingen.',
 'why': ['Hielden het <b>inundatiewater</b> op dertig tot veertig centimeter.',
         'Water moest in <b>compartimenten</b> met eigen sluizen worden gehouden.',
         'Vandaar het <b>grillige verloop</b> van het dijkenstelsel.',
         'Nu <b>corridors</b> met schrale, nooit bemeste bermen.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Bevertjes</b> trillen in de dijkberm.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Wilde marjolein en knoopkruid</b> bloeien.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Vlinders en bijen</b> op hun talrijkst.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Trekvogels</b> volgen de dijklijnen.'],
 'wild': ['\U0001f33c Knoopkruid \u00b7 Wilde marjolein \u00b7 Bevertjes', '\U0001f98b Icarusblauwtje \u00b7 Bruin zandoogje \u00b7 Dikkopjes', '\U0001f41d Wilde bijen \u00b7 Zweefvliegen', '\U0001f997 Sprinkhanen \u00b7 Krekels', '\U0001f426 Grasmus \u00b7 Roodborsttapuit \u00b7 Graspieper'],
 'trail': ['Parkeren bij een van de <b>forten</b>; de dijken zijn per fiets te volgen.',
           'De <b>zuidhellingen</b> zijn warmer en bloemrijker.',
           'Fiets van fort naar fort \u2014 dan zie je het <b>systeem</b> als geheel.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b4 Fietsroute langs de Stelling \u00b7 \U0001f3db\ufe0f UNESCO-werelderfgoed'
}, {
 'tags': ['North Holland \u00b7 Beverwijk', 'Dike system \u00b7 flower-rich verges of the Defence Line', 'list 36 \u00b7 no. 123'],
 'loc': '\U0001f4cd Between the forts of the Defence Line of Amsterdam \u00b7 Dike ribbons \u00b7 Medium-sized',
 'desc': 'The <b>Liniedijken</b> are the earthen connections between the forts of the Defence Line of Amsterdam, and they played a double role: they held the <b>inundation water</b> at the right level and served as a sheltered supply route for troops and equipment. The water management was surprisingly subtle \u2014 to reach the desired depth of thirty to forty centimetres the water had to be kept in <b>compartments</b>, each with its own sluices and dams. That is exactly why the dike system runs so erratically through the landscape. Ecologically the dikes are now <b>long linear landscape elements</b>: poor, never-fertilised verges working as a corridor between the fort woods. <b>Knapweed, wild marjoram and quaking grass</b> flower here, and many <b>butterflies, bees and grasshoppers</b> fly.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (verge flowering and insects), Sep\u2013Oct (migrants along the ribbons)<br>\n    <b>Best time of day:</b> Warm afternoon \u2014 insects on the sunny dike slopes.',
 'why': ['Held the <b>inundation water</b> at thirty to forty centimetres.',
         'Water had to be kept in <b>compartments</b> with their own sluices.',
         'Hence the <b>erratic course</b> of the dike system.',
         'Now <b>corridors</b> with poor, never-fertilised verges.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33c <b>Quaking grass</b> trembles on the dike verge.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Wild marjoram and knapweed</b> flower.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Butterflies and bees</b> at their most numerous.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Migrants</b> follow the dike lines.'],
 'wild': ['\U0001f33c Knapweed \u00b7 Wild marjoram \u00b7 Quaking grass', '\U0001f98b Common blue \u00b7 Meadow brown \u00b7 Skippers', '\U0001f41d Wild bees \u00b7 Hoverflies', '\U0001f997 Grasshoppers \u00b7 Crickets', '\U0001f426 Whitethroat \u00b7 Stonechat \u00b7 Meadow pipit'],
 'trail': ['Park at one of the <b>forts</b>; the dikes can be followed by bike.',
           'The <b>south-facing slopes</b> are warmer and more flowery.',
           'Cycle fort to fort \u2014 then you see the <b>system</b> as a whole.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b4 Cycle route along the Line \u00b7 \U0001f3db\ufe0f UNESCO World Heritage'
}))

mk.insert(C, '1399')
mk.progress(1404)
mk.check()
