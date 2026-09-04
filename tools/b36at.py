# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1505, 'De Bruine Haar', {
 'tags': ['Overijssel \u00b7 Twenterand', 'Veenrestant \u00b7 natte heide en bos op een dekzandrug', 'list 36 \u00b7 no. 224'],
 'loc': '\U0001f4cd Bij Kloosterhaar, oostelijk Overijssel \u00b7 Veen en heide \u00b7 Middelgroot',
 'desc': '<b>De Bruine Haar</b> ligt tegen de Engbertsdijksvenen aan en heeft een naam die het landschap letterlijk beschrijft. Een <b>haar</b> is in het oosten van Nederland een <b>langgerekte zandrug</b> \u2014 hetzelfde woord dat terugkomt in Kloosterhaar en tientallen veldnamen \u2014 en <b>bruin</b> verwijst naar de kleur van het veen dat eromheen lag. Zo\u2019n zandrug midden in het veen was van grote waarde: het was de enige begaanbare route door een verder ondoordringbaar moeras, en er liepen dan ook oude <b>veenwegen</b> overheen. Nu ligt hier een mozaïek van <b>natte heide, berkenbroek en veenrestanten</b>, dat als bufferzone voor het hoogveen wordt vernat. Er leven <b>heikikker, adder, gladde slang</b> en broeden <b>wulp en roodborsttapuit</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (reptielen en broedvogels), aug\u2013sep (heidebloei)<br>\n    <b>Beste tijd van de dag:</b> Warme ochtend \u2014 adders zonnen langs de paden.',
 'why': ['Een <b>haar</b> is een langgerekte zandrug in het oosten van Nederland.',
         '<b>Bruin</b> verwijst naar de kleur van het omringende veen.',
         'De rug was de enige <b>begaanbare route</b> door het moeras.',
         'Nu vernat als <b>bufferzone</b> voor het hoogveen ernaast.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Heikikker</b> kleurt blauw in de paartijd.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Wulp en roodborsttapuit</b> broeden.',
          '<span class="months">Mei\u2013Aug</span> \U0001f98e <b>Adder en gladde slang</b> op warme plekken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Dopheide</b> bloeit op de natte delen.'],
 'wild': ['\U0001f98e Adder \u00b7 Gladde slang \u00b7 Levendbarende hagedis', '\U0001f438 Heikikker \u00b7 Kleine watersalamander', '\U0001f426 Wulp \u00b7 Roodborsttapuit \u00b7 Boomleeuwerik', '\U0001f9a0 Veenlibellen boven de slenken', '\U0001f333 Zachte berk \u00b7 Dopheide \u00b7 Veenmos'],
 'trail': ['Parkeren bij <b>Kloosterhaar</b>; paden over de zandrug.',
           'Volg de <b>rug</b> \u2014 dat is de oude veenweg door het moeras.',
           'Warme ochtend voor <b>adders</b>; blijf op de paden.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Adders: blijf op de paden \u00b7 \U0001f6b6 Natte paden'
}, {
 'tags': ['Overijssel \u00b7 Twenterand', 'Bog remnant \u00b7 wet heath and wood on a cover-sand ridge', 'list 36 \u00b7 no. 224'],
 'loc': '\U0001f4cd Near Kloosterhaar, eastern Overijssel \u00b7 Bog and heath \u00b7 Medium-sized',
 'desc': '<b>De Bruine Haar</b> adjoins the Engbertsdijksvenen and bears a name that literally describes the landscape. A <b>haar</b> is, in the east of the Netherlands, an <b>elongated sand ridge</b> \u2014 the same word recurring in Kloosterhaar and dozens of field names \u2014 and <b>bruin</b> (brown) refers to the colour of the peat that lay around it. Such a ridge in the middle of the bog was of great value: it was the only passable route through an otherwise impenetrable marsh, and old <b>bog roads</b> accordingly ran across it. Now a mosaic of <b>wet heath, birch carr and bog remnants</b> lies here, being rewetted as a buffer zone for the raised bog. <b>Moor frog, adder and smooth snake</b> live here, and <b>curlew and stonechat</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (reptiles and breeding birds), Aug\u2013Sep (heather bloom)<br>\n    <b>Best time of day:</b> Warm morning \u2014 adders bask along the paths.',
 'why': ['A <b>haar</b> is an elongated sand ridge in the eastern Netherlands.',
         '<b>Bruin</b> refers to the colour of the surrounding peat.',
         'The ridge was the only <b>passable route</b> through the marsh.',
         'Now rewetted as a <b>buffer zone</b> for the raised bog beside it.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Moor frog</b> turns blue in the breeding season.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Curlew and stonechat</b> breed.',
          '<span class="months">May\u2013Aug</span> \U0001f98e <b>Adder and smooth snake</b> on warm spots.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Cross-leaved heath</b> flowers on the wet parts.'],
 'wild': ['\U0001f98e Adder \u00b7 Smooth snake \u00b7 Common lizard', '\U0001f438 Moor frog \u00b7 Smooth newt', '\U0001f426 Curlew \u00b7 Stonechat \u00b7 Woodlark', '\U0001f9a0 Bog dragonflies above the hollows', '\U0001f333 Downy birch \u00b7 Cross-leaved heath \u00b7 Sphagnum'],
 'trail': ['Park at <b>Kloosterhaar</b>; paths cross the sand ridge.',
           'Follow the <b>ridge</b> \u2014 it is the old bog road through the marsh.',
           'Warm morning for <b>adders</b>; keep to the paths.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Adders: keep to paths \u00b7 \U0001f6b6 Wet paths'
}, card_class='card heath'))

