# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1440, "'t Zand A72", {
 'tags': ['Noord-Holland \u00b7 Schagen', 'Bermnatuur \u00b7 schrale wegbermen langs de snelweg', 'list 36 \u00b7 no. 159'],
 'loc': "\U0001f4cd Bij 't Zand, langs de A72/N245 \u00b7 Wegbermen \u00b7 Klein",
 'desc': 'Bij <b>\u2019t Zand</b> liggen langs de weg brede bermen die laten zien hoeveel natuurwaarde er in infrastructuur kan zitten. Wegbermen beslaan in Nederland samen tienduizenden hectaren, en omdat ze <b>nooit worden bemest</b> en meestal twee keer per jaar gemaaid met afvoer van het maaisel, ontwikkelen ze precies het schrale, kruidenrijke milieu dat in de landbouw verdwenen is. Ze werken bovendien als <b>lineaire corridor</b>: soorten kunnen er langs migreren door een verder ongastvrij landschap. De naam <b>\u2019t Zand</b> verwijst naar de zandige ondergrond, opgespoten of van nature aanwezig, en dat maakt de bermen hier extra schraal. Er groeien <b>knoopkruid, wilde peen en duizendblad</b>, en er vliegen veel <b>wilde bijen, zweefvliegen en vlinders</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (bermbloei en insecten), mei\u2013jun (eerste bloeigolf)<br>\n    <b>Beste tijd van de dag:</b> Warme middag \u2014 insecten zijn dan het talrijkst.',
 'why': ['Wegbermen beslaan in Nederland samen <b>tienduizenden hectaren</b>.',
         'Ze worden <b>nooit bemest</b> en het maaisel wordt afgevoerd.',
         'Daardoor ontstaat het <b>schrale milieu</b> dat elders verdween.',
         'Ze werken als <b>lineaire corridor</b> door onherbergzaam land.'],
 'phen': ['<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Eerste bloeigolf</b> met margriet en boterbloem.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Knoopkruid en wilde peen</b> in volle bloei.',
          '<span class="months">Jul\u2013Aug</span> \U0001f41d <b>Wilde bijen en zweefvliegen</b> op hun talrijkst.',
          '<span class="months">Aug\u2013Sep</span> \U0001f997 <b>Sprinkhanen</b> zingen in de bermen.'],
 'wild': ['\U0001f33c Knoopkruid \u00b7 Wilde peen \u00b7 Duizendblad \u00b7 Margriet', '\U0001f41d Wilde bijen \u00b7 Zweefvliegen \u00b7 Graafwespen', '\U0001f98b Icarusblauwtje \u00b7 Bruin zandoogje', '\U0001f997 Sprinkhanen \u00b7 Krekels', '\U0001f426 Graspieper \u00b7 Kneu \u00b7 Torenvalk'],
 'trail': ['Parkeren bij <b>\u2019t Zand</b>; volg de fiets- en wandelpaden langs de weg.',
           'Blijf uit de <b>rijbaan</b> \u2014 kijk vanaf het fietspad.',
           'Juli is de <b>beste maand</b> voor bloei en insecten.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Let op verkeer \u00b7 \U0001f6b4 Fietspad langs de bermen'
}, {
 'tags': ['North Holland \u00b7 Schagen', 'Verge nature \u00b7 poor roadside verges along the motorway', 'list 36 \u00b7 no. 159'],
 'loc': "\U0001f4cd Near 't Zand, along the A72/N245 \u00b7 Road verges \u00b7 Small",
 'desc': 'At <b>\u2019t Zand</b> broad verges run alongside the road, showing how much natural value infrastructure can hold. Road verges together cover tens of thousands of hectares in the Netherlands, and because they are <b>never fertilised</b> and usually mown twice a year with the cuttings removed, they develop precisely the poor, herb-rich environment that has vanished from farmland. They also work as a <b>linear corridor</b>: species can migrate along them through an otherwise inhospitable landscape. The name <b>\u2019t Zand</b> refers to the sandy subsoil, raised or naturally present, which makes the verges here especially poor. <b>Knapweed, wild carrot and yarrow</b> grow here, and many <b>wild bees, hoverflies and butterflies</b> fly.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (verge flowering and insects), May\u2013Jun (first flush)<br>\n    <b>Best time of day:</b> Warm afternoon \u2014 insects are then most numerous.',
 'why': ['Road verges together cover <b>tens of thousands of hectares</b> nationally.',
         'They are <b>never fertilised</b> and the cuttings are removed.',
         'This creates the <b>poor environment</b> that vanished elsewhere.',
         'They work as a <b>linear corridor</b> through inhospitable land.'],
 'phen': ['<span class="months">May\u2013Jun</span> \U0001f33c <b>First flush</b> with oxeye daisy and buttercup.',
          '<span class="months">Jun\u2013Aug</span> \U0001f33c <b>Knapweed and wild carrot</b> in full flower.',
          '<span class="months">Jul\u2013Aug</span> \U0001f41d <b>Wild bees and hoverflies</b> at their most numerous.',
          '<span class="months">Aug\u2013Sep</span> \U0001f997 <b>Grasshoppers</b> sing in the verges.'],
 'wild': ['\U0001f33c Knapweed \u00b7 Wild carrot \u00b7 Yarrow \u00b7 Oxeye daisy', '\U0001f41d Wild bees \u00b7 Hoverflies \u00b7 Digger wasps', '\U0001f98b Common blue \u00b7 Meadow brown', '\U0001f997 Grasshoppers \u00b7 Crickets', '\U0001f426 Meadow pipit \u00b7 Linnet \u00b7 Kestrel'],
 'trail': ['Park at <b>\u2019t Zand</b>; follow the cycle and foot paths beside the road.',
           'Stay off the <b>carriageway</b> \u2014 watch from the cycle path.',
           'July is the <b>best month</b> for flowering and insects.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Mind the traffic \u00b7 \U0001f6b4 Cycle path along the verges'
}))

