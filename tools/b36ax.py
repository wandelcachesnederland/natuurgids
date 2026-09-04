# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1525, 'Groenendaal', {
 'tags': ['Noord-Holland \u00b7 Heemstede', 'Wandelbos \u00b7 oudste openbare wandelbos van Nederland', 'list 36 \u00b7 no. 244'],
 'loc': '\U0001f4cd Heemstede, binnenduinrand \u00b7 Wandelbos \u00b7 Middelgroot',
 'desc': '<b>Groenendaal</b> is een van de oudste <b>openbaar toegankelijke wandelbossen</b> van Nederland. De buitenplaats werd in de achttiende eeuw aangelegd door de familie Hope, Amsterdamse bankiers, en al vroeg mochten wandelaars het park betreden \u2014 uitzonderlijk in een tijd waarin buitenplaatsen strikt privéterrein waren. In <b>1913</b> kocht de gemeente Heemstede het terrein op om het definitief voor het publiek te behouden, een van de eerste keren dat een Nederlandse gemeente natuur aankocht met recreatie als doel. Het bos heeft nu <b>oude beuken, vijvers en een hertenkamp</b>. In het oude hout broeden <b>bosuil, boomklever en grote bonte specht</b>, en in het voorjaar bloeit er rijke <b>stinzenflora</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013apr</b> (stinzenflora), apr\u2013jun (zang), okt\u2013nov (herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig, v\u00f3\u00f3r de wandelaars.',
 'why': ['Een van de oudste <b>openbare wandelbossen</b> van Nederland.',
         'Aangelegd door de Amsterdamse bankiersfamilie <b>Hope</b>.',
         'Al vroeg toegankelijk \u2014 uitzonderlijk voor een <b>buitenplaats</b>.',
         'In <b>1913</b> gekocht door de gemeente om het publiek te behouden.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzenflora</b> bloeit onder de oude beuken.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en bosuil</b> in de holtes.',
          '<span class="months">Mei\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> boven de vijvers.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> in de beukenlanen.'],
 'wild': ['\U0001f989 Bosuil \u00b7 \U0001f426 Boomklever \u00b7 Grote bonte specht', '\U0001f987 Vleermuizen in boomholtes', '\U0001f43f\ufe0f Eekhoorn \u00b7 \U0001f98c Damhert (hertenkamp)', '\U0001f33c Sneeuwklokje \u00b7 Bosanemoon \u00b7 Daslook', '\U0001f333 Oude beuk \u00b7 Eik \u00b7 Linde'],
 'trail': ['Parkeren in <b>Heemstede</b>; ruim padennet door het bos.',
           'Zoek de <b>oudste beuken</b> \u2014 sommige zijn ruim twee eeuwen oud.',
           'Maart voor de <b>stinzenflora</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f9d2 Gezinsvriendelijk \u00b7 \U0001f6b6 Veel paden'
}, {
 'tags': ['North Holland \u00b7 Heemstede', 'Amenity wood \u00b7 oldest public amenity wood in the Netherlands', 'list 36 \u00b7 no. 244'],
 'loc': '\U0001f4cd Heemstede, inner dune edge \u00b7 Amenity wood \u00b7 Medium-sized',
 'desc': '<b>Groenendaal</b> is one of the oldest <b>publicly accessible amenity woods</b> in the Netherlands. The estate was laid out in the eighteenth century by the Hope family, Amsterdam bankers, and walkers were allowed in early on \u2014 exceptional at a time when country estates were strictly private. In <b>1913</b> the municipality of Heemstede bought the grounds to preserve them permanently for the public, one of the first times a Dutch municipality acquired nature with recreation as the aim. The wood now has <b>old beeches, ponds and a deer park</b>. <b>Tawny owl, nuthatch and great spotted woodpecker</b> breed in the old timber, and rich <b>stinzen flora</b> blooms in spring.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Apr</b> (stinzen flora), Apr\u2013Jun (song), Oct\u2013Nov (autumn colour)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet, before the walkers.',
 'why': ['One of the oldest <b>public amenity woods</b> in the Netherlands.',
         'Laid out by the Amsterdam banking family <b>Hope</b>.',
         'Accessible early on \u2014 exceptional for a <b>country estate</b>.',
         'Bought by the municipality in <b>1913</b> to keep it public.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzen flora</b> flowers beneath the old beeches.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and tawny owl</b> in the cavities.',
          '<span class="months">May\u2013Aug</span> \U0001f987 <b>Bats</b> above the ponds.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> in the beech avenues.'],
 'wild': ['\U0001f989 Tawny owl \u00b7 \U0001f426 Nuthatch \u00b7 Great spotted woodpecker', '\U0001f987 Bats in tree cavities', '\U0001f43f\ufe0f Red squirrel \u00b7 \U0001f98c Fallow deer (deer park)', '\U0001f33c Snowdrop \u00b7 Wood anemone \u00b7 Ramsons', '\U0001f333 Old beech \u00b7 Oak \u00b7 Lime'],
 'trail': ['Park in <b>Heemstede</b>; an extensive path network.',
           'Find the <b>oldest beeches</b> \u2014 some are over two centuries old.',
           'March for the <b>stinzen flora</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f9d2 Family-friendly \u00b7 \U0001f6b6 Many paths'
}))

