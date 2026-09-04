# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1287, 'Steile Bank', {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Zandplaat \u00b7 hoogwatervluchtplaats in het IJsselmeer', 'list 36 \u00b7 no. 6'],
 'loc': '\U0001f4cd In het IJsselmeer bij Laaksum en Stavoren \u00b7 Onderwaterbank met plaat \u00b7 Alleen vanaf water of dijk zichtbaar',
 'desc': 'De <b>Steile Bank</b> is geen wandelgebied maar een <b>zandplaat</b> in het IJsselmeer, een paar honderd meter uit de Friese kust, en juist die onbereikbaarheid maakt hem zo belangrijk. De bank is een restant van de oude Zuiderzeebodem: een ondiepte waar de stroming zand heeft opgehoopt tot vlak onder \u2014 en bij lage waterstand net boven \u2014 het wateroppervlak. Voor vogels is dat de ideale combinatie van <b>ondiep foerageerwater</b> en een droogvallende plaat waar geen vos, marter of mens kan komen. Het resultaat is een van de belangrijkste <b>rustplaatsen</b> van het IJsselmeer. Hier verzamelen zich duizenden <b>aalscholvers, futen, visdieven en zwarte sterns</b>, en in de nazomer is de plaat een <b>slaapplaats</b> voor sterns die overdag kilometers verderop vissen. In de winter liggen er <b>brilduikers, nonnetjes en grote zaagbekken</b> op het diepere water eromheen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jul\u2013sep</b> (sternenconcentraties op de plaat), nov\u2013feb (zaagbekken en brilduikers)<br>\n    <b>Beste tijd van de dag:</b> Avond \u2014 dan komen de sterns van hun visgronden terug naar de slaapplaats.',
 'why': ['<b>Zandplaat</b> uit de oude Zuiderzeebodem, onbereikbaar voor predatoren.',
         'Een van de belangrijkste <b>rustplaatsen</b> van het IJsselmeer.',
         'Nazomerse <b>slaapplaats</b> voor visdief en zwarte stern.',
         'Winters water met <b>nonnetje en grote zaagbek</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Visdieven</b> foerageren rond de bank.',
          '<span class="months">Jul\u2013Sep</span> \U0001f426 <b>Zwarte sterns</b> verzamelen zich met duizenden.',
          '<span class="months">Sep\u2013Okt</span> \U0001f426 <b>Aalscholvers</b> drogen hun vleugels op de plaat.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Nonnetje en grote zaagbek</b> op het diepe water.'],
 'wild': ['\U0001f426 Visdief \u00b7 Zwarte stern', '\U0001f426 Aalscholver \u00b7 Fuut', '\U0001f986 Nonnetje \u00b7 Grote zaagbek \u00b7 Brilduiker', '\U0001f985 Zeearend (jagend)', '\U0001f41f Spiering \u00b7 Baars'],
 'trail': ['Te bekijken vanaf de <b>IJsselmeerdijk</b> bij Laaksum of Stavoren.',
           'Een <b>telescoop is onmisbaar</b> \u2014 de plaat ligt honderden meters uit de kust.',
           'De bank zelf is <b>niet toegankelijk</b>; ook varen erlangs verstoort.'],
 'foot': '\U0001f436 N.v.t. \u00b7 \U0001f4b6 Gratis vanaf de dijk \u00b7 \u26a0\ufe0f Niet benaderen per boot \u2014 rustgebied \u00b7 \U0001f52d Telescoop vereist'
}, {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Sandbank \u00b7 high-water roost in the IJsselmeer', 'list 36 \u00b7 no. 6'],
 'loc': '\U0001f4cd In the IJsselmeer near Laaksum and Stavoren \u00b7 Submerged bank with exposed flat \u00b7 Visible only from water or dike',
 'desc': 'The <b>Steile Bank</b> is not a walking area but a <b>sandbank</b> in the IJsselmeer, a few hundred metres off the Frisian coast, and it is precisely that inaccessibility that makes it so important. The bank is a remnant of the old Zuiderzee floor: a shallow where the current heaped up sand to just below \u2014 and at low water levels just above \u2014 the surface. For birds that is the ideal combination of <b>shallow feeding water</b> and an exposed flat no fox, marten or human can reach. The result is one of the most important <b>roosting sites</b> on the IJsselmeer. Thousands of <b>cormorants, great crested grebes, common terns and black terns</b> gather here, and in late summer the flat is a <b>roost</b> for terns that fish kilometres away by day. In winter <b>goldeneye, smew and goosander</b> lie on the deeper water around it.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jul\u2013Sep</b> (tern concentrations on the flat), Nov\u2013Feb (sawbills and goldeneye)<br>\n    <b>Best time of day:</b> Evening \u2014 when the terns return from their fishing grounds to the roost.',
 'why': ['<b>Sandbank</b> from the old Zuiderzee floor, unreachable by predators.',
         'One of the most important <b>roosting sites</b> on the IJsselmeer.',
         'Late-summer <b>roost</b> for common and black terns.',
         'Winter water with <b>smew and goosander</b>.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Common terns</b> feed around the bank.',
          '<span class="months">Jul\u2013Sep</span> \U0001f426 <b>Black terns</b> gather in their thousands.',
          '<span class="months">Sep\u2013Oct</span> \U0001f426 <b>Cormorants</b> dry their wings on the flat.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Smew and goosander</b> on the deep water.'],
 'wild': ['\U0001f426 Common tern \u00b7 Black tern', '\U0001f426 Cormorant \u00b7 Great crested grebe', '\U0001f986 Smew \u00b7 Goosander \u00b7 Goldeneye', '\U0001f985 White-tailed eagle (hunting)', '\U0001f41f Smelt \u00b7 Perch'],
 'trail': ['Viewable from the <b>IJsselmeer dike</b> at Laaksum or Stavoren.',
           'A <b>telescope is essential</b> \u2014 the flat lies hundreds of metres offshore.',
           'The bank itself is <b>closed</b>; even sailing past causes disturbance.'],
 'foot': '\U0001f436 N/A \u00b7 \U0001f4b6 Free from the dike \u00b7 \u26a0\ufe0f Do not approach by boat \u2014 refuge area \u00b7 \U0001f52d Telescope required'
}, card_class='card water',
   n2k='Natura 2000-gebied <b>IJsselmeer</b> \u2014 de Steile Bank is aangewezen als rust- en slaapplaats voor sterns, aalscholvers en overwinterende duikeenden.',
   n2k_en='Natura 2000 site <b>IJsselmeer</b> \u2014 the Steile Bank is designated as a resting and roosting site for terns, cormorants and wintering diving ducks.'))

