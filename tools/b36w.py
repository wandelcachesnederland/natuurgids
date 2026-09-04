# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1390, 'Ter Coulster', {
 'tags': ['Noord-Holland \u00b7 Heiloo', 'Landgoed \u00b7 park met vijvers en oude bomen', 'list 36 \u00b7 no. 109'],
 'loc': '\U0001f4cd Heiloo \u00b7 Landgoedpark \u00b7 Klein',
 'desc': '<b>Ter Coulster</b> is een landgoed op de strandwal van Heiloo waarvan de naam teruggaat op <i>coulster</i> of <i>kolster</i>, een oud woord dat verwant is aan <b>kolk</b> \u2014 een diepe plek of waterput. Dat past bij de plek: op de overgang van strandwal naar strandvlakte komt <b>kwelwater</b> aan de oppervlakte, en die natuurlijke waterrijkdom was precies de reden dat hier een buitenplaats werd aangelegd. Het park benut het water in vijvers en grachten. Ecologisch levert die combinatie van oud loofbos en helder kwelwater veel op: in het water groeien <b>waterviolier en holpijp</b>, planten die alleen bij schoon, kalkrijk kwelwater voorkomen. In de oude beuken broeden <b>boomklever en grote bonte specht</b>, en de <b>ijsvogel</b> jaagt boven de vijvers.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (stinzenflora), mei\u2013jul (kwelflora in de vijvers)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 ijsvogels jagen dan boven het stille water.',
 'why': ['<b>Coulster</b> is verwant aan <b>kolk</b> \u2014 diepe plek of waterput.',
         'Op de overgang strandwal\u2013strandvlakte komt <b>kwelwater</b> boven.',
         'Die waterrijkdom was de reden voor de <b>buitenplaats</b>.',
         '<b>Waterviolier en holpijp</b> wijzen op schoon kalkrijk kwelwater.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Stinzenflora</b> onder de oude bomen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> jaagt boven de vijvers.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33f <b>Waterviolier</b> bloeit in het kwelwater.',
          '<span class="months">Okt\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in het parkbos.'],
 'wild': ['\U0001f426 IJsvogel \u00b7 Boomklever \u00b7 Grote bonte specht', '\U0001f33f Waterviolier \u00b7 Holpijp \u00b7 Dotterbloem', '\U0001f987 Vleermuizen boven de vijvers', '\U0001f438 Kikkers \u00b7 Watersalamander', '\U0001f333 Oude beuk \u00b7 Eik \u00b7 Linde'],
 'trail': ['Parkeren in <b>Heiloo</b>; paden door het park.',
           'Kijk in de <b>vijvers</b> naar waterviolier \u2014 teken van schoon kwelwater.',
           'Wees stil bij het water voor de <b>ijsvogel</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historisch landgoed \u00b7 \U0001f6b6 Kort rondje'
}, {
 'tags': ['North Holland \u00b7 Heiloo', 'Estate \u00b7 park with ponds and old trees', 'list 36 \u00b7 no. 109'],
 'loc': '\U0001f4cd Heiloo \u00b7 Estate park \u00b7 Small',
 'desc': '<b>Ter Coulster</b> is an estate on the beach ridge at Heiloo whose name goes back to <i>coulster</i> or <i>kolster</i>, an old word related to <b>kolk</b> \u2014 a deep spot or well. That suits the place: at the transition from beach ridge to beach plain <b>seepage water</b> reaches the surface, and that natural abundance of water was exactly why a country seat was laid out here. The park uses the water in ponds and moats. Ecologically the combination of old broadleaf woodland and clear seepage water yields much: <b>water violet and horsetail</b> grow in the water, plants that occur only in clean, lime-rich seepage. <b>Nuthatch and great spotted woodpecker</b> breed in the old beeches, and the <b>kingfisher</b> hunts over the ponds.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (stinzen flora), May\u2013Jul (seepage flora in the ponds)<br>\n    <b>Best time of day:</b> Morning \u2014 kingfishers then hunt over the still water.',
 'why': ['<b>Coulster</b> is related to <b>kolk</b> \u2014 deep spot or well.',
         'At the beach ridge\u2013plain transition <b>seepage water</b> surfaces.',
         'That abundance of water was the reason for the <b>country seat</b>.',
         '<b>Water violet and horsetail</b> indicate clean lime-rich seepage.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Stinzen flora</b> beneath the old trees.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> hunts over the ponds.',
          '<span class="months">May\u2013Jul</span> \U0001f33f <b>Water violet</b> flowers in the seepage water.',
          '<span class="months">Oct\u2013Nov</span> \U0001f344 <b>Fungi</b> in the park woodland.'],
 'wild': ['\U0001f426 Kingfisher \u00b7 Nuthatch \u00b7 Great spotted woodpecker', '\U0001f33f Water violet \u00b7 Water horsetail \u00b7 Marsh marigold', '\U0001f987 Bats above the ponds', '\U0001f438 Frogs \u00b7 Newts', '\U0001f333 Old beech \u00b7 Oak \u00b7 Lime'],
 'trail': ['Park in <b>Heiloo</b>; paths through the park.',
           'Look in the <b>ponds</b> for water violet \u2014 a sign of clean seepage.',
           'Be quiet by the water for the <b>kingfisher</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic estate \u00b7 \U0001f6b6 Short circuit'
}))

