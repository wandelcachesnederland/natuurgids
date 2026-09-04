# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1380, 'Erm', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Esdorp \u00b7 es, brink en beekdal', 'list 36 \u00b7 no. 99'],
 'loc': '\U0001f4cd Tussen Sleen en Dalen \u00b7 Esdorp met es en beekdal \u00b7 Middelgroot',
 'desc': '<b>Erm</b> is een klein esdorp op de rand van het Sleenerstroomdal, en de naam wordt in verband gebracht met <i>erm</i> of <i>arm</i> in de betekenis van een <b>zijtak of uitloper</b> \u2014 hier de arm van het beekdal die het dorp bereikt. Het dorpje toont het klassieke Drentse driedelige model in miniatuur: de <b>es</b> op de hoge zandkop, de <b>madelanden</b> in het beekdal en de heide op de arme grond daarachter. Rond de brink staan eiken, en de esrand is een <b>steilrandje</b>: eeuwen plaggenbemesting hebben het akkerdek zo opgehoogd dat het nu meer dan een meter boven het maaiveld ligt. Vanaf die rand kijk je het dal in. Er broeden <b>steenuil, boerenzwaluw en geelgors</b>, en in het dal <b>watersnip en wulp</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (dorpsvogels en beekdal), okt\u2013nov (esreli\u00ebf zichtbaar)<br>\n    <b>Beste tijd van de dag:</b> Avond \u2014 steenuilen roepen dan vanaf de erven.',
 'why': ['<b>Erm</b> \u2014 mogelijk \u2018arm\u2019, een zijtak of uitloper van het beekdal.',
         'Klassiek Drents drieluik in miniatuur: <b>es, maden, heide</b>.',
         'De <b>esrand</b> ligt door plaggenbemesting meer dan een meter hoog.',
         '<b>Steenuil</b> op de erven, <b>watersnip en wulp</b> in het dal.'],
 'phen': ['<span class="months">Mrt\u2013Mei</span> \U0001f989 <b>Steenuil</b> roept vanaf de erven.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boerenzwaluw</b> boven de es.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33e <b>Akkerkruiden</b> op de esrand.',
          '<span class="months">Okt\u2013Nov</span> \U0001f7eb <b>Esreli\u00ebf</b> goed zichtbaar na de oogst.'],
 'wild': ['\U0001f989 Steenuil \u00b7 Kerkuil', '\U0001f426 Boerenzwaluw \u00b7 Geelgors \u00b7 Ringmus', '\U0001f426 Watersnip \u00b7 Wulp in het dal', '\U0001f333 Brinkeiken \u00b7 Houtwallen', '\U0001f98c Haas \u00b7 Ree'],
 'trail': ['Parkeren bij de <b>brink van Erm</b>; paden naar es en beekdal.',
           'Loop de <b>esrand</b> af om het steilrandje te zien.',
           'Kom in de <b>avond</b> voor de steenuil.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Esdorp \u00b7 \u26a0\ufe0f Respecteer erven en akkers'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Es village \u00b7 open field, green and brook valley', 'list 36 \u00b7 no. 99'],
 'loc': '\U0001f4cd Between Sleen and Dalen \u00b7 Es village with field and brook valley \u00b7 Medium-sized',
 'desc': '<b>Erm</b> is a small es village on the edge of the Sleenerstroom valley, and the name is linked to <i>erm</i> or <i>arm</i> in the sense of a <b>side branch or spur</b> \u2014 here the arm of the brook valley reaching the village. The little place shows the classic Drenthe threefold model in miniature: the <b>es</b> on the high sandy knoll, the <b>hay meadows</b> in the brook valley and the heath on the poor ground beyond. Oaks stand around the green, and the edge of the es is a <b>small scarp</b>: centuries of sod manuring have raised the arable layer so much that it now lies more than a metre above the surrounding land. From that edge you look out over the valley. <b>Little owl, barn swallow and yellowhammer</b> breed here, and <b>snipe and curlew</b> in the valley.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (village birds and brook valley), Oct\u2013Nov (es relief visible)<br>\n    <b>Best time of day:</b> Evening \u2014 little owls then call from the farmyards.',
 'why': ['<b>Erm</b> \u2014 possibly \u2018arm\u2019, a side branch or spur of the brook valley.',
         'Classic Drenthe triptych in miniature: <b>es, meadows, heath</b>.',
         'The <b>es edge</b> stands more than a metre high from sod manuring.',
         '<b>Little owl</b> in the yards, <b>snipe and curlew</b> in the valley.'],
 'phen': ['<span class="months">Mar\u2013May</span> \U0001f989 <b>Little owl</b> calls from the farmyards.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Barn swallow</b> above the es.',
          '<span class="months">May\u2013Jul</span> \U0001f33e <b>Arable flowers</b> on the es edge.',
          '<span class="months">Oct\u2013Nov</span> \U0001f7eb <b>Es relief</b> clearly visible after harvest.'],
 'wild': ['\U0001f989 Little owl \u00b7 Barn owl', '\U0001f426 Barn swallow \u00b7 Yellowhammer \u00b7 Tree sparrow', '\U0001f426 Snipe \u00b7 Curlew in the valley', '\U0001f333 Village-green oaks \u00b7 Hedgebanks', '\U0001f98c Brown hare \u00b7 Roe deer'],
 'trail': ['Park at the <b>green in Erm</b>; paths to the es and brook valley.',
           'Walk the <b>es edge</b> to see the small scarp.',
           'Come in the <b>evening</b> for the little owl.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Es village \u00b7 \u26a0\ufe0f Respect yards and fields'
}))

