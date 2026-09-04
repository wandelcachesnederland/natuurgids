# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1313, 'Braambos', {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Bosje \u00b7 kleinschalig loofbos', 'list 36 \u00b7 no. 32'],
 'loc': '\U0001f4cd Bij Steenwijkerwold \u00b7 Klein loofbos \u00b7 Klein',
 'desc': 'Het <b>Braambos</b> bij Steenwijkerwold is een van die kleine bosjes die het Overijsselse zandlandschap zijn korrelige structuur geven. De naam zegt waar het om draait: <b>braam</b> is hier geen onkruid maar een dragende soort. Bramenstruwelen worden vaak weggezet als verruiging, maar ecologisch zijn ze uitermate productief \u2014 ze bieden <b>ondoordringbare dekking</b> voor broedvogels die op de grond of laag in de struiklaag nestelen, en de bessen zijn in augustus en september een van de belangrijkste <b>voedselbronnen</b> voor zangvogels die vetreserves opbouwen voor de trek. In het Braambos profiteren daarvan <b>zwartkop, braamsluiper en tuinfluiter</b>, drie soorten die hun naam en levenswijze aan dit struweel danken. Onder de opgaande eiken en berken ligt een schrale bodem met <b>bochtige smele en blauwe bosbes</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (zang en bramenbloei), aug\u2013sep (bessen en trekvogels)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 dan zingen de struweelvogels het felst.',
 'why': ['<b>Bramenstruweel</b> als volwaardig habitat, niet als verruiging.',
         'Ondoordringbare <b>dekking</b> voor laagbroedende vogels.',
         'Bessen als <b>brandstof</b> voor trekvogels in aug\u2013sep.',
         'Schrale bodem met <b>bochtige smele en blauwe bosbes</b>.'],
 'phen': ['<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Braamsluiper en tuinfluiter</b> zingen uit het struweel.',
          '<span class="months">Jun\u2013Jul</span> \U0001f41d <b>Bramenbloei</b> trekt bijen en zweefvliegen.',
          '<span class="months">Aug\u2013Sep</span> \U0001fad0 <b>Bramen rijp</b> \u2014 zangvogels tanken bij.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> onder eik en berk.'],
 'wild': ['\U0001f426 Zwartkop \u00b7 Braamsluiper \u00b7 Tuinfluiter', '\U0001f426 Winterkoning \u00b7 Heggenmus', '\U0001f98c Ree \u00b7 Vos', '\U0001f33f Braam \u00b7 Bochtige smele \u00b7 Blauwe bosbes', '\U0001f41d Bijen \u00b7 Zweefvliegen'],
 'trail': ['Parkeren bij <b>Steenwijkerwold</b>; paden langs de bosrand.',
           'Klein gebied \u2014 combineer met <b>Krolsbergen</b> in de buurt.',
           'De <b>randen</b> zijn interessanter dan het midden.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Doornig struweel \u2014 blijf op de paden'
}, {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Copse \u00b7 small-scale broadleaf wood', 'list 36 \u00b7 no. 32'],
 'loc': '\U0001f4cd Near Steenwijkerwold \u00b7 Small broadleaf wood \u00b7 Small',
 'desc': 'The <b>Braambos</b> near Steenwijkerwold is one of those small copses that give the Overijssel sandy landscape its grainy texture. The name says what matters: <b>bramble</b> here is not a weed but a load-bearing species. Bramble thickets are often dismissed as scrub encroachment, but ecologically they are extremely productive \u2014 they offer <b>impenetrable cover</b> for birds nesting on the ground or low in the shrub layer, and in August and September the berries are one of the most important <b>food sources</b> for songbirds building fat reserves for migration. In the Braambos <b>blackcap, lesser whitethroat and garden warbler</b> benefit, three species that owe their name and way of life to this thicket. Beneath the standing oaks and birches lies poor soil with <b>wavy hair-grass and bilberry</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (song and bramble flowering), Aug\u2013Sep (berries and migrants)<br>\n    <b>Best time of day:</b> Early morning \u2014 when the scrub birds sing most fiercely.',
 'why': ['<b>Bramble thicket</b> as a habitat in its own right, not as neglect.',
         'Impenetrable <b>cover</b> for low-nesting birds.',
         'Berries as <b>fuel</b> for migrants in Aug\u2013Sep.',
         'Poor soil with <b>wavy hair-grass and bilberry</b>.'],
 'phen': ['<span class="months">May\u2013Jul</span> \U0001f426 <b>Lesser whitethroat and garden warbler</b> sing from the thicket.',
          '<span class="months">Jun\u2013Jul</span> \U0001f41d <b>Bramble flowering</b> attracts bees and hoverflies.',
          '<span class="months">Aug\u2013Sep</span> \U0001fad0 <b>Brambles ripe</b> \u2014 songbirds refuel.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> under oak and birch.'],
 'wild': ['\U0001f426 Blackcap \u00b7 Lesser whitethroat \u00b7 Garden warbler', '\U0001f426 Wren \u00b7 Dunnock', '\U0001f98c Roe deer \u00b7 Fox', '\U0001f33f Bramble \u00b7 Wavy hair-grass \u00b7 Bilberry', '\U0001f41d Bees \u00b7 Hoverflies'],
 'trail': ['Park at <b>Steenwijkerwold</b>; paths along the woodland edge.',
           'Small site \u2014 combine with nearby <b>Krolsbergen</b>.',
           'The <b>edges</b> are more interesting than the middle.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Thorny scrub \u2014 keep to the paths'
}))

