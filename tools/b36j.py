# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1325, 'Leggelderveld', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Heideveld \u00b7 vochtige heide en vennen', 'list 36 \u00b7 no. 44'],
 'loc': '\U0001f4cd Bij Leggeloo en Hoogersmilde \u00b7 Heideveld \u00b7 Middelgroot',
 'desc': 'Het <b>Leggelderveld</b> is een van de weinige Drentse heidevelden waar het complete <b>gradi\u00ebnt van droog naar nat</b> nog aanwezig is. Op de hoogste ruggen groeit struikheide op stuifzand, in de laagtes staat dopheide, en op de allernatste plekken ligt <b>veenmos</b> dat langzaam nieuw hoogveen opbouwt. Dat laatste is bijzonder, want veenvorming vereist dat er meer plantaardig materiaal wordt aangemaakt dan er afbreekt \u2014 en dat lukt alleen bij een permanent hoge, zure en volkomen voedselarme waterstand. Beheerders houden die situatie in stand door <b>opslag van berken en dennen</b> weg te halen: elke boom die blijft staan pompt water uit de bodem en verdroogt de omgeving. Op de heide broeden <b>korhoen-opvolgers</b> als boomleeuwerik, roodborsttapuit en veldleeuwerik, en in de vennen leeft de <b>heikikker</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Aug\u2013sep</b> (heidebloei), apr (heikikkers), mei\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 dan hangt er dauw op de heide en zingt alles.',
 'why': ['Compleet <b>gradi\u00ebnt van droge naar natte heide</b> tot veenmos.',
         'Actieve <b>veenvorming</b> op de natste plekken.',
         'Beheer draait om het weghalen van <b>boomopslag</b> die water wegpompt.',
         '<b>Heikikker</b> in de vennen, boomleeuwerik op de droge delen.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Heikikkers</b> \u2014 mannetjes blauw in de paartijd.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomleeuwerik en roodborsttapuit</b> broeden.',
          '<span class="months">Jul\u2013Aug</span> \U0001f338 <b>Dopheide</b> bloeit in de laagtes.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> kleurt de ruggen paars.'],
 'wild': ['\U0001f438 Heikikker \u00b7 Poelkikker', '\U0001f426 Boomleeuwerik \u00b7 Roodborsttapuit \u00b7 Veldleeuwerik', '\U0001f98e Levendbarende hagedis', '\U0001f338 Struikheide \u00b7 Dopheide \u00b7 Veenmos', '\U0001f98b Heidevlinders \u00b7 Libellen'],
 'trail': ['Parkeren bij <b>Leggeloo</b>; paden over de heide.',
           'Loop van de <b>hoge ruggen naar de laagtes</b> om de gradi\u00ebnt te zien.',
           'De <b>vennen</b> zijn in april het interessantst.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbaar veenmos \u2014 blijf op de paden \u00b7 \U0001f9ed Natuurmonumenten'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Heathland \u00b7 wet heath and pools', 'list 36 \u00b7 no. 44'],
 'loc': '\U0001f4cd Near Leggeloo and Hoogersmilde \u00b7 Heathland \u00b7 Medium-sized',
 'desc': 'The <b>Leggelderveld</b> is one of the few Drenthe heaths where the complete <b>gradient from dry to wet</b> is still present. On the highest ridges ling grows on drift sand, in the hollows stands cross-leaved heath, and on the very wettest spots lies <b>sphagnum</b> slowly building new raised bog. That last is remarkable, because peat formation requires more plant material to be produced than decays \u2014 and that only works with a permanently high, acid and utterly nutrient-poor water table. Managers maintain that situation by removing <b>birch and pine encroachment</b>: every tree left standing pumps water out of the soil and dries out its surroundings. On the heath breed the <b>successors of the black grouse</b> \u2014 woodlark, stonechat and skylark \u2014 and the <b>moor frog</b> lives in the pools.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Aug\u2013Sep</b> (heather), Apr (moor frogs), May\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Early morning \u2014 dew lies on the heath and everything sings.',
 'why': ['Complete <b>gradient from dry to wet heath</b> through to sphagnum.',
         'Active <b>peat formation</b> on the wettest spots.',
         'Management centres on removing <b>tree encroachment</b> that pumps water away.',
         '<b>Moor frog</b> in the pools, woodlark on the dry parts.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Moor frogs</b> \u2014 males blue in the breeding season.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Woodlark and stonechat</b> breed.',
          '<span class="months">Jul\u2013Aug</span> \U0001f338 <b>Cross-leaved heath</b> flowers in the hollows.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Ling</b> turns the ridges purple.'],
 'wild': ['\U0001f438 Moor frog \u00b7 Pool frog', '\U0001f426 Woodlark \u00b7 Stonechat \u00b7 Skylark', '\U0001f98e Common lizard', '\U0001f338 Ling \u00b7 Cross-leaved heath \u00b7 Sphagnum', '\U0001f98b Heathland butterflies \u00b7 Dragonflies'],
 'trail': ['Park at <b>Leggeloo</b>; paths across the heath.',
           'Walk from the <b>high ridges to the hollows</b> to see the gradient.',
           'The <b>pools</b> are most interesting in April.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile sphagnum \u2014 keep to the paths \u00b7 \U0001f9ed Natuurmonumenten'
}, card_class='card dune'))

