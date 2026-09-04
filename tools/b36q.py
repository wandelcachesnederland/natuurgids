# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1360, 'Bosgebied Hollandscheveld', {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Veenkoloniaal bos \u00b7 loofbos op dalgrond', 'list 36 \u00b7 no. 79'],
 'loc': '\U0001f4cd Bij Hollandscheveld \u00b7 Bos op dalgrond \u00b7 Middelgroot',
 'desc': 'Het bosgebied bij <b>Hollandscheveld</b> staat op <b>dalgrond</b> \u2014 de bodem die overblijft nadat het hoogveen is afgegraven. Die grond is een merkwaardig mengsel: een laagje resterend bonkveen en bagger, aangevuld met stadscompost en zand, kunstmatig samengesteld om er landbouw op te kunnen bedrijven. Bomen op zo\u2019n bodem hebben het lastig, want dalgrond droogt in de zomer sterk uit en klinkt in. Toch heeft zich hier in de loop van decennia een gevarieerd loofbos ontwikkeld, en de ondergroei laat de <b>kunstmatige oorsprong</b> nog zien: naast bosplanten groeien er soorten van voedselrijke, verstoorde grond. Ecologisch is het bos vooral belangrijk als <b>eiland</b> in een intensief agrarisch gebied \u2014 het is over kilometers de enige plek waar bosvogels als <b>bosuil, buizerd en grote bonte specht</b> terechtkunnen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (broedvogels), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 het zangkoor is hier verrassend vol.',
 'why': ['Staat op <b>dalgrond</b>: kunstmatig samengestelde bodem na vervening.',
         'Bomen hebben het zwaar \u2014 dalgrond <b>droogt uit en klinkt in</b>.',
         'Ondergroei verraadt de <b>kunstmatige oorsprong</b>.',
         'Enige <b>bosEiland</b> voor kilometers in agrarisch gebied.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Grote bonte specht</b> roffelt.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Zangkoor</b> van bosvogels.',
          '<span class="months">Jun\u2013Jul</span> \U0001f985 <b>Buizerd</b> met jongen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de vochtige dalgrond.'],
 'wild': ['\U0001f426 Bosuil \u00b7 Grote bonte specht \u00b7 Zwartkop', '\U0001f985 Buizerd \u00b7 Sperwer', '\U0001f98c Ree \u00b7 Vos', '\U0001f333 Eik \u00b7 Berk \u00b7 Els \u00b7 Es', '\U0001f344 Paddenstoelen op dood hout'],
 'trail': ['Parkeren bij <b>Hollandscheveld</b>; paden door het bos.',
           'Let op de <b>ondergroei</b> \u2014 die verraadt de kunstmatige bodem.',
           'Combineer met <b>Beukerswijk</b> en <b>Jufferswijk</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f97e Vochtig in de winter'
}, {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Peat-colony woodland \u00b7 broadleaf wood on residual soil', 'list 36 \u00b7 no. 79'],
 'loc': '\U0001f4cd Near Hollandscheveld \u00b7 Woodland on residual peat soil \u00b7 Medium-sized',
 'desc': 'The woodland at <b>Hollandscheveld</b> stands on <b>dalgrond</b> \u2014 the soil left behind after the raised bog was dug away. That ground is a curious mixture: a layer of residual coarse peat and dredgings, supplemented with town compost and sand, artificially composed so that farming could be practised on it. Trees have a hard time on such a soil, because dalgrond dries out badly in summer and subsides. Nevertheless a varied broadleaf wood has developed here over the decades, and the ground flora still shows the <b>artificial origin</b>: alongside woodland plants grow species of nutrient-rich, disturbed ground. Ecologically the wood matters mainly as an <b>island</b> in an intensively farmed area \u2014 for kilometres it is the only place where woodland birds such as <b>tawny owl, buzzard and great spotted woodpecker</b> can settle.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (breeding birds), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 the dawn chorus here is surprisingly full.',
 'why': ['Stands on <b>dalgrond</b>: artificially composed soil after peat extraction.',
         'Trees struggle \u2014 dalgrond <b>dries out and subsides</b>.',
         'Ground flora betrays the <b>artificial origin</b>.',
         'The only <b>woodland island</b> for kilometres in farmland.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Great spotted woodpecker</b> drumming.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Dawn chorus</b> of woodland birds.',
          '<span class="months">Jun\u2013Jul</span> \U0001f985 <b>Buzzard</b> with young.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the damp residual soil.'],
 'wild': ['\U0001f426 Tawny owl \u00b7 Great spotted woodpecker \u00b7 Blackcap', '\U0001f985 Buzzard \u00b7 Sparrowhawk', '\U0001f98c Roe deer \u00b7 Fox', '\U0001f333 Oak \u00b7 Birch \u00b7 Alder \u00b7 Ash', '\U0001f344 Fungi on deadwood'],
 'trail': ['Park at <b>Hollandscheveld</b>; paths through the wood.',
           'Note the <b>ground flora</b> \u2014 it betrays the artificial soil.',
           'Combine with <b>Beukerswijk</b> and <b>Jufferswijk</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f97e Damp in winter'
}))