C.append(mk.card(1391, 'Zeerijdtsdijkje', {
 'tags': ['Noord-Holland \u00b7 Heiloo', 'Oude dijk \u00b7 bloemrijke dijkberm', 'list 36 \u00b7 no. 110'],
 'loc': '\U0001f4cd Tussen Heiloo en Akersloot \u00b7 Historisch dijkje \u00b7 Klein',
 'desc': 'Het <b>Zeerijdtsdijkje</b> is een laag, kronkelend dijkje dat herinnert aan de tijd dat het water hier nog vrij spel had: het beschermde de landerijen tegen het <b>Zeerijdt</b>, een oude naam voor de zeearm die vanuit het IJ en de Schermer landinwaarts reikte. Zulke <b>slaperdijken</b> \u2014 dijken die hun waterkerende functie verloren toen er verderop een nieuwe zeewering kwam \u2014 zijn in Noord-Holland vaak eeuwenlang ongestoord blijven liggen. En daar zit hun waarde: de dijkbermen werden nooit bemest, nooit gescheurd en alleen gemaaid of beweid. Daardoor groeit er nu een <b>schrale, bloemrijke vegetatie</b> die in het omringende boerenland volledig is verdwenen, met <b>knoopkruid, margriet, kleine ratelaar en agrimonie</b>, en veel <b>vlinders en wilde bijen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (dijkbloei en insecten), mei\u2013jun (kleine ratelaar)<br>\n    <b>Beste tijd van de dag:</b> Warme middag \u2014 vlinders en bijen op de zuidhelling.',
 'why': ['<b>Slaperdijk</b>: verloor zijn waterkerende functie en bleef ongestoord.',
         'De bermen werden <b>nooit bemest of gescheurd</b>.',
         'Daardoor <b>schrale, bloemrijke vegetatie</b> zoals elders verdween.',
         '<b>Knoopkruid, margriet, kleine ratelaar en agrimonie</b>.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Kleine ratelaar</b> bloeit op de dijkhelling.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Knoopkruid en margriet</b> in volle bloei.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Vlinders en wilde bijen</b> op de bermen.',
          '<span class="months">Aug\u2013Sep</span> \U0001f997 <b>Sprinkhanen</b> zingen in het lange gras.'],
 'wild': ['\U0001f33c Knoopkruid \u00b7 Margriet \u00b7 Kleine ratelaar \u00b7 Agrimonie', '\U0001f98b Bruin zandoogje \u00b7 Icarusblauwtje \u00b7 Dikkopjes', '\U0001f41d Wilde bijen \u00b7 Zweefvliegen', '\U0001f997 Sprinkhanen \u00b7 Krekels', '\U0001f426 Graspieper \u00b7 Grasmus'],
 'trail': ['Parkeren bij <b>Heiloo</b> of <b>Akersloot</b>; het dijkje is te belopen.',
           'De <b>zuidhelling</b> is warmer en bloemrijker dan de noordkant.',
           'Kom in <b>juli</b> \u2014 dan is de bloei op zijn hoogtepunt.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historische dijk \u00b7 \u26a0\ufe0f Blijf op het pad'
}, {
 'tags': ['North Holland \u00b7 Heiloo', 'Old dike \u00b7 flower-rich dike verge', 'list 36 \u00b7 no. 110'],
 'loc': '\U0001f4cd Between Heiloo and Akersloot \u00b7 Historic dike \u00b7 Small',
 'desc': 'The <b>Zeerijdtsdijkje</b> is a low, winding dike recalling the days when the water still had free play here: it protected the fields against the <b>Zeerijdt</b>, an old name for the sea arm reaching inland from the IJ and the Schermer. Such <b>sleeper dikes</b> \u2014 dikes that lost their water-retaining role when a new sea defence was built further out \u2014 have often lain undisturbed for centuries in North Holland. And that is where their value lies: the dike verges were never fertilised, never ploughed and only mown or grazed. As a result a <b>poor, flower-rich vegetation</b> now grows there that has vanished completely from the surrounding farmland, with <b>knapweed, oxeye daisy, yellow rattle and agrimony</b>, and many <b>butterflies and wild bees</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (dike flowering and insects), May\u2013Jun (yellow rattle)<br>\n    <b>Best time of day:</b> Warm afternoon \u2014 butterflies and bees on the south slope.',
 'why': ['<b>Sleeper dike</b>: lost its water-retaining role and lay undisturbed.',
         'The verges were <b>never fertilised or ploughed</b>.',
         'Hence <b>poor, flower-rich vegetation</b> that vanished elsewhere.',
         '<b>Knapweed, oxeye daisy, yellow rattle and agrimony</b>.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33c <b>Yellow rattle</b> flowers on the dike slope.',
          '<span class="months">Jun\u2013Jul</span> \U0001f33c <b>Knapweed and oxeye daisy</b> in full flower.',
          '<span class="months">Jul\u2013Aug</span> \U0001f98b <b>Butterflies and wild bees</b> on the verges.',
          '<span class="months">Aug\u2013Sep</span> \U0001f997 <b>Grasshoppers</b> sing in the long grass.'],
 'wild': ['\U0001f33c Knapweed \u00b7 Oxeye daisy \u00b7 Yellow rattle \u00b7 Agrimony', '\U0001f98b Meadow brown \u00b7 Common blue \u00b7 Skippers', '\U0001f41d Wild bees \u00b7 Hoverflies', '\U0001f997 Grasshoppers \u00b7 Crickets', '\U0001f426 Meadow pipit \u00b7 Whitethroat'],
 'trail': ['Park at <b>Heiloo</b> or <b>Akersloot</b>; the dike can be walked.',
           'The <b>south slope</b> is warmer and more flowery than the north side.',
           'Come in <b>July</b> \u2014 the flowering then peaks.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic dike \u00b7 \u26a0\ufe0f Keep to the path'
}))

C.append(mk.card(1392, 'Het Die', {
 'tags': ['Noord-Holland \u00b7 Uitgeest', 'Water \u00b7 oude veenstroom', 'list 36 \u00b7 no. 111'],
 'loc': '\U0001f4cd Bij Uitgeest \u00b7 Open water met rietoevers \u00b7 Klein',
 'desc': '<b>Het Die</b> is een van de vele Noord-Hollandse wateren die dat woord in hun naam dragen \u2014 <i>die</i>, <i>dieze</i> of <i>diep</i> betekent eenvoudig <b>waterloop</b> of <b>vaargeul</b>, en het is een van de oudste waternamen in het Nederlands. Zulke wateren zijn geen gegraven kanalen maar <b>natuurlijke veenstromen</b>: geulen die zich in het veenlandschap vormden toen het overtollige regenwater een weg naar zee zocht. Ze zijn te herkennen aan hun onregelmatige, kronkelige loop, in scherp contrast met de latere rechte vaarten. Het Die verbindt de Uitgeester wateren met het Alkmaardermeer. Langs de oevers staan <b>riet en lisdodde</b>, waar <b>kleine karekiet, rietgors en bruine kiekendief</b> zitten; op het water zwemmen <b>fuut en meerkoet</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (rietvogels), nov\u2013feb (watervogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 stil water en rietvogelzang.',
 'why': ['<b>Die</b> = waterloop \u2014 een van de oudste waternamen in het Nederlands.',
         'Geen gegraven kanaal maar een <b>natuurlijke veenstroom</b>.',
         'Te herkennen aan de <b>kronkelige loop</b>, anders dan rechte vaarten.',
         'Verbindt de Uitgeester wateren met het <b>Alkmaardermeer</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f33e <b>Kleine karekiet</b> zingt in het riet.',
          '<span class="months">Mei\u2013Jul</span> \U0001f985 <b>Bruine kiekendief</b> jaagt boven de oevers.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven het water.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Watervogels</b> op het open water.'],
 'wild': ['\U0001f33e Kleine karekiet \u00b7 Rietgors \u00b7 Rietzanger', '\U0001f985 Bruine kiekendief', '\U0001f986 Fuut \u00b7 Meerkoet \u00b7 Kuifeend', '\U0001f9a0 Libellen \u00b7 Juffers', '\U0001f41f Snoek \u00b7 Baars \u00b7 Blankvoorn'],
 'trail': ['Parkeren bij <b>Uitgeest</b>; oeverpaden en fietsroute.',
           'Let op de <b>kronkelige loop</b> \u2014 bewijs van natuurlijke oorsprong.',
           'Vroege ochtend voor de <b>rietvogels</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6a3 Bevaarbaar \u00b7 \u26a0\ufe0f Rietoevers kwetsbaar in broedtijd'
}, {
 'tags': ['North Holland \u00b7 Uitgeest', 'Water \u00b7 old peat stream', 'list 36 \u00b7 no. 111'],
 'loc': '\U0001f4cd Near Uitgeest \u00b7 Open water with reed banks \u00b7 Small',
 'desc': '<b>Het Die</b> is one of the many North Holland waters carrying that word in their name \u2014 <i>die</i>, <i>dieze</i> or <i>diep</i> simply means <b>watercourse</b> or <b>channel</b>, and it is among the oldest water names in Dutch. Such waters are not dug canals but <b>natural peat streams</b>: channels that formed in the peat landscape as surplus rainwater found its way to the sea. They are recognisable by their irregular, winding course, in sharp contrast to the later straight canals. Het Die connects the Uitgeest waters with the Alkmaardermeer. Along the banks stand <b>reed and bulrush</b>, holding <b>reed warbler, reed bunting and marsh harrier</b>; on the water swim <b>great crested grebe and coot</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (reed birds), Nov\u2013Feb (waterfowl)<br>\n    <b>Best time of day:</b> Early morning \u2014 still water and reed-bird song.',
 'why': ['<b>Die</b> = watercourse \u2014 among the oldest water names in Dutch.',
         'Not a dug canal but a <b>natural peat stream</b>.',
         'Recognisable by its <b>winding course</b>, unlike straight canals.',
         'Connects the Uitgeest waters with the <b>Alkmaardermeer</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f33e <b>Reed warbler</b> sings in the reed.',
          '<span class="months">May\u2013Jul</span> \U0001f985 <b>Marsh harrier</b> hunts over the banks.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the water.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Waterfowl</b> on the open water.'],
 'wild': ['\U0001f33e Reed warbler \u00b7 Reed bunting \u00b7 Sedge warbler', '\U0001f985 Marsh harrier', '\U0001f986 Great crested grebe \u00b7 Coot \u00b7 Tufted duck', '\U0001f9a0 Dragonflies \u00b7 Damselflies', '\U0001f41f Pike \u00b7 Perch \u00b7 Roach'],
 'trail': ['Park at <b>Uitgeest</b>; bank paths and a cycle route.',
           'Note the <b>winding course</b> \u2014 evidence of natural origin.',
           'Early morning for the <b>reed birds</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6a3 Navigable \u00b7 \u26a0\ufe0f Reed banks fragile in the breeding season'
}, card_class='card water'))

C.append(mk.card(1393, 'Limmerveentje', {
 'tags': ['Noord-Holland \u00b7 Castricum', 'Veenrestant \u00b7 nat schraalland', 'list 36 \u00b7 no. 112'],
 'loc': '\U0001f4cd Bij Limmen \u00b7 Veenrestant \u00b7 Zeer klein',
 'desc': 'Het <b>Limmerveentje</b> is een postzegel van een gebied \u2014 nog geen paar hectare \u2014 maar het bewaart iets dat in heel Kennemerland vrijwel verdwenen is: een stukje <b>veen in de strandvlakte</b>. Tussen de strandwallen van Limmen en Heiloo groeide na de zeespiegelstijging veen, en dat werd bijna overal afgegraven of onder polderpeil gebracht. Hier bleef een laagte over waar het grondwater nog hoog staat en <b>kwel</b> uit de strandwal toestroomt. Die combinatie van nat, voedselarm en kalkrijk maakt een <b>blauwgraslandachtige vegetatie</b> mogelijk, met <b>blauwe zegge, moerasviooltje en gevlekte orchis</b>. Op zo\u2019n klein oppervlak is dat botanisch een schatkamer. Er vliegen bijzondere <b>libellen</b> en broeden <b>rietgors en grasmus</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (orchidee\u00ebn en schraallandflora), jun\u2013aug (libellen)<br>\n    <b>Beste tijd van de dag:</b> Late ochtend \u2014 warm genoeg voor insecten, met de bloei op zijn best.',
 'why': ['Zeldzaam <b>veenrestant in de strandvlakte</b> van Kennemerland.',
         'Hoog grondwater plus <b>kwel</b> uit de strandwal.',
         'Nat, voedselarm en kalkrijk \u2014 basis voor <b>blauwgrasland</b>.',
         '<b>Blauwe zegge, moerasviooltje en gevlekte orchis</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Moerasviooltje</b> bloeit in de natte laagte.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Gevlekte orchis</b> in bloei.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven de slootjes.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33f <b>Blauwe zegge</b> bepaalt het beeld.'],
 'wild': ['\U0001f33c Blauwe zegge \u00b7 Moerasviooltje \u00b7 Gevlekte orchis', '\U0001f9a0 Libellen \u00b7 Juffers', '\U0001f33e Rietgors \u00b7 Grasmus', '\U0001f438 Kleine watersalamander \u00b7 Bruine kikker', '\U0001f98b Zilveren maan (historisch)'],
 'trail': ['Parkeren bij <b>Limmen</b>; het gebiedje ligt aan een landweg.',
           'Zeer klein \u2014 bekijk het <b>vanaf de rand</b>.',
           'Juni is de maand van de <b>orchidee\u00ebn</b>.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Zeer kwetsbaar \u2014 niet betreden \u00b7 \U0001f97e Nat'
}, {
 'tags': ['North Holland \u00b7 Castricum', 'Peat remnant \u00b7 wet poor grassland', 'list 36 \u00b7 no. 112'],
 'loc': '\U0001f4cd Near Limmen \u00b7 Peat remnant \u00b7 Very small',
 'desc': 'The <b>Limmerveentje</b> is a postage stamp of an area \u2014 barely a couple of hectares \u2014 but it preserves something almost vanished from the whole of Kennemerland: a patch of <b>peat in the beach plain</b>. Between the beach ridges of Limmen and Heiloo peat grew after the sea level rose, and nearly everywhere it was dug away or drained to polder level. Here a hollow remained where the groundwater still stands high and <b>seepage</b> flows in from the beach ridge. That combination of wet, nutrient-poor and lime-rich makes a <b>blue-grassland type vegetation</b> possible, with <b>glaucous sedge, marsh violet and heath spotted orchid</b>. On such a small surface that is a botanical treasure house. Notable <b>dragonflies</b> fly here and <b>reed bunting and whitethroat</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (orchids and poor-grassland flora), Jun\u2013Aug (dragonflies)<br>\n    <b>Best time of day:</b> Late morning \u2014 warm enough for insects, with flowering at its best.',
 'why': ['Rare <b>peat remnant in the beach plain</b> of Kennemerland.',
         'High groundwater plus <b>seepage</b> from the beach ridge.',
         'Wet, nutrient-poor and lime-rich \u2014 the basis for <b>blue grassland</b>.',
         '<b>Glaucous sedge, marsh violet and heath spotted orchid</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh violet</b> flowers in the wet hollow.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Heath spotted orchid</b> in flower.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the ditches.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33f <b>Glaucous sedge</b> dominates the scene.'],
 'wild': ['\U0001f33c Glaucous sedge \u00b7 Marsh violet \u00b7 Heath spotted orchid', '\U0001f9a0 Dragonflies \u00b7 Damselflies', '\U0001f33e Reed bunting \u00b7 Whitethroat', '\U0001f438 Smooth newt \u00b7 Common frog', '\U0001f98b Silver-bordered fritillary (historic)'],
 'trail': ['Park at <b>Limmen</b>; the little site lies along a country lane.',
           'Very small \u2014 view it <b>from the edge</b>.',
           'June is the month of the <b>orchids</b>.'],
 'foot': '\U0001f436 Dogs not allowed \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Very fragile \u2014 do not enter \u00b7 \U0001f97e Wet'
}, card_class='card water'))

C.append(mk.card(1394, 'Eendenkooi bij Uitgeest', {
 'tags': ['Noord-Holland \u00b7 Uitgeest', 'Eendenkooi \u00b7 historisch vangsysteem met kooibos', 'list 36 \u00b7 no. 113'],
 'loc': '\U0001f4cd Bij Uitgeest \u00b7 Eendenkooi met kooibos \u00b7 Klein',
 'desc': 'Een <b>eendenkooi</b> is een van de vernuftigste vangsystemen die de mens ooit bedacht: een vijver met vier gebogen, overkapte <b>vangpijpen</b>, omringd door een dicht <b>kooibos</b> dat volstrekte rust waarborgt. De kooiker lokte wilde eenden met tamme <b>staleenden</b> en met een klein hondje, de <b>kooikershond</b>, dat zich langs schermen liet zien en weer verdween \u2014 eenden volgen zo\u2019n verschijning uit nieuwsgierigheid de pijp in. Rond elke kooi gold bovendien het <b>recht van afpaling</b>: binnen een straal van honderden meters mocht niemand lawaai maken of bouwen. Dat wettelijke stilteregime maakt oude kooien tot ecologische eilanden. Hier broeden nu <b>buizerd, boomvalk, ransuil en houtsnip</b>, en in het kooibos groeit een rijke voorjaarsflora.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013mei</b> (voorjaarsflora en broedvogels), okt\u2013mrt (watervogels op de kooiplas)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 rust in en om het kooibos.',
 'why': ['Vijver met vier gebogen <b>vangpijpen</b> en een dicht kooibos.',
         'Gelokt met <b>staleenden</b> en een <b>kooikershond</b>.',
         'Het <b>recht van afpaling</b> waarborgde stilte rondom.',
         'Dat stilteregime maakt oude kooien tot <b>ecologische eilanden</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f33c <b>Voorjaarsflora</b> in het kooibos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f985 <b>Buizerd en boomvalk</b> broeden in de rust.',
          '<span class="months">Okt\u2013Mrt</span> \U0001f986 <b>Watervogels</b> op de kooiplas.',
          '<span class="months">Nov\u2013Feb</span> \U0001f989 <b>Ransuilen</b> in de dichte struiken.'],
 'wild': ['\U0001f985 Buizerd \u00b7 Boomvalk \u00b7 \U0001f989 Ransuil', '\U0001f986 Wilde eend \u00b7 Wintertaling \u00b7 Slobeend', '\U0001f426 Houtsnip \u00b7 Grote bonte specht', '\U0001f33c Speenkruid \u00b7 Pinksterbloem \u00b7 Hondsdraf', '\U0001f987 Vleermuizen boven de plas'],
 'trail': ['Parkeren bij <b>Uitgeest</b>; kooien zijn vaak <b>alleen met excursie</b> te bezoeken.',
           'Respecteer de <b>rust</b> \u2014 dat is de kern van het gebied.',
           'Kijk of het silhouet van de <b>vangpijpen</b> vanaf de rand zichtbaar is.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Excursie \u00b7 \U0001f3db\ufe0f Historisch vangsysteem \u00b7 \u26a0\ufe0f Beperkt toegankelijk'
}, {
 'tags': ['North Holland \u00b7 Uitgeest', 'Duck decoy \u00b7 historic trapping system with decoy wood', 'list 36 \u00b7 no. 113'],
 'loc': '\U0001f4cd Near Uitgeest \u00b7 Duck decoy with decoy wood \u00b7 Small',
 'desc': 'A <b>duck decoy</b> is one of the most ingenious trapping systems people ever devised: a pond with four curved, netted <b>pipes</b>, surrounded by a dense <b>decoy wood</b> that guarantees absolute quiet. The decoyman lured wild ducks with tame <b>call ducks</b> and with a small dog, the <b>kooikerhondje</b>, which showed itself along screens and vanished again \u2014 ducks follow such an apparition into the pipe out of curiosity. Around every decoy the <b>right of enclosure</b> also applied: within a radius of hundreds of metres nobody might make noise or build. That legal regime of silence makes old decoys ecological islands. <b>Buzzard, hobby, long-eared owl and woodcock</b> now breed here, and a rich spring flora grows in the decoy wood.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013May</b> (spring flora and breeding birds), Oct\u2013Mar (waterfowl on the decoy pond)<br>\n    <b>Best time of day:</b> Morning \u2014 quiet in and around the decoy wood.',
 'why': ['Pond with four curved <b>trapping pipes</b> and a dense decoy wood.',
         'Lured with <b>call ducks</b> and a <b>kooikerhondje</b>.',
         'The <b>right of enclosure</b> guaranteed silence all around.',
         'That silence regime makes old decoys <b>ecological islands</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f33c <b>Spring flora</b> in the decoy wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f985 <b>Buzzard and hobby</b> breed in the quiet.',
          '<span class="months">Oct\u2013Mar</span> \U0001f986 <b>Waterfowl</b> on the decoy pond.',
          '<span class="months">Nov\u2013Feb</span> \U0001f989 <b>Long-eared owls</b> in the dense scrub.'],
 'wild': ['\U0001f985 Buzzard \u00b7 Hobby \u00b7 \U0001f989 Long-eared owl', '\U0001f986 Mallard \u00b7 Teal \u00b7 Shoveler', '\U0001f426 Woodcock \u00b7 Great spotted woodpecker', '\U0001f33c Lesser celandine \u00b7 Cuckooflower \u00b7 Ground ivy', '\U0001f987 Bats above the pond'],
 'trail': ['Park at <b>Uitgeest</b>; decoys are often visitable <b>only by guided tour</b>.',
           'Respect the <b>quiet</b> \u2014 that is the essence of the place.',
           'See whether the silhouette of the <b>pipes</b> is visible from the edge.'],
 'foot': '\U0001f436 Dogs not allowed \u00b7 \U0001f4b6 Guided tour \u00b7 \U0001f3db\ufe0f Historic trapping system \u00b7 \u26a0\ufe0f Limited access'
}, card_class='card water'))

mk.insert(C, '1389')
mk.progress(1394)
mk.check()