C.append(mk.card(1526, 'Eendenkooi Stokman', {
 'tags': ['Noord-Holland \u00b7 Haarlemmermeer', 'Eendenkooi \u00b7 historische vangstinstallatie in de polder', 'list 36 \u00b7 no. 245'],
 'loc': '\U0001f4cd Haarlemmermeer, bij Vijfhuizen \u00b7 Eendenkooi \u00b7 Zeer klein',
 'desc': 'Een <b>eendenkooi</b> is een van de vernuftigste vangstinstallaties die ooit in Nederland zijn ontwikkeld. Rond een vijver liggen gebogen, steeds smaller wordende <b>vangpijpen</b>, overspannen met netten en afgeschermd door rietschermen. De kooiker gebruikt een <b>kooikerhondje</b>, dat langs de schermen op en neer loopt; wilde eenden zijn zo nieuwsgierig naar dat kleine roofdiertje dat ze het achterna zwemmen de pijp in, waar ze niet meer terug kunnen. Tamme <b>staleenden</b> lokken hun soortgenoten. Rond een kooi geldt van oudsher het <b>recht van afpaling</b>: binnen een straal van honderden meters mag geen verstoring plaatsvinden \u2014 waardoor kooien eeuwenlang <b>rustgebieden</b> zijn geweest.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Okt\u2013mrt</b> (watervogels), apr\u2013jun (broedvogels in het kooibos)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 het rustigst rond de kooiplas.',
 'why': ['Een <b>eendenkooi</b> vangt eenden met pijpen, netten en rietschermen.',
         'Het <b>kooikerhondje</b> wekt de nieuwsgierigheid van wilde eenden.',
         'Tamme <b>staleenden</b> lokken hun soortgenoten de pijp in.',
         'Het <b>recht van afpaling</b> maakte kooien tot eeuwenoude rustgebieden.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Broedvogels</b> vestigen zich in het kooibos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Zangvogels</b> in het dichte struweel.',
          '<span class="months">Okt\u2013Dec</span> \U0001f986 <b>Trekkende eenden</b> op de kooiplas.',
          '<span class="months">Nov\u2013Mrt</span> \U0001f986 <b>Overwinterende watervogels</b> in de luwte.'],
 'wild': ['\U0001f986 Wilde eend \u00b7 Smient \u00b7 Wintertaling \u00b7 Krakeend', '\U0001f426 Zangvogels in het kooibos', '\U0001f989 Ransuil \u00b7 \U0001f985 Buizerd', '\U0001f98a Vos \u00b7 \U0001f43f\ufe0f Eekhoorn', '\U0001f333 Els \u00b7 Wilg \u00b7 Es \u00b7 Riet'],
 'trail': ['Parkeren bij <b>Vijfhuizen</b>; de kooi ligt in het polderland.',
           'Bekijk de <b>vangpijpen en rietschermen</b> van buitenaf.',
           'Kooien zijn meestal <b>alleen met gids</b> te bezoeken.'],
 'foot': '\U0001f436 Honden verboden \u00b7 \U0001f4b6 Alleen met excursie \u00b7 \u26a0\ufe0f Rustgebied \u00b7 \U0001f3fa Cultuurhistorisch monument'
}, {
 'tags': ['North Holland \u00b7 Haarlemmermeer', 'Duck decoy \u00b7 historic trapping installation in the polder', 'list 36 \u00b7 no. 245'],
 'loc': '\U0001f4cd Haarlemmermeer, near Vijfhuizen \u00b7 Duck decoy \u00b7 Very small',
 'desc': 'A <b>duck decoy</b> is among the most ingenious trapping installations ever developed in the Netherlands. Around a pond lie curved, progressively narrowing <b>pipes</b>, spanned with netting and screened by reed fences. The decoyman uses a <b>kooikerhondje</b>, a small dog that runs up and down along the screens; wild ducks are so curious about this little predator that they swim after it into the pipe, from which they cannot return. Tame <b>call ducks</b> lure their fellows in. Around a decoy the ancient <b>right of enclosure</b> applies: within a radius of hundreds of metres no disturbance is permitted \u2014 which has made decoys <b>refuges</b> for centuries.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Oct\u2013Mar</b> (waterfowl), Apr\u2013Jun (breeding birds in the decoy wood)<br>\n    <b>Best time of day:</b> Early morning \u2014 quietest around the decoy pool.',
 'why': ['A <b>duck decoy</b> traps ducks with pipes, nets and reed screens.',
         'The <b>kooikerhondje</b> arouses the curiosity of wild ducks.',
         'Tame <b>call ducks</b> lure their fellows into the pipe.',
         'The <b>right of enclosure</b> made decoys age-old refuges.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Breeding birds</b> settle in the decoy wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Songbirds</b> in the dense scrub.',
          '<span class="months">Oct\u2013Dec</span> \U0001f986 <b>Migrating ducks</b> on the decoy pool.',
          '<span class="months">Nov\u2013Mar</span> \U0001f986 <b>Wintering waterfowl</b> in the shelter.'],
 'wild': ['\U0001f986 Mallard \u00b7 Wigeon \u00b7 Teal \u00b7 Gadwall', '\U0001f426 Songbirds in the decoy wood', '\U0001f989 Long-eared owl \u00b7 \U0001f985 Buzzard', '\U0001f98a Fox \u00b7 \U0001f43f\ufe0f Red squirrel', '\U0001f333 Alder \u00b7 Willow \u00b7 Ash \u00b7 Reed'],
 'trail': ['Park at <b>Vijfhuizen</b>; the decoy lies in the polder land.',
           'View the <b>pipes and reed screens</b> from outside.',
           'Decoys can usually be visited <b>only with a guide</b>.'],
 'foot': '\U0001f436 No dogs \u00b7 \U0001f4b6 Guided visits only \u00b7 \u26a0\ufe0f Refuge area \u00b7 \U0001f3fa Cultural-historical monument'
}))