C.append(mk.card(1326, 'Dwingeloo-Smalbroek', {
 'tags': ['Drenthe \u00b7 Westerveld', 'Beekdal \u00b7 madelanden en houtwallen', 'list 36 \u00b7 no. 45'],
 'loc': '\U0001f4cd Tussen Dwingeloo en Smalbroek \u00b7 Beekdallandschap \u00b7 Middelgroot',
 'desc': 'Tussen <b>Dwingeloo</b> en het gehucht <b>Smalbroek</b> ligt een strook oud beekdal waarvan de naam alles verklapt: <b>broek</b> is het Nederlandse woord voor moerassig laagland, en <i>smal</i> slaat op de vorm van het dal. Dit is het type land dat eeuwenlang als <b>madeland</b> werd gebruikt \u2014 te nat om te ploegen, precies goed om te hooien. Het hooi ging naar de stal, de stalmest naar de es: het beekdal was daarmee letterlijk de <b>motor van de vruchtbaarheid</b> van het hele dorp. Toen kunstmest die functie overnam, verloren de madelanden hun nut en werden ze ontwaterd. Hier is dat deels teruggedraaid, met opvallend resultaat: <b>dotterbloem, echte koekoeksbloem en brede orchis</b> zijn teruggekeerd. De houtwallen op de dalrand zijn oude perceelscheidingen en herbergen <b>geelgors en gekraagde roodstaart</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jun</b> (dotterbloem en orchidee\u00ebn), apr\u2013jul (zang in de houtwallen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 mist in het dal en volle zang op de dalrand.',
 'why': ['<b>Broek</b> = moerassig laagland; het dal was ooit hooiland.',
         'Het beekdal was de <b>motor van de vruchtbaarheid</b> voor de es.',
         'Vernatting bracht <b>dotterbloem en brede orchis</b> terug.',
         'Houtwallen als oude <b>perceelscheidingen</b> met geelgors.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dotterbloem</b> kleurt het dal geel.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Brede orchis</b> in het natte hooiland.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors</b> zingt vanaf de houtwallen.',
          '<span class="months">Nov\u2013Mrt</span> \U0001f4a7 <b>Winterse plassen</b> in de laagste delen.'],
 'wild': ['\U0001f33c Dotterbloem \u00b7 Echte koekoeksbloem \u00b7 Brede orchis', '\U0001f426 Geelgors \u00b7 Gekraagde roodstaart', '\U0001f426 Watersnip \u00b7 Wulp', '\U0001f9a0 Beekjuffers', '\U0001f98c Ree'],
 'trail': ['Parkeren in <b>Dwingeloo</b>; paden het dal in.',
           'Combineer met het <b>Dwingelderveld</b> vlakbij.',
           'Draag <b>waterdicht schoeisel</b> \u2014 het dal is nat.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Nat in winter en voorjaar \u00b7 \U0001f9ed Natuurmonumenten'
}, {
 'tags': ['Drenthe \u00b7 Westerveld', 'Brook valley \u00b7 hay meadows and hedgebanks', 'list 36 \u00b7 no. 45'],
 'loc': '\U0001f4cd Between Dwingeloo and Smalbroek \u00b7 Brook-valley landscape \u00b7 Medium-sized',
 'desc': 'Between <b>Dwingeloo</b> and the hamlet of <b>Smalbroek</b> lies a strip of old brook valley whose name gives everything away: <b>broek</b> is the Dutch word for marshy lowland, and <i>smal</i> refers to the shape of the valley. This is the type of land used for centuries as <b>hay meadow</b> \u2014 too wet to plough, exactly right to mow. The hay went to the byre, the manure to the es: the brook valley was thus literally the <b>engine of fertility</b> for the whole village. When artificial fertiliser took over that role, the meadows lost their purpose and were drained. Here that has partly been reversed, with striking results: <b>marsh marigold, ragged robin and marsh orchid</b> have returned. The hedgebanks on the valley edge are old field boundaries and hold <b>yellowhammer and redstart</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jun</b> (marsh marigold and orchids), Apr\u2013Jul (song in the hedgebanks)<br>\n    <b>Best time of day:</b> Early morning \u2014 mist in the valley and full song on the valley edge.',
 'why': ['<b>Broek</b> = marshy lowland; the valley was once hay meadow.',
         'The brook valley was the <b>engine of fertility</b> for the es.',
         'Rewetting brought back <b>marsh marigold and marsh orchid</b>.',
         'Hedgebanks as old <b>field boundaries</b> with yellowhammer.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh marigold</b> turns the valley yellow.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Marsh orchid</b> in the wet hay meadow.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer</b> sings from the hedgebanks.',
          '<span class="months">Nov\u2013Mar</span> \U0001f4a7 <b>Winter pools</b> in the lowest parts.'],
 'wild': ['\U0001f33c Marsh marigold \u00b7 Ragged robin \u00b7 Marsh orchid', '\U0001f426 Yellowhammer \u00b7 Redstart', '\U0001f426 Snipe \u00b7 Curlew', '\U0001f9a0 Demoiselles', '\U0001f98c Roe deer'],
 'trail': ['Park in <b>Dwingeloo</b>; paths into the valley.',
           'Combine with the nearby <b>Dwingelderveld</b>.',
           'Wear <b>waterproof footwear</b> \u2014 the valley is wet.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Wet in winter and spring \u00b7 \U0001f9ed Natuurmonumenten'
}, card_class='card water'))

C.append(mk.card(1327, 'Terhorst', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Esgehucht \u00b7 essen, houtwallen en beekdal', 'list 36 \u00b7 no. 46'],
 'loc': '\U0001f4cd Het gehucht Terhorst bij Zuidwolde \u00b7 Esgehucht \u00b7 Klein',
 'desc': '<b>Terhorst</b> is een klein esgehucht waarvan de naam een landschappelijke term bevat: een <b>horst</b> is een hoger gelegen, drogere plek in een verder nat of laag gebied. Zulke horsten waren in Drenthe de logische vestigingsplaatsen \u2014 hoog genoeg om droge voeten te houden, dicht genoeg bij het beekdal om er hooi en weidegrond te hebben. Terhorst bestaat uit een handvol boerderijen rond een gezamenlijke <b>es</b>, omgeven door houtwallen. Wat het gehucht bijzonder maakt, is de <b>schaal</b>: alles ligt hier dicht op elkaar, zodat je binnen een paar honderd meter van bouwland via houtwal en weide naar het natte dal loopt. Die dichtheid van overgangen is precies wat veel soorten nodig hebben \u2014 de <b>steenuil</b> bijvoorbeeld jaagt in de weides maar nestelt in de oude bomen bij de boerderijen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang, bloei en steenuil), sep\u2013okt (herfstlicht over de es)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 steenuil en das worden dan actief.',
 'why': ['<b>Horst</b> = droge hoogte in nat land \u2014 de logische vestigingsplek.',
         'Handvol boerderijen rond een gezamenlijke <b>es</b>.',
         'Extreem korte afstand tussen <b>bouwland, houtwal, weide en dal</b>.',
         '<b>Steenuil</b> jaagt in de weides, nestelt bij de boerderijen.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f989 <b>Steenuil</b> roept in de schemering.',
          '<span class="months">Apr\u2013Mei</span> \U0001f338 <b>Meidoorn</b> bloeit in de houtwallen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors en grasmus</b> in het struweel.',
          '<span class="months">Sep\u2013Okt</span> \U0001f341 <b>Strijklicht</b> over het bolle esreli\u00ebf.'],
 'wild': ['\U0001f989 Steenuil \u00b7 Kerkuil', '\U0001f426 Geelgors \u00b7 Grasmus \u00b7 Boerenzwaluw', '\U0001f9a1 Das \u00b7 Steenmarter', '\U0001f333 Eik \u00b7 Meidoorn \u00b7 Hazelaar', '\U0001f98c Ree \u00b7 Haas'],
 'trail': ['Parkeren aan de rand van <b>Terhorst</b>; zandwegen door het gehucht.',
           'Klein gebied \u2014 reken op <b>een uur</b> voor het hele rondje.',
           'Kom bij <b>schemer</b> voor de uilen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Particulier erf \u2014 blijf op de openbare weg'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Es hamlet \u00b7 open fields, hedgebanks and brook valley', 'list 36 \u00b7 no. 46'],
 'loc': '\U0001f4cd The hamlet of Terhorst near Zuidwolde \u00b7 Es hamlet \u00b7 Small',
 'desc': '<b>Terhorst</b> is a small es hamlet whose name contains a landscape term: a <b>horst</b> is a higher, drier spot in an otherwise wet or low area. In Drenthe such horsts were the logical places to settle \u2014 high enough to keep dry feet, close enough to the brook valley to have hay and pasture. Terhorst consists of a handful of farms around a shared <b>es</b>, surrounded by hedgebanks. What makes the hamlet special is its <b>scale</b>: everything lies close together, so that within a few hundred metres you pass from arable through hedgebank and pasture to the wet valley. That density of transitions is exactly what many species need \u2014 the <b>little owl</b>, for instance, hunts in the pastures but nests in the old trees by the farms.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song, blossom and little owl), Sep\u2013Oct (autumn light over the es)<br>\n    <b>Best time of day:</b> Dusk \u2014 little owl and badger then become active.',
 'why': ['<b>Horst</b> = dry rise in wet land \u2014 the logical place to settle.',
         'A handful of farms around a shared <b>es</b>.',
         'Extremely short distances between <b>arable, hedgebank, pasture and valley</b>.',
         '<b>Little owl</b> hunts in the pastures, nests by the farms.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f989 <b>Little owl</b> calling at dusk.',
          '<span class="months">Apr\u2013May</span> \U0001f338 <b>Hawthorn</b> flowers in the hedgebanks.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer and whitethroat</b> in the scrub.',
          '<span class="months">Sep\u2013Oct</span> \U0001f341 <b>Raking light</b> over the domed es relief.'],
 'wild': ['\U0001f989 Little owl \u00b7 Barn owl', '\U0001f426 Yellowhammer \u00b7 Whitethroat \u00b7 Barn swallow', '\U0001f9a1 Badger \u00b7 Stone marten', '\U0001f333 Oak \u00b7 Hawthorn \u00b7 Hazel', '\U0001f98c Roe deer \u00b7 Brown hare'],
 'trail': ['Park at the edge of <b>Terhorst</b>; sandy tracks through the hamlet.',
           'Small area \u2014 allow <b>an hour</b> for the full circuit.',
           'Come at <b>dusk</b> for the owls.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Private yards \u2014 keep to public roads'
}))

C.append(mk.card(1328, 'Baarwelsleek', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Laagte \u00b7 nat grasland en moerasje', 'list 36 \u00b7 no. 47'],
 'loc': '\U0001f4cd Bij Wijster en Drijber \u00b7 Natte laagte \u00b7 Klein',
 'desc': 'De <b>Baarwelsleek</b> is een natte laagte in het Midden-Drentse zandlandschap, en het woord <b>sleek</b> \u2014 verwant aan <i>slenk</i> \u2014 wijst op precies dat: een langwerpige, ondiepe depressie waarin het water blijft staan. Zulke laagtes zijn de restanten van <b>smeltwatergeulen</b> uit de laatste ijstijd, toen water van smeltend permafrostijs over de bevroren ondergrond wegstroomde en ondiepe dalen uitsleep. Omdat de bodem er leemhoudend is, zakt regenwater niet weg en blijft de laagte nat \u2014 in een landschap dat verder kurkdroog zandzand is. Dat contrast maakt deze plekken tot <b>ecologische eilanden</b>: hier groeien zeggen, pijpenstrootje en veenpluis, en amfibie\u00ebn gebruiken de plassen om te paaien. In het broedseizoen zit er <b>watersnip</b>, en \u2019s winters foerageren er <b>watersnippen en houtsnippen</b> in de zachte bodem.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (amfibie\u00ebn en watersnip), mei\u2013jul (zeggen en veenpluis)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend of schemer \u2014 snippen zijn dan actief.',
 'why': ['<b>Sleek</b> = ondiepe smeltwatergeul uit de ijstijd.',
         'Leemhoudende bodem houdt water vast in een <b>kurkdroog zandlandschap</b>.',
         'Functioneert als <b>ecologisch eiland</b> voor natte soorten.',
         'Paaiplaats voor amfibie\u00ebn, foerageerplek voor <b>snippen</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Amfibie\u00ebn</b> paaien in de laagte.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Watersnip</b> baltst boven de natte delen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33f <b>Veenpluis</b> met witte pluizen.',
          '<span class="months">Okt\u2013Feb</span> \U0001f426 <b>Houtsnip</b> foerageert in de zachte bodem.'],
 'wild': ['\U0001f426 Watersnip \u00b7 Houtsnip', '\U0001f438 Bruine kikker \u00b7 Kleine watersalamander', '\U0001f33f Zeggen \u00b7 Pijpenstrootje \u00b7 Veenpluis', '\U0001f9a0 Libellen', '\U0001f98c Ree'],
 'trail': ['Parkeren bij <b>Wijster</b>; paden langs de laagte.',
           'Klein gebied \u2014 combineer met <b>Drijber</b> en <b>Kremboong</b>.',
           'Blijf op de <b>randen</b>: de laagte zelf is kwetsbaar en nat.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Nat het hele jaar \u00b7 \u26a0\ufe0f Kwetsbare vegetatie'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Hollow \u00b7 wet grassland and small marsh', 'list 36 \u00b7 no. 47'],
 'loc': '\U0001f4cd Near Wijster and Drijber \u00b7 Wet hollow \u00b7 Small',
 'desc': 'The <b>Baarwelsleek</b> is a wet hollow in the Mid-Drenthe sandy landscape, and the word <b>sleek</b> \u2014 related to <i>slenk</i>, a gully \u2014 points to exactly that: an elongated, shallow depression in which water stands. Such hollows are remnants of <b>meltwater channels</b> from the last ice age, when water from melting permafrost ice flowed across the frozen subsoil and scoured out shallow valleys. Because the soil there contains loam, rainwater does not drain away and the hollow stays wet \u2014 in a landscape that is otherwise bone-dry sand. That contrast makes these places <b>ecological islands</b>: sedges, purple moor-grass and cottongrass grow here, and amphibians use the pools to spawn. In the breeding season <b>snipe</b> are present, and in winter <b>snipe and woodcock</b> forage in the soft ground.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (amphibians and snipe), May\u2013Jul (sedges and cottongrass)<br>\n    <b>Best time of day:</b> Early morning or dusk \u2014 snipe are then active.',
 'why': ['<b>Sleek</b> = shallow ice-age meltwater channel.',
         'Loamy soil retains water in a <b>bone-dry sandy landscape</b>.',
         'Functions as an <b>ecological island</b> for wetland species.',
         'Spawning site for amphibians, feeding ground for <b>snipe</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Amphibians</b> spawn in the hollow.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Snipe</b> drumming above the wet parts.',
          '<span class="months">May\u2013Jul</span> \U0001f33f <b>Cottongrass</b> with white tufts.',
          '<span class="months">Oct\u2013Feb</span> \U0001f426 <b>Woodcock</b> forages in the soft ground.'],
 'wild': ['\U0001f426 Snipe \u00b7 Woodcock', '\U0001f438 Common frog \u00b7 Smooth newt', '\U0001f33f Sedges \u00b7 Purple moor-grass \u00b7 Cottongrass', '\U0001f9a0 Dragonflies', '\U0001f98c Roe deer'],
 'trail': ['Park at <b>Wijster</b>; paths along the hollow.',
           'Small area \u2014 combine with <b>Drijber</b> and <b>Kremboong</b>.',
           'Keep to the <b>edges</b>: the hollow itself is fragile and wet.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Wet all year \u00b7 \u26a0\ufe0f Fragile vegetation'
}, card_class='card water'))

C.append(mk.card(1329, 'Makkum-Holthe', {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Esdorpen \u00b7 essen, houtwallen en beekdal', 'list 36 \u00b7 no. 48'],
 'loc': '\U0001f4cd De gehuchten Makkum en Holthe bij Beilen \u00b7 Esdorplandschap \u00b7 Middelgroot',
 'desc': 'De naburige gehuchten <b>Makkum</b> en <b>Holthe</b> bij Beilen delen \u00e9\u00e9n landschap, en de naam Holthe verraadt de oorspronkelijke begroeiing: <b>holt</b> is het oude woord voor hout of bos. Dat wijst erop dat hier ooit \u2014 v\u00f3\u00f3r de grootschalige ontbossing van de middeleeuwen \u2014 nog echt bos stond, terwijl het grootste deel van Drenthe toen al heide was. Wat er nu ligt is een fijnmazig <b>esdorplandschap</b> met bouwland op de hoogtes, houtwallen als perceelscheiding en madelanden langs de <b>Beilerstroom</b>. De houtwallen zijn hier opvallend dicht en oud, met eikenstoven die generaties zijn afgezet. Dat levert een netwerk op waarin <b>das, ree en vleermuizen</b> zich door het hele gebied kunnen bewegen, en waar <b>geelgors, gekraagde roodstaart en grote lijster</b> broeden.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (zang en bloei), okt\u2013nov (herfstkleur van de wallen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend voor zang, avondschemer voor das en vleermuizen.',
 'why': ['<b>Holt</b> = hout: hier stond ooit echt bos, uitzonderlijk in Drenthe.',
         'Fijnmazig <b>esdorplandschap</b> met es, wal en madeland.',
         'Oude <b>eikenstoven</b> die generaties zijn afgezet.',
         'Netwerk waarin <b>das en vleermuizen</b> zich vrij bewegen.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f338 <b>Sleedoorn en meidoorn</b> bloeien wit.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Gekraagde roodstaart</b> in de oude eiken.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> langs de houtwallen bij schemer.',
          '<span class="months">Okt\u2013Nov</span> \U0001f341 <b>Herfstkleur</b> maakt het wallennetwerk zichtbaar.'],
 'wild': ['\U0001f426 Geelgors \u00b7 Gekraagde roodstaart \u00b7 Grote lijster', '\U0001f9a1 Das \u00b7 Steenmarter', '\U0001f987 Gewone dwergvleermuis \u00b7 Rosse vleermuis', '\U0001f333 Eikenstoven \u00b7 Meidoorn \u00b7 Sleedoorn', '\U0001f98c Ree'],
 'trail': ['Parkeren in <b>Beilen</b> of bij <b>Holthe</b>; zandwegen tussen de gehuchten.',
           'Loop van gehucht naar gehucht \u2014 de <b>kerkepaden</b> zijn nog intact.',
           'Combineer met het <b>Bos aan de Beilerstraat</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Deels particulier land \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Drenthe \u00b7 Midden-Drenthe', 'Es villages \u00b7 open fields, hedgebanks and brook valley', 'list 36 \u00b7 no. 48'],
 'loc': '\U0001f4cd The hamlets of Makkum and Holthe near Beilen \u00b7 Es-village landscape \u00b7 Medium-sized',
 'desc': 'The neighbouring hamlets of <b>Makkum</b> and <b>Holthe</b> near Beilen share one landscape, and the name Holthe betrays the original vegetation: <b>holt</b> is the old word for wood or timber. That indicates real woodland once stood here \u2014 before the large-scale medieval clearances \u2014 while most of Drenthe was already heath by then. What lies here now is a fine-grained <b>es-village landscape</b> with arable on the rises, hedgebanks as field boundaries and hay meadows along the <b>Beilerstroom</b>. The hedgebanks here are notably dense and old, with oak stools coppiced over generations. That produces a network in which <b>badger, roe deer and bats</b> can move through the whole area, and where <b>yellowhammer, redstart and mistle thrush</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (song and blossom), Oct\u2013Nov (autumn colour of the banks)<br>\n    <b>Best time of day:</b> Early morning for song, dusk for badger and bats.',
 'why': ['<b>Holt</b> = timber: real woodland once stood here, exceptional in Drenthe.',
         'Fine-grained <b>es-village landscape</b> with es, bank and hay meadow.',
         'Old <b>oak stools</b> coppiced over generations.',
         'Network in which <b>badger and bats</b> move freely.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f338 <b>Blackthorn and hawthorn</b> flower white.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Redstart</b> in the old oaks.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> along the hedgebanks at dusk.',
          '<span class="months">Oct\u2013Nov</span> \U0001f341 <b>Autumn colour</b> reveals the network of banks.'],
 'wild': ['\U0001f426 Yellowhammer \u00b7 Redstart \u00b7 Mistle thrush', '\U0001f9a1 Badger \u00b7 Stone marten', '\U0001f987 Common pipistrelle \u00b7 Noctule', '\U0001f333 Oak stools \u00b7 Hawthorn \u00b7 Blackthorn', '\U0001f98c Roe deer'],
 'trail': ['Park in <b>Beilen</b> or at <b>Holthe</b>; sandy tracks between the hamlets.',
           'Walk hamlet to hamlet \u2014 the old <b>church paths</b> are still intact.',
           'Combine with the <b>wood on the Beilerstraat</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Partly private land \u00b7 \U0001f6b4 Cycle route'
}))

mk.insert(C, '1324')
mk.progress(1329)
mk.check()
