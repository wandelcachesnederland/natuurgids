# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1335, 'Orvelte', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Museumdorp \u00b7 esdorp met houtwallen en essen', 'list 36 \u00b7 no. 54'],
 'loc': '\U0001f4cd Het dorp Orvelte bij Westerbork \u00b7 Beschermd esdorp \u00b7 Middelgroot',
 'desc': '<b>Orvelte</b> is het bekendste esdorp van Drenthe en sinds 1967 een <b>beschermd dorpsgezicht</b> \u2014 een status die het te danken heeft aan een merkwaardig toeval: het dorp was in de jaren zestig zo verpauperd dat niemand er ge\u00efnvesteerd had, waardoor de negentiende-eeuwse structuur ongeschonden bewaard bleef. Wat toen achterstand leek, bleek erfgoed. Voor de natuurliefhebber is niet het dorp zelf maar het <b>omringende landschap</b> de reden om te komen: de es, de houtwallen, de oude zandwegen en de madelanden langs het Oranjekanaal liggen er nog in hun onderlinge samenhang. In de <b>eeuwenoude eiken</b> rond het dorp broeden steenuil, holenduif en boomklever, en de zwaluwen die onder de boerderijdaken nestelen zijn hier nog talrijk \u2014 iets wat in gemoderniseerde dorpen juist verdwenen is.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (zwaluwen, steenuil en bloei), sep\u2013okt (herfstlicht)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 v\u00f3\u00f3r de toeristen, en de beste tijd voor vogels.',
 'why': ['Beschermd esdorp \u2014 bewaard doordat er <b>nooit ge\u00efnvesteerd</b> werd.',
         'Es, houtwallen, zandwegen en madelanden nog in <b>onderlinge samenhang</b>.',
         '<b>Eeuwenoude eiken</b> met steenuil, holenduif en boomklever.',
         'Boerenzwaluwen nog talrijk onder de <b>oude daken</b>.'],
 'phen': ['<span class="months">Apr\u2013Sep</span> \U0001f426 <b>Boerenzwaluwen</b> broeden in de schuren.',
          '<span class="months">Apr\u2013Jun</span> \U0001f989 <b>Steenuil</b> in de oude eiken.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Bloeiende bermen</b> langs de zandwegen.',
          '<span class="months">Sep\u2013Okt</span> \U0001f341 <b>Herfstlicht</b> over es en houtwallen.'],
 'wild': ['\U0001f989 Steenuil \u00b7 Kerkuil', '\U0001f426 Boerenzwaluw \u00b7 Huiszwaluw \u00b7 Holenduif', '\U0001f426 Boomklever \u00b7 Grote bonte specht', '\U0001f333 Eeuwenoude eiken \u00b7 Houtwallen', '\U0001f98c Ree \u00b7 Haas'],
 'trail': ['Parkeren aan de <b>rand van Orvelte</b>; het dorp is autovrij.',
           'Loop het dorp <b>uit</b> \u2014 de es en de houtwallen zijn het echte doel.',
           'Kom <b>vroeg</b>: het dorp is \u2019s middags druk met bezoekers.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis (parkeren betaald) \u00b7 \U0001f3db\ufe0f Beschermd dorpsgezicht \u00b7 \u26a0\ufe0f Druk in het seizoen'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Museum village \u00b7 es village with hedgebanks and open fields', 'list 36 \u00b7 no. 54'],
 'loc': '\U0001f4cd The village of Orvelte near Westerbork \u00b7 Protected es village \u00b7 Medium-sized',
 'desc': '<b>Orvelte</b> is the best-known es village in Drenthe and since 1967 a <b>protected village conservation area</b> \u2014 a status it owes to a curious accident: in the 1960s the village was so impoverished that nobody had invested in it, so the nineteenth-century structure survived unspoilt. What then looked like backwardness turned out to be heritage. For the nature lover it is not the village itself but the <b>surrounding landscape</b> that is the reason to come: the es, the hedgebanks, the old sandy tracks and the hay meadows along the Oranjekanaal still lie there in their mutual coherence. Little owl, stock dove and nuthatch breed in the <b>centuries-old oaks</b> around the village, and the swallows nesting under the farm roofs are still numerous here \u2014 something that has disappeared from modernised villages.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (swallows, little owl and blossom), Sep\u2013Oct (autumn light)<br>\n    <b>Best time of day:</b> Early morning \u2014 before the tourists, and the best time for birds.',
 'why': ['Protected es village \u2014 preserved because <b>nobody ever invested</b>.',
         'Es, hedgebanks, tracks and hay meadows still in <b>mutual coherence</b>.',
         '<b>Centuries-old oaks</b> with little owl, stock dove and nuthatch.',
         'Barn swallows still numerous under the <b>old roofs</b>.'],
 'phen': ['<span class="months">Apr\u2013Sep</span> \U0001f426 <b>Barn swallows</b> breed in the barns.',
          '<span class="months">Apr\u2013Jun</span> \U0001f989 <b>Little owl</b> in the old oaks.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Flowering verges</b> along the sandy tracks.',
          '<span class="months">Sep\u2013Oct</span> \U0001f341 <b>Autumn light</b> over es and hedgebanks.'],
 'wild': ['\U0001f989 Little owl \u00b7 Barn owl', '\U0001f426 Barn swallow \u00b7 House martin \u00b7 Stock dove', '\U0001f426 Nuthatch \u00b7 Great spotted woodpecker', '\U0001f333 Centuries-old oaks \u00b7 Hedgebanks', '\U0001f98c Roe deer \u00b7 Brown hare'],
 'trail': ['Park at the <b>edge of Orvelte</b>; the village is car-free.',
           'Walk <b>out</b> of the village \u2014 the es and hedgebanks are the real goal.',
           'Come <b>early</b>: the village is busy with visitors in the afternoon.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free (parking paid) \u00b7 \U0001f3db\ufe0f Protected village \u00b7 \u26a0\ufe0f Busy in season'
}))

