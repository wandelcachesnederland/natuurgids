# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1395, 'Wandelpad Dorregeesterpolder', {
 'tags': ['Noord-Holland \u00b7 Uitgeest', 'Polder \u00b7 wandelpad door veenweide', 'list 36 \u00b7 no. 114'],
 'loc': '\U0001f4cd Tussen Uitgeest en Akersloot \u00b7 Veenweidepolder \u00b7 Middelgroot',
 'desc': 'De <b>Dorregeesterpolder</b> is genoemd naar het verdwenen dorpje <b>Dorregeest</b>, en dat achtervoegsel <b>-geest</b> is in Noord-Holland een landschapsaanduiding van de eerste orde: <i>geest</i> betekent <b>hoge, droge zandgrond</b>, van dezelfde stam als <i>gust</i> \u2014 onvruchtbaar. Geestgronden zijn de oude strandwallen, en daar stonden de dorpen; het lage veen ertussen was weiland. Dorregeest verdween, maar zijn naam bleef aan de polder hangen. Het <b>wandelpad</b> loopt dwars door de veenweide, langs sloten en over dammetjes \u2014 in dit deel van Noord-Holland een zeldzaamheid, want de meeste polders zijn alleen vanaf de weg te zien. Onderweg zie je <b>grutto, tureluur, kievit en slobeend</b>, en in de sloten bloeit in mei de <b>waterviolier</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (weidevogels), mei\u2013jun (waterviolier in de sloten)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 weidevogels roepen boven de polder.',
 'why': ['<b>-geest</b> = hoge, droge zandgrond \u2014 de oude strandwallen.',
         'Genoemd naar het <b>verdwenen dorpje Dorregeest</b>.',
         'Zeldzaam <b>wandelpad dwars door de veenweide</b>.',
         '<b>Grutto, tureluur en slobeend</b> langs de route.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Grutto en kievit</b> keren terug.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tureluur en slobeend</b> broeden.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33f <b>Waterviolier</b> bloeit in de sloten.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Ganzen en smienten</b> op de weilanden.'],
 'wild': ['\U0001f426 Grutto \u00b7 Tureluur \u00b7 Kievit \u00b7 Scholekster', '\U0001f986 Slobeend \u00b7 Krakeend \u00b7 Smient', '\U0001f33f Waterviolier \u00b7 Krabbenscheer \u00b7 Dotterbloem', '\U0001f985 Bruine kiekendief \u00b7 Buizerd', '\U0001f9a0 Libellen langs de sloten'],
 'trail': ['Parkeren bij <b>Uitgeest</b>; het wandelpad start aan de polderrand.',
           'Volg de <b>dammetjes en klaphekjes</b> door het weiland.',
           'Blijf in het broedseizoen strikt <b>op het pad</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Weidevogelgebied mrt\u2013jun \u00b7 \U0001f97e Nat'
}, {
 'tags': ['North Holland \u00b7 Uitgeest', 'Polder \u00b7 footpath through peat meadow', 'list 36 \u00b7 no. 114'],
 'loc': '\U0001f4cd Between Uitgeest and Akersloot \u00b7 Peat-meadow polder \u00b7 Medium-sized',
 'desc': 'The <b>Dorregeesterpolder</b> is named after the vanished hamlet of <b>Dorregeest</b>, and the suffix <b>-geest</b> is a first-order landscape term in North Holland: <i>geest</i> means <b>high, dry sandy ground</b>, from the same stem as <i>gust</i> \u2014 barren. Geest grounds are the old beach ridges, and that is where the villages stood; the low peat in between was pasture. Dorregeest vanished, but its name stuck to the polder. The <b>footpath</b> runs straight through the peat meadow, along ditches and over little dams \u2014 a rarity in this part of North Holland, since most polders can only be seen from the road. Along the way you see <b>godwit, redshank, lapwing and shoveler</b>, and in May the <b>water violet</b> flowers in the ditches.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (meadow birds), May\u2013Jun (water violet in the ditches)<br>\n    <b>Best time of day:</b> Early morning \u2014 meadow birds calling over the polder.',
 'why': ['<b>-geest</b> = high, dry sandy ground \u2014 the old beach ridges.',
         'Named after the <b>vanished hamlet of Dorregeest</b>.',
         'Rare <b>footpath straight through the peat meadow</b>.',
         '<b>Godwit, redshank and shoveler</b> along the route.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Godwit and lapwing</b> return.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redshank and shoveler</b> breed.',
          '<span class="months">May\u2013Jun</span> \U0001f33f <b>Water violet</b> flowers in the ditches.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Geese and wigeon</b> on the meadows.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Redshank \u00b7 Lapwing \u00b7 Oystercatcher', '\U0001f986 Shoveler \u00b7 Gadwall \u00b7 Wigeon', '\U0001f33f Water violet \u00b7 Water soldier \u00b7 Marsh marigold', '\U0001f985 Marsh harrier \u00b7 Buzzard', '\U0001f9a0 Dragonflies along the ditches'],
 'trail': ['Park at <b>Uitgeest</b>; the footpath starts at the polder edge.',
           'Follow the <b>little dams and kissing gates</b> through the meadow.',
           'In the breeding season keep strictly <b>to the path</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Meadow-bird area Mar\u2013Jun \u00b7 \U0001f97e Wet'
}, card_class='card water'))

