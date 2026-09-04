# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1425, 'Fort bij Spijkerboor', {
 'tags': ['Noord-Holland \u00b7 Alkmaar', 'Stelling van Amsterdam \u00b7 grootste fort van de linie', 'list 36 \u00b7 no. 144'],
 'loc': '\U0001f4cd Spijkerboor, aan de Beemsterringvaart \u00b7 Fortterrein \u00b7 Klein',
 'desc': '<b>Fort bij Spijkerboor</b> is het grootste en zwaarst bewapende fort van de Stelling van Amsterdam, en dat heeft een reden: hier kruisten drie belangrijke <b>accessen</b> \u2014 de Beemsterringvaart, de Westdijk en de weg naar Purmerend. Waar meerdere hoge lijnen bijeenkwamen moest de verdediging het sterkst zijn, en dus kreeg dit fort als enige twee <b>gepantserde geschutskoepels</b> met kanonnen die tot ver in het inundatiegebied konden schieten. Het fort werd in de Tweede Wereldoorlog nog als <b>gevangenis</b> gebruikt. Nu is het een monument met een uitgestrekt terrein, en de dikke betonnen gangen vormen een van de belangrijkste <b>vleermuiswinterverblijven</b> van Noord-Holland. Op het terrein broeden <b>ijsvogel, groene specht en kerkuil</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels), okt\u2013mrt (grote vleermuisaantallen)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 vleermuizen verlaten dan de koepels en gangen.',
 'why': ['Het <b>grootste en zwaarst bewapende</b> fort van de hele Stelling.',
         'Hier kruisten drie <b>accessen</b>: ringvaart, dijk en weg.',
         'Als enige met twee <b>gepantserde geschutskoepels</b>.',
         'In de oorlog als <b>gevangenis</b> gebruikt; nu vleermuisbolwerk.'],
 'phen': ['<span class="months">Okt\u2013Mrt</span> \U0001f987 <b>Vleermuizen</b> in grote aantallen in de gangen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> broedt in de fortgracht.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Bloemrijke taluds</b> op de aarden wallen.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Zwermgedrag</b> bij de ingangen.'],
 'wild': ['\U0001f987 Watervleermuis \u00b7 Baardvleermuis \u00b7 Franjestaart \u00b7 Grootoorvleermuis', '\U0001f426 IJsvogel \u00b7 Groene specht \u00b7 \U0001f989 Kerkuil', '\U0001f33c Knoopkruid \u00b7 Margriet op de wallen', '\U0001f438 Amfibie\u00ebn in de gracht', '\U0001f333 Es \u00b7 Iep \u00b7 Meidoorn'],
 'trail': ['Parkeren bij <b>Spijkerboor</b>; fort te bezoeken tijdens openstelling.',
           'Let op de <b>geschutskoepels</b> \u2014 uniek binnen de Stelling.',
           'Betreed de <b>gangen</b> niet in de winter \u2014 vleermuizen in winterslaap.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Entree bij rondleiding \u00b7 \U0001f3db\ufe0f UNESCO-werelderfgoed \u00b7 \u26a0\ufe0f Belangrijk vleermuisverblijf'
}, {
 'tags': ['North Holland \u00b7 Alkmaar', 'Defence Line of Amsterdam \u00b7 largest fort of the line', 'list 36 \u00b7 no. 144'],
 'loc': '\U0001f4cd Spijkerboor, on the Beemster ring canal \u00b7 Fort grounds \u00b7 Small',
 'desc': '<b>Fort bij Spijkerboor</b> is the largest and most heavily armed fort of the Defence Line of Amsterdam, and there is a reason: three important <b>accesses</b> crossed here \u2014 the Beemster ring canal, the Westdijk and the road to Purmerend. Where several high lines met the defence had to be strongest, and so this fort alone received two <b>armoured gun turrets</b> with guns that could fire far into the inundation zone. In the Second World War the fort was still used as a <b>prison</b>. It is now a monument with extensive grounds, and the thick concrete corridors form one of the most important <b>bat hibernacula</b> in North Holland. <b>Kingfisher, green woodpecker and barn owl</b> breed on the site.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds), Oct\u2013Mar (large bat numbers)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats then leave the turrets and corridors.',
 'why': ['The <b>largest and most heavily armed</b> fort of the entire Line.',
         'Three <b>accesses</b> crossed here: ring canal, dike and road.',
         'The only one with two <b>armoured gun turrets</b>.',
         'Used as a <b>prison</b> in the war; now a bat stronghold.'],
 'phen': ['<span class="months">Oct\u2013Mar</span> \U0001f987 <b>Bats</b> in large numbers in the corridors.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> breeds in the fort moat.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Flower-rich banks</b> on the earthen ramparts.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Swarming</b> at the entrances.'],
 'wild': ['\U0001f987 Daubenton\u2019s \u00b7 Whiskered \u00b7 Natterer\u2019s \u00b7 Brown long-eared bat', '\U0001f426 Kingfisher \u00b7 Green woodpecker \u00b7 \U0001f989 Barn owl', '\U0001f33c Knapweed \u00b7 Oxeye daisy on the ramparts', '\U0001f438 Amphibians in the moat', '\U0001f333 Ash \u00b7 Elm \u00b7 Hawthorn'],
 'trail': ['Park at <b>Spijkerboor</b>; fort visitable during opening times.',
           'Note the <b>gun turrets</b> \u2014 unique within the Line.',
           'Do not enter the <b>corridors</b> in winter \u2014 bats are hibernating.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Entry with guided tour \u00b7 \U0001f3db\ufe0f UNESCO World Heritage \u00b7 \u26a0\ufe0f Important bat roost'
}))