C.append(mk.card(1288, 'Onderdijken', {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Moeras \u00b7 rietland en petgaten', 'list 36 \u00b7 no. 7'],
 'loc': '\U0001f4cd Bij Nijhuizum en Workum \u00b7 Rietmoeras met open water \u00b7 Middelgroot',
 'desc': 'De <b>Onderdijken</b> vormen een moerasgebied achter de oude zeedijk bij Workum, ontstaan op een plek waar de bodem zo laag lag dat ontwatering nooit rendabel was. Het is een klassiek <b>laagveenmoeras</b>: rietland, open water, wilgenstruweel en enkele graslandjes, in een mozaa\u00efek dat het hele jaar door natuurwaarde levert. Voor het beheer draait alles om het tegengaan van <b>successie</b>. Onbeheerd verandert rietland binnen twintig jaar in wilgenbos, en met dat bos verdwijnen de soorten waar het om gaat. Daarom wordt hier <b>gefaseerd gemaaid</b>: elk jaar een ander deel, zodat er altijd overjarig riet blijft staan \u2014 en juist d\u00e1\u00e1rin broeden <b>roerdomp, snor, grote karekiet en baardman</b>. In het open water leven <b>snoek en grote modderkruiper</b>, en de <b>otter</b> is er sinds enkele jaren weer gesignaleerd. In de winter jaagt hier de <b>zeearend</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jul</b> (rietvogels, roerdomp hoorbaar), nov\u2013feb (zeearend en watervogels)<br>\n    <b>Beste tijd van de dag:</b> Zonsopkomst \u2014 de roerdomp roept vooral in de vroege ochtend.',
 'why': ['Klassiek <b>laagveenmoeras</b> met riet, open water en struweel.',
         '<b>Gefaseerd maaien</b> houdt overjarig riet in stand \u2014 essentieel voor moerasvogels.',
         'Broedplaats van <b>roerdomp, grote karekiet en baardman</b>.',
         'Terugkeer van de <b>otter</b>; winters jachtgebied van de zeearend.'],
 'phen': ['<span class="months">Mrt\u2013Mei</span> \U0001f4a8 <b>Roerdomp</b> \u2014 de hoempende roep draagt kilometers ver.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Snor en grote karekiet</b> in het overjarig riet.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven de petgaten.',
          '<span class="months">Nov\u2013Feb</span> \U0001f985 <b>Zeearend</b> boven het moeras.'],
 'wild': ['\U0001f426 Roerdomp \u00b7 Grote karekiet \u00b7 Snor', '\U0001f426 Baardman \u00b7 Bruine kiekendief', '\U0001f9a6 Otter', '\U0001f41f Snoek \u00b7 Grote modderkruiper', '\U0001f33f Riet \u00b7 Lisdodde \u00b7 Wilgenstruweel'],
 'trail': ['Parkeren bij <b>Nijhuizum</b>; paden langs de rand van het moeras.',
           'Het <b>kerngebied is gesloten</b> \u2014 rust is voor deze soorten essentieel.',
           'Luister vooral: de <b>roerdomp</b> hoor je eerder dan je hem ziet.'],
 'foot': '\U0001f436 Honden niet toegestaan \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kerngebied gesloten in broedseizoen \u00b7 \U0001f9ed It Fryske Gea'
}, {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Marsh \u00b7 reedland and peat cuttings', 'list 36 \u00b7 no. 7'],
 'loc': '\U0001f4cd Near Nijhuizum and Workum \u00b7 Reed marsh with open water \u00b7 Medium-sized',
 'desc': 'The <b>Onderdijken</b> form a marsh behind the old sea dike at Workum, arisen where the ground lay so low that drainage was never worthwhile. It is a classic <b>fen marsh</b>: reedland, open water, willow scrub and a few small meadows, in a mosaic that yields natural value all year round. For management, everything turns on countering <b>succession</b>. Left alone, reedland becomes willow carr within twenty years, and with that woodland the species that matter disappear. So the site is <b>mown in phases</b>: a different section each year, so that old standing reed always remains \u2014 and it is precisely there that <b>bittern, Savi\u2019s warbler, great reed warbler and bearded reedling</b> breed. In the open water live <b>pike and spined loach</b>, and the <b>otter</b> has been recorded again in recent years. In winter the <b>white-tailed eagle</b> hunts here.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jul</b> (reed birds, bittern audible), Nov\u2013Feb (white-tailed eagle and waterfowl)<br>\n    <b>Best time of day:</b> Sunrise \u2014 the bittern calls mainly in the early morning.',
 'why': ['Classic <b>fen marsh</b> with reed, open water and scrub.',
         '<b>Phased mowing</b> maintains old standing reed \u2014 essential for marsh birds.',
         'Breeding site for <b>bittern, great reed warbler and bearded reedling</b>.',
         'Return of the <b>otter</b>; winter hunting ground of the white-tailed eagle.'],
 'phen': ['<span class="months">Mar\u2013May</span> \U0001f4a8 <b>Bittern</b> \u2014 the booming call carries for kilometres.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Savi\u2019s warbler and great reed warbler</b> in the old reed.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the peat cuttings.',
          '<span class="months">Nov\u2013Feb</span> \U0001f985 <b>White-tailed eagle</b> above the marsh.'],
 'wild': ['\U0001f426 Bittern \u00b7 Great reed warbler \u00b7 Savi\u2019s warbler', '\U0001f426 Bearded reedling \u00b7 Marsh harrier', '\U0001f9a6 Otter', '\U0001f41f Pike \u00b7 Spined loach', '\U0001f33f Reed \u00b7 Bulrush \u00b7 Willow scrub'],
 'trail': ['Park at <b>Nijhuizum</b>; paths along the edge of the marsh.',
           'The <b>core area is closed</b> \u2014 quiet is essential for these species.',
           'Above all, listen: you hear the <b>bittern</b> long before you see it.'],
 'foot': '\U0001f436 No dogs \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Core area closed in the breeding season \u00b7 \U0001f9ed It Fryske Gea'
}, card_class='card water'))