C.append(mk.card(1527, 'Meerbos', {
 'tags': ['Noord-Holland \u00b7 Haarlemmermeer', 'Polderbos \u00b7 jong bos in de droogmakerij', 'list 36 \u00b7 no. 246'],
 'loc': '\U0001f4cd Haarlemmermeer, bij Zwanenburg \u00b7 Polderbos \u00b7 Middelgroot',
 'desc': 'Het <b>Meerbos</b> ligt in de <b>Haarlemmermeerpolder</b>, en dat is landschappelijk gezien een bijzondere plek: hier lag tot <b>1852</b> een groot binnenmeer dat door stormen zo hard om zich heen vrat dat het een bedreiging vormde voor Amsterdam en Leiden. Het meer werd drooggemalen met drie stoomgemalen \u2014 destijds een technisch hoogstandje van wereldformaat. De bodem die vrijkwam ligt <b>vijf meter onder NAP</b> en bestaat uit zware, natte zeeklei. Bos aanplanten op zulke grond is lastig: de wortels verdragen de natte klei slecht. Het Meerbos bestaat dan ook grotendeels uit <b>populier, es en wilg</b>. Er broeden <b>havik, grote bonte specht en ijsvogel</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig langs de waterpartijen.',
 'why': ['De Haarlemmermeer was tot <b>1852</b> een gevaarlijk binnenmeer.',
         'Het meer bedreigde door stormen <b>Amsterdam en Leiden</b>.',
         'Drooggemalen met drie <b>stoomgemalen</b> \u2014 wereldwijd toonaangevend.',
         'De bodem ligt <b>vijf meter onder NAP</b> in zware zeeklei.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f985 <b>Havik</b> baltst boven het bos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Spechten en zangvogels</b> in het loofbos.',
          '<span class="months">Jun\u2013Aug</span> \U0001f426 <b>IJsvogel</b> bij de waterpartijen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de kleibodem.'],
 'wild': ['\U0001f985 Havik \u00b7 Buizerd \u00b7 Sperwer', '\U0001f426 Grote bonte specht \u00b7 IJsvogel \u00b7 Zwartkop', '\U0001f98c Ree \u00b7 \U0001f98a Vos \u00b7 Haas', '\U0001f9a0 Libellen boven het water', '\U0001f333 Populier \u00b7 Es \u00b7 Wilg \u00b7 Els'],
 'trail': ['Parkeren bij <b>Zwanenburg</b>; paden en fietsroutes door het bos.',
           'Let op de <b>diepte</b> \u2014 je loopt hier vijf meter onder zeeniveau.',
           'Vroege ochtend voor <b>havik en ijsvogel</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b4 Fietspaden \u00b7 \U0001f9d2 Gezinsvriendelijk'
}, {
 'tags': ['North Holland \u00b7 Haarlemmermeer', 'Polder wood \u00b7 young woodland in the drained lake', 'list 36 \u00b7 no. 246'],
 'loc': '\U0001f4cd Haarlemmermeer, near Zwanenburg \u00b7 Polder wood \u00b7 Medium-sized',
 'desc': 'The <b>Meerbos</b> lies in the <b>Haarlemmermeer polder</b>, a remarkable place in landscape terms: until <b>1852</b> a large inland lake lay here that storms made eat away at its shores so fiercely that it threatened Amsterdam and Leiden. The lake was pumped dry with three steam engines \u2014 at the time a technical feat of world class. The exposed floor lies <b>five metres below sea level</b> and consists of heavy, wet marine clay. Planting woodland on such ground is difficult: roots tolerate wet clay poorly. The Meerbos therefore consists largely of <b>poplar, ash and willow</b>. <b>Goshawk, great spotted woodpecker and kingfisher</b> breed.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet along the pools.',
 'why': ['The Haarlemmermeer was a dangerous inland lake until <b>1852</b>.',
         'Storm-driven erosion threatened <b>Amsterdam and Leiden</b>.',
         'Pumped dry with three <b>steam engines</b> \u2014 world-leading at the time.',
         'The floor lies <b>five metres below sea level</b> in heavy clay.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f985 <b>Goshawk</b> displays above the wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Woodpeckers and songbirds</b> in the broadleaf wood.',
          '<span class="months">Jun\u2013Aug</span> \U0001f426 <b>Kingfisher</b> at the pools.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the clay soil.'],
 'wild': ['\U0001f985 Goshawk \u00b7 Buzzard \u00b7 Sparrowhawk', '\U0001f426 Great spotted woodpecker \u00b7 Kingfisher \u00b7 Blackcap', '\U0001f98c Roe deer \u00b7 \U0001f98a Fox \u00b7 Brown hare', '\U0001f9a0 Dragonflies above the water', '\U0001f333 Poplar \u00b7 Ash \u00b7 Willow \u00b7 Alder'],
 'trail': ['Park at <b>Zwanenburg</b>; paths and cycle routes cross the wood.',
           'Note the <b>depth</b> \u2014 you walk five metres below sea level here.',
           'Early morning for <b>goshawk and kingfisher</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b4 Cycle paths \u00b7 \U0001f9d2 Family-friendly'
}))

C.append(mk.card(1528, 'Haarlemmermeerse Bos', {
 'tags': ['Noord-Holland \u00b7 Haarlemmermeer', 'Recreatiebos \u00b7 park met evenemententerrein bij Hoofddorp', 'list 36 \u00b7 no. 247'],
 'loc': '\U0001f4cd Hoofddorp, Haarlemmermeer \u00b7 Recreatiebos \u00b7 Middelgroot',
 'desc': 'Het <b>Haarlemmermeerse Bos</b> bij Hoofddorp is aangelegd in de jaren zeventig als groene long voor een polder die vrijwel geen bos had. De Haarlemmermeer werd na de droogmaking volledig als <b>landbouwgebied</b> ingericht: efficiënte rechthoekige kavels, brede wegen, geen bomen die schaduw zouden werpen op het gewas. Toen Hoofddorp en Schiphol explosief groeiden, ontbrak daardoor elk recreatief groen op korte afstand. De aanleg van dit bos was het antwoord. Inmiddels is het volwassen genoeg voor <b>holenbroeders en roofvogels</b>: <b>havik, grote bonte specht, boomklever</b>, en de waterpartijen trekken <b>ijsvogel, futen en libellen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang), sep\u2013nov (paddenstoelen en herfstkleur)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig v\u00f3\u00f3r de recreanten.',
 'why': ['De Haarlemmermeer werd volledig als <b>landbouwgebied</b> ingericht.',
         'Geen bomen \u2014 die zouden <b>schaduw op het gewas</b> werpen.',
         'Door de groei van Hoofddorp en Schiphol ontbrak <b>recreatief groen</b>.',
         'Dit bos was het antwoord, nu volwassen genoeg voor <b>holenbroeders</b>.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f985 <b>Havik</b> baltst boven de kruinen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en spechten</b> in het loofbos.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven de waterpartijen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de kleibodem.'],
 'wild': ['\U0001f985 Havik \u00b7 Buizerd \u00b7 Sperwer', '\U0001f426 Grote bonte specht \u00b7 Boomklever \u00b7 IJsvogel', '\U0001f986 Fuut \u00b7 Meerkoet \u00b7 Wilde eend', '\U0001f9a0 Libellen \u00b7 \U0001f438 Amfibieën', '\U0001f333 Populier \u00b7 Es \u00b7 Eik \u00b7 Wilg'],
 'trail': ['Parkeren in <b>Hoofddorp</b>; ruim padennet en fietsroutes.',
           'Zoek de <b>rustige randen</b> \u2014 het middengebied is druk.',
           'Vroege ochtend voor <b>havik en spechten</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f9d2 Gezinsvriendelijk \u00b7 \U0001f3aa Evenemententerrein'
}, {
 'tags': ['North Holland \u00b7 Haarlemmermeer', 'Recreational wood \u00b7 park with events ground near Hoofddorp', 'list 36 \u00b7 no. 247'],
 'loc': '\U0001f4cd Hoofddorp, Haarlemmermeer \u00b7 Recreational wood \u00b7 Medium-sized',
 'desc': 'The <b>Haarlemmermeerse Bos</b> near Hoofddorp was laid out in the 1970s as a green lung for a polder that had almost no woodland. After drainage the Haarlemmermeer was arranged entirely as <b>farmland</b>: efficient rectangular parcels, wide roads, no trees that would cast shade on the crops. When Hoofddorp and Schiphol grew explosively, all recreational greenery within reach was therefore lacking. Creating this wood was the answer. It is now mature enough for <b>hole-nesters and raptors</b>: <b>goshawk, great spotted woodpecker, nuthatch</b>, and the pools attract <b>kingfisher, grebes and dragonflies</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song), Sep\u2013Nov (fungi and autumn colour)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet before the visitors.',
 'why': ['The Haarlemmermeer was arranged entirely as <b>farmland</b>.',
         'No trees \u2014 they would cast <b>shade on the crops</b>.',
         'Growth of Hoofddorp and Schiphol left no <b>recreational greenery</b>.',
         'This wood was the answer, now mature enough for <b>hole-nesters</b>.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f985 <b>Goshawk</b> displays above the canopy.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and woodpeckers</b> in the broadleaf wood.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the pools.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the clay soil.'],
 'wild': ['\U0001f985 Goshawk \u00b7 Buzzard \u00b7 Sparrowhawk', '\U0001f426 Great spotted woodpecker \u00b7 Nuthatch \u00b7 Kingfisher', '\U0001f986 Great crested grebe \u00b7 Coot \u00b7 Mallard', '\U0001f9a0 Dragonflies \u00b7 \U0001f438 Amphibians', '\U0001f333 Poplar \u00b7 Ash \u00b7 Oak \u00b7 Willow'],
 'trail': ['Park in <b>Hoofddorp</b>; an extensive path and cycle network.',
           'Seek out the <b>quiet margins</b> \u2014 the centre is busy.',
           'Early morning for <b>goshawk and woodpeckers</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f9d2 Family-friendly \u00b7 \U0001f3aa Events ground'
}))

C.append(mk.card(1529, 'Eikenrode', {
 'tags': ['Noord-Holland \u00b7 Heemstede', 'Buitenplaatspark \u00b7 klein park met oude bomen', 'list 36 \u00b7 no. 248'],
 'loc': '\U0001f4cd Heemstede, binnenduinrand \u00b7 Buitenplaatspark \u00b7 Zeer klein',
 'desc': '<b>Eikenrode</b> is een kleine buitenplaats in Heemstede met een naam die uit twee oude landschapswoorden bestaat. <b>Rode</b> of <b>rade</b> betekent <b>gerooid land</b> \u2014 een plek waar bos is gekapt om er akkerland van te maken. Het komt terug in honderden Nederlandse plaatsnamen (Roden, Rijsbergen, Nieuwerode) en dateert uit de grote middeleeuwse ontginningsgolf tussen de tiende en dertiende eeuw, toen de bevolking groeide en overal bos werd omgezet in landbouwgrond. Dat uitgerekend een <b>eikenbos</b> hier ooit is gerooid en er later weer bomen zijn geplant, is een aardige kringloop. Het park heeft nu <b>oude bomen, een vijver en stinzenflora</b>, met <b>boomklever, specht en vleermuizen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mrt\u2013apr</b> (stinzenflora), apr\u2013jun (zang)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig in het kleine park.',
 'why': ['<b>Rode</b> betekent gerooid land \u2014 bos gekapt voor akkerland.',
         'Het woord zit in <b>honderden plaatsnamen</b>.',
         'Uit de middeleeuwse <b>ontginningsgolf</b> (10e\u201313e eeuw).',
         'Hier gerooid eikenbos, later weer <b>bomen geplant</b> \u2014 een kringloop.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzenflora</b> onder de oude bomen.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Boomklever en zwartkop</b> zingen.',
          '<span class="months">Mei\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> boven de vijver.',
          '<span class="months">Okt\u2013Nov</span> \U0001f342 <b>Herfstkleur</b> in de oude bomen.'],
 'wild': ['\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Zwartkop', '\U0001f987 Vleermuizen in boomholtes', '\U0001f43f\ufe0f Eekhoorn \u00b7 Egel', '\U0001f33c Sneeuwklokje \u00b7 Bosanemoon', '\U0001f333 Oude eik \u00b7 Beuk \u00b7 Linde'],
 'trail': ['Parkeren in <b>Heemstede</b>; korte paden door het park.',
           'Combineer met <b>Groenendaal</b> en het Enschedépark ernaast.',
           'Maart voor de <b>stinzenflora</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Kort rondje \u00b7 \u26a0\ufe0f Deels particulier'
}, {
 'tags': ['North Holland \u00b7 Heemstede', 'Estate park \u00b7 small park with old trees', 'list 36 \u00b7 no. 248'],
 'loc': '\U0001f4cd Heemstede, inner dune edge \u00b7 Estate park \u00b7 Very small',
 'desc': '<b>Eikenrode</b> is a small estate in Heemstede with a name made of two old landscape words. <b>Rode</b> or <b>rade</b> means <b>cleared land</b> \u2014 a place where woodland was felled to make arable. It recurs in hundreds of Dutch place names (Roden, Rijsbergen, Nieuwerode) and dates from the great medieval clearance wave between the tenth and thirteenth centuries, when population grew and woodland everywhere was converted to farmland. That an <b>oak wood</b> was once cleared here and trees were later planted again is a pleasing full circle. The park now has <b>old trees, a pond and stinzen flora</b>, with <b>nuthatch, woodpecker and bats</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Mar\u2013Apr</b> (stinzen flora), Apr\u2013Jun (song)<br>\n    <b>Best time of day:</b> Early morning \u2014 quiet in the small park.',
 'why': ['<b>Rode</b> means cleared land \u2014 woodland felled for arable.',
         'The word occurs in <b>hundreds of place names</b>.',
         'From the medieval <b>clearance wave</b> (10th\u201313th centuries).',
         'Oak wood cleared here, later <b>trees planted again</b> \u2014 full circle.'],
 'phen': ['<span class="months">Feb\u2013Apr</span> \U0001f33c <b>Stinzen flora</b> beneath the old trees.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Nuthatch and blackcap</b> sing.',
          '<span class="months">May\u2013Aug</span> \U0001f987 <b>Bats</b> above the pond.',
          '<span class="months">Oct\u2013Nov</span> \U0001f342 <b>Autumn colour</b> in the old trees.'],
 'wild': ['\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Blackcap', '\U0001f987 Bats in tree cavities', '\U0001f43f\ufe0f Red squirrel \u00b7 Hedgehog', '\U0001f33c Snowdrop \u00b7 Wood anemone', '\U0001f333 Old oak \u00b7 Beech \u00b7 Lime'],
 'trail': ['Park in <b>Heemstede</b>; short paths cross the park.',
           'Combine with <b>Groenendaal</b> and the Enschedépark next door.',
           'March for the <b>stinzen flora</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Short circuit \u00b7 \u26a0\ufe0f Partly private'
}))

mk.insert(C, '1524')
mk.progress(1529)
mk.check()