C.append(mk.card(1314, 'Krolsbergen', {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Stuifzandheuvels \u00b7 heide en naaldbos', 'list 36 \u00b7 no. 33'],
 'loc': '\U0001f4cd Bij Steenwijkerwold en De Bult \u00b7 Zandheuvels met heide \u00b7 Klein',
 'desc': 'De <b>Krolsbergen</b> zijn een groepje lage zandheuvels ten noorden van Steenwijk, ontstaan als <b>landduinen</b>: in de middeleeuwen en vroegmoderne tijd raakte hier de heide overbegraasd en overbetreden, waarna de wind het blootgelegde zand opnam en tot heuvels opstoof. Dat proces staat bekend als <b>verstuiving</b> en was destijds een regelrechte ramp \u2014 hele akkers en soms dorpen werden ondergestoven. Vanaf de negentiende eeuw bestreed men het door massaal <b>grove den</b> aan te planten, en dat naaldbos bepaalt hier nog steeds het beeld. Op de open toppen is de <b>heide</b> bewaard gebleven, en juist die combinatie van warme, kale zandplekken en heide maakt het gebied waardevol voor <b>reptielen en graafbijen</b>. Er leeft de <b>levendbarende hagedis</b>, en in de open plekken nestelen <b>zandbijen en graafwespen</b> in de zonbeschenen steilrandjes.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Aug\u2013sep</b> (heidebloei), apr\u2013jun (reptielen en graafbijen)<br>\n    <b>Beste tijd van de dag:</b> Ochtend \u2014 hagedissen zonnen zich dan op de warme zandpaden.',
 'why': ['<b>Landduinen</b> ontstaan door middeleeuwse overbegrazing en verstuiving.',
         'Bestreden met massale <b>grove-dennenaanplant</b> in de 19e eeuw.',
         'Open toppen met bewaarde <b>heide</b> en kale zandplekken.',
         'Warm microklimaat voor <b>hagedissen en graafbijen</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f98e <b>Levendbarende hagedis</b> zont op de paden.',
          '<span class="months">Mei\u2013Jun</span> \U0001f41d <b>Zandbijen</b> nestelen in de steilrandjes.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Struikheide</b> in bloei op de toppen.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Paddenstoelen</b> onder de grove dennen.'],
 'wild': ['\U0001f98e Levendbarende hagedis', '\U0001f41d Zandbijen \u00b7 Graafwespen', '\U0001f426 Boomleeuwerik \u00b7 Roodborsttapuit', '\U0001f338 Struikheide \u00b7 Buntgras', '\U0001f333 Grove den \u00b7 Berk'],
 'trail': ['Parkeren bij <b>De Bult</b>; paden over de heuvelruggen.',
           'De <b>open toppen</b> zijn het interessantst \u2014 daar zit alle warmte.',
           'Combineer met <b>Braambos</b> en <b>De Eese</b> in de omgeving.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Kwetsbare heide \u2014 blijf op de paden \u00b7 \U0001f9ed Natuurmonumenten'
}, {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Inland dunes \u00b7 heath and pine woodland', 'list 36 \u00b7 no. 33'],
 'loc': '\U0001f4cd Near Steenwijkerwold and De Bult \u00b7 Sand hills with heath \u00b7 Small',
 'desc': 'The <b>Krolsbergen</b> are a cluster of low sand hills north of Steenwijk, formed as <b>inland dunes</b>: in the medieval and early modern periods the heath here became overgrazed and over-trampled, after which the wind picked up the exposed sand and blew it into hills. That process is known as <b>sand drift</b> and was an outright disaster at the time \u2014 whole fields and sometimes villages were buried. From the nineteenth century it was combated by planting <b>Scots pine</b> on a massive scale, and that conifer wood still dominates the scene. On the open summits the <b>heath</b> has survived, and it is precisely that combination of warm, bare sandy spots and heath that makes the area valuable for <b>reptiles and mining bees</b>. The <b>common lizard</b> lives here, and in the clearings <b>mining bees and digger wasps</b> nest in the sunlit miniature cliffs.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Aug\u2013Sep</b> (heather flowering), Apr\u2013Jun (reptiles and mining bees)<br>\n    <b>Best time of day:</b> Morning \u2014 lizards then bask on the warm sandy paths.',
 'why': ['<b>Inland dunes</b> formed by medieval overgrazing and sand drift.',
         'Combated with mass <b>Scots pine planting</b> in the 19th century.',
         'Open summits with surviving <b>heath</b> and bare sandy patches.',
         'Warm microclimate for <b>lizards and mining bees</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f98e <b>Common lizard</b> basks on the paths.',
          '<span class="months">May\u2013Jun</span> \U0001f41d <b>Mining bees</b> nest in the small cliffs.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heather</b> in flower on the summits.',
          '<span class="months">Sep\u2013Nov</span> \U0001f344 <b>Fungi</b> under the Scots pines.'],
 'wild': ['\U0001f98e Common lizard', '\U0001f41d Mining bees \u00b7 Digger wasps', '\U0001f426 Woodlark \u00b7 Stonechat', '\U0001f338 Heather \u00b7 Grey hair-grass', '\U0001f333 Scots pine \u00b7 Birch'],
 'trail': ['Park at <b>De Bult</b>; paths over the ridges.',
           'The <b>open summits</b> are most interesting \u2014 all the warmth is there.',
           'Combine with <b>Braambos</b> and <b>De Eese</b> nearby.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Fragile heath \u2014 keep to the paths \u00b7 \U0001f9ed Natuurmonumenten'
}, card_class='card dune'))

C.append(mk.card(1315, 'Paasloo-Kerkbuurt landschapselementen', {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Landschapselementen \u00b7 houtwallen, singels en poelen', 'list 36 \u00b7 no. 34'],
 'loc': '\U0001f4cd Rond de kerkbuurt van Paasloo \u00b7 Kleinschalig cultuurlandschap \u00b7 Lijnvormig',
 'desc': 'Rond de oude <b>kerkbuurt van Paasloo</b> ligt een verzameling <b>landschapselementen</b> die samen een compleet beeld geven van hoe een Overijssels esdorp eruitzag voordat de ruilverkaveling toesloeg. Het gaat om <b>houtwallen, elzensingels, hoogstamboomgaarden en poelen</b> \u2014 op zichzelf allemaal klein, maar juist hun <b>samenhang</b> maakt het geheel waardevol. Zo\u2019n netwerk werkt als een ecologische infrastructuur: een das of steenmarter kan er kilometers door afleggen zonder ooit open veld te hoeven kruisen, en vleermuizen gebruiken de singels als <b>navigatielijn</b> tussen verblijfplaats en jachtgebied. De poelen \u2014 oorspronkelijk gegraven als <b>drinkplaats voor vee</b> \u2014 zijn nu de kraamkamers voor amfibie\u00ebn. In de houtwallen broeden <b>geelgors, grasmus en steenuil</b>, en de hoogstammen leveren nestholtes.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (bloei van de hoogstammen en zang), mrt\u2013apr (amfibie\u00ebn in de poelen)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 steenuil en vleermuizen worden dan actief.',
 'why': ['Compleet netwerk van <b>houtwallen, singels, boomgaarden en poelen</b>.',
         'Werkt als <b>ecologische infrastructuur</b> door het boerenland.',
         'Singels als <b>navigatielijn</b> voor vleermuizen.',
         'Broedplaats van <b>geelgors en steenuil</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f438 <b>Amfibie\u00ebn</b> paaien in de veedrinkpoelen.',
          '<span class="months">Apr\u2013Mei</span> \U0001f338 <b>Hoogstamboomgaarden</b> in bloei.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors</b> zingt vanaf de houtwaltoppen.',
          '<span class="months">Sep\u2013Okt</span> \U0001f34e <b>Oude appelrassen</b> rijp in de boomgaarden.'],
 'wild': ['\U0001f426 Geelgors \u00b7 Grasmus \u00b7 Steenuil', '\U0001f987 Gewone dwergvleermuis \u00b7 Laatvlieger', '\U0001f9a1 Das \u00b7 Steenmarter', '\U0001f438 Kleine watersalamander \u00b7 Bruine kikker', '\U0001f333 Els \u00b7 Eik \u00b7 Oude appelrassen'],
 'trail': ['Parkeren bij de <b>kerk van Paasloo</b>; landweggetjes verbinden de elementen.',
           'Uitstekend per <b>fiets</b> \u2014 de schaal is klein en het netwerk uitgestrekt.',
           'Kom bij <b>avondschemer</b> voor steenuil en vleermuizen.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Veel is <b>particulier land</b> \u2014 blijf op de openbare weg \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Landscape elements \u00b7 hedgebanks, tree lines and ponds', 'list 36 \u00b7 no. 34'],
 'loc': '\U0001f4cd Around the church hamlet of Paasloo \u00b7 Small-scale farmed landscape \u00b7 Linear',
 'desc': 'Around the old <b>church hamlet of Paasloo</b> lies a collection of <b>landscape elements</b> that together give a complete picture of how an Overijssel village looked before land consolidation struck. These are <b>hedgebanks, alder lines, standard orchards and ponds</b> \u2014 individually all small, but it is precisely their <b>coherence</b> that makes the whole valuable. Such a network functions as ecological infrastructure: a badger or stone marten can cover kilometres through it without ever crossing open field, and bats use the tree lines as a <b>navigation line</b> between roost and hunting ground. The ponds \u2014 originally dug as <b>drinking places for cattle</b> \u2014 are now nurseries for amphibians. <b>Yellowhammer, whitethroat and little owl</b> breed in the hedgebanks, and the standard trees provide nest cavities.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (orchard blossom and song), Mar\u2013Apr (amphibians in the ponds)<br>\n    <b>Best time of day:</b> Evening dusk \u2014 little owl and bats then become active.',
 'why': ['Complete network of <b>hedgebanks, tree lines, orchards and ponds</b>.',
         'Functions as <b>ecological infrastructure</b> through the farmland.',
         'Tree lines as a <b>navigation line</b> for bats.',
         'Breeding site for <b>yellowhammer and little owl</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f438 <b>Amphibians</b> spawn in the cattle ponds.',
          '<span class="months">Apr\u2013May</span> \U0001f338 <b>Standard orchards</b> in blossom.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer</b> sings from the hedgebank tops.',
          '<span class="months">Sep\u2013Oct</span> \U0001f34e <b>Old apple varieties</b> ripe in the orchards.'],
 'wild': ['\U0001f426 Yellowhammer \u00b7 Whitethroat \u00b7 Little owl', '\U0001f987 Common pipistrelle \u00b7 Serotine', '\U0001f9a1 Badger \u00b7 Stone marten', '\U0001f438 Smooth newt \u00b7 Common frog', '\U0001f333 Alder \u00b7 Oak \u00b7 Old apple varieties'],
 'trail': ['Park by the <b>church of Paasloo</b>; country lanes connect the elements.',
           'Excellent <b>by bicycle</b> \u2014 the scale is small and the network extensive.',
           'Come at <b>dusk</b> for little owl and bats.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Much is <b>private land</b> \u2014 keep to public roads \u00b7 \U0001f6b4 Cycle route'
}))

C.append(mk.card(1316, 'Paaslo', {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Esdorplandschap \u00b7 essen, weiden en bosjes', 'list 36 \u00b7 no. 35'],
 'loc': '\U0001f4cd Het dorpsgebied van Paaslo \u00b7 Esdorplandschap \u00b7 Middelgroot',
 'desc': 'Het dorpsgebied van <b>Paaslo</b> \u2014 een van de oudste nederzettingen van Noordwest-Overijssel \u2014 laat de klassieke <b>drieledige opbouw</b> van het esdorplandschap zien. Er is de <b>es</b>: het hooggelegen bouwland, eeuwenlang opgehoogd met plaggen uit de heide vermengd met stalmest, waardoor de bodem hier soms meer dan een meter dikker is dan elders. Er zijn de <b>maden</b>: de lage, natte hooilanden langs de beek, die de winterse mest en het hooi leverden. En er is de voormalige <b>heide</b>, waar de schapen liepen die het hele systeem draaiende hielden. Die drie onderdelen waren onlosmakelijk verbonden \u2014 zonder heide geen plaggen, zonder plaggen geen vruchtbare es. Rond Paaslo zijn alle drie nog herkenbaar, en op de esranden groeien akkerkruiden als <b>korenbloem en gele ganzenbloem</b> die elders zijn verdwenen.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (akkerkruiden en weidevogels), sep\u2013okt (herfstlicht over de es)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend of avond \u2014 strijklicht toont het reli\u00ebf van de es.',
 'why': ['Klassieke <b>drieledige opbouw</b>: es, maden en heide.',
         'De es is eeuwenlang <b>opgehoogd met plaggen en mest</b> \u2014 soms meer dan een meter.',
         'Alle drie de onderdelen zijn nog in het landschap <b>herkenbaar</b>.',
         'Akkerkruiden als <b>korenbloem en gele ganzenbloem</b> op de esranden.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Weidevogels</b> in de lage maden langs de beek.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Akkerkruiden</b> bloeien op de esranden.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33e <b>Graanoogst</b> op de es \u2014 het oude beeld.',
          '<span class="months">Sep\u2013Okt</span> \U0001f341 <b>Strijklicht</b> maakt het bolle esreli\u00ebf zichtbaar.'],
 'wild': ['\U0001f426 Veldleeuwerik \u00b7 Geelgors \u00b7 Kievit', '\U0001f33c Korenbloem \u00b7 Gele ganzenbloem \u00b7 Klaproos', '\U0001f985 Torenvalk \u00b7 Buizerd', '\U0001f98c Ree \u00b7 Haas', '\U0001f333 Eiken op de esrandwallen'],
 'trail': ['Parkeren in <b>Paaslo</b>; zandwegen over en om de es.',
           'Let op het <b>hoogteverschil</b> tussen es en maden \u2014 dat is duizend jaar plaggen.',
           'Goed te combineren met de <b>landschapselementen</b> bij de kerkbuurt.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Betreed geen akkers \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Overijssel \u00b7 Steenwijkerland', 'Es-village landscape \u00b7 open fields, meadows and copses', 'list 36 \u00b7 no. 35'],
 'loc': '\U0001f4cd The village lands of Paaslo \u00b7 Es-village landscape \u00b7 Medium-sized',
 'desc': 'The village lands of <b>Paaslo</b> \u2014 one of the oldest settlements in north-west Overijssel \u2014 show the classic <b>threefold structure</b> of the es-village landscape. There is the <b>es</b>: the high-lying arable, raised for centuries with sods from the heath mixed with stable manure, so that the soil here is sometimes more than a metre thicker than elsewhere. There are the <b>maden</b>: the low, wet hay meadows along the brook, which supplied the winter manure and the hay. And there is the former <b>heath</b>, where the sheep grazed that kept the whole system running. Those three parts were inseparably linked \u2014 without heath no sods, without sods no fertile es. Around Paaslo all three are still recognisable, and on the field margins grow arable weeds such as <b>cornflower and corn marigold</b> that have vanished elsewhere.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (arable flowers and meadow birds), Sep\u2013Oct (autumn light over the es)<br>\n    <b>Best time of day:</b> Early morning or evening \u2014 raking light shows the relief of the es.',
 'why': ['Classic <b>threefold structure</b>: es, hay meadows and heath.',
         'The es was <b>raised with sods and manure</b> for centuries \u2014 sometimes over a metre.',
         'All three components are still <b>recognisable</b> in the landscape.',
         'Arable flowers such as <b>cornflower and corn marigold</b> on the margins.'],
 'phen': ['<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Meadow birds</b> in the low meadows along the brook.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Arable flowers</b> bloom on the field margins.',
          '<span class="months">Jul\u2013Aug</span> \U0001f33e <b>Grain harvest</b> on the es \u2014 the old picture.',
          '<span class="months">Sep\u2013Oct</span> \U0001f341 <b>Raking light</b> reveals the domed relief of the es.'],
 'wild': ['\U0001f426 Skylark \u00b7 Yellowhammer \u00b7 Lapwing', '\U0001f33c Cornflower \u00b7 Corn marigold \u00b7 Poppy', '\U0001f985 Kestrel \u00b7 Buzzard', '\U0001f98c Roe deer \u00b7 Brown hare', '\U0001f333 Oaks on the field-edge banks'],
 'trail': ['Park in <b>Paaslo</b>; sandy tracks across and around the es.',
           'Note the <b>height difference</b> between es and meadows \u2014 that is a thousand years of sods.',
           'Easily combined with the <b>landscape elements</b> by the church hamlet.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Do not enter arable fields \u00b7 \U0001f6b4 Cycle route'
}))

C.append(mk.card(1317, 'De Blesse', {
 'tags': ['Friesland \u00b7 Weststellingwerf', 'Beekdal \u00b7 nat grasland langs de Linde', 'list 36 \u00b7 no. 36'],
 'loc': '\U0001f4cd Bij het dorp De Blesse, langs de Linde \u00b7 Beekdal \u00b7 Klein',
 'desc': 'Bij <b>De Blesse</b> raakt het dorpsgebied aan het dal van de <b>Linde</b>, de laatste Friese beek die nog grotendeels <b>vrij mag meanderen</b>. Dat is uitzonderlijk: bijna alle Nederlandse beken zijn in de twintigste eeuw rechtgetrokken om water sneller af te voeren, met als gevolg dat de beekdalen verdroogden en hun karakteristieke flora verloren. De Linde ontsnapte daaraan grotendeels, en langs De Blesse zie je nog wat een levende beek doet: hij <b>schuurt</b> in de buitenbochten steilrandjes uit en zet in de binnenbochten zand af, waardoor er een voortdurend wisselend mozа\u00efek van oevertypen ontstaat. In de aangrenzende <b>natte graslanden</b> broeden watersnip en tureluur, en bij hoogwater treedt de beek buiten haar oevers \u2014 wat de graslanden hun vruchtbaarheid en hun soortenrijkdom geeft. In de steilrandjes nestelt de <b>ijsvogel</b>.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (weidevogels en beekflora), nov\u2013mrt (hoogwater en overstroming)<br>\n    <b>Beste tijd van de dag:</b> Vroege ochtend \u2014 ijsvogel en watersnip zijn dan actief.',
 'why': ['Ligt aan de <b>Linde</b>: de laatste vrij meanderende Friese beek.',
         'Beek <b>schuurt en zet af</b> \u2014 wisselend mozа\u00efek van oevertypen.',
         '<b>Overstroming bij hoogwater</b> houdt de graslanden rijk.',
         'Steilrandjes als nestplaats voor de <b>ijsvogel</b>.'],
 'phen': ['<span class="months">Mrt\u2013Apr</span> \U0001f426 <b>Watersnip</b> baltst boven de natte graslanden.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>IJsvogel</b> broedt in de uitgeschuurde steilrandjes.',
          '<span class="months">Mei\u2013Jul</span> \U0001f33c <b>Beekdalflora</b> met dotterbloem en echte koekoeksbloem.',
          '<span class="months">Nov\u2013Mrt</span> \U0001f4a7 <b>Hoogwater</b> \u2014 de beek treedt buiten haar oevers.'],
 'wild': ['\U0001f426 IJsvogel \u00b7 Watersnip \u00b7 Tureluur', '\U0001f41f Bermpje \u00b7 Riviergrondel', '\U0001f9a6 Otter (sporadisch)', '\U0001f33c Dotterbloem \u00b7 Echte koekoeksbloem', '\U0001f9a0 Beekjuffers'],
 'trail': ['Parkeren in <b>De Blesse</b>; paden langs de Linde.',
           'Volg de beek <b>stroomopwaarts</b> richting Wolvega voor de mooiste meanders.',
           'In de winter kan het pad <b>onder water</b> staan \u2014 dat hoort erbij.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Bij hoogwater natte voeten \u00b7 \U0001f9ed It Fryske Gea'
}, {
 'tags': ['Friesland \u00b7 Weststellingwerf', 'Brook valley \u00b7 wet grassland along the Linde', 'list 36 \u00b7 no. 36'],
 'loc': '\U0001f4cd By the village of De Blesse, along the Linde \u00b7 Brook valley \u00b7 Small',
 'desc': 'At <b>De Blesse</b> the village lands touch the valley of the <b>Linde</b>, the last Frisian brook still largely allowed to <b>meander freely</b>. That is exceptional: almost all Dutch brooks were straightened in the twentieth century to drain water faster, with the result that the brook valleys dried out and lost their characteristic flora. The Linde largely escaped that, and along De Blesse you can still see what a living brook does: it <b>scours</b> small cliffs on the outer bends and deposits sand on the inner ones, producing a constantly shifting mosaic of bank types. <b>Snipe and redshank</b> breed in the adjoining <b>wet grasslands</b>, and at high water the brook overtops its banks \u2014 which gives the grasslands their fertility and their species richness. The <b>kingfisher</b> nests in the small cliffs.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (meadow birds and brook flora), Nov\u2013Mar (high water and flooding)<br>\n    <b>Best time of day:</b> Early morning \u2014 kingfisher and snipe are then active.',
 'why': ['Lies on the <b>Linde</b>: the last freely meandering Frisian brook.',
         'The brook <b>scours and deposits</b> \u2014 a shifting mosaic of bank types.',
         '<b>Flooding at high water</b> keeps the grasslands rich.',
         'Small cliffs as nesting sites for the <b>kingfisher</b>.'],
 'phen': ['<span class="months">Mar\u2013Apr</span> \U0001f426 <b>Snipe</b> drumming above the wet grasslands.',
          '<span class="months">Apr\u2013Jun</span> \U0001f426 <b>Kingfisher</b> breeds in the scoured cliffs.',
          '<span class="months">May\u2013Jul</span> \U0001f33c <b>Brook-valley flora</b> with marsh marigold and ragged robin.',
          '<span class="months">Nov\u2013Mar</span> \U0001f4a7 <b>High water</b> \u2014 the brook overtops its banks.'],
 'wild': ['\U0001f426 Kingfisher \u00b7 Snipe \u00b7 Redshank', '\U0001f41f Stone loach \u00b7 Gudgeon', '\U0001f9a6 Otter (occasional)', '\U0001f33c Marsh marigold \u00b7 Ragged robin', '\U0001f9a0 Demoiselles'],
 'trail': ['Park in <b>De Blesse</b>; paths along the Linde.',
           'Follow the brook <b>upstream</b> towards Wolvega for the finest meanders.',
           'In winter the path may be <b>under water</b> \u2014 that is part of it.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Wet feet at high water \u00b7 \U0001f9ed It Fryske Gea'
}, card_class='card water'))

mk.insert(C, '1312')
mk.progress(1317)
mk.check()