C.append(mk.card(1396, 'Alkmaardermeer', {
 'tags': ['Noord-Holland \u00b7 Uitgeest', 'Meer \u00b7 veenmeer met rietoevers en moeraslanden', 'list 36 \u00b7 no. 115'],
 'loc': '\U0001f4cd Tussen Alkmaar, Uitgeest en Krommenie \u00b7 Veenmeer \u00b7 Groot',
 'desc': 'Het <b>Alkmaardermeer</b> is een van de weinige overgebleven <b>veenmeren</b> van Noord-Holland, en het bestaat nog doordat het niet werd drooggemalen zoals de Beemster, Purmer en Schermer. Zulke meren ontstonden niet natuurlijk maar door <b>turfwinning en golfslag</b>: als er eenmaal open water was, sloegen de golven bij storm steeds meer veenoever weg \u2014 een zichzelf versterkend proces dat hele dorpen verzwolg. Toen de wateroverlast onhoudbaar werd, verdween in de zeventiende eeuw het ene na het andere meer onder de molens. Het Alkmaardermeer bleef als boezemwater gespaard. Nu is het een groot open water met <b>rietoevers, moeraslanden en legakkers</b>, waar <b>fuut, aalscholver, zwarte stern en bruine kiekendief</b> broeden en in de winter duizenden <b>watervogels</b> pleisteren.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Nov\u2013feb</b> (watervogelconcentraties), mei\u2013jul (zwarte stern en rietvogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 spiegelglad water en actieve vogels.',
 'why': ['Zeldzaam overgebleven <b>veenmeer</b> \u2014 niet drooggemalen.',
         'Ontstaan door <b>turfwinning en golfslag</b>, een zichzelf versterkend proces.',
         'Bleef gespaard als <b>boezemwater</b> toen de Beemster en Schermer verdwenen.',
         '<b>Zwarte stern</b> broedt op vlotjes tussen de rietoevers.'],
 'phen': ['<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Zwarte stern</b> broedt op krabbenscheer en vlotjes.',
          '<span class="months">Apr\u2013Jun</span> \U0001f985 <b>Bruine kiekendief</b> jaagt boven het riet.',
          '<span class="months">Aug\u2013Okt</span> \U0001f426 <b>Doortrekkende steltlopers</b> op de oevers.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Duizenden watervogels</b> op het meer.'],
 'wild': ['\U0001f426 Zwarte stern \u00b7 Fuut \u00b7 Aalscholver', '\U0001f985 Bruine kiekendief \u00b7 Visarend (doortrek)', '\U0001f986 Kuifeend \u00b7 Tafeleend \u00b7 Smient \u00b7 Nonnetje', '\U0001f33e Riet \u00b7 Krabbenscheer \u00b7 Lisdodde', '\U0001f41f Snoek \u00b7 Baars \u00b7 Brasem'],
 'trail': ['Parkeren bij <b>Uitgeest</b> of <b>Akersloot</b>; oeverpaden en uitkijkpunten.',
           'De <b>oostoever</b> bij de moeraslanden is het rijkst aan vogels.',
           'Winter voor aantallen, <b>juni</b> voor de zwarte sterns.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6a3 Watersport \u00b7 \u26a0\ufe0f Rietoevers kwetsbaar'
}, {
 'tags': ['North Holland \u00b7 Uitgeest', 'Lake \u00b7 peat lake with reed banks and marshland', 'list 36 \u00b7 no. 115'],
 'loc': '\U0001f4cd Between Alkmaar, Uitgeest and Krommenie \u00b7 Peat lake \u00b7 Large',
 'desc': 'The <b>Alkmaardermeer</b> is one of the few surviving <b>peat lakes</b> of North Holland, and it still exists because it was not pumped dry like the Beemster, Purmer and Schermer. Such lakes did not arise naturally but through <b>peat cutting and wave action</b>: once there was open water, storms tore away ever more peat bank \u2014 a self-reinforcing process that swallowed whole villages. When the flooding became untenable, one lake after another disappeared beneath the windmills in the seventeenth century. The Alkmaardermeer was spared as storage water. It is now a large open water with <b>reed banks, marshland and peat baulks</b>, where <b>great crested grebe, cormorant, black tern and marsh harrier</b> breed and thousands of <b>waterfowl</b> stage in winter.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Nov\u2013Feb</b> (waterfowl concentrations), May\u2013Jul (black tern and reed birds)<br>\n    <b>Best time of day:</b> Early morning \u2014 mirror-calm water and active birds.',
 'why': ['Rare surviving <b>peat lake</b> \u2014 never pumped dry.',
         'Formed by <b>peat cutting and wave action</b>, a self-reinforcing process.',
         'Spared as <b>storage water</b> when the Beemster and Schermer vanished.',
         '<b>Black tern</b> breeds on rafts among the reed banks.'],
 'phen': ['<span class="months">May\u2013Jul</span> \U0001f426 <b>Black tern</b> breeds on water soldier and rafts.',
          '<span class="months">Apr\u2013Jun</span> \U0001f985 <b>Marsh harrier</b> hunts over the reed.',
          '<span class="months">Aug\u2013Oct</span> \U0001f426 <b>Passage waders</b> on the banks.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Thousands of waterfowl</b> on the lake.'],
 'wild': ['\U0001f426 Black tern \u00b7 Great crested grebe \u00b7 Cormorant', '\U0001f985 Marsh harrier \u00b7 Osprey (on passage)', '\U0001f986 Tufted duck \u00b7 Pochard \u00b7 Wigeon \u00b7 Smew', '\U0001f33e Reed \u00b7 Water soldier \u00b7 Bulrush', '\U0001f41f Pike \u00b7 Perch \u00b7 Bream'],
 'trail': ['Park at <b>Uitgeest</b> or <b>Akersloot</b>; bank paths and viewpoints.',
           'The <b>eastern shore</b> by the marshland is richest in birds.',
           'Winter for numbers, <b>June</b> for the black terns.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6a3 Water sports \u00b7 \u26a0\ufe0f Reed banks fragile'
}, card_class='card water'))

C.append(mk.card(1397, 'Marquette en Huldtoneel', {
 'tags': ['Noord-Holland \u00b7 Heemskerk', 'Landgoed \u00b7 kasteelbos en oude weilanden', 'list 36 \u00b7 no. 116'],
 'loc': '\U0001f4cd Heemskerk \u00b7 Kasteellandgoed \u00b7 Middelgroot',
 'desc': 'Landgoed <b>Marquette</b> bij Heemskerk draait om een middeleeuws kasteel dat in de zeventiende eeuw werd verbouwd tot buitenplaats; de naam kreeg het van een Franse eigenaar. Het aangrenzende <b>Huldtoneel</b> heeft een veel oudere naam met een verrassende betekenis: een <b>huldtoneel</b> of <i>huldigingstoneel</i> was de plek waar de heer van het gebied door zijn onderdanen werd <b>gehuldigd</b> \u2014 een openbare ceremoni\u00eble weide waar trouw werd gezworen. Zulke plekken lagen buiten het kasteel, in het open veld, zodat iedereen kon toekijken. Ecologisch is het landgoed nu vooral waardevol om zijn <b>oude parkbomen</b> op de strandwal en de natte weilanden erachter. Er broeden <b>boomklever, grote bonte specht, bosuil en gekraagde roodstaart</b>, en in het voorjaar bloeit een rijke <b>stinzenflora</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013mei</b> (stinzenflora en zang), okt\u2013nov (herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 licht door het oude parkbos.',
 'why': ['Middeleeuws kasteel, in de 17e eeuw tot <b>buitenplaats</b> verbouwd.',
         '<b>Huldtoneel</b> = ceremoni\u00eble weide waar de heer werd gehuldigd.',
         'Zulke plekken lagen <b>in het open veld</b>, zichtbaar voor iedereen.',
         'Oude parkbomen op de strandwal plus <b>natte weilanden</b>.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzenflora</b>: sneeuwklokje, winterakoniet, boshyacint.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Gekraagde roodstaart</b> in de oude bomen.',
          '<span class="months">Mei\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> boven de kasteelgracht.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> in het parkbos.'],
 'wild': ['\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Gekraagde roodstaart', '\U0001f989 Bosuil \u00b7 Ransuil', '\U0001f33c Sneeuwklokje \u00b7 Winterakoniet \u00b7 Boshyacint', '\U0001f987 Watervleermuis boven de gracht', '\U0001f333 Oude beuk \u00b7 Eik \u00b7 Linde'],
 'trail': ['Parkeren bij <b>Heemskerk</b>; het landgoedpark is vrij toegankelijk.',
           'Zoek het <b>Huldtoneel</b> \u2014 de open weide naast het kasteelbos.',
           'Maart is de maand van de <b>stinzenflora</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Park gratis \u00b7 \U0001f3db\ufe0f Kasteel en historisch huldigingsveld'
}, {
 'tags': ['North Holland \u00b7 Heemskerk', 'Estate \u00b7 castle woodland and old meadows', 'list 36 \u00b7 no. 116'],
 'loc': '\U0001f4cd Heemskerk \u00b7 Castle estate \u00b7 Medium-sized',
 'desc': 'The <b>Marquette</b> estate at Heemskerk centres on a medieval castle converted into a country seat in the seventeenth century; it took its name from a French owner. The adjoining <b>Huldtoneel</b> has a far older name with a surprising meaning: a <b>huldtoneel</b> or homage ground was the place where the lord of the district was <b>paid homage</b> by his subjects \u2014 a public ceremonial meadow where allegiance was sworn. Such places lay outside the castle, in the open field, so that everyone could watch. Ecologically the estate is now valuable above all for its <b>old park trees</b> on the beach ridge and the wet meadows behind. <b>Nuthatch, great spotted woodpecker, tawny owl and redstart</b> breed here, and a rich <b>stinzen flora</b> flowers in spring.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013May</b> (stinzen flora and song), Oct\u2013Nov (autumn colour)<br>\n    <b>Best time of day:</b> Morning \u2014 light through the old park woodland.',
 'why': ['Medieval castle, converted into a <b>country seat</b> in the 17th century.',
         '<b>Huldtoneel</b> = ceremonial meadow where the lord was paid homage.',
         'Such places lay <b>in the open field</b>, visible to all.',
         'Old park trees on the beach ridge plus <b>wet meadows</b>.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzen flora</b>: snowdrop, winter aconite, bluebell.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redstart</b> in the old trees.',
          '<span class="months">May\u2013Aug</span> \U0001f987 <b>Bats</b> above the castle moat.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> in the park woodland.'],
 'wild': ['\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Redstart', '\U0001f989 Tawny owl \u00b7 Long-eared owl', '\U0001f33c Snowdrop \u00b7 Winter aconite \u00b7 Bluebell', '\U0001f987 Daubenton\u2019s bat above the moat', '\U0001f333 Old beech \u00b7 Oak \u00b7 Lime'],
 'trail': ['Park at <b>Heemskerk</b>; the estate park is freely accessible.',
           'Look for the <b>Huldtoneel</b> \u2014 the open meadow beside the castle wood.',
           'March is the month of the <b>stinzen flora</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Park free \u00b7 \U0001f3db\ufe0f Castle and historic homage field'
}))

C.append(mk.card(1398, 'Weijenbus en Vroonmeer', {
 'tags': ['Noord-Holland \u00b7 Heemskerk', 'Duinrand \u00b7 bosje en verlande duinplas', 'list 36 \u00b7 no. 117'],
 'loc': '\U0001f4cd Tussen Heemskerk en de duinen \u00b7 Duinrandbos met laagte \u00b7 Klein',
 'desc': '<b>Weijenbus</b> en <b>Vroonmeer</b> liggen op de overgang van de binnenduinrand naar de strandvlakte, en beide namen zijn oud. <b>Bus</b> of <i>bosch</i> spreekt voor zich, maar <b>vroon</b> is een juridische term uit de vroege middeleeuwen: het betekent <b>heerlijk bezit</b>, grond die aan de landsheer toebehoorde. Vroonlanden waren vaak woeste gronden \u2014 duinen, moerassen, meren \u2014 die niemand kon ontginnen en die daarom bij de graaf bleven. De naam Vroonmeer bewaart dus het bezitsrecht van een meer dat allang verland is. Wat resteert is een <b>vochtige laagte</b> in de duinrand, met elzen- en wilgenstruweel en veenmosrijke plekken. Er broeden <b>nachtegaal, sprinkhaanzanger en grote bonte specht</b>, en in de laagte groeien <b>orchidee\u00ebn</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (nachtegaal en duinrandflora), mei\u2013jul (orchidee\u00ebn)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend of avondschemer \u2014 nachtegalen zingen dan.',
 'why': ['<b>Vroon</b> = heerlijk bezit, grond van de landsheer.',
         'Vroonlanden waren <b>woeste gronden</b> die niemand kon ontginnen.',
         'De naam bewaart een meer dat allang <b>verland</b> is.',
         'Vochtige laagte in de duinrand met <b>orchidee\u00ebn</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nachtegaal</b> zingt in het struweel.',
          '<span class="months">Mei\u2013Jun</span> \U0001f426 <b>Sprinkhaanzanger</b> ratelt in de laagte.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Orchidee\u00ebn</b> in de vochtige duinvallei.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in het duinrandbos.'],
 'wild': ['\U0001f426 Nachtegaal \u00b7 Sprinkhaanzanger \u00b7 Grote bonte specht', '\U0001f33c Rietorchis \u00b7 Moeraswespenorchis', '\U0001f333 Els \u00b7 Wilg \u00b7 Duindoorn', '\U0001f98c Ree \u00b7 Konijn \u00b7 Vos', '\U0001f9a0 Libellen in de laagte'],
 'trail': ['Parkeren bij <b>Heemskerk</b>; paden vanaf de binnenduinrand.',
           'Kom in <b>mei</b> voor de nachtegaal \u2014 hij zingt ook \u2019s nachts.',
           'Zoek de <b>laagte</b> voor orchidee\u00ebn; blijf op het pad.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbare duinvallei \u00b7 \U0001f6b6 Smalle paden'
}, {
 'tags': ['North Holland \u00b7 Heemskerk', 'Dune edge \u00b7 copse and silted-up dune lake', 'list 36 \u00b7 no. 117'],
 'loc': '\U0001f4cd Between Heemskerk and the dunes \u00b7 Dune-edge wood with hollow \u00b7 Small',
 'desc': '<b>Weijenbus</b> and <b>Vroonmeer</b> lie on the transition from the inner dune edge to the beach plain, and both names are old. <b>Bus</b> or <i>bosch</i> speaks for itself, but <b>vroon</b> is a legal term from the early Middle Ages: it means <b>seigneurial property</b>, land belonging to the territorial lord. Vroon lands were often waste grounds \u2014 dunes, marshes, lakes \u2014 that nobody could reclaim and which therefore stayed with the count. The name Vroonmeer thus preserves the ownership right to a lake long since silted up. What remains is a <b>damp hollow</b> in the dune edge, with alder and willow scrub and sphagnum-rich patches. <b>Nightingale, grasshopper warbler and great spotted woodpecker</b> breed here, and <b>orchids</b> grow in the hollow.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (nightingale and dune-edge flora), May\u2013Jul (orchids)<br>\n    <b>Best time of day:</b> Early morning or dusk \u2014 nightingales sing then.',
 'why': ['<b>Vroon</b> = seigneurial property, land of the territorial lord.',
         'Vroon lands were <b>waste grounds</b> nobody could reclaim.',
         'The name preserves a lake long since <b>silted up</b>.',
         'Damp hollow in the dune edge with <b>orchids</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nightingale</b> sings in the scrub.',
          '<span class="months">May\u2013Jun</span> \U0001f426 <b>Grasshopper warbler</b> reels in the hollow.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Orchids</b> in the damp dune slack.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> in the dune-edge wood.'],
 'wild': ['\U0001f426 Nightingale \u00b7 Grasshopper warbler \u00b7 Great spotted woodpecker', '\U0001f33c Marsh orchid \u00b7 Marsh helleborine', '\U0001f333 Alder \u00b7 Willow \u00b7 Sea buckthorn', '\U0001f98c Roe deer \u00b7 Rabbit \u00b7 Fox', '\U0001f9a0 Dragonflies in the hollow'],
 'trail': ['Park at <b>Heemskerk</b>; paths from the inner dune edge.',
           'Come in <b>May</b> for the nightingale \u2014 it sings at night too.',
           'Seek the <b>hollow</b> for orchids; keep to the path.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile dune slack \u00b7 \U0001f6b6 Narrow paths'
}, card_class='card dune'))

C.append(mk.card(1399, 'Fort Krommeniedijk', {
 'tags': ['Noord-Holland \u00b7 Uitgeest', 'Stelling van Amsterdam \u00b7 fort met gracht en fortbos', 'list 36 \u00b7 no. 118'],
 'loc': '\U0001f4cd Krommeniedijk, aan de Stelling van Amsterdam \u00b7 Fortterrein \u00b7 Klein',
 'desc': '<b>Fort Krommeniedijk</b> maakt deel uit van de <b>Stelling van Amsterdam</b>, de 135 kilometer lange verdedigingsring van 42 forten die tussen 1880 en 1920 rond de hoofdstad werd aangelegd en sinds 1996 UNESCO-werelderfgoed is. De stelling werkte niet met muren maar met <b>water</b>: bij dreiging zou een ring van polders onder water worden gezet, precies diep genoeg om onbegaanbaar te zijn voor infanterie maar te ondiep voor boten. De forten bewaakten de <b>accessen</b> \u2014 de dijken en wegen die boven het inundatiewater uitstaken. Militair is er nooit uit geschoten. Wat bleef is een betonnen fort in een <b>gracht met fortbos</b>, en de dikke muren zijn nu winterverblijf voor <b>vleermuizen</b>. Op het terrein broeden <b>ijsvogel, kerkuil en boomkruiper</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels en fortbos), okt\u2013mrt (vleermuizen in winterslaap)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 vleermuizen verlaten dan het fort.',
 'why': ['Onderdeel van de <b>Stelling van Amsterdam</b>, UNESCO-werelderfgoed.',
         'Verdedigde met <b>water</b>: te ondiep voor boten, te nat voor infanterie.',
         'Forten bewaakten de <b>accessen</b> boven het inundatiewater.',
         'Dikke muren nu <b>winterverblijf voor vleermuizen</b>.'],
 'phen': ['<span class="months">Okt\u2013Mrt</span> \U0001f987 <b>Vleermuizen</b> overwinteren in de fortgangen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> broedt in de grachtoever.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Muurflora</b> op het oude beton.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Zwermgedrag</b> van vleermuizen bij de ingang.'],
 'wild': ['\U0001f987 Watervleermuis \u00b7 Baardvleermuis \u00b7 Grootoorvleermuis', '\U0001f426 IJsvogel \u00b7 Boomkruiper \u00b7 \U0001f989 Kerkuil', '\U0001f33f Muurvarens \u00b7 Mossen op beton', '\U0001f438 Kikkers in de fortgracht', '\U0001f333 Fortbos: es \u00b7 iep \u00b7 meidoorn'],
 'trail': ['Parkeren bij <b>Krommeniedijk</b>; terrein deels vrij, fort op afspraak.',
           'Loop <b>om de gracht</b> voor het beste zicht op het fort.',
           'Betreed de <b>vleermuiskelders</b> niet in de winter.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Terrein gratis \u00b7 \U0001f3db\ufe0f UNESCO-werelderfgoed \u00b7 \u26a0\ufe0f Vleermuisverblijf'
}, {
 'tags': ['North Holland \u00b7 Uitgeest', 'Defence Line of Amsterdam \u00b7 fort with moat and fort wood', 'list 36 \u00b7 no. 118'],
 'loc': '\U0001f4cd Krommeniedijk, on the Defence Line of Amsterdam \u00b7 Fort grounds \u00b7 Small',
 'desc': '<b>Fort Krommeniedijk</b> forms part of the <b>Defence Line of Amsterdam</b>, the 135-kilometre ring of 42 forts built around the capital between 1880 and 1920 and a UNESCO World Heritage Site since 1996. The line worked not with walls but with <b>water</b>: in an emergency a ring of polders would be flooded, exactly deep enough to be impassable for infantry but too shallow for boats. The forts guarded the <b>accesses</b> \u2014 the dikes and roads standing above the inundation water. Militarily, not a shot was ever fired from them. What remains is a concrete fort in a <b>moat with fort wood</b>, and the thick walls are now a winter roost for <b>bats</b>. <b>Kingfisher, barn owl and treecreeper</b> breed on the grounds.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds and fort wood), Oct\u2013Mar (hibernating bats)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats then leave the fort.',
 'why': ['Part of the <b>Defence Line of Amsterdam</b>, UNESCO World Heritage.',
         'Defended with <b>water</b>: too shallow for boats, too wet for infantry.',
         'Forts guarded the <b>accesses</b> above the inundation water.',
         'Thick walls now a <b>winter roost for bats</b>.'],
 'phen': ['<span class="months">Oct\u2013Mar</span> \U0001f987 <b>Bats</b> hibernate in the fort corridors.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> breeds in the moat bank.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Wall flora</b> on the old concrete.',
          '<span class="months">Aug\u2013Sep</span> \U0001f987 <b>Swarming behaviour</b> of bats at the entrance.'],
 'wild': ['\U0001f987 Daubenton\u2019s bat \u00b7 Whiskered bat \u00b7 Brown long-eared bat', '\U0001f426 Kingfisher \u00b7 Treecreeper \u00b7 \U0001f989 Barn owl', '\U0001f33f Wall ferns \u00b7 Mosses on concrete', '\U0001f438 Frogs in the fort moat', '\U0001f333 Fort wood: ash \u00b7 elm \u00b7 hawthorn'],
 'trail': ['Park at <b>Krommeniedijk</b>; grounds partly open, fort by appointment.',
           'Walk <b>around the moat</b> for the best view of the fort.',
           'Do not enter the <b>bat cellars</b> in winter.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Grounds free \u00b7 \U0001f3db\ufe0f UNESCO World Heritage \u00b7 \u26a0\ufe0f Bat roost'
}))

mk.insert(C, '1394')
mk.progress(1399)
mk.check()