C.append(mk.card(1289, 'De Weelen', {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Moeras en petgaten \u00b7 verlandingsreeks', 'list 36 \u00b7 no. 8'],
 'loc': '\U0001f4cd Bij Gaastmeer en Oudega \u00b7 Petgaten en rietland \u00b7 Middelgroot',
 'desc': '<b>De Weelen</b> is een oud <b>vervenersgebied</b> in het merengebied van Zuidwest-Friesland: hier is eeuwenlang veen weggebaggerd, waardoor een patroon van <b>petgaten</b> (uitgebaggerde stroken water) en <b>legakkers</b> (smalle ruggen waarop de turf te drogen lag) is ontstaan. Dat patroon is het skelet van het gebied en bepaalt tot vandaag wat er groeit. In de petgaten voltrekt zich de <b>verlanding</b> in alle stadia tegelijk: van open water via drijvende <b>krabbenscheervelden</b> en veenmosrietland tot moerasbos op de oudste legakkers. Wie hier vaart ziet dus een levend leerboek. De <b>krabbenscheer</b> is de sleutelsoort \u2014 een drijvende waterplant die alleen in schoon, mineraalrijk water groeit en die de enige eiafzetplaats vormt van de zeldzame <b>groene glazenmaker</b>, een libel die zonder deze plant simpelweg verdwijnt. Verder broeden er <b>purperreiger, roerdomp en zwarte stern</b>, die laatste op vlotjes tussen de krabbenscheer.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (krabbenscheer, groene glazenmaker en zwarte stern), apr\u2013jun (moerasvogels)<br>\n    <b>Beste tijd van de dag:</b> Zonnige middag \u2014 de groene glazenmaker vliegt bij warm, windstil weer.',
 'why': ['<b>Petgaten en legakkers</b> als skelet van een oud vervenersgebied.',
         'Alle stadia van <b>verlanding</b> naast elkaar zichtbaar.',
         '<b>Krabbenscheer</b> als sleutelsoort voor de groene glazenmaker.',
         '<b>Zwarte sterns</b> broeden op vlotjes tussen de waterplanten.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33f <b>Krabbenscheer</b> komt boven water drijven.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Groene glazenmaker</b> zet eieren af in de krabbenscheer.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Zwarte stern</b> broedt op drijvende vlotjes.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Purperreiger</b> foerageert in de petgaten.'],
 'wild': ['\U0001f9a0 Groene glazenmaker', '\U0001f426 Zwarte stern \u00b7 Purperreiger', '\U0001f426 Roerdomp \u00b7 Snor', '\U0001f33f Krabbenscheer \u00b7 Veenmosrietland', '\U0001f9a6 Otter'],
 'trail': ['Startpunt bij <b>Gaastmeer</b> of <b>Oudega</b>.',
           'Het gebied is het best te beleven <b>per kano of fluisterboot</b>.',
           'Ook enkele <b>wandelpaden</b> langs de rand met uitzicht op de petgaten.'],
 'foot': '\U0001f436 Honden aan de lijn op de randpaden \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Legakkers kwetsbaar \u2014 niet aanmeren \u00b7 \U0001f6f6 Kano aanbevolen'
}, {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Marsh and peat cuttings \u00b7 terrestrialisation sequence', 'list 36 \u00b7 no. 8'],
 'loc': '\U0001f4cd Near Gaastmeer and Oudega \u00b7 Peat cuttings and reedland \u00b7 Medium-sized',
 'desc': '<b>De Weelen</b> is an old <b>peat-digging area</b> in the lake district of south-west Friesland: for centuries peat was dredged away here, creating a pattern of <b>petgaten</b> (dredged strips of water) and <b>legakkers</b> (narrow ridges on which the peat was laid to dry). That pattern is the skeleton of the area and still determines what grows there. In the cuttings <b>terrestrialisation</b> proceeds in every stage at once: from open water through floating <b>water-soldier beds</b> and sphagnum reedland to swamp woodland on the oldest ridges. Anyone boating here sees a living textbook. <b>Water soldier</b> is the key species \u2014 a floating plant that grows only in clean, mineral-rich water and forms the sole egg-laying site of the rare <b>green hawker</b>, a dragonfly that simply disappears without it. <b>Purple heron, bittern and black tern</b> also breed here, the last on small rafts among the water soldier.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (water soldier, green hawker and black tern), Apr\u2013Jun (marsh birds)<br>\n    <b>Best time of day:</b> Sunny afternoon \u2014 the green hawker flies in warm, windless weather.',
 'why': ['<b>Peat cuttings and drying ridges</b> as the skeleton of an old peat-digging area.',
         'All stages of <b>terrestrialisation</b> visible side by side.',
         '<b>Water soldier</b> as the key species for the green hawker.',
         '<b>Black terns</b> breed on rafts among the water plants.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33f <b>Water soldier</b> rises to float at the surface.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Green hawker</b> lays its eggs in the water soldier.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Black tern</b> breeds on floating rafts.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Purple heron</b> feeds in the cuttings.'],
 'wild': ['\U0001f9a0 Green hawker', '\U0001f426 Black tern \u00b7 Purple heron', '\U0001f426 Bittern \u00b7 Savi\u2019s warbler', '\U0001f33f Water soldier \u00b7 Sphagnum reedland', '\U0001f9a6 Otter'],
 'trail': ['Starting point at <b>Gaastmeer</b> or <b>Oudega</b>.',
           'The area is best experienced <b>by canoe or electric boat</b>.',
           'There are also a few <b>footpaths</b> along the edge overlooking the cuttings.'],
 'foot': '\U0001f436 Dogs on lead on the edge paths \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Drying ridges fragile \u2014 do not moor \u00b7 \U0001f6f6 Canoe recommended'
}, card_class='card water'))