C.append(mk.card(1506, 'Bosbeek, Burg. Rijkenspark en Spaarneberg', {
 'tags': ['Noord-Holland \u00b7 Heemstede', 'Buitenplaatsen \u00b7 parken op de strandwal langs het Spaarne', 'list 36 \u00b7 no. 225'],
 'loc': '\U0001f4cd Heemstede, langs het Spaarne \u00b7 Buitenplaatsparken \u00b7 Klein',
 'desc': 'Langs het <b>Spaarne</b> bij Heemstede ligt een reeks oude buitenplaatsparken: <b>Bosbeek</b>, het <b>Burgemeester Rijkenspark</b> en de <b>Spaarneberg</b>. Ze liggen alle drie op een <b>strandwal</b> \u2014 een oude, hooggelegen zandrug die vijfduizend jaar geleden als kustlijn functioneerde en nu kilometers landinwaarts ligt. Die combinatie van hoge, droge zandgrond en nabijheid van water maakte de strook aantrekkelijk voor Amsterdamse kooplieden, die er vanaf de zeventiende eeuw hun buitens bouwden op korte trekschuitafstand van de stad. De oude bomen zijn nu ecologisch waardevol: <b>boomklever, grote bonte specht, holenduif, vleermuizen</b> en zeldzame <b>stinzenflora</b> die met de aanleg is meegekomen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013apr</b> (stinzenflora), apr\u2013jun (zang), okt\u2013nov (herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rust in de parken langs het water.',
 'why': ['Drie oude buitenplaatsparken op een <b>strandwal</b> langs het Spaarne.',
         'Een strandwal was <b>vijfduizend jaar geleden kustlijn</b>.',
         'Hoge droge grond bij water trok <b>Amsterdamse kooplieden</b>.',
         'Op korte <b>trekschuitafstand</b> van de stad.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzenflora</b> bloeit onder de oude bomen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en holenduif</b> in de holtes.',
          '<span class="months">Mei\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> boven het Spaarne.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> in beuk en linde.'],
 'wild': ['\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Holenduif', '\U0001f989 Bosuil \u00b7 \U0001f985 Sperwer', '\U0001f987 Vleermuizen in boomholtes', '\U0001f33c Sneeuwklokje \u00b7 Bostulp \u00b7 Boshyacint', '\U0001f333 Oude beuk \u00b7 Linde \u00b7 Plataan'],
 'trail': ['Parkeren in <b>Heemstede</b>; de parken liggen aaneengesloten langs het Spaarne.',
           'Loop van park naar park \u2014 de <b>strandwal</b> is als lichte hoogte voelbaar.',
           'Maart voor de <b>stinzenflora</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historische buitenplaatsen \u00b7 \U0001f6b6 Korte routes'
}, {
 'tags': ['North Holland \u00b7 Heemstede', 'Country estates \u00b7 parks on the beach ridge along the Spaarne', 'list 36 \u00b7 no. 225'],
 'loc': '\U0001f4cd Heemstede, along the Spaarne \u00b7 Estate parks \u00b7 Small',
 'desc': 'Along the <b>Spaarne</b> near Heemstede lies a series of old estate parks: <b>Bosbeek</b>, the <b>Burgemeester Rijkenspark</b> and the <b>Spaarneberg</b>. All three sit on a <b>beach ridge</b> \u2014 an old, elevated sand ridge that functioned as the coastline five thousand years ago and now lies kilometres inland. That combination of high, dry sandy ground and nearness to water made the strip attractive to Amsterdam merchants, who from the seventeenth century built their country houses here, a short tow-barge journey from the city. The old trees are now ecologically valuable: <b>nuthatch, great spotted woodpecker, stock dove, bats</b> and rare <b>stinzen flora</b> that arrived with the landscaping.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Apr</b> (stinzen flora), Apr\u2013Jun (song), Oct\u2013Nov (autumn colour)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet in the parks along the water.',
 'why': ['Three old estate parks on a <b>beach ridge</b> along the Spaarne.',
         'A beach ridge was the <b>coastline five thousand years ago</b>.',
         'High dry ground by water attracted <b>Amsterdam merchants</b>.',
         'A short <b>tow-barge journey</b> from the city.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzen flora</b> flowers beneath the old trees.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and stock dove</b> in the cavities.',
          '<span class="months">May\u2013Aug</span> \U0001f987 <b>Bats</b> above the Spaarne.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> in beech and lime.'],
 'wild': ['\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Stock dove', '\U0001f989 Tawny owl \u00b7 \U0001f985 Sparrowhawk', '\U0001f987 Bats in tree cavities', '\U0001f33c Snowdrop \u00b7 Wild tulip \u00b7 Bluebell', '\U0001f333 Old beech \u00b7 Lime \u00b7 Plane'],
 'trail': ['Park in <b>Heemstede</b>; the parks adjoin one another along the Spaarne.',
           'Walk park to park \u2014 the <b>beach ridge</b> is felt as a slight rise.',
           'March for the <b>stinzen flora</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic estates \u00b7 \U0001f6b6 Short routes'
}))

C.append(mk.card(1507, 'Landgoed Schapenduinen Bloemendaal', {
 'tags': ['Noord-Holland \u00b7 Bloemendaal', 'Binnenduinrand \u00b7 landgoed met duinbos en graslanden', 'list 36 \u00b7 no. 226'],
 'loc': '\U0001f4cd Bloemendaal, binnenduinrand \u00b7 Landgoed \u00b7 Klein',
 'desc': '<b>Schapenduinen</b> in Bloemendaal ligt op de <b>binnenduinrand</b>, en de naam verwijst naar het oude gebruik van de duinen als <b>schapenweide</b>. Voordat de duinen natuurgebied werden, waren ze eeuwenlang gemeenschappelijk graasland: dorpen aan de duinvoet lieten er hun schapen lopen, wat de vegetatie kort hield en het zand plaatselijk liet stuiven. Die begrazing was bepalend voor het open duinlandschap dat we nu als natuurlijk beschouwen \u2014 zonder vee groeit duin dicht met struweel. Op het landgoed wisselen nu <b>duinbos, graslanden en oude lanen</b> elkaar af. Er broeden <b>nachtegaal, boomklever en groene specht</b>, en op de kalkrijke duinbodem groeien zeldzame <b>orchideeën</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (nachtegaal en orchideeën)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 nachtegalen zingen in het struweel.',
 'why': ['De naam verwijst naar het gebruik van de duinen als <b>schapenweide</b>.',
         'Duinen waren eeuwenlang <b>gemeenschappelijk graasland</b>.',
         'Begrazing hield de vegetatie kort en het duin <b>open</b>.',
         'Zonder vee groeit duin dicht met <b>struweel</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nachtegaal</b> zingt in het duinstruweel.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33a <b>Orchideeën</b> op de kalkrijke duinbodem.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Vlinders</b> op de duingraslanden.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in het duinbos.'],
 'wild': ['\U0001f426 Nachtegaal \u00b7 Boomklever \u00b7 Groene specht', '\U0001f98c Ree \u00b7 \U0001f98a Vos \u00b7 Konijn', '\U0001f33a Rietorchis \u00b7 Bijenorchis \u00b7 Bokkenorchis', '\U0001f98b Duinparelmoervlinder \u00b7 \U0001f41d Wilde bijen', '\U0001f333 Duineik \u00b7 Beuk \u00b7 Duindoorn'],
 'trail': ['Parkeren in <b>Bloemendaal</b>; paden door het landgoed.',
           'Zoek de <b>overgang</b> van duinbos naar open grasland.',
           'Mei voor <b>nachtegaal en orchideeën</b> tegelijk.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbare duinvegetatie \u00b7 \U0001f6b6 Duinpaden'
}, {
 'tags': ['North Holland \u00b7 Bloemendaal', 'Inner dune edge \u00b7 estate with dune woodland and grassland', 'list 36 \u00b7 no. 226'],
 'loc': '\U0001f4cd Bloemendaal, inner dune edge \u00b7 Estate \u00b7 Small',
 'desc': '<b>Schapenduinen</b> in Bloemendaal lies on the <b>inner dune edge</b>, and the name refers to the old use of the dunes as <b>sheep pasture</b>. Before the dunes became nature reserves they were common grazing land for centuries: villages at the dune foot ran their sheep there, which kept the vegetation short and let the sand drift locally. That grazing determined the open dune landscape we now regard as natural \u2014 without livestock, dunes grow over with scrub. On the estate <b>dune woodland, grasslands and old avenues</b> now alternate. <b>Nightingale, nuthatch and green woodpecker</b> breed, and rare <b>orchids</b> grow on the lime-rich dune soil.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (nightingale and orchids)<br>\n    <b>Best time of day:</b> Early morning \u2014 nightingales sing in the scrub.',
 'why': ['The name refers to the dunes\u2019 use as <b>sheep pasture</b>.',
         'Dunes were <b>common grazing land</b> for centuries.',
         'Grazing kept the vegetation short and the dune <b>open</b>.',
         'Without livestock, dunes grow over with <b>scrub</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nightingale</b> sings in the dune scrub.',
          '<span class="months">May\u2013Jun</span> \U0001f33a <b>Orchids</b> on the lime-rich dune soil.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Butterflies</b> on the dune grasslands.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> in the dune woodland.'],
 'wild': ['\U0001f426 Nightingale \u00b7 Nuthatch \u00b7 Green woodpecker', '\U0001f98c Roe deer \u00b7 \U0001f98a Fox \u00b7 Rabbit', '\U0001f33a Marsh orchid \u00b7 Bee orchid \u00b7 Lizard orchid', '\U0001f98b Niobe fritillary \u00b7 \U0001f41d Wild bees', '\U0001f333 Dune oak \u00b7 Beech \u00b7 Sea buckthorn'],
 'trail': ['Park in <b>Bloemendaal</b>; paths cross the estate.',
           'Look for the <b>transition</b> from dune wood to open grassland.',
           'May for <b>nightingale and orchids</b> together.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile dune vegetation \u00b7 \U0001f6b6 Dune paths'
}, card_class='card dune'))

C.append(mk.card(1508, 'Bloemendaalsebos', {
 'tags': ['Noord-Holland \u00b7 Bloemendaal', 'Duinbos \u00b7 oud loofbos op de binnenduinrand', 'list 36 \u00b7 no. 227'],
 'loc': '\U0001f4cd Bloemendaal, binnenduinrand \u00b7 Duinbos \u00b7 Klein',
 'desc': 'Het <b>Bloemendaalsebos</b> is een oud loofbos op de binnenduinrand, en juist die ligging maakt het bijzonder. De <b>binnenduinrand</b> is de smalle strook waar het duin overgaat in het lager gelegen achterland: hier is de bodem <b>kalkrijk maar beschut</b>, er valt genoeg regen en er is geen zoute wind. Dat is de gunstigste combinatie in het hele duingebied, en het verklaart waarom hier bos kon groeien terwijl het duin er zelf te droog en te winderig voor is. Bovendien komt aan de binnenduinrand <b>kwelwater</b> aan de oppervlakte dat door het duinzand is gezakt. Het bos herbergt <b>boomklever, bosuil, grote bonte specht</b> en een rijke <b>voorjaarsflora</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013mei</b> (voorjaarsflora en zang), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 vogelzang in het loofbos.',
 'why': ['De <b>binnenduinrand</b> is de overgang van duin naar achterland.',
         'De bodem is er <b>kalkrijk maar beschut</b>, zonder zoute wind.',
         'De gunstigste combinatie van het hele <b>duingebied</b>.',
         'Aan de duinvoet komt <b>kwelwater</b> aan de oppervlakte.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Voorjaarsflora</b> bloeit voor het bladerdek sluit.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en zwartkop</b> zingen.',
          '<span class="months">Mei\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> jagen boven de open plekken.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de kalkrijke bodem.'],
 'wild': ['\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Zwartkop', '\U0001f989 Bosuil \u00b7 \U0001f985 Sperwer \u00b7 Havik', '\U0001f98c Ree \u00b7 \U0001f98a Vos \u00b7 \U0001f43f\ufe0f Eekhoorn', '\U0001f33c Bosanemoon \u00b7 Speenkruid \u00b7 Daslook', '\U0001f333 Beuk \u00b7 Eik \u00b7 Es \u00b7 Esdoorn'],
 'trail': ['Parkeren in <b>Bloemendaal</b>; paden door het bos naar het duin.',
           'Loop van het bos <b>het duin in</b> \u2014 de overgang is scherp.',
           'April voor de <b>voorjaarsflora</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Bospaden \u00b7 \U0001f9d2 Gezinsvriendelijk'
}, {
 'tags': ['North Holland \u00b7 Bloemendaal', 'Dune wood \u00b7 old broadleaf wood on the inner dune edge', 'list 36 \u00b7 no. 227'],
 'loc': '\U0001f4cd Bloemendaal, inner dune edge \u00b7 Dune wood \u00b7 Small',
 'desc': 'The <b>Bloemendaalsebos</b> is an old broadleaf wood on the inner dune edge, and it is precisely that position which makes it special. The <b>inner dune edge</b> is the narrow strip where the dune passes into the lower hinterland: here the soil is <b>lime-rich but sheltered</b>, rainfall is sufficient and there is no salt wind. That is the most favourable combination in the entire dune region, and it explains why woodland could grow here while the dune itself is too dry and windy for it. Moreover, <b>seepage water</b> that sank through the dune sand surfaces at the inner edge. The wood holds <b>nuthatch, tawny owl, great spotted woodpecker</b> and a rich <b>spring flora</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013May</b> (spring flora and song), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 birdsong in the broadleaf wood.',
 'why': ['The <b>inner dune edge</b> is the transition from dune to hinterland.',
         'The soil is <b>lime-rich but sheltered</b>, without salt wind.',
         'The most favourable combination in the whole <b>dune region</b>.',
         '<b>Seepage water</b> surfaces at the dune foot.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Spring flora</b> blooms before the canopy closes.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and blackcap</b> sing.',
          '<span class="months">May\u2013Aug</span> \U0001f987 <b>Bats</b> hunt above the glades.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the lime-rich soil.'],
 'wild': ['\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Blackcap', '\U0001f989 Tawny owl \u00b7 \U0001f985 Sparrowhawk \u00b7 Goshawk', '\U0001f98c Roe deer \u00b7 \U0001f98a Fox \u00b7 \U0001f43f\ufe0f Red squirrel', '\U0001f33c Wood anemone \u00b7 Lesser celandine \u00b7 Ramsons', '\U0001f333 Beech \u00b7 Oak \u00b7 Ash \u00b7 Maple'],
 'trail': ['Park in <b>Bloemendaal</b>; paths run through the wood into the dunes.',
           'Walk from the wood <b>into the dune</b> \u2014 the transition is sharp.',
           'April for the <b>spring flora</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Woodland paths \u00b7 \U0001f9d2 Family-friendly'
}))

C.append(mk.card(1509, 'Thijsse\u2019s Hof', {
 'tags': ['Noord-Holland \u00b7 Bloemendaal', 'Heemtuin \u00b7 eerste heemtuin van Nederland', 'list 36 \u00b7 no. 228'],
 'loc': '\U0001f4cd Bloemendaal, binnenduinrand \u00b7 Heemtuin \u00b7 Zeer klein',
 'desc': '<b>Thijsse\u2019s Hof</b> is de <b>eerste heemtuin van Nederland</b>, aangelegd in <b>1925</b> als geschenk aan de natuuronderwijzer en publicist <b>Jac. P. Thijsse</b>. Het idee erachter was revolutionair: in plaats van exotische sierplanten te tonen zou een tuin de <b>inheemse plantengemeenschappen</b> van de eigen streek laten zien, gerangschikt naar bodemtype \u2014 duingrasland naast duinbos naast vochtige laagte. Zo kon iedere stadsbewoner in een half uur zien hoe de natuur van zijn eigen omgeving in elkaar zat. Dat concept is sindsdien wereldwijd nagevolgd. Op nog geen twee hectare groeien honderden inheemse soorten, met <b>orchideeën, salomonszegel en daslook</b>, en er broeden <b>nachtegaal, tuinfluiter en zwartkop</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (voorjaarsflora en zang), mei\u2013jun (orchideeën)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 rustig en goed licht in de tuin.',
 'why': ['De <b>eerste heemtuin van Nederland</b>, aangelegd in 1925.',
         'Geschenk aan natuuronderwijzer <b>Jac. P. Thijsse</b>.',
         'Toont <b>inheemse plantengemeenschappen</b> gerangschikt naar bodem.',
         'Het concept is sindsdien <b>wereldwijd nagevolgd</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Voorjaarsflora</b> in de bosvakken.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nachtegaal en tuinfluiter</b> zingen.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33a <b>Orchideeën</b> in het duingrasland.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Vlinders en bijen</b> op de bloemenvakken.'],
 'wild': ['\U0001f426 Nachtegaal \u00b7 Tuinfluiter \u00b7 Zwartkop', '\U0001f33a Orchideeën \u00b7 Salomonszegel \u00b7 Daslook', '\U0001f98b Vlinders \u00b7 \U0001f41d Wilde bijen', '\U0001f438 Amfibieën in de poel', '\U0001f333 Inheemse bomen en struiken naar bodemtype'],
 'trail': ['Parkeren in <b>Bloemendaal</b>; de tuin ligt bij het Bloemendaalsebos.',
           'Volg de <b>bodemvolgorde</b> door de tuin \u2014 dat is het ontwerpidee.',
           'Mei voor <b>orchideeën en nachtegaal</b>.'],
 'foot': '\U0001f436 Honden verboden \u00b7 \U0001f4b6 Vrijwillige bijdrage \u00b7 \U0001f552 Beperkte openingstijden \u00b7 \U0001f33f Heemtuin'
}, {
 'tags': ['North Holland \u00b7 Bloemendaal', 'Native plant garden \u00b7 the first heemtuin in the Netherlands', 'list 36 \u00b7 no. 228'],
 'loc': '\U0001f4cd Bloemendaal, inner dune edge \u00b7 Native plant garden \u00b7 Very small',
 'desc': '<b>Thijsse\u2019s Hof</b> is the <b>first heemtuin in the Netherlands</b>, laid out in <b>1925</b> as a gift to the nature teacher and writer <b>Jac. P. Thijsse</b>. The idea behind it was revolutionary: instead of displaying exotic ornamentals, a garden would show the <b>native plant communities</b> of its own region, arranged by soil type \u2014 dune grassland beside dune wood beside damp hollow. Any city dweller could thus see in half an hour how the nature of his own surroundings fitted together. The concept has been imitated worldwide ever since. On barely two hectares hundreds of native species grow, with <b>orchids, Solomon\u2019s seal and ramsons</b>, and <b>nightingale, garden warbler and blackcap</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (spring flora and song), May\u2013Jun (orchids)<br>\n    <b>Best time of day:</b> Morning \u2014 quiet and good light in the garden.',
 'why': ['The <b>first native plant garden in the Netherlands</b>, from 1925.',
         'A gift to the nature teacher <b>Jac. P. Thijsse</b>.',
         'Shows <b>native plant communities</b> arranged by soil type.',
         'The concept has been <b>imitated worldwide</b> ever since.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Spring flora</b> in the woodland sections.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nightingale and garden warbler</b> sing.',
          '<span class="months">May\u2013Jun</span> \U0001f33a <b>Orchids</b> in the dune grassland.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Butterflies and bees</b> on the flower beds.'],
 'wild': ['\U0001f426 Nightingale \u00b7 Garden warbler \u00b7 Blackcap', '\U0001f33a Orchids \u00b7 Solomon\u2019s seal \u00b7 Ramsons', '\U0001f98b Butterflies \u00b7 \U0001f41d Wild bees', '\U0001f438 Amphibians in the pool', '\U0001f333 Native trees and shrubs arranged by soil'],
 'trail': ['Park in <b>Bloemendaal</b>; the garden adjoins the Bloemendaalsebos.',
           'Follow the <b>soil sequence</b> through the garden \u2014 that is the design idea.',
           'May for <b>orchids and nightingale</b>.'],
 'foot': '\U0001f436 No dogs \u00b7 \U0001f4b6 Voluntary contribution \u00b7 \U0001f552 Limited opening hours \u00b7 \U0001f33f Native plant garden'
}))

mk.insert(C, '1504')
mk.progress(1509)
mk.check()