C.append(mk.card(1361, 'Beukerswijk', {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Veenkanaal \u00b7 wijk met oevers en bermen', 'list 36 \u00b7 no. 80'],
 'loc': '\U0001f4cd Bij Hollandscheveld en Hoogeveen \u00b7 Veenkanaal \u00b7 Lijnvormig',
 'desc': 'De <b>Beukerswijk</b> is een <b>wijk</b>, en dat woord heeft in de veenkoloni\u00ebn een heel eigen betekenis: geen woonwijk maar een <b>zijkanaal</b>, loodrecht op het hoofddiep gegraven om turf af te voeren. Het hele veenkoloniale landschap is opgebouwd uit dit patroon \u2014 een hoofdkanaal met daar haaks op tientallen wijken, elk een paar honderd meter uit elkaar, zodat geen turfsteker meer dan een korte afstand hoefde te kruien. Toen de turf op was, verloren de wijken hun functie; sommige zijn gedempt, andere bleven liggen. Wat overbleef is ecologisch waardevoller dan verwacht: de <b>oevers en bermen</b> zijn nooit bemest en vormen lange, smalle stroken half-natuurlijk grasland door een verder kaal akkerbouwgebied. Ze werken als <b>corridor</b>, en er groeien nog moerasplanten en bloeiende kruiden.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (oeverbloei en libellen), apr\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Late ochtend \u2014 libellen boven het water en insecten op de bermen.',
 'why': ['<b>Wijk</b> = zijkanaal voor turfafvoer, geen woonwijk.',
         'Wijken lagen zo dicht dat niemand ver hoefde te <b>kruien</b>.',
         'Oevers en bermen zijn <b>nooit bemest</b> \u2014 half-natuurlijk grasland.',
         'Lange smalle <b>corridor</b> door kaal akkerbouwgebied.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Rietgors en kleine karekiet</b> in de oeverzoom.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Oeverbloei</b> met moerasplanten.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven het kanaalwater.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Doortrekkers</b> volgen de lijn van de wijk.'],
 'wild': ['\U0001f426 Rietgors \u00b7 Kleine karekiet \u00b7 Blauwborst', '\U0001f9a0 Libellen \u00b7 Waterjuffers', '\U0001f33c Moerasplanten \u00b7 Wilgenroosje', '\U0001f438 Amfibie\u00ebn in het kanaal', '\U0001f987 Vleermuizen boven het water'],
 'trail': ['Volg de <b>Beukerswijk</b> per fiets of te voet vanaf Hollandscheveld.',
           'Let op de <b>haakse structuur</b> op de kaart \u2014 dat is het veenkoloniale raster.',
           'De bermen zijn het interessantst in <b>juli</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b4 Fietsroute \u00b7 \U0001f3db\ufe0f Veenkoloniaal erfgoed'
}, {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Peat canal \u00b7 side canal with banks and verges', 'list 36 \u00b7 no. 80'],
 'loc': '\U0001f4cd Near Hollandscheveld and Hoogeveen \u00b7 Peat canal \u00b7 Linear',
 'desc': 'The <b>Beukerswijk</b> is a <b>wijk</b>, and in the peat colonies that word has a meaning all its own: not a residential district but a <b>side canal</b>, dug at right angles to the main canal to carry turf away. The entire peat-colony landscape is built from this pattern \u2014 a main canal with dozens of wijken at right angles to it, each a few hundred metres apart, so that no turf-cutter had to barrow more than a short distance. When the peat ran out the wijken lost their function; some were filled in, others remained. What survived is ecologically more valuable than expected: the <b>banks and verges</b> were never fertilised and form long, narrow strips of semi-natural grassland through otherwise bare arable land. They work as a <b>corridor</b>, and marsh plants and flowering herbs still grow there.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (bank flowering and dragonflies), Apr\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Late morning \u2014 dragonflies above the water and insects on the verges.',
 'why': ['<b>Wijk</b> = side canal for turf transport, not a residential district.',
         'Wijken lay so close that nobody had to <b>barrow</b> far.',
         'Banks and verges were <b>never fertilised</b> \u2014 semi-natural grassland.',
         'A long narrow <b>corridor</b> through bare arable land.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Reed bunting and reed warbler</b> in the bank fringe.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Bank flowering</b> with marsh plants.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the canal water.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Migrants</b> follow the line of the canal.'],
 'wild': ['\U0001f426 Reed bunting \u00b7 Reed warbler \u00b7 Bluethroat', '\U0001f9a0 Dragonflies \u00b7 Damselflies', '\U0001f33c Marsh plants \u00b7 Rosebay willowherb', '\U0001f438 Amphibians in the canal', '\U0001f987 Bats above the water'],
 'trail': ['Follow the <b>Beukerswijk</b> by bicycle or on foot from Hollandscheveld.',
           'Note the <b>right-angled structure</b> on the map \u2014 that is the peat-colony grid.',
           'The verges are most interesting in <b>July</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b4 Cycle route \u00b7 \U0001f3db\ufe0f Peat-colony heritage'
}, card_class='card water'))

C.append(mk.card(1362, 'Hollandsche Veld', {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Veenkoloniaal landschap \u00b7 lintdorp, wijken en bermen', 'list 36 \u00b7 no. 81'],
 'loc': '\U0001f4cd Het dorp Hollandscheveld bij Hoogeveen \u00b7 Veenkolonie \u00b7 Groot',
 'desc': 'Het <b>Hollandsche Veld</b> is de veenkolonie waar Hoogeveen uit is voortgekomen, en de naam vertelt het verhaal: het waren <b>Hollandse investeerders</b> uit Amsterdam en omstreken die in de zeventiende eeuw het kapitaal leverden om dit veengebied te ontginnen. Zij kochten het veen, lieten kanalen graven en huurden arbeiders in \u2014 een vroege vorm van kapitaalintensieve, op export gerichte grondstofwinning. De turf ging per schip naar de Hollandse steden, waar hij de bakkerijen, brouwerijen en steenovens van de Gouden Eeuw stookte. Het landschap dat overbleef is een <b>lintdorp</b> langs het hoofddiep met haaks daarop de wijken. Voor de natuur zijn vooral de <b>bermen, wijkoevers en erfbeplantingen</b> van belang: samen vormen ze een fijnmazig netwerk met <b>geelgors, kneu en huismus</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (broedvogels en bermbloei), sep\u2013okt (doortrek langs de linten)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 en fiets de linten af voor het volledige beeld.',
 'why': ['Ontgonnen met kapitaal van <b>Hollandse investeerders</b> in de 17e eeuw.',
         'De turf stookte de <b>Gouden Eeuw</b>: bakkerijen, brouwerijen, steenovens.',
         '<b>Lintdorp</b> langs het hoofddiep met haakse wijken.',
         'Bermen en erfbeplantingen als <b>fijnmazig netwerk</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Geelgors en kneu</b> in de erfbeplantingen.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Bermbloei</b> langs de wijken.',
          '<span class="months">Jun\u2013Aug</span> \U0001f426 <b>Huismus en boerenzwaluw</b> bij de erven.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Doortrekkers</b> volgen de beplantingslinten.'],
 'wild': ['\U0001f426 Geelgors \u00b7 Kneu \u00b7 Huismus \u00b7 Boerenzwaluw', '\U0001f985 Torenvalk \u00b7 Buizerd', '\U0001f33c Bermkruiden \u00b7 Moerasplanten', '\U0001f987 Vleermuizen langs de wijken', '\U0001f98c Haas'],
 'trail': ['Parkeren in <b>Hollandscheveld</b>; fiets langs het hoofddiep.',
           'Bekijk het <b>raster</b> op de kaart: hoofddiep met haakse wijken.',
           'Let op <b>erfbeplantingen</b> \u2014 daar zitten de vogels.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b4 Fietsroute \u00b7 \U0001f3db\ufe0f Veenkoloniaal erfgoed'
}, {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Peat-colony landscape \u00b7 ribbon village, canals and verges', 'list 36 \u00b7 no. 81'],
 'loc': '\U0001f4cd The village of Hollandscheveld near Hoogeveen \u00b7 Peat colony \u00b7 Large',
 'desc': 'The <b>Hollandsche Veld</b> is the peat colony from which Hoogeveen grew, and the name tells the story: it was <b>Dutch investors</b> from Amsterdam and its surroundings who supplied the capital in the seventeenth century to reclaim this bog. They bought the peat, had canals dug and hired labourers \u2014 an early form of capital-intensive, export-oriented raw material extraction. The turf went by boat to the cities of Holland, where it fired the bakeries, breweries and brick kilns of the Golden Age. The landscape left behind is a <b>ribbon village</b> along the main canal with the side canals at right angles. For nature it is chiefly the <b>verges, canal banks and farmyard planting</b> that matter: together they form a fine-grained network with <b>yellowhammer, linnet and house sparrow</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (breeding birds and verge flowering), Sep\u2013Oct (passage along the ribbons)<br>\n    <b>Best time of day:</b> Morning \u2014 and cycle the ribbons for the full picture.',
 'why': ['Reclaimed with capital from <b>Dutch investors</b> in the 17th century.',
         'The turf fired the <b>Golden Age</b>: bakeries, breweries, brick kilns.',
         '<b>Ribbon village</b> along the main canal with side canals at right angles.',
         'Verges and farmyard planting as a <b>fine-grained network</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Yellowhammer and linnet</b> in the farmyard planting.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Verge flowering</b> along the canals.',
          '<span class="months">Jun\u2013Aug</span> \U0001f426 <b>House sparrow and barn swallow</b> at the farms.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Migrants</b> follow the planted ribbons.'],
 'wild': ['\U0001f426 Yellowhammer \u00b7 Linnet \u00b7 House sparrow \u00b7 Barn swallow', '\U0001f985 Kestrel \u00b7 Buzzard', '\U0001f33c Verge herbs \u00b7 Marsh plants', '\U0001f987 Bats along the canals', '\U0001f98c Brown hare'],
 'trail': ['Park in <b>Hollandscheveld</b>; cycle along the main canal.',
           'Study the <b>grid</b> on the map: main canal with side canals at right angles.',
           'Watch the <b>farmyard planting</b> \u2014 that is where the birds are.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b4 Cycle route \u00b7 \U0001f3db\ufe0f Peat-colony heritage'
}))

C.append(mk.card(1363, 'Geeslo', {
 'tags': ['Drenthe \u00b7 Coevorden', 'Natte laagte \u00b7 grasland en houtsingels', 'list 36 \u00b7 no. 82'],
 'loc': '\U0001f4cd Bij Geesbrug en Gees \u00b7 Natte laagte \u00b7 Klein',
 'desc': '<b>Geeslo</b> combineert twee oude landschapswoorden: <i>Gees</i> van het naburige dorp, en <b>lo</b> \u2014 een van de oudste plaatsnaamelementen van Nederland, dat <b>open plek in het bos</b> of licht bos op hoge zandgrond betekent. Namen op -lo (Almelo, Hengelo, Ruinerwold) markeren gebieden die al in de vroege middeleeuwen in gebruik waren, toen er nog wel bos stond. Dat maakt zulke namen tot archeologische aanwijzingen: waar een -lo ligt, was ooit bos en vroege bewoning. Het gebied bestaat nu uit natte graslanden met houtsingels, en het beheer richt zich op het vasthouden van water. In de singels broeden <b>geelgors en grasmus</b>, in het natte grasland <b>watersnip en tureluur</b>, en in de sloten leeft de <b>grote modderkruiper</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels en zang), mei\u2013jul (bloei in de singelzomen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 watersnippen baltsen bij zonsopkomst.',
 'why': ['<b>-lo</b> = open plek in het bos: een van de oudste plaatsnaamelementen.',
         'Namen op -lo markeren <b>vroegmiddeleeuwse bewoning</b>.',
         'Natte graslanden met <b>houtsingels</b> als perceelscheiding.',
         '<b>Grote modderkruiper</b> in de sloten.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Watersnip</b> baltst boven de natte percelen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Tureluur</b> met kuikens.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Zoombloei</b> langs de houtsingels.',
          '<span class="months">Sep\u2013Okt</span> \U0001fad0 <b>Bessen</b> in de singels voor doortrekkers.'],
 'wild': ['\U0001f426 Watersnip \u00b7 Tureluur \u00b7 Geelgors \u00b7 Grasmus', '\U0001f41f Grote modderkruiper', '\U0001f438 Amfibie\u00ebn in de sloten', '\U0001f333 Els \u00b7 Eik \u00b7 Meidoorn', '\U0001f98c Ree \u00b7 Haas'],
 'trail': ['Parkeren bij <b>Geesbrug</b>; landweggetjes langs de percelen.',
           'Klein gebied \u2014 combineer met de <b>Geeserstroom</b>.',
           'Blijf op de wegen in het <b>broedseizoen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Broedgebied mrt\u2013jun \u00b7 \U0001f97e Nat'
}, {
 'tags': ['Drenthe \u00b7 Coevorden', 'Wet hollow \u00b7 grassland and tree lines', 'list 36 \u00b7 no. 82'],
 'loc': '\U0001f4cd Near Geesbrug and Gees \u00b7 Wet hollow \u00b7 Small',
 'desc': '<b>Geeslo</b> combines two old landscape words: <i>Gees</i> from the neighbouring village, and <b>lo</b> \u2014 one of the oldest place-name elements in the Netherlands, meaning a <b>clearing in the wood</b> or open woodland on high sandy ground. Names in -lo (Almelo, Hengelo, Ruinerwold) mark areas already in use in the early Middle Ages, when woodland still stood. That makes such names archaeological clues: where there is a -lo, there was once woodland and early settlement. The area now consists of wet grasslands with tree lines, and management aims at retaining water. <b>Yellowhammer and whitethroat</b> breed in the tree lines, <b>snipe and redshank</b> in the wet grassland, and the <b>spined loach</b> lives in the ditches.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds and song), May\u2013Jul (flowering in the tree-line fringes)<br>\n    <b>Best time of day:</b> Early morning \u2014 snipe drum at sunrise.',
 'why': ['<b>-lo</b> = clearing in the wood: one of the oldest place-name elements.',
         'Names in -lo mark <b>early medieval settlement</b>.',
         'Wet grasslands with <b>tree lines</b> as field boundaries.',
         '<b>Spined loach</b> in the ditches.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Snipe</b> drumming above the wet parcels.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Redshank</b> with chicks.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Fringe flowering</b> along the tree lines.',
          '<span class="months">Sep\u2013Oct</span> \U0001fad0 <b>Berries</b> in the lines for passage birds.'],
 'wild': ['\U0001f426 Snipe \u00b7 Redshank \u00b7 Yellowhammer \u00b7 Whitethroat', '\U0001f41f Spined loach', '\U0001f438 Amphibians in the ditches', '\U0001f333 Alder \u00b7 Oak \u00b7 Hawthorn', '\U0001f98c Roe deer \u00b7 Brown hare'],
 'trail': ['Park at <b>Geesbrug</b>; country lanes along the parcels.',
           'Small area \u2014 combine with the <b>Geeserstroom</b>.',
           'Keep to the roads in the <b>breeding season</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Breeding ground Mar\u2013Jun \u00b7 \U0001f97e Wet'
}))

C.append(mk.card(1364, 'Jufferswijk', {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Veenkanaal \u00b7 wijk met bermen en beplanting', 'list 36 \u00b7 no. 83'],
 'loc': '\U0001f4cd Bij Hoogeveen en Nieuweroord \u00b7 Veenkanaal \u00b7 Lijnvormig',
 'desc': 'De <b>Jufferswijk</b> is een van de vele wijken in het Hoogeveense veengebied, en de naam bewaart een spoor van de eigendomsverhoudingen: veel wijken zijn genoemd naar de <b>compagnie of familie</b> die het recht had er turf te winnen, en \u2018juffer\u2019 duidde op een ongehuwde vrouw van stand \u2014 vermoedelijk een investeerster of erfgename die een aandeel in de vervening bezat. Dat is opmerkelijk, want in de zeventiende en achttiende eeuw was zelfstandig grondbezit door vrouwen bepaald niet vanzelfsprekend. De wijk zelf is nu vooral van belang als <b>lijnvormig landschapselement</b>: het water, de onbemeste bermen en de begeleidende bomenrij vormen samen een lange corridor. Er jagen <b>vleermuizen</b> boven het water, in de bermen bloeien kruiden, en langs de oever broeden <b>rietgors en kleine karekiet</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (bermbloei, libellen en vleermuizen), apr\u2013jun (broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 vleermuizen jagen dan boven het kanaalwater.',
 'why': ['Naam bewaart de <b>eigendomsgeschiedenis</b> van de vervening.',
         '\u2018Juffer\u2019 duidt op een <b>vrouwelijke investeerster</b> of erfgename.',
         'Zelfstandig grondbezit door vrouwen was toen <b>ongebruikelijk</b>.',
         'Water, bermen en bomenrij vormen samen een <b>corridor</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Rietgors en kleine karekiet</b> in de oeverzoom.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Bermbloei</b> langs de wijk.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> jagen boven het water.',
          '<span class="months">Jul\u2013Aug</span> \U0001f9a0 <b>Libellen</b> langs de oevers.'],
 'wild': ['\U0001f987 Watervleermuis \u00b7 Gewone dwergvleermuis', '\U0001f426 Rietgors \u00b7 Kleine karekiet', '\U0001f9a0 Libellen \u00b7 Waterjuffers', '\U0001f33c Bermkruiden \u00b7 Moerasplanten', '\U0001f438 Amfibie\u00ebn'],
 'trail': ['Volg de <b>Jufferswijk</b> per fiets vanaf Hoogeveen.',
           'Kom bij <b>schemer</b> \u2014 watervleermuizen scheren vlak boven het water.',
           'Combineer met <b>Beukerswijk</b> voor het complete wijkenpatroon.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b4 Fietsroute \u00b7 \U0001f3db\ufe0f Veenkoloniaal erfgoed'
}, {
 'tags': ['Drenthe \u00b7 Hoogeveen', 'Peat canal \u00b7 side canal with verges and planting', 'list 36 \u00b7 no. 83'],
 'loc': '\U0001f4cd Near Hoogeveen and Nieuweroord \u00b7 Peat canal \u00b7 Linear',
 'desc': 'The <b>Jufferswijk</b> is one of the many side canals in the Hoogeveen peat district, and its name preserves a trace of the ownership arrangements: many wijken are named after the <b>company or family</b> that held the right to cut turf there, and \u2018juffer\u2019 denoted an unmarried woman of standing \u2014 presumably an investor or heiress holding a share in the extraction. That is notable, because in the seventeenth and eighteenth centuries independent landholding by women was far from a matter of course. The canal itself now matters chiefly as a <b>linear landscape element</b>: the water, the unfertilised verges and the accompanying row of trees together form a long corridor. <b>Bats</b> hunt above the water, herbs flower in the verges, and <b>reed bunting and reed warbler</b> breed along the bank.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (verge flowering, dragonflies and bats), Apr\u2013Jun (breeding birds)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats then hunt above the canal water.',
 'why': ['The name preserves the <b>ownership history</b> of the peat extraction.',
         '\u2018Juffer\u2019 denotes a <b>female investor</b> or heiress.',
         'Independent landholding by women was then <b>unusual</b>.',
         'Water, verges and tree row together form a <b>corridor</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Reed bunting and reed warbler</b> in the bank fringe.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Verge flowering</b> along the canal.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> hunt above the water.',
          '<span class="months">Jul\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> along the banks.'],
 'wild': ['\U0001f987 Daubenton\u2019s bat \u00b7 Common pipistrelle', '\U0001f426 Reed bunting \u00b7 Reed warbler', '\U0001f9a0 Dragonflies \u00b7 Damselflies', '\U0001f33c Verge herbs \u00b7 Marsh plants', '\U0001f438 Amphibians'],
 'trail': ['Follow the <b>Jufferswijk</b> by bicycle from Hoogeveen.',
           'Come at <b>dusk</b> \u2014 Daubenton\u2019s bats skim just above the water.',
           'Combine with the <b>Beukerswijk</b> for the complete canal pattern.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b4 Cycle route \u00b7 \U0001f3db\ufe0f Peat-colony heritage'
}, card_class='card water'))

mk.insert(C, '1359')
mk.progress(1364)
mk.check()