C.append(mk.card(1426, 'Fort aan de Jisperweg', {
 'tags': ['Noord-Holland \u00b7 Wormerland', 'Stelling van Amsterdam \u00b7 fort in de Beemster', 'list 36 \u00b7 no. 145'],
 'loc': '\U0001f4cd Aan de Jisperweg in de Beemster \u00b7 Fortterrein \u00b7 Klein',
 'desc': 'Het <b>Fort aan de Jisperweg</b> staat midden in de <b>Beemster</b>, de droogmakerij uit 1612 die als UNESCO-werelderfgoed geldt vanwege haar volmaakt rationele indeling: een raster van rechte wegen en vaarten, gebaseerd op renaissance-idealen over de ideale ordening van de ruimte. Dat het fort daarin staat is dubbel bijzonder, want hier raken <b>twee werelderfgoederen</b> elkaar \u2014 de Beemster en de Stelling van Amsterdam. Het contrast is scherp: de Beemster is een monument voor het droogmaken, het fort een instrument om alles weer onder water te zetten. Het fortterrein is nu een groen eiland in het strakke rasterlandschap, met <b>gracht, wallen en dichte beplanting</b>. Er overwinteren <b>vleermuizen</b> en er broeden <b>ijsvogel, boomkruiper en groene specht</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels), okt\u2013mrt (overwinterende vleermuizen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 zicht over het Beemsterraster vanaf de wal.',
 'why': ['Staat midden in de <b>Beemster</b> (1612), zelf UNESCO-werelderfgoed.',
         'Hier raken <b>twee werelderfgoederen</b> elkaar.',
         'De Beemster viert het droogmaken, het fort de <b>herinundatie</b>.',
         'Groen eiland met gracht en wallen in een <b>strak raster</b>.'],
 'phen': ['<span class="months">Okt\u2013Mrt</span> \U0001f987 <b>Vleermuizen</b> overwinteren in de kelders.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> aan de fortgracht.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Bloemrijke wallen</b> in het open polderland.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Trekvogels</b> gebruiken het fortbos als steunpunt.'],
 'wild': ['\U0001f987 Watervleermuis \u00b7 Grootoorvleermuis', '\U0001f426 IJsvogel \u00b7 Boomkruiper \u00b7 Groene specht', '\U0001f33c Knoopkruid \u00b7 Margriet', '\U0001f438 Amfibie\u00ebn in de gracht', '\U0001f985 Buizerd \u00b7 Torenvalk boven de polder'],
 'trail': ['Parkeren aan de <b>Jisperweg</b>; terrein beperkt toegankelijk.',
           'Kijk vanaf de wal over het <b>Beemsterraster</b> \u2014 kaarsrechte lijnen tot de horizon.',
           'Combineer met een fietstocht door de <b>Beemster</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Twee keer UNESCO \u00b7 \u26a0\ufe0f Vleermuisverblijf'
}, {
 'tags': ['North Holland \u00b7 Wormerland', 'Defence Line of Amsterdam \u00b7 fort in the Beemster', 'list 36 \u00b7 no. 145'],
 'loc': '\U0001f4cd On the Jisperweg in the Beemster \u00b7 Fort grounds \u00b7 Small',
 'desc': 'The <b>Fort aan de Jisperweg</b> stands in the middle of the <b>Beemster</b>, the polder drained in 1612 and listed as UNESCO World Heritage for its perfectly rational layout: a grid of straight roads and canals based on Renaissance ideals about the ideal ordering of space. That the fort stands within it is doubly remarkable, for here <b>two World Heritage sites</b> touch \u2014 the Beemster and the Defence Line of Amsterdam. The contrast is sharp: the Beemster is a monument to draining, the fort an instrument for flooding it all again. The fort grounds are now a green island in the crisp grid landscape, with <b>moat, ramparts and dense planting</b>. <b>Bats</b> hibernate here and <b>kingfisher, treecreeper and green woodpecker</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds), Oct\u2013Mar (hibernating bats)<br>\n    <b>Best time of day:</b> Morning \u2014 views over the Beemster grid from the rampart.',
 'why': ['Stands in the middle of the <b>Beemster</b> (1612), itself World Heritage.',
         'Here <b>two World Heritage sites</b> touch.',
         'The Beemster celebrates draining, the fort <b>re-flooding</b>.',
         'A green island with moat and ramparts in a <b>crisp grid</b>.'],
 'phen': ['<span class="months">Oct\u2013Mar</span> \U0001f987 <b>Bats</b> hibernate in the cellars.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> at the fort moat.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Flower-rich ramparts</b> in the open polder.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Migrants</b> use the fort wood as a stepping stone.'],
 'wild': ['\U0001f987 Daubenton\u2019s bat \u00b7 Brown long-eared bat', '\U0001f426 Kingfisher \u00b7 Treecreeper \u00b7 Green woodpecker', '\U0001f33c Knapweed \u00b7 Oxeye daisy', '\U0001f438 Amphibians in the moat', '\U0001f985 Buzzard \u00b7 Kestrel over the polder'],
 'trail': ['Park on the <b>Jisperweg</b>; grounds with limited access.',
           'Look from the rampart over the <b>Beemster grid</b> \u2014 straight lines to the horizon.',
           'Combine with a cycle tour through the <b>Beemster</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Twice UNESCO \u00b7 \u26a0\ufe0f Bat roost'
}))

C.append(mk.card(1427, 'Fort aan de Middenweg', {
 'tags': ['Noord-Holland \u00b7 Beemster', 'Stelling van Amsterdam \u00b7 fort met open schootsveld', 'list 36 \u00b7 no. 146'],
 'loc': '\U0001f4cd Aan de Middenweg in de Beemster \u00b7 Fortterrein \u00b7 Klein',
 'desc': 'Het <b>Fort aan de Middenweg</b> bewaakte de centrale as van de Beemster, en het laat een principe zien dat bij alle forten gold maar hier extra zichtbaar is: de <b>Kringenwet</b>. Die wet uit 1853 verbood binnen een straal van driehonderd tot duizend meter rond een fort het bouwen in steen \u2014 alleen hout was toegestaan, zodat alles bij een aanval snel kon worden platgebrand om vrij schootsveld te krijgen. Rond veel forten leverde dat karakteristieke <b>houten Kringenwetboerderijen</b> op, en het verklaart waarom de omgeving nog altijd opvallend <b>open en onbebouwd</b> is. Die openheid is nu een ecologische kwaliteit: het fortbos ligt als geïsoleerd bosje in een leeg polderlandschap en trekt daardoor veel <b>trekvogels</b> aan. In de kelders overwinteren <b>vleermuizen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Sep\u2013okt</b> (trekvogels in het geïsoleerde bosje), okt\u2013mrt (vleermuizen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 trekvogels landen dan in het fortbos.',
 'why': ['De <b>Kringenwet</b> (1853) verbood steenbouw rond forten.',
         'Alleen <b>hout</b> was toegestaan \u2014 snel plat te branden voor schootsveld.',
         'Vandaar de karakteristieke <b>houten Kringenwetboerderijen</b>.',
         'De opgelegde openheid maakt het fortbos een <b>vogelmagneet</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Voorjaarstrekkers</b> strijken neer in het fortbos.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Bloemrijke taluds</b> op de wallen.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Najaarstrek</b> \u2014 het bosje is een oase in de lege polder.',
          '<span class="months">Okt\u2013Mrt</span> \U0001f987 <b>Vleermuizen</b> in de fortkelders.'],
 'wild': ['\U0001f426 Trekvogels: tjiftjaf \u00b7 zwartkop \u00b7 goudhaan \u00b7 vuurgoudhaan', '\U0001f987 Watervleermuis \u00b7 Grootoorvleermuis', '\U0001f985 Sperwer jaagt op de trekvogels', '\U0001f33c Knoopkruid \u00b7 Margriet', '\U0001f438 Amfibie\u00ebn in de gracht'],
 'trail': ['Parkeren aan de <b>Middenweg</b>; terrein beperkt toegankelijk.',
           'Zoek de <b>houten boerderijen</b> in de omgeving \u2014 gevolg van de Kringenwet.',
           'Kom in <b>oktober</b>: geïsoleerde bosjes vangen dan veel trekvogels.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f UNESCO-werelderfgoed \u00b7 \u26a0\ufe0f Vleermuisverblijf'
}, {
 'tags': ['North Holland \u00b7 Beemster', 'Defence Line of Amsterdam \u00b7 fort with open field of fire', 'list 36 \u00b7 no. 146'],
 'loc': '\U0001f4cd On the Middenweg in the Beemster \u00b7 Fort grounds \u00b7 Small',
 'desc': 'The <b>Fort aan de Middenweg</b> guarded the central axis of the Beemster, and it illustrates a principle that applied to all the forts but is especially visible here: the <b>Kringenwet</b>, the Zones Act. That law of 1853 forbade building in stone within a radius of three hundred to a thousand metres around a fort \u2014 only timber was allowed, so that everything could be swiftly burnt down in an attack to clear the field of fire. Around many forts this produced characteristic <b>timber Zones Act farmhouses</b>, and it explains why the surroundings are still strikingly <b>open and unbuilt</b>. That openness is now an ecological quality: the fort wood lies as an isolated copse in an empty polder landscape and therefore attracts many <b>migrant birds</b>. <b>Bats</b> hibernate in the cellars.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Sep\u2013Oct</b> (migrants in the isolated copse), Oct\u2013Mar (bats)<br>\n    <b>Best time of day:</b> Early morning \u2014 migrants then drop into the fort wood.',
 'why': ['The <b>Kringenwet</b> (1853) forbade stone building around forts.',
         'Only <b>timber</b> was allowed \u2014 quickly burnt to clear the field of fire.',
         'Hence the characteristic <b>timber Zones Act farmhouses</b>.',
         'The imposed openness makes the fort wood a <b>bird magnet</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f426 <b>Spring migrants</b> drop into the fort wood.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Flower-rich banks</b> on the ramparts.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Autumn migration</b> \u2014 the copse is an oasis in the empty polder.',
          '<span class="months">Oct\u2013Mar</span> \U0001f987 <b>Bats</b> in the fort cellars.'],
 'wild': ['\U0001f426 Migrants: chiffchaff \u00b7 blackcap \u00b7 goldcrest \u00b7 firecrest', '\U0001f987 Daubenton\u2019s bat \u00b7 Brown long-eared bat', '\U0001f985 Sparrowhawk hunting the migrants', '\U0001f33c Knapweed \u00b7 Oxeye daisy', '\U0001f438 Amphibians in the moat'],
 'trail': ['Park on the <b>Middenweg</b>; grounds with limited access.',
           'Look for the <b>timber farmhouses</b> nearby \u2014 a consequence of the Zones Act.',
           'Come in <b>October</b>: isolated copses then catch many migrants.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f UNESCO World Heritage \u00b7 \u26a0\ufe0f Bat roost'
}))

C.append(mk.card(1428, 'Kwadijkker Vlot', {
 'tags': ['Noord-Holland \u00b7 Edam-Volendam', 'Veenweide \u00b7 nat grasland met drijvende oevers', 'list 36 \u00b7 no. 147'],
 'loc': '\U0001f4cd Bij Kwadijk, ten noorden van Purmerend \u00b7 Veenweide \u00b7 Klein',
 'desc': 'Het <b>Kwadijkker Vlot</b> ontleent zijn naam aan twee elementen. <b>Kwadijk</b> is het dorp, en dat betekent letterlijk \u2018kwade dijk\u2019 \u2014 een dijkvak dat berucht was om zijn doorbraken, want <i>kwaad</i> had in het Middelnederlands de betekenis van slecht of onbetrouwbaar. En <b>vlot</b> is een landschapsterm voor <b>drijvend land</b>: veenpakketten die zo licht en waterverzadigd zijn dat ze bij hoog water meestijgen. Wie erover loopt voelt de bodem deinen. Zulke trilvenen zijn zeldzaam geworden, want ze verdwijnen zodra het peil wordt vastgezet. Hier is het bewaard gebleven als nat grasland met veenmosrijke randen. Er broeden <b>watersnip, tureluur en rietgors</b>, en er groeien <b>zeggen, veenpluis en orchidee\u00ebn</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels), mei\u2013jul (veenflora en orchidee\u00ebn)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 baltsende watersnippen boven het vlot.',
 'why': ['<b>Kwadijk</b> = \u2018kwade dijk\u2019, berucht om zijn doorbraken.',
         '<b>Vlot</b> = drijvend land dat bij hoog water meestijgt.',
         'Zulke <b>trilvenen</b> verdwijnen zodra het peil wordt vastgezet.',
         'Bewaard als nat grasland met <b>veenmosrijke randen</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Watersnip</b> baltst boven het vlot.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tureluur en rietgors</b> broeden.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33f <b>Veenpluis</b> pluist wit uit.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Orchidee\u00ebn</b> in de veenmosranden.'],
 'wild': ['\U0001f426 Watersnip \u00b7 Tureluur \u00b7 Rietgors', '\U0001f33f Veenmos \u00b7 Veenpluis \u00b7 Zeggen', '\U0001f33c Rietorchis \u00b7 Moeraskartelblad', '\U0001f9a0 Libellen boven de natte laagten', '\U0001f438 Heikikker \u00b7 Groene kikker'],
 'trail': ['Parkeren bij <b>Kwadijk</b>; kijk vanaf de paden aan de rand.',
           'Betreed het <b>vlot</b> niet \u2014 het draagt nauwelijks en is kwetsbaar.',
           'Juni voor de <b>orchidee\u00ebn</b> aan de randen.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Zeer kwetsbaar trilveen \u00b7 \U0001f97e Zeer nat'
}, {
 'tags': ['North Holland \u00b7 Edam-Volendam', 'Peat meadow \u00b7 wet grassland with floating banks', 'list 36 \u00b7 no. 147'],
 'loc': '\U0001f4cd Near Kwadijk, north of Purmerend \u00b7 Peat meadow \u00b7 Small',
 'desc': 'The <b>Kwadijkker Vlot</b> takes its name from two elements. <b>Kwadijk</b> is the village, and it means literally \u2018bad dike\u2019 \u2014 a stretch notorious for its breaches, since <i>kwaad</i> in Middle Dutch meant bad or unreliable. And <b>vlot</b> is a landscape term for <b>floating land</b>: peat layers so light and waterlogged that they rise with high water. Walking on it, you feel the ground sway. Such quaking fens have become rare, for they vanish as soon as the water level is fixed. Here it survives as wet grassland with sphagnum-rich edges. <b>Snipe, redshank and reed bunting</b> breed, and <b>sedges, cottongrass and orchids</b> grow.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds), May\u2013Jul (bog flora and orchids)<br>\n    <b>Best time of day:</b> Early morning \u2014 drumming snipe above the floating land.',
 'why': ['<b>Kwadijk</b> = \u2018bad dike\u2019, notorious for its breaches.',
         '<b>Vlot</b> = floating land that rises with high water.',
         'Such <b>quaking fens</b> vanish as soon as the level is fixed.',
         'Preserved as wet grassland with <b>sphagnum-rich edges</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Snipe</b> drums above the floating land.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redshank and reed bunting</b> breed.',
          '<span class="months">May\u2013Jun</span> \U0001f33f <b>Cottongrass</b> turns white.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Orchids</b> in the sphagnum edges.'],
 'wild': ['\U0001f426 Snipe \u00b7 Redshank \u00b7 Reed bunting', '\U0001f33f Sphagnum \u00b7 Cottongrass \u00b7 Sedges', '\U0001f33c Marsh orchid \u00b7 Marsh lousewort', '\U0001f9a0 Dragonflies above the wet hollows', '\U0001f438 Moor frog \u00b7 Edible frog'],
 'trail': ['Park at <b>Kwadijk</b>; watch from the paths along the edge.',
           'Do not walk onto the <b>vlot</b> \u2014 it barely bears weight and is fragile.',
           'June for the <b>orchids</b> along the edges.'],
 'foot': '\U0001f436 Dogs not allowed \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Very fragile quaking fen \u00b7 \U0001f97e Very wet'
}, card_class='card water'))

C.append(mk.card(1429, 'Fort Edam', {
 'tags': ['Noord-Holland \u00b7 Edam-Volendam', 'Stelling van Amsterdam \u00b7 noordelijkste fort van de linie', 'list 36 \u00b7 no. 148'],
 'loc': '\U0001f4cd Bij Edam, aan het Markermeer \u00b7 Fortterrein \u00b7 Klein',
 'desc': '<b>Fort Edam</b> is het noordelijkste fort van de Stelling van Amsterdam en sluit de ring af tegen de voormalige Zuiderzee. Die positie was strategisch cruciaal: hier eindigde de inundatielinie tegen open water, en een vijand die de zeedijk zou volgen kon alleen langs dit punt. Het fort bewaakte dus letterlijk het <b>eindpunt van de linie</b>. Interessant is dat de bouwers hier een probleem hadden dat elders niet speelde: de zeedijk zelf mocht niet worden verzwakt, dus het fort staat er vlak naast in plaats van erop. Het terrein bestaat uit een betonnen gebouw met <b>gracht en beplanting</b>, gelegen tussen dijk en polder. Er overwinteren <b>vleermuizen</b>, en op het terrein broeden <b>groene specht, boomkruiper en gekraagde roodstaart</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels), okt\u2013mrt (vleermuizen en watervogels op het Markermeer)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 vleermuizen en zicht over het Markermeer.',
 'why': ['Het <b>noordelijkste fort</b> \u2014 sluit de ring tegen de Zuiderzee.',
         'Bewaakte het <b>eindpunt van de inundatielinie</b> bij open water.',
         'Staat n\u00e1\u00e1st de zeedijk, want die mocht niet worden <b>verzwakt</b>.',
         'Nu vleermuisverblijf met uitzicht over het <b>Markermeer</b>.'],
 'phen': ['<span class="months">Okt\u2013Mrt</span> \U0001f987 <b>Vleermuizen</b> overwinteren in het fort.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Gekraagde roodstaart</b> in de oude bomen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Watervogels</b> op het aangrenzende Markermeer.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Trek</b> langs de dijk en het fortbos.'],
 'wild': ['\U0001f987 Watervleermuis \u00b7 Grootoorvleermuis', '\U0001f426 Groene specht \u00b7 Boomkruiper \u00b7 Gekraagde roodstaart', '\U0001f986 Kuifeend \u00b7 Smient \u00b7 Fuut op het Markermeer', '\U0001f33c Taludflora op de wallen', '\U0001f438 Amfibie\u00ebn in de gracht'],
 'trail': ['Parkeren bij <b>Edam</b>; terrein en dijk te belopen.',
           'Klim de <b>zeedijk</b> op voor uitzicht over het Markermeer.',
           'Combineer met de <b>Uiterdijken</b> langs dezelfde dijk.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f UNESCO-werelderfgoed \u00b7 \U0001f6b4 Fietsroute over de dijk'
}, {
 'tags': ['North Holland \u00b7 Edam-Volendam', 'Defence Line of Amsterdam \u00b7 northernmost fort of the line', 'list 36 \u00b7 no. 148'],
 'loc': '\U0001f4cd Near Edam, on the Markermeer \u00b7 Fort grounds \u00b7 Small',
 'desc': '<b>Fort Edam</b> is the northernmost fort of the Defence Line of Amsterdam and closes the ring against the former Zuiderzee. That position was strategically crucial: here the inundation line ended against open water, and an enemy following the sea dike could only pass at this point. The fort therefore literally guarded the <b>end point of the line</b>. Interestingly, the builders faced a problem that did not arise elsewhere: the sea dike itself must not be weakened, so the fort stands beside it rather than on it. The site consists of a concrete building with <b>moat and planting</b>, set between dike and polder. <b>Bats</b> hibernate here, and <b>green woodpecker, treecreeper and redstart</b> breed on the grounds.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds), Oct\u2013Mar (bats and waterfowl on the Markermeer)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats and views over the Markermeer.',
 'why': ['The <b>northernmost fort</b> \u2014 closing the ring against the Zuiderzee.',
         'Guarded the <b>end point of the inundation line</b> at open water.',
         'Stands beside the sea dike, which must not be <b>weakened</b>.',
         'Now a bat roost with views over the <b>Markermeer</b>.'],
 'phen': ['<span class="months">Oct\u2013Mar</span> \U0001f987 <b>Bats</b> hibernate in the fort.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redstart</b> in the old trees.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Waterfowl</b> on the adjoining Markermeer.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Migration</b> along the dike and fort wood.'],
 'wild': ['\U0001f987 Daubenton\u2019s bat \u00b7 Brown long-eared bat', '\U0001f426 Green woodpecker \u00b7 Treecreeper \u00b7 Redstart', '\U0001f986 Tufted duck \u00b7 Wigeon \u00b7 Great crested grebe on the Markermeer', '\U0001f33c Bank flora on the ramparts', '\U0001f438 Amphibians in the moat'],
 'trail': ['Park at <b>Edam</b>; grounds and dike can be walked.',
           'Climb the <b>sea dike</b> for views over the Markermeer.',
           'Combine with the <b>Uiterdijken</b> along the same dike.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f UNESCO World Heritage \u00b7 \U0001f6b4 Cycle route on the dike'
}))

mk.insert(C, '1424')
mk.progress(1429)
mk.check()
