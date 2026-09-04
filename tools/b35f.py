# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1272, 'De Weelpolder', {
 'tags': ['Noord-Holland \u00b7 Hollands Kroon', 'Poldernatuur \u00b7 weel met natte graslanden', 'list 35 \u00b7 no. 25'],
 'loc': '\U0001f4cd Bij Wieringerwaard \u00b7 Nat poldergrasland rond een weel \u00b7 Klein gebied',
 'desc': 'De <b>Weelpolder</b> dankt zijn naam aan de <b>weel</b> in het hart ervan \u2014 opnieuw een doorbraakkolk, maar hier met een hele polder eromheen die als natuurgebied wordt beheerd. Dat maakt het geval leerzaam: je ziet niet alleen de kolk, maar ook hoe het water zich vanuit zo\u2019n diep punt door het omringende land verspreidt. Rond de weel liggen <b>natte graslanden</b> waar het peil bewust hoog wordt gehouden, met <b>greppels en laagtes</b> die in het voorjaar blank staan. Het beheer mikt op <b>kruidenrijk hooiland</b>: eenmaal per jaar maaien na half juni, maaisel afvoeren, geen bemesting. In enkele jaren tijd levert dat <b>echte koekoeksbloem, kale jonker, moerasrolklaver en zeggen</b> op. De vogelrijkdom volgt vanzelf \u2014 <b>grutto, tureluur, slobeend en zomertaling</b> broeden er, en boven de weel jaagt de <b>bruine kiekendief</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels en hooilandbloei), jul\u2013aug (insecten en libellen bij de weel)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 weidevogels alarmeren en het hooiland ligt in de dauw.',
 'why': ['Een <b>weel</b> met een complete natuurpolder eromheen.',
         'Bewust <b>hoog peil</b> met blank staande laagtes in het voorjaar.',
         'Hooilandbeheer levert <b>kruidenrijk grasland</b> met kale jonker en zeggen.',
         'Broedgebied voor <b>grutto, slobeend en zomertaling</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f4a7 <b>Blank staande laagtes</b> trekken de eerste steltlopers.',
          '<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Echte koekoeksbloem en pinksterbloem</b> in bloei.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Kuikens</b> in het hooiland; maaien uitgesteld.',
          '<span class="months">Jul\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven de weel.'],
 'wild': ['\U0001f426 Grutto \u00b7 Tureluur', '\U0001f986 Slobeend \u00b7 Zomertaling', '\U0001f985 Bruine kiekendief', '\U0001f33c Echte koekoeksbloem \u00b7 Kale jonker', '\U0001f9a0 Libellen bij de weel'],
 'trail': ['Parkeren in <b>Wieringerwaard</b>; het gebied ligt aan polderwegen.',
           'Bekijken vanaf de <b>randpaden</b> \u2014 het hooiland zelf is broedgebied.',
           'Combineer met het <b>Amstelmeer</b> en de Wieringermeerdijken.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Broedgebied \u2014 niet betreden mrt\u2013jun \u00b7 \U0001f52d Verrekijker'
}, {
 'tags': ['North Holland \u00b7 Hollands Kroon', 'Polder nature \u00b7 breach pool with wet grassland', 'list 35 \u00b7 no. 25'],
 'loc': '\U0001f4cd Near Wieringerwaard \u00b7 Wet polder grassland around a pool \u00b7 Small area',
 'desc': 'The <b>Weelpolder</b> takes its name from the <b>weel</b> at its heart \u2014 another breach pool, but here with a whole polder around it managed as a nature reserve. That makes the case instructive: you see not only the pool but also how water spreads from such a deep point through the surrounding land. Around the pool lie <b>wet grasslands</b> where the level is deliberately kept high, with <b>gullies and hollows</b> that stand under water in spring. Management aims at <b>herb-rich hay meadow</b>: mown once a year after mid-June, cuttings removed, no fertiliser. Within a few years that yields <b>ragged robin, marsh thistle, greater bird\u2019s-foot trefoil and sedges</b>. The bird life follows of its own accord \u2014 <b>black-tailed godwit, redshank, shoveler and garganey</b> breed here, and the <b>marsh harrier</b> hunts above the pool.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds and hay-meadow flowering), Jul\u2013Aug (insects and dragonflies at the pool)<br>\n    <b>Best time of day:</b> Early morning \u2014 meadow birds calling and the hay meadow still in dew.',
 'why': ['A <b>weel</b> with an entire nature polder around it.',
         'Deliberately <b>high water level</b> with flooded hollows in spring.',
         'Hay management yields <b>herb-rich grassland</b> with marsh thistle and sedges.',
         'Breeding grounds for <b>godwit, shoveler and garganey</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f4a7 <b>Flooded hollows</b> attract the first waders.',
          '<span class="months">Apr\u2013May</span> \U0001f33c <b>Ragged robin and cuckooflower</b> in bloom.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Chicks</b> in the hay meadow; mowing postponed.',
          '<span class="months">Jul\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the pool.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Redshank', '\U0001f986 Shoveler \u00b7 Garganey', '\U0001f985 Marsh harrier', '\U0001f33c Ragged robin \u00b7 Marsh thistle', '\U0001f9a0 Dragonflies at the pool'],
 'trail': ['Park in <b>Wieringerwaard</b>; the area lies along polder roads.',
           'View from the <b>edge paths</b> \u2014 the hay meadow itself is breeding ground.',
           'Combine with the <b>Amstelmeer</b> and the Wieringermeer dikes.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Breeding ground \u2014 do not enter Mar\u2013Jun \u00b7 \U0001f52d Binoculars'
}, card_class='card water'))