C.append(mk.card(1441, 'Zuigerplasbos', {
 'tags': ['Flevoland \u00b7 Lelystad', 'Stadsbos \u00b7 bos rond een zandwinplas', 'list 36 \u00b7 no. 160'],
 'loc': '\U0001f4cd Noordrand van Lelystad \u00b7 Bos met plas \u00b7 Middelgroot',
 'desc': 'Het <b>Zuigerplasbos</b> dankt zijn naam aan de <b>zuigerplas</b> in het midden: een waterplas die ontstond doordat er met een <b>zandzuiger</b> zand werd gewonnen voor de bouw van Lelystad. Dat is typerend voor heel Flevoland \u2014 de polder viel in 1957 droog, en alles wat je er ziet is jonger dan dat. Een bos van nog geen zeventig jaar oud zou je ecologisch weinig verwachten, maar de <b>jonge zeeklei</b> is uitzonderlijk vruchtbaar, waardoor bomen hier twee keer zo snel groeien als op de zandgronden. Het resultaat is een verrassend volgroeid bos met een dichte ondergroei. Er broeden <b>havik, buizerd, boomklever en grote bonte specht</b>, en op de plas zitten <b>fuut, aalscholver en duikeenden</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang), nov\u2013feb (duikeenden op de plas)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 rustig water en actieve vogels.',
 'why': ['Genoemd naar de plas die ontstond door <b>zandzuigen</b> voor Lelystad.',
         'Flevoland viel in <b>1957</b> droog \u2014 alles is jonger dan dat.',
         'Op de vruchtbare <b>jonge zeeklei</b> groeien bomen twee keer zo snel.',
         'Verrassend volgroeid bos van nog geen zeventig jaar oud.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f985 <b>Havik</b> baltst boven het bos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f3b6 <b>Voorjaarskoor</b> in de dichte ondergroei.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> op de vruchtbare bodem.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Duikeenden</b> op de zuigerplas.'],
 'wild': ['\U0001f985 Havik \u00b7 Buizerd \u00b7 \U0001f989 Ransuil', '\U0001f426 Boomklever \u00b7 Grote bonte specht \u00b7 Zwartkop', '\U0001f986 Fuut \u00b7 Aalscholver \u00b7 Kuifeend \u00b7 Tafeleend', '\U0001f98c Ree \u00b7 Vos \u00b7 Haas', '\U0001f333 Es \u00b7 Populier \u00b7 Eik \u00b7 Wilg'],
 'trail': ['Parkeren aan de <b>noordrand van Lelystad</b>; rondje om de plas.',
           'Bedenk dat dit hele landschap <b>jonger is dan 1957</b>.',
           'Winter voor de <b>duikeenden</b>, voorjaar voor de zang.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Goed padennet \u00b7 \U0001f3ca Recreatieplas'
}, {
 'tags': ['Flevoland \u00b7 Lelystad', 'City wood \u00b7 woodland around a sand-extraction lake', 'list 36 \u00b7 no. 160'],
 'loc': '\U0001f4cd Northern edge of Lelystad \u00b7 Woodland with lake \u00b7 Medium-sized',
 'desc': 'The <b>Zuigerplasbos</b> owes its name to the <b>suction-dredger lake</b> at its centre: a pool created when sand was extracted with a <b>suction dredger</b> for building Lelystad. That is typical of the whole of Flevoland \u2014 the polder fell dry in 1957, and everything you see there is younger than that. You would expect little ecologically from a wood barely seventy years old, but the <b>young marine clay</b> is exceptionally fertile, so trees grow twice as fast here as on sandy soils. The result is a surprisingly mature wood with a dense understorey. <b>Goshawk, buzzard, nuthatch and great spotted woodpecker</b> breed, and <b>great crested grebe, cormorant and diving ducks</b> use the lake.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song), Nov\u2013Feb (diving ducks on the lake)<br>\n    <b>Best time of day:</b> Early morning \u2014 calm water and active birds.',
 'why': ['Named after the lake created by <b>suction dredging</b> for Lelystad.',
         'Flevoland fell dry in <b>1957</b> \u2014 everything is younger than that.',
         'On the fertile <b>young marine clay</b> trees grow twice as fast.',
         'A surprisingly mature wood barely seventy years old.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f985 <b>Goshawk</b> displays above the wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f3b6 <b>Spring chorus</b> in the dense understorey.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> on the fertile soil.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Diving ducks</b> on the lake.'],
 'wild': ['\U0001f985 Goshawk \u00b7 Buzzard \u00b7 \U0001f989 Long-eared owl', '\U0001f426 Nuthatch \u00b7 Great spotted woodpecker \u00b7 Blackcap', '\U0001f986 Great crested grebe \u00b7 Cormorant \u00b7 Tufted duck \u00b7 Pochard', '\U0001f98c Roe deer \u00b7 Fox \u00b7 Brown hare', '\U0001f333 Ash \u00b7 Poplar \u00b7 Oak \u00b7 Willow'],
 'trail': ['Park on the <b>northern edge of Lelystad</b>; a circuit runs round the lake.',
           'Remember this entire landscape is <b>younger than 1957</b>.',
           'Winter for the <b>diving ducks</b>, spring for the song.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Good path network \u00b7 \U0001f3ca Recreation lake'
}, card_class='card water'))

C.append(mk.card(1442, 'Visvijverbos', {
 'tags': ['Flevoland \u00b7 Lelystad', 'Stadsbos \u00b7 bos met vijvers op jonge zeeklei', 'list 36 \u00b7 no. 161'],
 'loc': '\U0001f4cd Bij Lelystad \u00b7 Bos met vijvers \u00b7 Klein',
 'desc': 'Het <b>Visvijverbos</b> is een van de kleinere bossen rond Lelystad, aangelegd met een reeks <b>vijvers</b> die oorspronkelijk voor de hengelsport waren bedoeld. Wat begon als recreatievoorziening is ecologisch interessanter geworden dan bedoeld: de vijvers hebben inmiddels begroeide oevers met riet en waterplanten, en vormen daarmee een <b>waterrijk element</b> in een polder waar bijna al het water in rechte tochten stroomt. De overgang van bos naar water is precies wat veel soorten nodig hebben \u2014 <b>ijsvogels</b> hebben oevers met wortels nodig om in te graven, <b>libellen</b> vragen om beschutte, zonnige waterkanten. Er broeden ook <b>grote bonte specht, boomkruiper en waterhoen</b>, en in de winter zitten er <b>dodaars en kuifeend</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Jun\u2013aug</b> (libellen bij de vijvers), apr\u2013jun (zang en broedvogels)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 ijsvogels jagen boven het stille water.',
 'why': ['Vijvers oorspronkelijk aangelegd voor de <b>hengelsport</b>.',
         'Nu <b>waterrijk element</b> in een polder vol rechte tochten.',
         'De <b>overgang bos\u2013water</b> is wat veel soorten nodig hebben.',
         '<b>IJsvogels</b> vragen oevers met wortels om in te graven.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> jaagt boven de vijvers.',
          '<span class="months">Mei\u2013Jul</span> \U0001f3b6 <b>Zang</b> van bosvogels rond het water.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Libellen</b> boven de begroeide oevers.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Dodaars en kuifeend</b> op de vijvers.'],
 'wild': ['\U0001f426 IJsvogel \u00b7 Grote bonte specht \u00b7 Boomkruiper', '\U0001f986 Dodaars \u00b7 Kuifeend \u00b7 Waterhoen', '\U0001f9a0 Libellen \u00b7 Juffers', '\U0001f438 Kikkers \u00b7 Watersalamander', '\U0001f333 Es \u00b7 Els \u00b7 Wilg \u00b7 Populier'],
 'trail': ['Parkeren bij <b>Lelystad</b>; paden rond de vijvers.',
           'Wees <b>stil bij het water</b> \u2014 dat verhoogt de kans op de ijsvogel.',
           'Juli voor de <b>libellen</b> langs de oevers.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3a3 Hengelsport \u00b7 \U0001f6b6 Kort rondje'
}, {
 'tags': ['Flevoland \u00b7 Lelystad', 'City wood \u00b7 woodland with ponds on young marine clay', 'list 36 \u00b7 no. 161'],
 'loc': '\U0001f4cd Near Lelystad \u00b7 Woodland with ponds \u00b7 Small',
 'desc': 'The <b>Visvijverbos</b> is one of the smaller woods around Lelystad, laid out with a series of <b>ponds</b> originally intended for angling. What began as a recreational facility has become ecologically more interesting than intended: the ponds now have vegetated banks with reed and water plants, forming a <b>water-rich element</b> in a polder where almost all water flows in straight channels. The transition from wood to water is exactly what many species need \u2014 <b>kingfishers</b> require banks with roots to burrow into, <b>dragonflies</b> need sheltered, sunny waterside. <b>Great spotted woodpecker, treecreeper and moorhen</b> also breed, and in winter <b>little grebe and tufted duck</b> are present.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Jun\u2013Aug</b> (dragonflies at the ponds), Apr\u2013Jun (song and breeding birds)<br>\n    <b>Best time of day:</b> Morning \u2014 kingfishers hunting over the still water.',
 'why': ['Ponds originally created for <b>angling</b>.',
         'Now a <b>water-rich element</b> in a polder of straight channels.',
         'The <b>wood\u2013water transition</b> is what many species need.',
         '<b>Kingfishers</b> require banks with roots to burrow into.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> hunts over the ponds.',
          '<span class="months">May\u2013Jul</span> \U0001f3b6 <b>Song</b> of woodland birds around the water.',
          '<span class="months">Jun\u2013Aug</span> \U0001f9a0 <b>Dragonflies</b> above the vegetated banks.',
          '<span class="months">Nov\u2013Feb</span> \U0001f986 <b>Little grebe and tufted duck</b> on the ponds.'],
 'wild': ['\U0001f426 Kingfisher \u00b7 Great spotted woodpecker \u00b7 Treecreeper', '\U0001f986 Little grebe \u00b7 Tufted duck \u00b7 Moorhen', '\U0001f9a0 Dragonflies \u00b7 Damselflies', '\U0001f438 Frogs \u00b7 Newts', '\U0001f333 Ash \u00b7 Alder \u00b7 Willow \u00b7 Poplar'],
 'trail': ['Park at <b>Lelystad</b>; paths run around the ponds.',
           'Be <b>quiet by the water</b> \u2014 it improves your chance of the kingfisher.',
           'July for the <b>dragonflies</b> along the banks.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3a3 Angling \u00b7 \U0001f6b6 Short circuit'
}, card_class='card water'))

C.append(mk.card(1443, 'Rivierduingebied Lelystad', {
 'tags': ['Flevoland \u00b7 Lelystad', 'Rivierduin \u00b7 pleistocene zandrug onder de polderklei', 'list 36 \u00b7 no. 162'],
 'loc': '\U0001f4cd Bij Lelystad \u00b7 Rivierduin met schraal grasland \u00b7 Klein',
 'desc': 'Het <b>Rivierduingebied</b> bij Lelystad is een van de merkwaardigste plekken van Flevoland, want hier steekt iets oeroud door de jonge polderbodem heen. Onder de zeeklei ligt een <b>pleistoceen landschap</b> van zo\u2019n twaalfduizend jaar oud, gevormd aan het eind van de laatste ijstijd toen de wind zand uit droge rivierbeddingen opblies tot <b>rivierduinen</b>. Die duinen werden later door de zee bedekt met klei, maar op een paar plaatsen komen ze net aan de oppervlakte. Waar dat gebeurt verandert alles: de bodem is er <b>zuur, droog en voedselarm</b> in plaats van vet en nat. Daardoor groeit hier een schrale vegetatie met <b>buntgras, schapenzuring en korstmossen</b>, en vliegen er <b>graafbijen en zandloopkevers</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013aug</b> (schrale flora en insecten), aug\u2013sep (heidebloei op de zandkoppen)<br>\n    <b>Beste tijd van de dag:</b> Warme middag \u2014 graafbijen en kevers op het open zand.',
 'why': ['Onder de zeeklei ligt een <b>pleistoceen landschap</b> van 12.000 jaar oud.',
         '<b>Rivierduinen</b> ontstonden toen wind zand uit droge beddingen opblies.',
         'Op enkele plekken komen ze <b>net aan de oppervlakte</b>.',
         'Daar is de bodem <b>zuur, droog en voedselarm</b> \u2014 uniek in Flevoland.'],
 'phen': ['<span class="months">Mei\u2013Jul</span> \U0001f41d <b>Graafbijen</b> nestelen in het open zand.',
          '<span class="months">Jun\u2013Aug</span> \U0001fab2 <b>Zandloopkevers</b> jagen op de kale plekken.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heide</b> bloeit op de zandkoppen.',
          '<span class="months">Sep\u2013Okt</span> \U0001f344 <b>Korstmossen</b> vallen op na de zomer.'],
 'wild': ['\U0001f338 Buntgras \u00b7 Schapenzuring \u00b7 Struikheide \u00b7 Korstmossen', '\U0001f41d Graafbijen \u00b7 Graafwespen', '\U0001fab2 Zandloopkevers', '\U0001f426 Graspieper \u00b7 Roodborsttapuit \u00b7 Boomleeuwerik', '\U0001f98e Zandhagedis (mogelijk)'],
 'trail': ['Parkeren bij <b>Lelystad</b>; paden over de zandruggen.',
           'Let op het <b>hoogteverschil</b> \u2014 het oudste reliëf van Flevoland.',
           'Warme middag voor <b>bijen en kevers</b> op het zand.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbaar zand \u2014 blijf op de paden \u00b7 \U0001f3db\ufe0f Geologisch monument'
}, {
 'tags': ['Flevoland \u00b7 Lelystad', 'River dune \u00b7 Pleistocene sand ridge beneath the polder clay', 'list 36 \u00b7 no. 162'],
 'loc': '\U0001f4cd Near Lelystad \u00b7 River dune with poor grassland \u00b7 Small',
 'desc': 'The <b>river dune area</b> near Lelystad is one of the strangest places in Flevoland, for here something ancient pushes up through the young polder floor. Beneath the marine clay lies a <b>Pleistocene landscape</b> some twelve thousand years old, formed at the end of the last ice age when wind blew sand from dry river beds into <b>river dunes</b>. Those dunes were later covered by the sea with clay, but in a few places they just reach the surface. Where that happens everything changes: the soil there is <b>acid, dry and nutrient-poor</b> instead of rich and wet. As a result a sparse vegetation grows here with <b>grey hair-grass, sheep\u2019s sorrel and lichens</b>, and <b>mining bees and tiger beetles</b> fly.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Aug</b> (poor-soil flora and insects), Aug\u2013Sep (heather on the sand knolls)<br>\n    <b>Best time of day:</b> Warm afternoon \u2014 mining bees and beetles on the open sand.',
 'why': ['Beneath the marine clay lies a <b>Pleistocene landscape</b> 12,000 years old.',
         '<b>River dunes</b> formed as wind blew sand from dry river beds.',
         'In a few places they <b>just reach the surface</b>.',
         'There the soil is <b>acid, dry and nutrient-poor</b> \u2014 unique in Flevoland.'],
 'phen': ['<span class="months">May\u2013Jul</span> \U0001f41d <b>Mining bees</b> nest in the open sand.',
          '<span class="months">Jun\u2013Aug</span> \U0001fab2 <b>Tiger beetles</b> hunt on the bare patches.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heather</b> flowers on the sand knolls.',
          '<span class="months">Sep\u2013Oct</span> \U0001f344 <b>Lichens</b> stand out after the summer.'],
 'wild': ['\U0001f338 Grey hair-grass \u00b7 Sheep\u2019s sorrel \u00b7 Ling \u00b7 Lichens', '\U0001f41d Mining bees \u00b7 Digger wasps', '\U0001fab2 Tiger beetles', '\U0001f426 Meadow pipit \u00b7 Stonechat \u00b7 Woodlark', '\U0001f98e Sand lizard (possible)'],
 'trail': ['Park at <b>Lelystad</b>; paths cross the sand ridges.',
           'Note the <b>height difference</b> \u2014 the oldest relief in Flevoland.',
           'Warm afternoon for <b>bees and beetles</b> on the sand.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile sand \u2014 keep to the paths \u00b7 \U0001f3db\ufe0f Geological monument'
}, card_class='card dune'))

C.append(mk.card(1444, 'Overijsselse Hout', {
 'tags': ['Flevoland \u00b7 Lelystad', 'Polderbos \u00b7 provinciebos op jonge zeeklei', 'list 36 \u00b7 no. 163'],
 'loc': '\U0001f4cd Ten zuiden van Lelystad \u00b7 Polderbos \u00b7 Middelgroot',
 'desc': 'De <b>Overijsselse Hout</b> hoort bij een reeks bossen rond Lelystad die naar de omringende provincies zijn genoemd \u2014 er is ook een Gelderse Hout en een Hollandse Hout. Die naamgeving is geen toeval: bij de inrichting van Oostelijk Flevoland in de jaren zestig werd bewust verwezen naar de provincies die aan de nieuwe polder grensden, alsof het jonge land zich een <b>afstamming</b> moest geven. De bossen zelf zijn productie- en recreatiebossen op vruchtbare zeeklei, met es, populier en eik in rechte vakken. Zeventig jaar later zijn ze ecologisch volwaardig: er broeden <b>havik, buizerd, ransuil, boomklever en groene specht</b>, en er leven <b>ree\u00ebn en vossen</b>. In de herfst is het rijk aan <b>paddenstoelen</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang en roofvogelbalts), sep\u2013nov (paddenstoelen)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 roofvogels boven de bosranden.',
 'why': ['Genoemd naar de <b>omringende provincies</b>, net als de Gelderse en Hollandse Hout.',
         'Het jonge polderland gaf zich zo een <b>afstamming</b>.',
         'Productie- en recreatiebos op vruchtbare <b>zeeklei</b>.',
         'Na zeventig jaar ecologisch volwaardig \u2014 met <b>havik en boomklever</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f985 <b>Havik en buizerd</b> baltsen boven het bos.',
          '<span class="months">Apr\u2013Jun</span> \U0001f3b6 <b>Voorjaarskoor</b> in de bosvakken.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> in grote aantallen.',
          '<span class="months">Nov\u2013Feb</span> \U0001f989 <b>Ransuilen</b> in vaste roestbomen.'],
 'wild': ['\U0001f985 Havik \u00b7 Buizerd \u00b7 \U0001f989 Ransuil \u00b7 Bosuil', '\U0001f426 Boomklever \u00b7 Groene specht \u00b7 Grote bonte specht', '\U0001f98c Ree \u00b7 Vos \u00b7 Haas', '\U0001f344 Boleten \u00b7 Inktzwammen \u00b7 Elfenbankje', '\U0001f333 Es \u00b7 Populier \u00b7 Eik'],
 'trail': ['Parkeren ten zuiden van <b>Lelystad</b>; brede paden door de bosvakken.',
           'Let op de <b>rechte vakindeling</b> \u2014 typisch polderbos.',
           'Oktober is de beste maand voor <b>paddenstoelen</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f6b6 Goed padennet \u00b7 \U0001f6b4 Fietspaden'
}, {
 'tags': ['Flevoland \u00b7 Lelystad', 'Polder wood \u00b7 province-named wood on young marine clay', 'list 36 \u00b7 no. 163'],
 'loc': '\U0001f4cd South of Lelystad \u00b7 Polder wood \u00b7 Medium-sized',
 'desc': 'The <b>Overijsselse Hout</b> belongs to a series of woods around Lelystad named after the surrounding provinces \u2014 there is also a Gelderse Hout and a Hollandse Hout. That naming is no accident: when Eastern Flevoland was laid out in the 1960s, deliberate reference was made to the provinces bordering the new polder, as if the young land had to give itself an <b>ancestry</b>. The woods themselves are production and recreation woodland on fertile marine clay, with ash, poplar and oak in straight compartments. Seventy years on they are ecologically fully fledged: <b>goshawk, buzzard, long-eared owl, nuthatch and green woodpecker</b> breed, and <b>roe deer and foxes</b> live here. In autumn it is rich in <b>fungi</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song and raptor display), Sep\u2013Nov (fungi)<br>\n    <b>Best time of day:</b> Early morning \u2014 raptors above the wood edges.',
 'why': ['Named after the <b>surrounding provinces</b>, like the Gelderse and Hollandse Hout.',
         'The young polder land thus gave itself an <b>ancestry</b>.',
         'Production and recreation woodland on fertile <b>marine clay</b>.',
         'After seventy years ecologically fully fledged \u2014 with <b>goshawk and nuthatch</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f985 <b>Goshawk and buzzard</b> display above the wood.',
          '<span class="months">Apr\u2013Jun</span> \U0001f3b6 <b>Spring chorus</b> in the compartments.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> in large numbers.',
          '<span class="months">Nov\u2013Feb</span> \U0001f989 <b>Long-eared owls</b> at regular roosts.'],
 'wild': ['\U0001f985 Goshawk \u00b7 Buzzard \u00b7 \U0001f989 Long-eared owl \u00b7 Tawny owl', '\U0001f426 Nuthatch \u00b7 Green woodpecker \u00b7 Great spotted woodpecker', '\U0001f98c Roe deer \u00b7 Fox \u00b7 Brown hare', '\U0001f344 Boletes \u00b7 Inkcaps \u00b7 Turkeytail', '\U0001f333 Ash \u00b7 Poplar \u00b7 Oak'],
 'trail': ['Park south of <b>Lelystad</b>; broad paths through the compartments.',
           'Note the <b>straight compartment layout</b> \u2014 typical polder woodland.',
           'October is the best month for <b>fungi</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f6b6 Good path network \u00b7 \U0001f6b4 Cycle paths'
}))

mk.insert(C, '1439')
mk.progress(1444)
mk.check()
