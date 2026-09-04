# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1370, 'Roswinkel', {
 'tags': ['Drenthe \u00b7 Emmen', 'Veenkolonie \u00b7 lintdorp, wijken en bermen', 'list 36 \u00b7 no. 89'],
 'loc': '\U0001f4cd Het dorp Roswinkel bij Emmen \u00b7 Veenkolonie \u00b7 Middelgroot',
 'desc': '<b>Roswinkel</b> ligt in de uiterste oosthoek van Drenthe, tegen de Duitse grens, en het dorp heeft een geschiedenis die je aan het landschap niet afziet: het was eeuwenlang een <b>enclave</b>, een stukje Drents grondgebied dat door veen en moeras van de rest van de provincie was afgesneden en alleen via Duits gebied bereikbaar was. Pas met de vervening en de aanleg van kanalen kwam er verbinding. De <b>winkel</b> in de naam heeft niets met handel te maken maar betekent <b>hoek</b> of uitspringend stuk land \u2014 een oud woord dat nog voortleeft in \u2018winkelhaak\u2019. Het landschap is nu veenkoloniaal: lintbebouwing, wijken en rechte percelen. De <b>bermen en oevers</b> vormen de ecologische ruggengraat, met <b>gele kwikstaart, kneu en veldleeuwerik</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (akkervogels en bermbloei), sep\u2013okt (doortrek langs de linten)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 veldleeuweriken zingen dan boven de akkers.',
 'why': ['Was eeuwenlang een <b>enclave</b>, alleen via Duitsland bereikbaar.',
         '<b>Winkel</b> = hoek of uitspringend land, zoals in \u2018winkelhaak\u2019.',
         'Veenkoloniale structuur met lint, wijken en rechte percelen.',
         'Bermen en oevers als <b>ecologische ruggengraat</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Veldleeuwerik</b> zingt boven de akkers.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Gele kwikstaart</b> in de gewassen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Bermbloei</b> langs de wijken.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Doortrekkers</b> volgen de beplantingslinten.'],
 'wild': ['\U0001f426 Veldleeuwerik \u00b7 Gele kwikstaart \u00b7 Kneu', '\U0001f985 Torenvalk \u00b7 Buizerd \u00b7 Blauwe kiekendief (winter)', '\U0001f33c Bermkruiden \u00b7 Akkerkruiden', '\U0001f98c Haas \u00b7 Ree', '\U0001f987 Vleermuizen langs de linten'],
 'trail': ['Parkeren in <b>Roswinkel</b>; fiets de linten en wijken af.',
           'Bedenk bij het kijken dat dit ooit <b>alleen via Duitsland</b> bereikbaar was.',
           'De <b>bermen</b> zijn in juli het interessantst.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b4 Fietsroute \u00b7 \U0001f3db\ufe0f Voormalige enclave'
}, {
 'tags': ['Drenthe \u00b7 Emmen', 'Peat colony \u00b7 ribbon village, canals and verges', 'list 36 \u00b7 no. 89'],
 'loc': '\U0001f4cd The village of Roswinkel near Emmen \u00b7 Peat colony \u00b7 Medium-sized',
 'desc': '<b>Roswinkel</b> lies in the far eastern corner of Drenthe against the German border, and the village has a history you would not guess from the landscape: for centuries it was an <b>enclave</b>, a piece of Drenthe territory cut off from the rest of the province by bog and marsh and reachable only through German territory. Only with the peat extraction and the digging of canals did a connection appear. The <b>winkel</b> in the name has nothing to do with shops but means <b>corner</b> or projecting piece of land \u2014 an old word that survives in <i>winkelhaak</i>, a set square. The landscape is now peat-colonial: ribbon development, side canals and straight plots. The <b>verges and banks</b> form the ecological backbone, with <b>yellow wagtail, linnet and skylark</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (farmland birds and verge flowering), Sep\u2013Oct (passage along the ribbons)<br>\n    <b>Best time of day:</b> Early morning \u2014 skylarks then sing above the fields.',
 'why': ['Was for centuries an <b>enclave</b>, reachable only through Germany.',
         '<b>Winkel</b> = corner or projecting land, as in <i>winkelhaak</i>.',
         'Peat-colony structure with ribbon, canals and straight plots.',
         'Verges and banks as the <b>ecological backbone</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Skylark</b> sings above the fields.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellow wagtail</b> in the crops.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Verge flowering</b> along the canals.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Migrants</b> follow the planted ribbons.'],
 'wild': ['\U0001f426 Skylark \u00b7 Yellow wagtail \u00b7 Linnet', '\U0001f985 Kestrel \u00b7 Buzzard \u00b7 Hen harrier (winter)', '\U0001f33c Verge herbs \u00b7 Arable flowers', '\U0001f98c Brown hare \u00b7 Roe deer', '\U0001f987 Bats along the ribbons'],
 'trail': ['Park in <b>Roswinkel</b>; cycle the ribbons and canals.',
           'Bear in mind while looking that this was once <b>reachable only via Germany</b>.',
           'The <b>verges</b> are most interesting in July.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b4 Cycle route \u00b7 \U0001f3db\ufe0f Former enclave'
}))