C.append(mk.card(1381, 'Ermerveen', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Veenontginning \u00b7 natte graslanden en petgaten', 'list 36 \u00b7 no. 100'],
 'loc': '\U0001f4cd Ten oosten van Erm \u00b7 Veenontginning \u00b7 Middelgroot',
 'desc': 'Het <b>Ermerveen</b> was het veengebied dat bij het dorp Erm hoorde: elk esdorp had zijn eigen veen, waar de boeren turf voor eigen gebruik staken. Deze <b>boerenvervening</b> was iets heel anders dan de grootschalige industri\u00eble afgraving verderop in de Veenkoloni\u00ebn. Ze ging langzaam, perceel voor perceel, en liet een grillig patroon achter van kleine natte laagten, greppels en overgebleven veenkopjes \u2014 juist die onregelmatigheid maakt oude boerenveenontginningen ecologisch rijker dan de kaarsrechte industri\u00eble variant. Nu is het een gebied van <b>natte graslanden en petgaten</b> met veenmos in de natste hoeken. Er broeden <b>watersnip, kievit en gele kwikstaart</b>, en er groeien <b>veenpluis en zonnedauw</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels), mei\u2013jul (veenpluis en zonnedauw)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 mist boven de laagten en baltsende watersnippen.',
 'why': ['Het <b>eigen veen</b> van esdorp Erm \u2014 boerenvervening, geen industrie.',
         'Perceel voor perceel gestoken \u2014 daardoor een <b>grillig patroon</b>.',
         'Die onregelmatigheid maakt het <b>ecologisch rijker</b> dan de rechte variant.',
         '<b>Veenmos, veenpluis en zonnedauw</b> in de natste hoeken.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Watersnip</b> baltst boven de laagten.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kievit en gele kwikstaart</b> broeden.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33f <b>Veenpluis</b> pluist wit uit.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Zonnedauw</b> vangt insecten.'],
 'wild': ['\U0001f426 Watersnip \u00b7 Kievit \u00b7 Gele kwikstaart', '\U0001f33f Veenmos \u00b7 Veenpluis \u00b7 Ronde zonnedauw', '\U0001f9a0 Libellen boven de petgaten', '\U0001f438 Heikikker \u00b7 Kleine watersalamander', '\U0001f98c Ree \u00b7 Haas'],
 'trail': ['Parkeren bij <b>Erm</b>; landwegen door het veengebied.',
           'Let op het <b>grillige perceelspatroon</b> \u2014 spoor van boerenvervening.',
           'Betreed de <b>petgaten</b> niet; blijf op de paden.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Nat \u00b7 \u26a0\ufe0f Broedgebied maart\u2013juni'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Peat reclamation \u00b7 wet grasslands and turf pits', 'list 36 \u00b7 no. 100'],
 'loc': '\U0001f4cd East of Erm \u00b7 Peat reclamation \u00b7 Medium-sized',
 'desc': 'The <b>Ermerveen</b> was the bog belonging to the village of Erm: every es village had its own peatland where the farmers cut turf for their own use. This <b>farmers\u2019 peat cutting</b> was something quite different from the large-scale industrial extraction further out in the Peat Colonies. It went slowly, parcel by parcel, and left behind an irregular pattern of small wet hollows, ditches and surviving peat knolls \u2014 and it is precisely that irregularity that makes old farmers\u2019 peat workings ecologically richer than the ruler-straight industrial version. It is now an area of <b>wet grasslands and turf pits</b> with sphagnum in the wettest corners. <b>Snipe, lapwing and yellow wagtail</b> breed here, and <b>cottongrass and sundew</b> grow.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds), May\u2013Jul (cottongrass and sundew)<br>\n    <b>Best time of day:</b> Early morning \u2014 mist over the hollows and drumming snipe.',
 'why': ['The <b>own bog</b> of the es village of Erm \u2014 farmers\u2019 cutting, not industry.',
         'Cut parcel by parcel \u2014 hence an <b>irregular pattern</b>.',
         'That irregularity makes it <b>ecologically richer</b> than the straight version.',
         '<b>Sphagnum, cottongrass and sundew</b> in the wettest corners.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Snipe</b> drumming above the hollows.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Lapwing and yellow wagtail</b> breed.',
          '<span class="months">May\u2013Jun</span> \U0001f33f <b>Cottongrass</b> turns white.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Sundew</b> catches insects.'],
 'wild': ['\U0001f426 Snipe \u00b7 Lapwing \u00b7 Yellow wagtail', '\U0001f33f Sphagnum \u00b7 Cottongrass \u00b7 Round-leaved sundew', '\U0001f9a0 Dragonflies above the turf pits', '\U0001f438 Moor frog \u00b7 Smooth newt', '\U0001f98c Roe deer \u00b7 Brown hare'],
 'trail': ['Park at <b>Erm</b>; country lanes cross the peat area.',
           'Note the <b>irregular parcel pattern</b> \u2014 trace of farmers\u2019 cutting.',
           'Do not enter the <b>turf pits</b>; keep to the paths.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Wet \u00b7 \u26a0\ufe0f Breeding ground March\u2013June'
}, card_class='card water'))

C.append(mk.card(1382, 'Dalen', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Esdorp \u00b7 brink, es en houtwallen', 'list 36 \u00b7 no. 101'],
 'loc': '\U0001f4cd Ten noordoosten van Coevorden \u00b7 Esdorp met es en houtwallen \u00b7 Groot',
 'desc': '<b>Dalen</b> is een van de grotere en gaafste esdorpen van Zuidoost-Drenthe, en de naam betekent eenvoudigweg \u2018de dalen\u2019: het dorp ligt tussen de laagten van de Sleenerstroom en het Drostendiep. Wat Dalen bijzonder maakt, is dat de <b>brink met eeuwenoude eiken</b> en de omringende <b>esakkers</b> nog grotendeels in hun oorspronkelijke verhouding aanwezig zijn \u2014 in veel Drentse dorpen zijn brinken volgebouwd of tot parkeerplaats gedegradeerd. Rond de es liggen nog <b>houtwallen</b>, de levende hekwerken die het vee buiten de akkers hielden. Die wallen zijn nu de belangrijkste ecologische structuur: ze verbinden bosjes, bieden nestgelegenheid en zijn vliegroute voor vleermuizen. Er broeden <b>steenuil, geelgors en grauwe vliegenvanger</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang in de houtwallen), sep\u2013okt (bessen en trek)<br>\n    <b>Beste tijd van de dag:</b> Schemer \u2014 steenuilen en vleermuizen langs de wallen.',
 'why': ['<b>Dalen</b> = de laagten tussen Sleenerstroom en Drostendiep.',
         'Brink met <b>eeuwenoude eiken</b> nog in oorspronkelijke verhouding.',
         '<b>Houtwallen</b> als levende hekwerken rond de es.',
         'Wallen als <b>verbinding en vliegroute</b> voor vleermuizen.'],
 'phen': ['<span class="months">Mrt\u2013Mei</span> \U0001f989 <b>Steenuil</b> roept vanaf de erven.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Geelgors</b> zingt vanaf de houtwallen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f987 <b>Vleermuizen</b> volgen de wallen in de schemer.',
          '<span class="months">Sep\u2013Okt</span> \U0001fad0 <b>Bessen</b> in de wallen trekken lijsters.'],
 'wild': ['\U0001f989 Steenuil \u00b7 Kerkuil', '\U0001f426 Geelgors \u00b7 Grauwe vliegenvanger \u00b7 Ringmus', '\U0001f987 Gewone dwergvleermuis \u00b7 Laatvlieger', '\U0001f333 Brinkeiken \u00b7 Meidoorn \u00b7 Hazelaar', '\U0001f98c Ree \u00b7 Haas \u00b7 Egel'],
 'trail': ['Parkeren aan de <b>brink van Dalen</b>; wandelpaden langs de es.',
           'Volg de <b>houtwallen</b> \u2014 de mooiste route loopt eromheen.',
           'Kom in de <b>schemer</b> voor uilen en vleermuizen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Beschermd dorpsgezicht \u00b7 \U0001f6b4 Fietsroutes'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Es village \u00b7 green, open field and hedgebanks', 'list 36 \u00b7 no. 101'],
 'loc': '\U0001f4cd North-east of Coevorden \u00b7 Es village with field and hedgebanks \u00b7 Large',
 'desc': '<b>Dalen</b> is one of the larger and best-preserved es villages of south-east Drenthe, and the name simply means \u2018the valleys\u2019: the village lies between the hollows of the Sleenerstroom and the Drostendiep. What makes Dalen special is that the <b>green with centuries-old oaks</b> and the surrounding <b>es fields</b> are still largely present in their original proportions \u2014 in many Drenthe villages the greens have been built over or demoted to car parks. Around the es there are still <b>hedgebanks</b>, the living fences that kept livestock out of the fields. Those banks are now the key ecological structure: they connect copses, provide nest sites and serve as flight routes for bats. <b>Little owl, yellowhammer and spotted flycatcher</b> breed here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song in the hedgebanks), Sep\u2013Oct (berries and migration)<br>\n    <b>Best time of day:</b> Dusk \u2014 little owls and bats along the banks.',
 'why': ['<b>Dalen</b> = the hollows between Sleenerstroom and Drostendiep.',
         'Green with <b>centuries-old oaks</b> still in original proportion.',
         '<b>Hedgebanks</b> as living fences around the es.',
         'Banks as <b>connection and flight route</b> for bats.'],
 'phen': ['<span class="months">Mar\u2013May</span> \U0001f989 <b>Little owl</b> calls from the farmyards.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Yellowhammer</b> sings from the hedgebanks.',
          '<span class="months">May\u2013Jul</span> \U0001f987 <b>Bats</b> follow the banks at dusk.',
          '<span class="months">Sep\u2013Oct</span> \U0001fad0 <b>Berries</b> in the banks draw thrushes.'],
 'wild': ['\U0001f989 Little owl \u00b7 Barn owl', '\U0001f426 Yellowhammer \u00b7 Spotted flycatcher \u00b7 Tree sparrow', '\U0001f987 Common pipistrelle \u00b7 Serotine', '\U0001f333 Village-green oaks \u00b7 Hawthorn \u00b7 Hazel', '\U0001f98c Roe deer \u00b7 Brown hare \u00b7 Hedgehog'],
 'trail': ['Park at the <b>green in Dalen</b>; footpaths along the es.',
           'Follow the <b>hedgebanks</b> \u2014 the finest route runs around them.',
           'Come at <b>dusk</b> for owls and bats.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Protected village scene \u00b7 \U0001f6b4 Cycle routes'
}))

C.append(mk.card(1383, 'Rigterinkbos', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Landgoedbos \u00b7 oud loofbos met lanen', 'list 36 \u00b7 no. 102'],
 'loc': '\U0001f4cd Bij Dalen \u00b7 Oud loofbos \u00b7 Klein',
 'desc': 'Het <b>Rigterinkbos</b> bij Dalen draagt een echte Drentse familienaam: <b>Rigterink</b> is een <i>-ink</i>-naam, het achtervoegsel dat in Oost-Nederland en Westfalen \u2018behorend bij\u2019 of \u2018nakomelingen van\u2019 betekent. De stam <i>rigter</i> verwijst naar de <b>richter</b>, de plaatselijke rechter of schulte \u2014 een bestuurder met aanzien. Het bos hoorde dus bij het erf van de richtersfamilie, en dat verklaart het karakter: geen productiebos maar een <b>statusbos</b>, met lanen, oude eiken en beuken die om hun aanzien en niet om hun houtopbrengst werden geplant. Zulke oude erfbossen zijn ecologisch waardevol door hun <b>continu\u00efteit</b>: eeuwenlang bos op dezelfde plek betekent een rijke bodemflora en veel <b>holtebroeders</b>, met <b>boomklever, bosuil en grote bonte specht</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (bosanemonen en zang), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 licht tussen de laanbomen.',
 'why': ['<b>-ink</b> = \u2018behorend bij\u2019; <b>rigter</b> = de plaatselijke rechter.',
         'Geen productiebos maar een <b>statusbos</b> bij het erf.',
         'Lanen met eiken en beuken, geplant om <b>aanzien</b>.',
         '<b>Continu\u00efteit</b> van eeuwenlang bos \u2014 rijke bodemflora.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Bosanemoon</b> bedekt de bodem.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever</b> in de oude laanbomen.',
          '<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Bosuil</b> roept in de schemer.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op oude stobben.'],
 'wild': ['\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Glanskop', '\U0001f989 Bosuil', '\U0001f33c Bosanemoon \u00b7 Salomonszegel \u00b7 Dalkruid', '\U0001f344 Zwavelkop \u00b7 Elfenbankje', '\U0001f333 Oude eik \u00b7 Beuk \u00b7 Linde'],
 'trail': ['Parkeren bij <b>Dalen</b>; paden door het bos en langs de lanen.',
           'Let op de <b>rechte lanen</b> \u2014 typisch voor een erfbos.',
           'April is de maand van de <b>bosanemonen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historisch erfbos \u00b7 \U0001f6b6 Kort rondje'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Estate wood \u00b7 old broadleaf wood with avenues', 'list 36 \u00b7 no. 102'],
 'loc': '\U0001f4cd Near Dalen \u00b7 Old broadleaf wood \u00b7 Small',
 'desc': 'The <b>Rigterinkbos</b> near Dalen bears a genuine Drenthe family name: <b>Rigterink</b> is an <i>-ink</i> name, the suffix that in eastern Netherlands and Westphalia means \u2018belonging to\u2019 or \u2018descendants of\u2019. The stem <i>rigter</i> refers to the <b>richter</b>, the local judge or schout \u2014 an official of standing. The wood therefore belonged to the farmstead of the judge\u2019s family, and that explains its character: not a production wood but a <b>status wood</b>, with avenues, old oaks and beeches planted for prestige rather than timber yield. Such old farmstead woods are ecologically valuable through their <b>continuity</b>: centuries of woodland on the same spot means a rich ground flora and many <b>hole-nesters</b>, with <b>nuthatch, tawny owl and great spotted woodpecker</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (wood anemones and song), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Morning \u2014 light between the avenue trees.',
 'why': ['<b>-ink</b> = \u2018belonging to\u2019; <b>rigter</b> = the local judge.',
         'Not a production wood but a <b>status wood</b> beside the farmstead.',
         'Avenues of oak and beech planted for <b>prestige</b>.',
         '<b>Continuity</b> of centuries of woodland \u2014 rich ground flora.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Wood anemone</b> carpets the floor.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch</b> in the old avenue trees.',
          '<span class="months">Feb\u2013Apr</span> \U0001f989 <b>Tawny owl</b> calls at dusk.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on old stumps.'],
 'wild': ['\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Marsh tit', '\U0001f989 Tawny owl', '\U0001f33c Wood anemone \u00b7 Solomon\u2019s seal \u00b7 May lily', '\U0001f344 Sulphur tuft \u00b7 Turkeytail', '\U0001f333 Old oak \u00b7 Beech \u00b7 Lime'],
 'trail': ['Park at <b>Dalen</b>; paths through the wood and along the avenues.',
           'Note the <b>straight avenues</b> \u2014 typical of a farmstead wood.',
           'April is the month of the <b>wood anemones</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic farmstead wood \u00b7 \U0001f6b6 Short circuit'
}))

C.append(mk.card(1384, 'Dalerveen', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Veenontginning \u00b7 lintdorp en natte laagten', 'list 36 \u00b7 no. 103'],
 'loc': '\U0001f4cd Ten zuidwesten van Dalen \u00b7 Veenontginning \u00b7 Middelgroot',
 'desc': 'Het <b>Dalerveen</b> was het veen van het dorp Dalen, en het lintdorp dat er nu ligt bewaart nog het ritme van de ontginning: langgerekte percelen loodrecht op de weg, elk ooit toegewezen aan \u00e9\u00e9n boer die van voren naar achteren zijn eigen strook afveende. Dat verklaart de karakteristieke <b>opstrekkende verkaveling</b> die je vanaf de weg ziet: sloot, akker, sloot, akker, kilometers achtereen. In de laagste delen bleef het te nat om te ontginnen, en juist daar zit de natuur: <b>natte graslanden, rietkragen en poelen</b>. Er broeden <b>grutto, kievit en tureluur</b>, in de rietkragen <b>rietgors en kleine karekiet</b>. In de winter foerageren <b>ganzen en zwanen</b> op de natte percelen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013jun</b> (weidevogels), nov\u2013feb (ganzen en zwanen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 weidevogelbaltz boven de laagten.',
 'why': ['Het <b>veen van Dalen</b>, ontgonnen strook voor strook.',
         'Karakteristieke <b>opstrekkende verkaveling</b> vanaf de weg zichtbaar.',
         'De laagste delen bleven te nat \u2014 daar zit nu de <b>natuur</b>.',
         '<b>Grutto, kievit en tureluur</b>; \u2019s winters ganzen en zwanen.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Grutto</b> keert terug op de natte percelen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kievit en tureluur</b> broeden.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33e <b>Rietgors</b> zingt in de kragen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Ganzen en wilde zwanen</b> foerageren.'],
 'wild': ['\U0001f426 Grutto \u00b7 Kievit \u00b7 Tureluur', '\U0001f33e Rietgors \u00b7 Kleine karekiet', '\U0001f9a2 Kolgans \u00b7 Toendrarietgans \u00b7 Wilde zwaan', '\U0001f985 Blauwe kiekendief \u00b7 Buizerd', '\U0001f438 Kikkers in de poelen'],
 'trail': ['Parkeren in <b>Dalerveen</b>; kijk vanaf de lintweg de percelen in.',
           'Let op de <b>opstrekkende stroken</b> \u2014 sloot, akker, sloot, akker.',
           'Kom in <b>maart</b> voor de terugkerende grutto\u2019s.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Weidevogelgebied \u2014 blijf op de weg \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Peat reclamation \u00b7 ribbon village and wet hollows', 'list 36 \u00b7 no. 103'],
 'loc': '\U0001f4cd South-west of Dalen \u00b7 Peat reclamation \u00b7 Medium-sized',
 'desc': 'The <b>Dalerveen</b> was the peatland of the village of Dalen, and the ribbon village that lies there now still keeps the rhythm of the reclamation: elongated parcels at right angles to the road, each once allotted to one farmer who cut his own strip from front to back. That explains the characteristic <b>strip parcelling</b> you see from the road: ditch, field, ditch, field, for kilometres on end. In the lowest parts it stayed too wet to reclaim, and that is exactly where the nature is: <b>wet grasslands, reed fringes and pools</b>. <b>Black-tailed godwit, lapwing and redshank</b> breed here, and <b>reed bunting and reed warbler</b> in the reed. In winter <b>geese and swans</b> forage on the wet parcels.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Jun</b> (meadow birds), Nov\u2013Feb (geese and swans)<br>\n    <b>Best time of day:</b> Early morning \u2014 meadow-bird display above the hollows.',
 'why': ['The <b>peatland of Dalen</b>, reclaimed strip by strip.',
         'Characteristic <b>strip parcelling</b> visible from the road.',
         'The lowest parts stayed too wet \u2014 that is where the <b>nature</b> is.',
         '<b>Godwit, lapwing and redshank</b>; geese and swans in winter.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Black-tailed godwit</b> returns to the wet parcels.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Lapwing and redshank</b> breed.',
          '<span class="months">May\u2013Jul</span> \U0001f33e <b>Reed bunting</b> sings in the fringes.',
          '<span class="months">Nov\u2013Feb</span> \U0001f9a2 <b>Geese and whooper swans</b> forage.'],
 'wild': ['\U0001f426 Black-tailed godwit \u00b7 Lapwing \u00b7 Redshank', '\U0001f33e Reed bunting \u00b7 Reed warbler', '\U0001f9a2 White-fronted goose \u00b7 Tundra bean goose \u00b7 Whooper swan', '\U0001f985 Hen harrier \u00b7 Buzzard', '\U0001f438 Frogs in the pools'],
 'trail': ['Park in <b>Dalerveen</b>; look into the parcels from the ribbon road.',
           'Note the <b>strips</b> \u2014 ditch, field, ditch, field.',
           'Come in <b>March</b> for the returning godwits.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Meadow-bird area \u2014 keep to the road \u00b7 \U0001f6b4 Cycle route'
}, card_class='card water'))

mk.insert(C, '1379')
mk.progress(1384)
mk.check()