C.append(mk.card(1290, 'De Ven', {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Meer met rietkragen \u00b7 vogelrijk water', 'list 36 \u00b7 no. 9'],
 'loc': '\U0001f4cd Bij Oudega en Heeg \u00b7 Ondiep meer met moeraszomen \u00b7 Middelgroot',
 'desc': '<b>De Ven</b> is een van de kleinere Friese meren, maar ecologisch een van de interessantere, omdat het ondiep is gebleven en brede <b>moeraszomen</b> heeft behouden. De meeste Friese meren zijn door recreatievaart, oeverbeschoeiing en golfslag hun rietkragen kwijtgeraakt; hier niet. Het water is er <b>helder genoeg</b> voor uitgestrekte velden <b>fonteinkruiden en kranswieren</b> \u2014 ondergedoken waterplanten die als graadmeter gelden, want ze verdwijnen zodra het water te troebel of te voedselrijk wordt. Die plantenvelden zijn het fundament: ze leveren zuurstof, dekking voor jonge vis en voedsel voor duikeenden. \u2019s Winters foerageren er honderden <b>tafeleenden, kuifeenden en meerkoeten</b> op de kranswiervelden. In de rietkragen broeden <b>rietzanger, snor en bruine kiekendief</b>, en op het open water jagen in de zomer <b>zwarte sterns</b> die in de nabijgelegen petgaten nestelen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013aug</b> (waterplanten en sterns), nov\u2013feb (duikeenden op de kranswiervelden)<br>\n    <b>Beste tijd van de dag:</b> Ochtend bij windstil weer \u2014 dan zijn de waterplanten door het heldere water te zien.',
 'why': ['<b>Ondiep gebleven</b> meer met brede, intacte rietkragen.',
         'Uitgestrekte velden <b>fonteinkruiden en kranswieren</b> als kwaliteitsindicator.',
         'Winterse concentraties <b>tafel- en kuifeenden</b> op de waterplanten.',
         'Zomerse jachtvluchten van <b>zwarte sterns</b>.'],
 'phen': ['<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Zwarte sterns</b> jagen laag over het water.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Kranswier- en fonteinkruidvelden</b> op hun grootst.',
          '<span class="months">Apr\u2013Jul</span> \U0001f985 <b>Bruine kiekendief</b> boven de rietkragen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Tafeleend en kuifeend</b> in grote groepen.'],
 'wild': ['\U0001f426 Zwarte stern \u00b7 Visdief', '\U0001f986 Tafeleend \u00b7 Kuifeend \u00b7 Meerkoet', '\U0001f985 Bruine kiekendief', '\U0001f426 Rietzanger \u00b7 Snor', '\U0001f33f Kranswieren \u00b7 Fonteinkruiden'],
 'trail': ['Bereikbaar vanaf <b>Oudega</b> of <b>Heeg</b>; kijkpunten aan de oever.',
           'Het meer is onderdeel van het <b>Friese merennetwerk</b> \u2014 goed per boot.',
           'Blijf met de boot <b>uit de rietkragen</b>; daar zit alles.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Recreatievaart in de zomer \u2014 vaar rustig langs het riet \u00b7 \U0001f6f6 Per boot of vanaf de oever'
}, {
 'tags': ['Friesland \u00b7 S\u00fbdwest-Frysl\u00e2n', 'Lake with reed fringes \u00b7 bird-rich water', 'list 36 \u00b7 no. 9'],
 'loc': '\U0001f4cd Near Oudega and Heeg \u00b7 Shallow lake with marsh fringes \u00b7 Medium-sized',
 'desc': '<b>De Ven</b> is one of the smaller Frisian lakes, but ecologically one of the more interesting, because it has stayed shallow and retained broad <b>marsh fringes</b>. Most Frisian lakes have lost their reed edges to recreational boating, bank revetment and wave action; not this one. The water is <b>clear enough</b> for extensive beds of <b>pondweeds and stoneworts</b> \u2014 submerged plants that serve as a yardstick, since they vanish as soon as the water becomes too turbid or too nutrient-rich. Those plant beds are the foundation: they supply oxygen, cover for young fish and food for diving ducks. In winter hundreds of <b>pochard, tufted duck and coot</b> feed on the stonewort beds. In the reed fringes <b>sedge warbler, Savi\u2019s warbler and marsh harrier</b> breed, and in summer <b>black terns</b> nesting in the nearby peat cuttings hunt over the open water.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Aug</b> (water plants and terns), Nov\u2013Feb (diving ducks on the stonewort beds)<br>\n    <b>Best time of day:</b> Morning in calm weather \u2014 the water plants are then visible through the clear water.',
 'why': ['A lake that has <b>stayed shallow</b>, with broad intact reed fringes.',
         'Extensive beds of <b>pondweed and stonewort</b> as a quality indicator.',
         'Winter concentrations of <b>pochard and tufted duck</b> on the plant beds.',
         'Summer hunting flights of <b>black terns</b>.'],
 'phen': ['<span class="months">May\u2013Jul</span> \U0001f426 <b>Black terns</b> hunt low over the water.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33f <b>Stonewort and pondweed beds</b> at their largest.',
          '<span class="months">Apr\u2013Jul</span> \U0001f985 <b>Marsh harrier</b> above the reed fringes.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Pochard and tufted duck</b> in large flocks.'],
 'wild': ['\U0001f426 Black tern \u00b7 Common tern', '\U0001f986 Pochard \u00b7 Tufted duck \u00b7 Coot', '\U0001f985 Marsh harrier', '\U0001f426 Sedge warbler \u00b7 Savi\u2019s warbler', '\U0001f33f Stoneworts \u00b7 Pondweeds'],
 'trail': ['Reachable from <b>Oudega</b> or <b>Heeg</b>; viewpoints on the shore.',
           'The lake is part of the <b>Frisian lakes network</b> \u2014 good by boat.',
           'Keep your boat <b>out of the reed fringes</b>; that is where everything is.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Recreational boating in summer \u2014 pass the reeds slowly \u00b7 \U0001f6f6 By boat or from the shore'
}, card_class='card water'))

mk.insert(C, '1286')
mk.progress(1290)
mk.check()