C.append(mk.card(1371, 'Sleenerstroom', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Beekdal \u00b7 hermeanderde beek en natte graslanden', 'list 36 \u00b7 no. 90'],
 'loc': '\U0001f4cd Tussen Sleen, Erm en Dalen \u00b7 Beekdal \u00b7 Groot',
 'desc': 'De <b>Sleenerstroom</b> is een van de beken die het Drents plateau afwateren richting het Coevordense laagland, en het dal ervan is de laatste decennia grondig hersteld. Wat hier gebeurde staat model voor de hele Nederlandse beekherstelpraktijk: eerst werd de beek in de jaren zestig <b>genormaliseerd</b> \u2014 rechtgetrokken, verdiept en van stuwen voorzien om landbouwgrond sneller te ontwateren. Het gevolg was dat het water in de winter razendsnel wegstroomde en er in de zomer niets meer was, precies het omgekeerde van wat een gezond beeksysteem doet. Sinds 2000 is het teruggedraaid: de beek <b>meandert weer</b>, de oevers zijn verflauwd en de aangrenzende percelen vernat. Nu groeit er beekdalflora en broeden er <b>watersnip, wulp en blauwborst</b>; de <b>ijsvogel</b> nestelt in de steilrandjes.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels en beekflora), nov\u2013mrt (hoogwater en overstroming)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 mist boven het dal, en ijsvogels actief.',
 'why': ['Klassiek verhaal van <b>normalisatie en herstel</b> van een Drentse beek.',
         'Rechttrekken leverde <b>winterse piekafvoer</b> en zomerse droogte op.',
         'Sinds 2000 <b>meandert de beek weer</b> en zijn de oevers verflauwd.',
         'Terugkeer van <b>watersnip, wulp en ijsvogel</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Watersnip</b> baltst boven de natte percelen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> broedt in de steilrandjes.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Beekdalflora</b> met dotterbloem en orchidee\u00ebn.',
          '<span class="months">Nov\u2013Mrt</span> \U0001f4a7 <b>Hoogwater</b> \u2014 het dal loopt onder.'],
 'wild': ['\U0001f426 IJsvogel \u00b7 Watersnip \u00b7 Wulp \u00b7 Blauwborst', '\U0001f41f Bermpje \u00b7 Riviergrondel \u00b7 Kleine modderkruiper', '\U0001f33c Dotterbloem \u00b7 Brede orchis', '\U0001f9a0 Beekjuffers', '\U0001f9a6 Otter (sporadisch)'],
 'trail': ['Parkeren bij <b>Erm</b> of <b>Sleen</b>; paden langs de beek.',
           'Volg de beek <b>stroomafwaarts</b> om de meanders te zien.',
           'In de winter staan delen van het pad <b>onder water</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Nat in winter \u00b7 \u26a0\ufe0f Broedgebied \u2014 blijf op de paden'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Brook valley \u00b7 remeandered brook and wet grasslands', 'list 36 \u00b7 no. 90'],
 'loc': '\U0001f4cd Between Sleen, Erm and Dalen \u00b7 Brook valley \u00b7 Large',
 'desc': 'The <b>Sleenerstroom</b> is one of the brooks draining the Drenthe plateau towards the Coevorden lowland, and its valley has been thoroughly restored in recent decades. What happened here is a model for the whole of Dutch brook restoration: first, in the 1960s, the brook was <b>normalised</b> \u2014 straightened, deepened and fitted with weirs to drain farmland faster. The result was that in winter the water rushed away and in summer there was none left, precisely the reverse of what a healthy brook system does. Since 2000 it has been reversed: the brook <b>meanders again</b>, the banks have been gently graded and the adjoining parcels rewetted. Brook-valley flora now grows and <b>snipe, curlew and bluethroat</b> breed; the <b>kingfisher</b> nests in the small cliffs.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds and brook flora), Nov\u2013Mar (high water and flooding)<br>\n    <b>Best time of day:</b> Early morning \u2014 mist over the valley, and kingfishers active.',
 'why': ['Classic story of the <b>normalisation and restoration</b> of a Drenthe brook.',
         'Straightening produced <b>winter peak flows</b> and summer drought.',
         'Since 2000 the brook <b>meanders again</b> and the banks are graded.',
         'Return of <b>snipe, curlew and kingfisher</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Snipe</b> drumming above the wet parcels.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> breeds in the small cliffs.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Brook-valley flora</b> with marsh marigold and orchids.',
          '<span class="months">Nov\u2013Mar</span> \U0001f4a7 <b>High water</b> \u2014 the valley floods.'],
 'wild': ['\U0001f426 Kingfisher \u00b7 Snipe \u00b7 Curlew \u00b7 Bluethroat', '\U0001f41f Stone loach \u00b7 Gudgeon \u00b7 Spined loach', '\U0001f33c Marsh marigold \u00b7 Marsh orchid', '\U0001f9a0 Demoiselles', '\U0001f9a6 Otter (occasional)'],
 'trail': ['Park at <b>Erm</b> or <b>Sleen</b>; paths along the brook.',
           'Follow the brook <b>downstream</b> to see the meanders.',
           'In winter parts of the path are <b>under water</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Wet in winter \u00b7 \u26a0\ufe0f Breeding ground \u2014 keep to the paths'
}, card_class='card water'))

C.append(mk.card(1372, 'Boschmaden en De Blikken', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Madelanden \u00b7 nat hooiland en bosjes', 'list 36 \u00b7 no. 91'],
 'loc': '\U0001f4cd Langs de Sleenerstroom bij Erm \u00b7 Madelanden \u00b7 Klein',
 'desc': 'De <b>Boschmaden</b> en <b>De Blikken</b> zijn twee aangrenzende percelen oud hooiland langs de Sleenerstroom, en beide namen zijn landschapstermen. <b>Maden</b> kennen we inmiddels: hooilanden in het beekdal. <b>Blik</b> is minder bekend en betekent een <b>open plek</b> of een vrij uitzicht \u2014 verwant aan het werkwoord <i>blikken</i>, kijken. Samen beschrijven ze dus bebost hooiland naast een open plek, en die combinatie is precies wat het gebied ecologisch waardevol maakt: de bosjes leveren beschutting en broedgelegenheid, het open hooiland de bloemen en insecten. Op de natste plekken groeien <b>dotterbloem, waterviolier en gevlekte orchis</b>, en in de zomen langs de bosjes vliegen vlinders. Er broeden <b>watersnip, blauwborst en grasmus</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (hooilandflora en vlinders), apr\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Late ochtend \u2014 warm genoeg voor vlinders, en de zang is nog gaande.',
 'why': ['<b>Maden</b> = hooiland; <b>blik</b> = open plek of vrij uitzicht.',
         'Combinatie van <b>bosje en open hooiland</b> maakt het rijk.',
         'Bosjes leveren beschutting, hooiland de <b>bloemen en insecten</b>.',
         '<b>Dotterbloem, waterviolier en gevlekte orchis</b> op de natte delen.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dotterbloem</b> in de natste maden.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Gevlekte orchis</b> bloeit.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Vlinders</b> in de zomen langs de bosjes.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Blauwborst</b> zingt vanuit het struweel.'],
 'wild': ['\U0001f33c Dotterbloem \u00b7 Waterviolier \u00b7 Gevlekte orchis', '\U0001f426 Watersnip \u00b7 Blauwborst \u00b7 Grasmus', '\U0001f98b Zomervlinders \u00b7 Zilveren maan', '\U0001f9a0 Libellen langs de beek', '\U0001f333 Els \u00b7 Wilg \u00b7 Eik'],
 'trail': ['Parkeren bij <b>Erm</b>; paden langs de Sleenerstroom.',
           'Klein gebied \u2014 combineer met de <b>Sleenerstroom</b> zelf.',
           'Betreed het hooiland <b>niet</b> voor de maai.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbaar hooiland \u00b7 \U0001f97e Nat'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Hay meadows \u00b7 wet meadow and copses', 'list 36 \u00b7 no. 91'],
 'loc': '\U0001f4cd Along the Sleenerstroom near Erm \u00b7 Hay meadows \u00b7 Small',
 'desc': 'The <b>Boschmaden</b> and <b>De Blikken</b> are two adjoining parcels of old hay meadow along the Sleenerstroom, and both names are landscape terms. <b>Maden</b> we now know: hay meadows in the brook valley. <b>Blik</b> is less familiar and means an <b>open place</b> or a clear view \u2014 related to the verb <i>blikken</i>, to glance. Together they describe wooded hay meadow beside an open spot, and that combination is exactly what makes the area ecologically valuable: the copses provide shelter and nesting places, the open meadow the flowers and insects. On the wettest spots grow <b>marsh marigold, water violet and heath spotted orchid</b>, and butterflies fly in the fringes along the copses. <b>Snipe, bluethroat and whitethroat</b> breed here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (meadow flora and butterflies), Apr\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Late morning \u2014 warm enough for butterflies, with song still going.',
 'why': ['<b>Maden</b> = hay meadow; <b>blik</b> = open place or clear view.',
         'The combination of <b>copse and open meadow</b> makes it rich.',
         'Copses provide shelter, the meadow the <b>flowers and insects</b>.',
         '<b>Marsh marigold, water violet and spotted orchid</b> on the wet parts.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh marigold</b> in the wettest meadows.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Heath spotted orchid</b> in flower.',
          '<span class="months">Jun\u2013Aug</span> \U0001f98b <b>Butterflies</b> in the fringes along the copses.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Bluethroat</b> sings from the scrub.'],
 'wild': ['\U0001f33c Marsh marigold \u00b7 Water violet \u00b7 Heath spotted orchid', '\U0001f426 Snipe \u00b7 Bluethroat \u00b7 Whitethroat', '\U0001f98b Summer butterflies \u00b7 Silver-bordered fritillary', '\U0001f9a0 Dragonflies along the brook', '\U0001f333 Alder \u00b7 Willow \u00b7 Oak'],
 'trail': ['Park at <b>Erm</b>; paths along the Sleenerstroom.',
           'Small area \u2014 combine with the <b>Sleenerstroom</b> itself.',
           '<b>Do not</b> enter the hay meadow before mowing.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile hay meadow \u00b7 \U0001f97e Wet'
}, card_class='card water'))

C.append(mk.card(1373, 'Lutkeland', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Grasland \u00b7 kleinschalig perceel met singels', 'list 36 \u00b7 no. 92'],
 'loc': '\U0001f4cd Bij Erm en Sleen \u00b7 Grasland met singels \u00b7 Klein',
 'desc': '<b>Lutkeland</b> betekent letterlijk \u2018klein land\u2019: <i>lutke</i> is een oud Noord-Nederlands woord voor klein, verwant aan het Engelse <i>little</i> en het Duitse <i>l\u00fctt</i>. Zulke namen werden gegeven aan percelen die opvielen door hun bescheiden formaat, vaak omdat ze als restje overbleven bij de verdeling van gemeenschappelijke grond. Precies die kleine, hoekige restpercelen zijn in het moderne landschap goud waard: ze zijn te klein voor efficiënte machinale bewerking, waardoor ze <b>extensief beheerd</b> bleven en hun perceelsranden behielden. Hier ligt een kruidenrijk grasland omgeven door <b>houtsingels</b>, met in de zomen <b>knoopkruid, margriet en duizendblad</b>. Er foerageren <b>vlinders en wilde bijen</b>, en in de singels broeden <b>grasmus, geelgors en heggenmus</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (bloei en insecten), apr\u2013jun (zang in de singels)<br>\n    <b>Beste tijd van de dag:</b> Warme middag \u2014 dan zijn vlinders en bijen op hun actiefst.',
 'why': ['<b>Lutke</b> = klein, verwant aan Engels <i>little</i>.',
         'Kleine restpercelen zijn <b>te klein voor machines</b> \u2014 en dus extensief.',
         'Kruidenrijk grasland omgeven door <b>houtsingels</b>.',
         'Zomen met <b>knoopkruid, margriet en duizendblad</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Grasmus en geelgors</b> zingen in de singels.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Kruidenrijk grasland</b> in volle bloei.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Vlinders en wilde bijen</b> op de bloemen.',
          '<span class="months">Sep\u2013Okt</span> \U0001fad0 <b>Bessen</b> in de singels.'],
 'wild': ['\U0001f98b Vlinders \u00b7 \U0001f41d Wilde bijen \u00b7 Zweefvliegen', '\U0001f33c Knoopkruid \u00b7 Margriet \u00b7 Duizendblad', '\U0001f426 Grasmus \u00b7 Geelgors \u00b7 Heggenmus', '\U0001f333 Meidoorn \u00b7 Els \u00b7 Hazelaar', '\U0001f98c Haas'],
 'trail': ['Parkeren bij <b>Erm</b>; het perceel ligt aan een landweg.',
           'Zeer klein \u2014 combineer met <b>Boschmaden</b> en de <b>Sleenerstroom</b>.',
           'Kom op een <b>warme middag</b> voor de insecten.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Klein perceel \u2014 bekijk vanaf de rand'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Grassland \u00b7 small-scale parcel with tree lines', 'list 36 \u00b7 no. 92'],
 'loc': '\U0001f4cd Near Erm and Sleen \u00b7 Grassland with tree lines \u00b7 Small',
 'desc': '<b>Lutkeland</b> means literally \u2018little land\u2019: <i>lutke</i> is an old northern Dutch word for small, cognate with English <i>little</i> and German <i>l\u00fctt</i>. Such names were given to parcels notable for their modest size, often because they were left over as scraps when common land was divided. Precisely those small, angular residual parcels are worth their weight in gold in the modern landscape: they are too small for efficient machine working, which has kept them <b>extensively managed</b> and preserved their field margins. Here lies a herb-rich grassland surrounded by <b>tree lines</b>, with <b>knapweed, oxeye daisy and yarrow</b> in the fringes. <b>Butterflies and wild bees</b> forage here, and <b>whitethroat, yellowhammer and dunnock</b> breed in the lines.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (flowering and insects), Apr\u2013Jun (song in the tree lines)<br>\n    <b>Best time of day:</b> Warm afternoon \u2014 when butterflies and bees are most active.',
 'why': ['<b>Lutke</b> = small, cognate with English <i>little</i>.',
         'Small residual parcels are <b>too small for machines</b> \u2014 hence extensive.',
         'Herb-rich grassland surrounded by <b>tree lines</b>.',
         'Fringes with <b>knapweed, oxeye daisy and yarrow</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Whitethroat and yellowhammer</b> sing in the lines.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Herb-rich grassland</b> in full flower.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Butterflies and wild bees</b> on the flowers.',
          '<span class="months">Sep\u2013Oct</span> \U0001fad0 <b>Berries</b> in the tree lines.'],
 'wild': ['\U0001f98b Butterflies \u00b7 \U0001f41d Wild bees \u00b7 Hoverflies', '\U0001f33c Knapweed \u00b7 Oxeye daisy \u00b7 Yarrow', '\U0001f426 Whitethroat \u00b7 Yellowhammer \u00b7 Dunnock', '\U0001f333 Hawthorn \u00b7 Alder \u00b7 Hazel', '\U0001f98c Brown hare'],
 'trail': ['Park at <b>Erm</b>; the parcel lies along a country lane.',
           'Very small \u2014 combine with <b>Boschmaden</b> and the <b>Sleenerstroom</b>.',
           'Come on a <b>warm afternoon</b> for the insects.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Small parcel \u2014 view from the edge'
}))

C.append(mk.card(1374, 'Schietbaanbosje', {
 'tags': ['Drenthe \u00b7 Emmen', 'Bosje \u00b7 voormalig militair terrein', 'list 36 \u00b7 no. 93'],
 'loc': '\U0001f4cd Bij Emmen \u00b7 Klein bos op oud oefenterrein \u00b7 Klein',
 'desc': 'Het <b>Schietbaanbosje</b> bij Emmen is genoemd naar de <b>schietbaan</b> die hier ooit lag, en dat militaire verleden heeft een onverwacht gunstig effect gehad. Op oefenterreinen mocht decennialang niemand komen: geen boeren, geen wandelaars, geen bebouwing. Er werd niet bemest, niet ontwaterd en niet ontgonnen \u2014 alleen af en toe geschoten. Dat regime van <b>afwezigheid</b> heeft er wereldwijd voor gezorgd dat oude militaire terreinen tot de best bewaarde natuurgebieden behoren. Hier bleef daardoor een schraal bosje met open zandplekken bewaard, met de <b>kogelvanger</b> \u2014 de aarden wal achter de doelen \u2014 nog als reli\u00ebf herkenbaar. Op de zuidhelling daarvan is het warm en kaal, ideaal voor <b>graafbijen en zandloopkevers</b>, en er broeden <b>boompieper en gekraagde roodstaart</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (graafbijen en broedvogels), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Warme ochtend \u2014 bijen en kevers op de zonnige wal.',
 'why': ['Militair verleden betekende decennia <b>afwezigheid van gebruik</b>.',
         'Niet bemest, niet ontwaterd, niet ontgonnen \u2014 daardoor <b>schraal gebleven</b>.',
         'De <b>kogelvanger</b> is nog als aarden wal herkenbaar.',
         'Warme zuidhelling met <b>graafbijen en zandloopkevers</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boompieper</b> zingt boven de open plekken.',
          '<span class="months">Mei\u2013Jul</span> \U0001f41d <b>Graafbijen</b> nestelen in de zonnige wal.',
          '<span class="months">Jun\u2013Aug</span> \U0001fab2 <b>Zandloopkevers</b> jagen op het kale zand.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de schrale bodem.'],
 'wild': ['\U0001f41d Graafbijen \u00b7 Graafwespen', '\U0001fab2 Zandloopkevers', '\U0001f426 Boompieper \u00b7 Gekraagde roodstaart', '\U0001f338 Struikheide \u00b7 Buntgras', '\U0001f333 Eik \u00b7 Berk \u00b7 Grove den'],
 'trail': ['Parkeren aan de rand van <b>Emmen</b>; smalle paden door het bosje.',
           'Zoek het <b>reli\u00ebf van de kogelvanger</b> \u2014 een rechte aarden wal.',
           'De <b>zuidkant</b> van de wal is het interessantst voor insecten.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Militair erfgoed \u00b7 \u26a0\ufe0f Klein en kwetsbaar'
}, {
 'tags': ['Drenthe \u00b7 Emmen', 'Copse \u00b7 former military ground', 'list 36 \u00b7 no. 93'],
 'loc': '\U0001f4cd Near Emmen \u00b7 Small wood on an old training ground \u00b7 Small',
 'desc': 'The <b>Schietbaanbosje</b> near Emmen is named after the <b>rifle range</b> that once lay here, and that military past has had an unexpectedly favourable effect. For decades nobody was allowed onto training grounds: no farmers, no walkers, no building. Nothing was fertilised, drained or reclaimed \u2014 only occasionally shot at. That regime of <b>absence</b> has made old military sites among the best-preserved nature areas worldwide. As a result a poor little wood with open sandy patches survived here, with the <b>butt</b> \u2014 the earthen bank behind the targets \u2014 still recognisable as relief. Its south-facing slope is warm and bare, ideal for <b>mining bees and tiger beetles</b>, and <b>tree pipit and redstart</b> breed here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (mining bees and breeding birds), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Warm morning \u2014 bees and beetles on the sunny bank.',
 'why': ['The military past meant decades of <b>absence of use</b>.',
         'Not fertilised, drained or reclaimed \u2014 hence it <b>stayed poor</b>.',
         'The <b>butt</b> is still recognisable as an earthen bank.',
         'Warm south slope with <b>mining bees and tiger beetles</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tree pipit</b> sings above the clearings.',
          '<span class="months">May\u2013Jul</span> \U0001f41d <b>Mining bees</b> nest in the sunny bank.',
          '<span class="months">Jun\u2013Aug</span> \U0001fab2 <b>Tiger beetles</b> hunt on the bare sand.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the poor soil.'],
 'wild': ['\U0001f41d Mining bees \u00b7 Digger wasps', '\U0001fab2 Tiger beetles', '\U0001f426 Tree pipit \u00b7 Redstart', '\U0001f338 Ling \u00b7 Grey hair-grass', '\U0001f333 Oak \u00b7 Birch \u00b7 Scots pine'],
 'trail': ['Park at the edge of <b>Emmen</b>; narrow paths through the copse.',
           'Look for the <b>relief of the butt</b> \u2014 a straight earthen bank.',
           'The <b>south side</b> of the bank is most interesting for insects.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Military heritage \u00b7 \u26a0\ufe0f Small and fragile'
}, card_class='card dune'))

mk.insert(C, '1369')
mk.progress(1374)
mk.check()