C.append(mk.card(1273, 'Kadetjesland Twisk', {
 'tags': ['Noord-Holland \u00b7 Medemblik', 'Historisch verkavelingslandschap \u00b7 smalle percelen', 'list 35 \u00b7 no. 26'],
 'loc': '\U0001f4cd Bij Twisk, West-Friesland \u00b7 Historisch kavelpatroon \u00b7 Klein gebied',
 'desc': 'De naam <b>Kadetjesland</b> is puur volksvernuft: van bovenaf lijken de akkertjes op een bakplaat vol <b>kadetjes</b>, kleine ronde broodjes naast elkaar. Het gaat om een uitzonderlijk gaaf bewaard stuk <b>middeleeuwse verkaveling</b>, waarbij smalle percelen tussen sloten liggen die door <b>bolle ligging</b> \u2014 hoger in het midden, aflopend naar de sloten \u2014 hun water kwijt konden. Die bolling was geen toeval maar techniek: in een tijd zonder gemalen was dit de enige manier om op natte veenklei akkerbouw te bedrijven. In heel Nederland zijn er nog maar weinig plekken waar dit patroon niet door <b>ruilverkaveling</b> is uitgewist; Twisk is er een van, en het staat dan ook op de lijst van beschermde <b>cultuurhistorische landschappen</b>. Ecologisch zit de waarde in de vele <b>slootkanten</b>: tientallen kilometers oever per vierkante kilometer, met <b>dotterbloem, zwanenbloem en waterviolier</b>, en volop <b>weidevogels</b> en amfibie\u00ebn.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (slootkantflora en weidevogels), okt\u2013nov (strijklicht toont de bolle akkers)<br>\n    <b>Beste tijd van de dag:</b> Laat in de middag \u2014 dan tekent de bolling van de percelen zich in schaduwen af.',
 'why': ['Uitzonderlijk gaaf <b>middeleeuws kavelpatroon</b>, ontsnapt aan ruilverkaveling.',
         '<b>Bolle akkers</b> als waterhuishouding zonder gemalen.',
         'Tientallen kilometers <b>slootkant</b> per vierkante kilometer.',
         'Beschermd <b>cultuurhistorisch landschap</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dotterbloem en pinksterbloem</b> langs de slootkanten.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Grutto, kievit en tureluur</b> op de percelen.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Zwanenbloem</b> bloeit roze boven het slootwater.',
          '<span class="months">Okt\u2013Nov</span> \U0001f31e <b>Strijklicht</b> maakt de bolle ligging zichtbaar.'],
 'wild': ['\U0001f426 Grutto \u00b7 Kievit \u00b7 Tureluur', '\U0001f33c Dotterbloem \u00b7 Zwanenbloem', '\U0001f33f Waterviolier \u00b7 Kikkerbeet', '\U0001f438 Groene kikker \u00b7 Kleine watersalamander', '\U0001f426 Rietgors in de slootkanten'],
 'trail': ['Parkeren in <b>Twisk</b>, zelf een beschermd dorpsgezicht met stolpboerderijen.',
           'Wandel- en fietspaden voeren <b>langs</b> de percelen \u2014 het land is particulier.',
           'Combineer met het <b>dorp Twisk</b> voor het volledige historische beeld.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Particulier akkerland \u2014 blijf op de openbare paden \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['North Holland \u00b7 Medemblik', 'Historic field pattern \u00b7 narrow strips', 'list 35 \u00b7 no. 26'],
 'loc': '\U0001f4cd Near Twisk, West Friesland \u00b7 Historic field pattern \u00b7 Small area',
 'desc': 'The name <b>Kadetjesland</b> (\u2018bread-roll land\u2019) is pure popular wit: seen from above the little fields resemble a baking tray full of <b>kadetjes</b>, small round rolls side by side. This is an exceptionally well-preserved piece of <b>medieval field division</b>, in which narrow strips lie between ditches and shed their water thanks to a <b>convex profile</b> \u2014 higher in the middle, sloping to the ditches. That camber was not accidental but a technique: in an age without pumping stations it was the only way to farm arable crops on wet peaty clay. In the whole of the Netherlands few places remain where this pattern has not been erased by <b>land consolidation</b>; Twisk is one, and it is accordingly listed as a protected <b>historic cultural landscape</b>. Ecologically the value lies in the many <b>ditch banks</b>: tens of kilometres of bank per square kilometre, with <b>marsh marigold, flowering rush and water violet</b>, and plenty of <b>meadow birds</b> and amphibians.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (ditch-bank flora and meadow birds), Oct\u2013Nov (raking light reveals the cambered fields)<br>\n    <b>Best time of day:</b> Late afternoon \u2014 when the camber of the strips shows up in shadow.',
 'why': ['Exceptionally intact <b>medieval field pattern</b>, spared by land consolidation.',
         '<b>Cambered fields</b> as water management without pumping stations.',
         'Tens of kilometres of <b>ditch bank</b> per square kilometre.',
         'Protected <b>historic cultural landscape</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh marigold and cuckooflower</b> along the ditch banks.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Godwit, lapwing and redshank</b> on the strips.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Flowering rush</b> blooms pink above the ditch water.',
          '<span class="months">Oct\u2013Nov</span> \U0001f31e <b>Raking light</b> makes the camber visible.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Lapwing \u00b7 Redshank', '\U0001f33c Marsh marigold \u00b7 Flowering rush', '\U0001f33f Water violet \u00b7 Frogbit', '\U0001f438 Green frog \u00b7 Smooth newt', '\U0001f426 Reed bunting on the ditch banks'],
 'trail': ['Park in <b>Twisk</b>, itself a protected village with traditional stolp farmhouses.',
           'Footpaths and cycle paths run <b>alongside</b> the strips \u2014 the land is private.',
           'Combine with the <b>village of Twisk</b> for the full historical picture.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Private arable land \u2014 keep to the public paths \u00b7 \U0001f6b4 Cycle route'
}))

C.append(mk.card(1274, 'Groote Vliet', {
 'tags': ['Noord-Holland \u00b7 Hollands Kroon', 'Waterplas \u00b7 moeras en rietland', 'list 35 \u00b7 no. 27'],
 'loc': '\U0001f4cd Bij Slootdorp, Wieringermeer \u00b7 Plas met rietmoeras \u00b7 Middelgroot',
 'desc': 'De <b>Groote Vliet</b> ligt in de <b>Wieringermeer</b>, de eerste van de IJsselmeerpolders (drooggevallen in 1930), en is daarmee jonge natuur in een jong land. De plas is aangelegd als <b>waterberging</b> en tegelijk als natuurgebied, en dat dubbele doel werkt hier verrassend goed. Doordat de bodem van de Wieringermeer uit <b>oude Zuiderzeeklei</b> bestaat met plaatselijk zoute kwel, is het water licht <b>brak</b> \u2014 en dat trekt een andere gemeenschap aan dan de zoete polderplassen elders. Langs de oevers groeit <b>riet, ruwe bies en zilte rus</b>, en op de slikrandjes foerageren in de trektijd <b>kluut, kemphaan en groenpootruiter</b>. Broedvogels zijn <b>bruine kiekendief, baardman, rietzanger en snor</b>. De grote rietvelden zijn bovendien een <b>slaapplaats</b>: in het najaar komen er duizenden spreeuwen en zwaluwen slapen, met soms een <b>bruine kiekendief</b> die er op jaagt.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (rietvogels), aug\u2013sep (steltlopertrek en slaapplaatsen van zwaluwen)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 het invallen van de slaapplaatsvogels is het schouwspel.',
 'why': ['Jonge natuur in de <b>Wieringermeer</b>, de eerste IJsselmeerpolder (1930).',
         'Licht <b>brak water</b> door zoute kwel uit oude Zuiderzeeklei.',
         'Grote rietvelden als <b>slaapplaats</b> voor spreeuwen en zwaluwen.',
         'Steltlopertrek met <b>kluut, kemphaan en groenpootruiter</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Snor en rietzanger</b> zingen in het rietmoeras.',
          '<span class="months">Mei\u2013Jul</span> \U0001f985 <b>Bruine kiekendief</b> broedt in het riet.',
          '<span class="months">Aug\u2013Sep</span> \U0001f426 <b>Zwaluwenslaapplaats</b> \u2014 duizenden vogels bij zonsondergang.',
          '<span class="months">Aug\u2013Okt</span> \U0001f426 <b>Steltlopertrek</b> op de slikranden.'],
 'wild': ['\U0001f985 Bruine kiekendief', '\U0001f426 Baardman \u00b7 Snor \u00b7 Rietzanger', '\U0001f426 Kluut \u00b7 Kemphaan \u00b7 Groenpootruiter', '\U0001f33f Riet \u00b7 Ruwe bies \u00b7 Zilte rus', '\U0001f986 Watervogels in de winter'],
 'trail': ['Parkeren bij <b>Slootdorp</b>; paden en een kijkpunt langs de plas.',
           'Kom in <b>augustus of september</b> tegen zonsondergang voor de slaapplaats.',
           'Neem een <b>telescoop</b> mee voor de slikranden.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Rietmoeras niet betreden \u00b7 \U0001f52d Telescoop nuttig'
}, {
 'tags': ['North Holland \u00b7 Hollands Kroon', 'Lake \u00b7 marsh and reedland', 'list 35 \u00b7 no. 27'],
 'loc': '\U0001f4cd Near Slootdorp, Wieringermeer \u00b7 Lake with reed marsh \u00b7 Medium-sized',
 'desc': 'The <b>Groote Vliet</b> lies in the <b>Wieringermeer</b>, the first of the IJsselmeer polders (drained in 1930), making it young nature in a young land. The lake was created as <b>water storage</b> and as a nature reserve at the same time, and that dual purpose works surprisingly well here. Because the Wieringermeer floor consists of <b>old Zuiderzee clay</b> with locally salty seepage, the water is slightly <b>brackish</b> \u2014 attracting a different community from the freshwater polder lakes elsewhere. Along the shores grow <b>reed, common club-rush and saltmarsh rush</b>, and on the muddy margins <b>avocet, ruff and greenshank</b> feed during migration. Breeding birds include <b>marsh harrier, bearded reedling, sedge warbler and Savi\u2019s warbler</b>. The large reedbeds are also a <b>roost</b>: in autumn thousands of starlings and swallows come to sleep there, sometimes with a <b>marsh harrier</b> hunting among them.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (reed birds), Aug\u2013Sep (wader passage and swallow roosts)<br>\n    <b>Best time of day:</b> Dusk \u2014 the arrival of the roosting birds is the spectacle.',
 'why': ['Young nature in the <b>Wieringermeer</b>, the first IJsselmeer polder (1930).',
         'Slightly <b>brackish water</b> from salty seepage through old Zuiderzee clay.',
         'Large reedbeds as a <b>roost</b> for starlings and swallows.',
         'Wader passage with <b>avocet, ruff and greenshank</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Savi\u2019s warbler and sedge warbler</b> sing in the reed marsh.',
          '<span class="months">May\u2013Jul</span> \U0001f985 <b>Marsh harrier</b> breeds in the reeds.',
          '<span class="months">Aug\u2013Sep</span> \U0001f426 <b>Swallow roost</b> \u2014 thousands of birds at sunset.',
          '<span class="months">Aug\u2013Oct</span> \U0001f426 <b>Wader passage</b> on the muddy margins.'],
 'wild': ['\U0001f985 Marsh harrier', '\U0001f426 Bearded reedling \u00b7 Savi\u2019s warbler \u00b7 Sedge warbler', '\U0001f426 Avocet \u00b7 Ruff \u00b7 Greenshank', '\U0001f33f Reed \u00b7 Club-rush \u00b7 Saltmarsh rush', '\U0001f986 Waterfowl in winter'],
 'trail': ['Park at <b>Slootdorp</b>; paths and a viewpoint along the lake.',
           'Come in <b>August or September</b> towards sunset for the roost.',
           'Bring a <b>telescope</b> for the muddy margins.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Do not enter the reed marsh \u00b7 \U0001f52d Telescope useful'
}, card_class='card water'))

C.append(mk.card(1275, 'Kleimeer', {
 'tags': ['Noord-Holland \u00b7 Alkmaar', 'Veenmoeras \u00b7 trilveen en petgaten', 'list 35 \u00b7 no. 28'],
 'loc': '\U0001f4cd Bij Koedijk en Sint Pancras \u00b7 Veenmoeras met petgaten \u00b7 Klein gebied',
 'desc': 'Het <b>Kleimeer</b> is een klein maar botanisch uitzonderlijk moerasgebied, een van de weinige plekken in Noord-Holland waar nog <b>trilveen</b> voorkomt. Trilveen ontstaat wanneer een <b>petgat</b> \u2014 een uitgeveende sloot \u2014 langzaam dichtgroeit met een drijvende mat van veenmossen en zeggen. Die mat is niet met de bodem verbonden en <b>trilt</b> letterlijk onder je voeten. Het is een uiterst kwetsbaar tussenstadium in de <b>verlanding</b>: te veel voedingsstoffen en het slaat om naar riet en struweel, te weinig water en het klinkt in. Het beheer bestaat daarom uit <b>zeer precies maaien</b>, met licht materieel of met de hand, en het openhouden van de petgaten. Wie in juni komt vindt er <b>ronde zonnedauw, veenmosorchis, moeraskartelblad en waterdrieblad</b>. Er broeden <b>rietzanger, blauwborst en waterral</b>, en het gebied is een bolwerk voor <b>zeldzame libellen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (trilveenflora en libellen), sep\u2013okt (herfstkleuren van het veen)<br>\n    <b>Beste tijd van de dag:</b> Zonnige late ochtend \u2014 libellen actief boven de petgaten.',
 'why': ['Zeldzaam <b>trilveen</b> \u2014 een drijvende mat die onder je voeten meebeweegt.',
         '<b>Petgaten</b> uit de vervening als basis van de verlanding.',
         'Bijzondere flora: <b>zonnedauw, veenmosorchis en waterdrieblad</b>.',
         'Beheer met <b>handmatig maaien</b> \u2014 het gebied verdraagt geen zware machines.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Waterdrieblad</b> bloeit wit boven het veenmos.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33a <b>Veenmosorchis en moeraskartelblad</b>.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Zeldzame libellen</b> boven de petgaten.',
          '<span class="months">Jun\u2013Sep</span> \U0001f33f <b>Ronde zonnedauw</b> vangt insecten op de veenmosmat.'],
 'wild': ['\U0001f33f Ronde zonnedauw \u00b7 Veenmos', '\U0001f33a Veenmosorchis \u00b7 Moeraskartelblad', '\U0001f426 Rietzanger \u00b7 Blauwborst \u00b7 Waterral', '\U0001f9a0 Zeldzame libellen', '\U0001f33c Waterdrieblad'],
 'trail': ['Parkeren bij <b>Koedijk</b>; het gebied ligt in het polderland.',
           '<b>Beperkt toegankelijk</b> \u2014 trilveen verdraagt geen betreding.',
           '<b>Excursies</b> via de beheerder zijn de beste manier om het te zien.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Zeer kwetsbaar trilveen \u2014 niet betreden \u00b7 \U0001f9ed Excursie aanbevolen'
}, {
 'tags': ['North Holland \u00b7 Alkmaar', 'Peat marsh \u00b7 quaking fen and peat cuttings', 'list 35 \u00b7 no. 28'],
 'loc': '\U0001f4cd Near Koedijk and Sint Pancras \u00b7 Peat marsh with cuttings \u00b7 Small area',
 'desc': 'The <b>Kleimeer</b> is a small but botanically exceptional marsh, one of the few places in North Holland where <b>quaking fen</b> still occurs. Quaking fen forms when a <b>petgat</b> \u2014 a ditch dug out for peat \u2014 slowly closes over with a floating mat of bog mosses and sedges. That mat is not attached to the bottom and literally <b>quakes</b> underfoot. It is an extremely fragile intermediate stage in <b>terrestrialisation</b>: too many nutrients and it turns to reed and scrub, too little water and it collapses. Management therefore consists of <b>very precise mowing</b>, with light machinery or by hand, and keeping the cuttings open. Visit in June and you find <b>round-leaved sundew, fen orchid, marsh lousewort and bogbean</b>. <b>Sedge warbler, bluethroat and water rail</b> breed here, and the site is a stronghold for <b>rare dragonflies</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (quaking fen flora and dragonflies), Sep\u2013Oct (autumn colours of the fen)<br>\n    <b>Best time of day:</b> Sunny late morning \u2014 dragonflies active above the cuttings.',
 'why': ['Rare <b>quaking fen</b> \u2014 a floating mat that moves underfoot.',
         '<b>Peat cuttings</b> from the extraction era as the basis of terrestrialisation.',
         'Remarkable flora: <b>sundew, fen orchid and bogbean</b>.',
         'Managed by <b>hand mowing</b> \u2014 the site tolerates no heavy machinery.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Bogbean</b> flowers white above the bog moss.',
          '<span class="months">May\u2013Jun</span> \U0001f33a <b>Fen orchid and marsh lousewort</b>.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Rare dragonflies</b> above the cuttings.',
          '<span class="months">Jun\u2013Sep</span> \U0001f33f <b>Round-leaved sundew</b> catches insects on the moss mat.'],
 'wild': ['\U0001f33f Round-leaved sundew \u00b7 Sphagnum', '\U0001f33a Fen orchid \u00b7 Marsh lousewort', '\U0001f426 Sedge warbler \u00b7 Bluethroat \u00b7 Water rail', '\U0001f9a0 Rare dragonflies', '\U0001f33c Bogbean'],
 'trail': ['Park at <b>Koedijk</b>; the site lies in the polder land.',
           '<b>Restricted access</b> \u2014 quaking fen cannot bear being walked on.',
           '<b>Guided excursions</b> via the site manager are the best way to see it.'],
 'foot': '\U0001f436 No dogs \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Very fragile quaking fen \u2014 do not enter \u00b7 \U0001f9ed Excursion recommended'
}, card_class='card water'))

C.append(mk.card(1276, 'Oosterdel', {
 'tags': ['Noord-Holland \u00b7 Langedijk', 'Eilandenrijk \u00b7 laatste restant Langedijker akkertjes', 'list 35 \u00b7 no. 29'],
 'loc': '\U0001f4cd Bij Broek op Langedijk en Sint Pancras \u00b7 Eilandenrijk \u00b7 Ruim 150 ha',
 'desc': 'Het <b>Oosterdel</b> is wat er over is van het beroemde <b>eilandenrijk van Langedijk</b> \u2014 en het is het enige stuk dat de ruilverkaveling heeft overleefd. Hier ligt nog steeds het landschap dat het Geestmerambacht tot in de jaren zestig kenmerkte: honderden minuscule <b>akkertjes</b>, gescheiden door smalle vaarsloten, alleen per <b>schuit</b> bereikbaar. Boeren voeren met platte bootjes naar hun perceeltjes om kool te oogsten, en de veiling in Broek op Langedijk was de enige ter wereld waar de schuiten <b>dwars door het veilinggebouw</b> voeren. Vandaag wordt het gebied beheerd als natuur- en cultuurhistorisch monument, met vrijwilligers die de sloten open houden en op de eilandjes <b>traditionele gewassen</b> telen. Ecologisch is de rijkdom overweldigend door de <b>oeverlengte</b>: honderden kilometers slootkant op 150 hectare, met <b>ijsvogel, rietzanger, ringslang</b> en een uitzonderlijke waterflora.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013aug</b> (waterflora, libellen en vaarseizoen), apr\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend per boot \u2014 stil water, ijsvogel en rietvogels vlak naast je.',
 'why': ['Laatste restant van het <b>eilandenrijk van Langedijk</b>.',
         'Honderden <b>akkertjes</b> alleen per schuit bereikbaar.',
         'Extreme <b>oeverlengte</b>: honderden kilometers slootkant op 150 ha.',
         'Beheerd door <b>vrijwilligers</b> met traditionele gewassen.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel en rietzanger</b> langs de vaarsloten.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Waterflora</b> \u2014 zwanenbloem, gele plomp en waterviolier.',
          '<span class="months">Jun\u2013Aug</span> \U0001f40d <b>Ringslang</b> zwemt tussen de eilandjes.',
          '<span class="months">Aug\u2013Sep</span> \U0001f955 <b>Oogst</b> van de traditionele gewassen op de akkertjes.'],
 'wild': ['\U0001f426 IJsvogel \u00b7 Rietzanger', '\U0001f40d Ringslang', '\U0001f9a0 Libellen', '\U0001f33c Zwanenbloem \u00b7 Waterviolier \u00b7 Gele plomp', '\U0001f986 Watervogels'],
 'trail': ['Startpunt bij <b>Museum BroekerVeiling</b> in Broek op Langedijk.',
           'Het gebied is het best te beleven <b>per fluisterboot of kano</b>.',
           'Ook wandelpaden langs de rand; de eilandjes zelf zijn per boot.'],
 'foot': '\U0001f436 Honden aan de lijn op de randpaden \u00b7 \U0001f4b6 Boot- en museumtickets betaald \u00b7 \u26a0\ufe0f Eilandjes alleen per boot \u00b7 \U0001f6f6 Kano of fluisterboot'
}, {
 'tags': ['North Holland \u00b7 Langedijk', 'Archipelago \u00b7 last remnant of the Langedijk fields', 'list 35 \u00b7 no. 29'],
 'loc': '\U0001f4cd Near Broek op Langedijk and Sint Pancras \u00b7 Archipelago \u00b7 Over 150 ha',
 'desc': 'The <b>Oosterdel</b> is what remains of the famous <b>archipelago of Langedijk</b> \u2014 and it is the only part that survived land consolidation. Here still lies the landscape that characterised the Geestmerambacht until the 1960s: hundreds of minute <b>fields</b>, separated by narrow boat ditches, reachable only by <b>punt</b>. Farmers rowed flat boats out to their plots to harvest cabbages, and the auction house at Broek op Langedijk was the only one in the world where the boats sailed <b>straight through the auction building</b>. Today the area is managed as a nature and heritage monument, with volunteers keeping the ditches open and growing <b>traditional crops</b> on the islets. Ecologically the richness is overwhelming because of the <b>length of bank</b>: hundreds of kilometres of ditch edge within 150 hectares, with <b>kingfisher, sedge warbler, grass snake</b> and an exceptional aquatic flora.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Aug</b> (aquatic flora, dragonflies and boating season), Apr\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Early morning by boat \u2014 still water, kingfisher and reed birds right beside you.',
 'why': ['Last remnant of the <b>Langedijk archipelago</b>.',
         'Hundreds of <b>small fields</b> reachable only by punt.',
         'Extreme <b>bank length</b>: hundreds of kilometres of ditch edge in 150 ha.',
         'Managed by <b>volunteers</b> growing traditional crops.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher and sedge warbler</b> along the boat ditches.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Aquatic flora</b> \u2014 flowering rush, yellow water-lily and water violet.',
          '<span class="months">Jun\u2013Aug</span> \U0001f40d <b>Grass snake</b> swimming between the islets.',
          '<span class="months">Aug\u2013Sep</span> \U0001f955 <b>Harvest</b> of the traditional crops on the little fields.'],
 'wild': ['\U0001f426 Kingfisher \u00b7 Sedge warbler', '\U0001f40d Grass snake', '\U0001f9a0 Dragonflies', '\U0001f33c Flowering rush \u00b7 Water violet \u00b7 Yellow water-lily', '\U0001f986 Waterfowl'],
 'trail': ['Starting point at <b>Museum BroekerVeiling</b> in Broek op Langedijk.',
           'The area is best experienced <b>by electric boat or canoe</b>.',
           'There are also footpaths along the edge; the islets are boat-only.'],
 'foot': '\U0001f436 Dogs on lead on the edge paths \u00b7 \U0001f4b6 Boat and museum tickets charged \u00b7 \u26a0\ufe0f Islets by boat only \u00b7 \U0001f6f6 Canoe or electric boat'
}, card_class='card water'))

mk.insert(C, '1271')
mk.progress(1276)
mk.check()