C.append(mk.card(1336, 'Elp', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Esdorp \u00b7 essen, beekdal en houtwallen', 'list 36 \u00b7 no. 55'],
 'loc': '\U0001f4cd Het dorp Elp bij Westerbork \u00b7 Esdorplandschap \u00b7 Middelgroot',
 'desc': 'Het dorp <b>Elp</b> is in de archeologie een begrip: hier werd in de jaren zestig een <b>bronstijdnederzetting</b> opgegraven die zo kenmerkend bleek dat een hele cultuurperiode ernaar is vernoemd \u2014 de <b>Elp-cultuur</b>, circa 1800\u2013800 v.Chr. De boerderijen die men vond waren <b>woonstalhuizen</b>: mens en vee onder \u00e9\u00e9n dak, een bouwvorm die in Drenthe drieduizend jaar zou blijven bestaan. Dat maakt Elp tot een plek waar je de continu\u00efteit van het landschapsgebruik letterlijk in de bodem kunt aanwijzen. Bovengronds ligt een klassiek esdorplandschap met een bolle es, houtwallen en het beekdal van het <b>Elperstroompje</b>. In dat dal komt <b>kwel</b> aan de oppervlakte, waardoor er dotterbloemhooiland ligt met orchidee\u00ebn, en in de houtwallen broeden geelgors en gekraagde roodstaart.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jun</b> (dotterbloem en orchidee\u00ebn), apr\u2013jul (zang in de wallen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 mist boven het beekdal is hier bijna standaard.',
 'why': ['Naamgever van de <b>Elp-cultuur</b> uit de bronstijd.',
         'Opgegraven <b>woonstalhuizen</b>: mens en vee onder \u00e9\u00e9n dak.',
         'Drieduizend jaar <b>continu\u00efteit</b> in landschapsgebruik.',
         '<b>Kwel</b> in het beekdal met dotterbloemhooiland en orchidee\u00ebn.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dotterbloem</b> in het beekdal.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Orchidee\u00ebn</b> op de kwelplekken.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors</b> zingt vanaf de houtwallen.',
          '<span class="months">Sep\u2013Okt</span> \U0001f341 <b>Ochtendmist</b> over het Elperstroompje.'],
 'wild': ['\U0001f33c Dotterbloem \u00b7 Brede orchis \u00b7 Waterviolier', '\U0001f426 Geelgors \u00b7 Gekraagde roodstaart', '\U0001f426 Watersnip \u00b7 Wulp', '\U0001f9a0 Beekjuffers', '\U0001f333 Oude eiken in de wallen'],
 'trail': ['Parkeren in <b>Elp</b>; paden van de es naar het beekdal.',
           'Loop van <b>hoog naar laag</b> om de gradi\u00ebnt te ervaren.',
           'Combineer met <b>Orvelte</b> en het <b>Orvelterzand</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3fa Archeologisch belangrijke plek \u00b7 \U0001f97e Nat in het dal'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Es village \u00b7 open fields, brook valley and hedgebanks', 'list 36 \u00b7 no. 55'],
 'loc': '\U0001f4cd The village of Elp near Westerbork \u00b7 Es-village landscape \u00b7 Medium-sized',
 'desc': 'The village of <b>Elp</b> is a household name in archaeology: in the 1960s a <b>Bronze Age settlement</b> was excavated here that proved so characteristic that a whole cultural period was named after it \u2014 the <b>Elp culture</b>, roughly 1800\u2013800 BC. The farmhouses found were <b>byre-dwellings</b>: people and livestock under one roof, a building form that would persist in Drenthe for three thousand years. That makes Elp a place where you can literally point to the continuity of land use in the soil. Above ground lies a classic es-village landscape with a domed es, hedgebanks and the valley of the <b>Elperstroompje</b>. In that valley <b>seepage</b> reaches the surface, producing marsh-marigold hay meadow with orchids, and yellowhammer and redstart breed in the hedgebanks.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jun</b> (marsh marigold and orchids), Apr\u2013Jul (song in the banks)<br>\n    <b>Best time of day:</b> Early morning \u2014 mist over the brook valley is almost standard here.',
 'why': ['Namesake of the Bronze Age <b>Elp culture</b>.',
         'Excavated <b>byre-dwellings</b>: people and livestock under one roof.',
         'Three thousand years of <b>continuity</b> in land use.',
         '<b>Seepage</b> in the brook valley with marsh-marigold meadow and orchids.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh marigold</b> in the brook valley.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Orchids</b> at the seepage spots.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer</b> sings from the hedgebanks.',
          '<span class="months">Sep\u2013Oct</span> \U0001f341 <b>Morning mist</b> over the Elperstroompje.'],
 'wild': ['\U0001f33c Marsh marigold \u00b7 Marsh orchid \u00b7 Water violet', '\U0001f426 Yellowhammer \u00b7 Redstart', '\U0001f426 Snipe \u00b7 Curlew', '\U0001f9a0 Demoiselles', '\U0001f333 Old oaks in the banks'],
 'trail': ['Park in <b>Elp</b>; paths from the es down to the brook valley.',
           'Walk from <b>high to low</b> to experience the gradient.',
           'Combine with <b>Orvelte</b> and the <b>Orvelterzand</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3fa Archaeologically important site \u00b7 \U0001f97e Wet in the valley'
}))

C.append(mk.card(1337, 'Orvelterzand', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Stuifzand \u00b7 zandverstuiving en heide', 'list 36 \u00b7 no. 56'],
 'loc': '\U0001f4cd Ten zuiden van Orvelte \u00b7 Stuifzandgebied \u00b7 Klein',
 'desc': 'Het <b>Orvelterzand</b> is een klein maar gaaf <b>stuifzandgebied</b>, en stuifzand is inmiddels een van de zeldzaamste landschapstypen van Europa \u2014 Nederland herbergt er een onevenredig groot deel van. Het ontstond door <b>menselijk falen</b>: overbegrazing en te intensief plaggen legden de zandbodem bloot, waarna de wind vrij spel kreeg. Eeuwenlang was dat een plaag, maar de soorten die zich erop specialiseerden hebben nergens anders meer plek. Het gaat om organismen die extreme omstandigheden verdragen: <b>bodemtemperaturen boven de vijftig graden</b> in de zomer, geen enkele voedingsstof en een ondergrond die verschuift. Pioniers als <b>buntgras en ruig haarmos</b> beginnen de vastlegging, daarna volgen <b>korstmossen</b> die decennia nodig hebben. Hier leven de <b>zandhagedis</b> en gespecialiseerde graafwespen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zandhagedis en graafwespen), aug\u2013sep (heidebloei aan de randen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 hagedissen zonnen zich dan voordat het zand te heet wordt.',
 'why': ['<b>Stuifzand</b>: een van de zeldzaamste landschapstypen van Europa.',
         'Ontstaan door <b>menselijk falen</b> \u2014 overbegrazing en te intensief plaggen.',
         'Extreme omstandigheden: bodem tot <b>boven de vijftig graden</b>.',
         '<b>Zandhagedis</b> en gespecialiseerde graafwespen.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f98e <b>Zandhagedis</b> \u2014 mannetjes fel groen in de paartijd.',
          '<span class="months">Mei\u2013Jul</span> \U0001f41d <b>Graafwespen</b> maken nestgangen in het zand.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33f <b>Buntgras</b> bloeit op de vastgelegde delen.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> aan de randen.'],
 'wild': ['\U0001f98e Zandhagedis \u00b7 Levendbarende hagedis', '\U0001f41d Graafwespen \u00b7 Zandbijen', '\U0001f426 Boomleeuwerik \u00b7 Tapuit', '\U0001f33f Buntgras \u00b7 Ruig haarmos \u00b7 Rendiermos', '\U0001f98b Kleine heivlinder'],
 'trail': ['Parkeren bij <b>Orvelte</b>; paden naar het stuifzand.',
           'Blijf op de paden \u2014 <b>korstmossen</b> hebben decennia nodig om te herstellen.',
           'Kom in <b>mei</b> voor de felgroene mannetjes zandhagedis.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Uiterst kwetsbare korstmossen \u2014 nooit afsteken \u00b7 \U0001f9ed Staatsbosbeheer'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Drift sand \u00b7 sand dunes and heath', 'list 36 \u00b7 no. 56'],
 'loc': '\U0001f4cd South of Orvelte \u00b7 Drift-sand area \u00b7 Small',
 'desc': 'The <b>Orvelterzand</b> is a small but intact <b>drift-sand area</b>, and drift sand has become one of the rarest landscape types in Europe \u2014 the Netherlands holds a disproportionate share of it. It arose through <b>human failure</b>: overgrazing and excessive sod-cutting exposed the sandy soil, after which the wind had free rein. For centuries that was a plague, but the species that specialised in it have nowhere else left. These are organisms that tolerate extremes: <b>soil temperatures above fifty degrees</b> in summer, no nutrients at all and a shifting substrate. Pioneers such as <b>grey hair-grass and hair moss</b> begin the stabilisation, followed by <b>lichens</b> that need decades. The <b>sand lizard</b> and specialised digger wasps live here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (sand lizard and digger wasps), Aug\u2013Sep (heather at the margins)<br>\n    <b>Best time of day:</b> Morning \u2014 lizards bask before the sand becomes too hot.',
 'why': ['<b>Drift sand</b>: one of the rarest landscape types in Europe.',
         'Created by <b>human failure</b> \u2014 overgrazing and excessive sod-cutting.',
         'Extreme conditions: soil above <b>fifty degrees</b>.',
         '<b>Sand lizard</b> and specialised digger wasps.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f98e <b>Sand lizard</b> \u2014 males bright green in the breeding season.',
          '<span class="months">May\u2013Jul</span> \U0001f41d <b>Digger wasps</b> excavate burrows in the sand.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33f <b>Grey hair-grass</b> flowers on the stabilised parts.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Ling</b> at the margins.'],
 'wild': ['\U0001f98e Sand lizard \u00b7 Common lizard', '\U0001f41d Digger wasps \u00b7 Mining bees', '\U0001f426 Woodlark \u00b7 Wheatear', '\U0001f33f Grey hair-grass \u00b7 Hair moss \u00b7 Reindeer lichen', '\U0001f98b Grayling butterfly'],
 'trail': ['Park at <b>Orvelte</b>; paths to the drift sand.',
           'Keep to the paths \u2014 <b>lichens</b> need decades to recover.',
           'Come in <b>May</b> for the bright green male sand lizards.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Extremely fragile lichens \u2014 never cut corners \u00b7 \U0001f9ed Staatsbosbeheer'
}, card_class='card dune'))

C.append(mk.card(1338, 'Korte Maten', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Madeland \u00b7 nat hooiland langs de beek', 'list 36 \u00b7 no. 57'],
 'loc': '\U0001f4cd Bij Zwiggelte, langs het Oranjekanaal \u00b7 Madeland \u00b7 Klein',
 'desc': 'De <b>Korte Maten</b> is een strook oud hooiland waarvan de naam een landbouwkundige term bevat: <b>maat</b> (of <i>made</i>) betekent hooiland, en gaat terug op het werkwoord <i>maaien</i>. De toevoeging <i>korte</i> onderscheidde dit perceel van de langere maten verderop \u2014 een aanwijzing dat de kavels ooit met grote precisie werden benoemd en verdeeld, want hooiland was schaars en kostbaar. Elk dorp had maar een beperkte oppervlakte nat land langs de beek, en dat bepaalde hoeveel vee er \u2019s winters gehouden kon worden \u2014 en daarmee hoeveel mest er voor de es beschikbaar was. Ecologisch is dit type grasland waardevol door het eeuwenlange <b>maairegime zonder bemesting</b>: dat houdt de bodem schraal, en schraal betekent soortenrijk. Hier groeien <b>blauwe knoop, moerasviooltje en gevlekte orchis</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (orchidee\u00ebn en blauwe knoop), aug\u2013sep (vlinders op blauwe knoop)<br>\n    <b>Beste tijd van de dag:</b> Late ochtend \u2014 dan zijn de vlinders actief boven het hooiland.',
 'why': ['<b>Maat</b> = hooiland, van het werkwoord maaien \u2014 een oude landbouwterm.',
         'Hooiland bepaalde hoeveel <b>vee</b> een dorp \u2019s winters kon houden.',
         'Eeuwenlang <b>maaien zonder bemesting</b> houdt de bodem schraal.',
         '<b>Blauwe knoop, moerasviooltje en gevlekte orchis</b>.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Gevlekte orchis</b> bloeit in het hooiland.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Moerasviooltje</b> op de natste plekken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f33c <b>Blauwe knoop</b> bloeit \u2014 magneet voor vlinders.',
          '<span class="months">Aug\u2013Sep</span> \U0001f98b <b>Vlinders</b> op de late bloei.'],
 'wild': ['\U0001f33c Blauwe knoop \u00b7 Moerasviooltje \u00b7 Gevlekte orchis', '\U0001f98b Zilveren maan \u00b7 Bruine vuurvlinder', '\U0001f426 Watersnip \u00b7 Graspieper', '\U0001f9a0 Libellen', '\U0001f33f Zeggen \u00b7 Pijpenstrootje'],
 'trail': ['Parkeren bij <b>Zwiggelte</b>; paden langs het hooiland.',
           'Klein perceel \u2014 combineer met <b>Zwiggelte-Westerbork</b>.',
           'Betreed het hooiland <b>niet</b> voor de maai in juli.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbaar hooiland \u2014 blijf op de randen \u00b7 \U0001f97e Nat'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Hay meadow \u00b7 wet meadow along the brook', 'list 36 \u00b7 no. 57'],
 'loc': '\U0001f4cd Near Zwiggelte, along the Oranjekanaal \u00b7 Hay meadow \u00b7 Small',
 'desc': 'The <b>Korte Maten</b> is a strip of old hay meadow whose name contains an agricultural term: <b>maat</b> (or <i>made</i>) means hay meadow, and goes back to the verb <i>maaien</i>, to mow. The addition <i>korte</i> (short) distinguished this plot from the longer ones further along \u2014 an indication that the parcels were once named and divided with great precision, because hay meadow was scarce and precious. Each village had only a limited area of wet land along the brook, and that determined how much livestock could be kept through the winter \u2014 and hence how much manure was available for the es. Ecologically this type of grassland is valuable because of the centuries-long <b>mowing regime without fertiliser</b>: that keeps the soil poor, and poor means species-rich. <b>Devil\u2019s-bit scabious, marsh violet and heath spotted orchid</b> grow here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (orchids and scabious), Aug\u2013Sep (butterflies on the scabious)<br>\n    <b>Best time of day:</b> Late morning \u2014 butterflies are then active above the meadow.',
 'why': ['<b>Maat</b> = hay meadow, from the verb to mow \u2014 an old farming term.',
         'Hay meadow determined how much <b>livestock</b> a village could overwinter.',
         'Centuries of <b>mowing without fertiliser</b> keeps the soil poor.',
         '<b>Devil\u2019s-bit scabious, marsh violet and heath spotted orchid</b>.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33c <b>Heath spotted orchid</b> flowers in the meadow.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Marsh violet</b> on the wettest spots.',
          '<span class="months">Aug\u2013Sep</span> \U0001f33c <b>Devil\u2019s-bit scabious</b> flowers \u2014 a butterfly magnet.',
          '<span class="months">Aug\u2013Sep</span> \U0001f98b <b>Butterflies</b> on the late blooms.'],
 'wild': ['\U0001f33c Devil\u2019s-bit scabious \u00b7 Marsh violet \u00b7 Heath spotted orchid', '\U0001f98b Silver-bordered fritillary \u00b7 Sooty copper', '\U0001f426 Snipe \u00b7 Meadow pipit', '\U0001f9a0 Dragonflies', '\U0001f33f Sedges \u00b7 Purple moor-grass'],
 'trail': ['Park at <b>Zwiggelte</b>; paths along the meadow.',
           'Small parcel \u2014 combine with <b>Zwiggelte-Westerbork</b>.',
           '<b>Do not</b> enter the meadow before the July cut.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile meadow \u2014 keep to the edges \u00b7 \U0001f97e Wet'
}, card_class='card water'))

C.append(mk.card(1339, 'Nuilerveld', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Heideveld \u00b7 heiderestant en houtwallen', 'list 36 \u00b7 no. 58'],
 'loc': '\U0001f4cd Bij Nuil en Westerbork \u00b7 Heiderestant \u00b7 Klein',
 'desc': 'Het <b>Nuilerveld</b> is een klein heiderestant bij het gehucht Nuil, en het illustreert wat er van de Drentse heide is overgebleven. Rond 1850 bestond nog ongeveer <b>de helft van Drenthe uit heide</b>; een eeuw later was daar minder dan vijf procent van over. De oorzaak was de uitvinding van <b>kunstmest</b> rond 1900: zodra boeren stikstof konden kopen, hadden ze geen plaggen en geen schapen meer nodig, en werd de woeste grond in \u00e9\u00e9n generatie omgezet in bouwland of bos. Wat hier ligt, overleefde omdat de grond te arm of te nat was om rendabel te ontginnen. Het veld is klein maar compleet: <b>struikheide, dopheide, buntgras en enkele natte laagtes</b>. Er broeden <b>boomleeuwerik en roodborsttapuit</b>, en de omringende houtwallen verbinden het met andere restanten in de omgeving.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Aug\u2013sep</b> (heidebloei), apr\u2013jun (broedvogels en reptielen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 en in augustus is het licht op de bloeiende heide het mooist.',
 'why': ['Restant van de heide die ooit <b>de helft van Drenthe</b> besloeg.',
         '<b>Kunstmest</b> maakte plaggen en schapen in \u00e9\u00e9n generatie overbodig.',
         'Overleefde omdat de grond <b>te arm of te nat</b> was.',
         'Houtwallen verbinden het met andere <b>heiderestanten</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomleeuwerik</b> zingt boven het veld.',
          '<span class="months">Mei\u2013Aug</span> \U0001f98e <b>Hagedissen</b> op de zandige paden.',
          '<span class="months">Jul\u2013Aug</span> \U0001f338 <b>Dopheide</b> in de natte laagtes.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> kleurt het veld paars.'],
 'wild': ['\U0001f426 Boomleeuwerik \u00b7 Roodborsttapuit', '\U0001f98e Levendbarende hagedis', '\U0001f338 Struikheide \u00b7 Dopheide \u00b7 Buntgras', '\U0001f98b Heidevlinders', '\U0001f98c Ree'],
 'trail': ['Parkeren bij <b>Nuil</b>; paden over het veldje.',
           'Klein gebied \u2014 combineer met <b>Scharreveld</b> en <b>Gijsselte</b>.',
           'Volg de <b>houtwallen</b> naar de aangrenzende restanten.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbare heide \u2014 blijf op de paden'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Heathland \u00b7 heath remnant and hedgebanks', 'list 36 \u00b7 no. 58'],
 'loc': '\U0001f4cd Near Nuil and Westerbork \u00b7 Heath remnant \u00b7 Small',
 'desc': 'The <b>Nuilerveld</b> is a small heath remnant by the hamlet of Nuil, and it illustrates what is left of the Drenthe heath. Around 1850 roughly <b>half of Drenthe was still heath</b>; a century later less than five per cent of that remained. The cause was the invention of <b>artificial fertiliser</b> around 1900: as soon as farmers could buy nitrogen, they no longer needed sods or sheep, and the waste ground was converted to arable or woodland within a single generation. What lies here survived because the ground was too poor or too wet to reclaim profitably. The field is small but complete: <b>ling, cross-leaved heath, grey hair-grass and a few wet hollows</b>. <b>Woodlark and stonechat</b> breed here, and the surrounding hedgebanks connect it to other remnants nearby.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Aug\u2013Sep</b> (heather), Apr\u2013Jun (breeding birds and reptiles)<br>\n    <b>Best time of day:</b> Morning \u2014 and in August the light on the flowering heather is finest.',
 'why': ['Remnant of the heath that once covered <b>half of Drenthe</b>.',
         '<b>Artificial fertiliser</b> made sods and sheep redundant in one generation.',
         'Survived because the ground was <b>too poor or too wet</b>.',
         'Hedgebanks connect it to other <b>heath remnants</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Woodlark</b> sings above the field.',
          '<span class="months">May\u2013Aug</span> \U0001f98e <b>Lizards</b> on the sandy paths.',
          '<span class="months">Jul\u2013Aug</span> \U0001f338 <b>Cross-leaved heath</b> in the wet hollows.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Ling</b> turns the field purple.'],
 'wild': ['\U0001f426 Woodlark \u00b7 Stonechat', '\U0001f98e Common lizard', '\U0001f338 Ling \u00b7 Cross-leaved heath \u00b7 Grey hair-grass', '\U0001f98b Heathland butterflies', '\U0001f98c Roe deer'],
 'trail': ['Park at <b>Nuil</b>; paths across the small field.',
           'Small area \u2014 combine with <b>Scharreveld</b> and <b>Gijsselte</b>.',
           'Follow the <b>hedgebanks</b> to the adjoining remnants.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile heath \u2014 keep to the paths'
}, card_class='card dune'))

mk.insert(C, '1334')
mk.progress(1339)
mk.check()
