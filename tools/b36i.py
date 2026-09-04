# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk
C = []

C.append(mk.card(1323, 'Noordwolde', {
 'tags': ['Friesland \u00b7 Weststellingwerf', 'Heideontginning \u00b7 bos, heiderestanten en lanen', 'list 36 \u00b7 no. 42'],
 'loc': '\U0001f4cd Rond Noordwolde en Boijl \u00b7 Ontginningslandschap \u00b7 Groot',
 'desc': 'Het gebied rond <b>Noordwolde</b> draagt de sporen van een van de grootste sociale experimenten uit de Nederlandse geschiedenis. Hier lag de rand van de <b>Maatschappij van Weldadigheid</b>, die vanaf 1818 armen uit de steden naar de Drents-Friese heide bracht om die te ontginnen. Het landschap dat daaruit voortkwam is meteen herkenbaar: <b>kaarsrechte lanen</b>, rechthoekige percelen en gelijkvormige boerderijtjes op vaste afstand van elkaar \u2014 een landschap dat op de tekentafel is ontworpen. Noordwolde zelf werd bekend om de <b>rietvlechterij</b>, een nijverheid die op de lokale rietvelden dreef. Ecologisch zijn juist de <b>randen</b> van dit strakke systeem waardevol: op de armste percelen, die nooit rendabel werden, bleef <b>heide</b> liggen, en de lanen zijn inmiddels oude bomenrijen vol holtes waar <b>vleermuizen en holenbroeders</b> in zitten.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Apr\u2013jun</b> (zang en laanbomen in blad), aug\u2013sep (heiderestanten in bloei)<br>\n    <b>Beste tijd van de dag:</b> Avondschemer \u2014 vleermuizen jagen dan langs de rechte lanen.',
 'why': ['Rand van de <b>Maatschappij van Weldadigheid</b> \u2014 ontginning door stadsarmen.',
         'Landschap <b>op de tekentafel ontworpen</b>: rechte lanen, gelijke percelen.',
         'Op de armste percelen bleef <b>heide</b> liggen.',
         'Oude laanbomen met holtes voor <b>vleermuizen en holenbroeders</b>.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f426 <b>Holenbroeders</b> bezetten de laanboomholtes.',
          '<span class="months">Mei\u2013Jul</span> \U0001f426 <b>Geelgors en boompieper</b> op de heiderestanten.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heidebloei</b> op de nooit rendabele percelen.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Vleermuizen</b> volgen de lanen bij schemer.'],
 'wild': ['\U0001f987 Rosse vleermuis \u00b7 Laatvlieger', '\U0001f426 Holenduif \u00b7 Spreeuw \u00b7 Boomklever', '\U0001f426 Geelgors \u00b7 Boompieper', '\U0001f338 Struikheide op de restpercelen', '\U0001f333 Oude eiken- en beukenlanen'],
 'trail': ['Parkeren in <b>Noordwolde</b>; het lanenstelsel is zelf de route.',
           'Bekijk het <b>Vlechtmuseum</b> voor de context van de rietvlechterij.',
           'Fietsen is ideaal \u2014 de <b>rechte lanen</b> maken de ontwerplogica voelbaar.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \U0001f3db\ufe0f Historisch ontginningslandschap \u00b7 \U0001f6b4 Fietsroute'
}, {
 'tags': ['Friesland \u00b7 Weststellingwerf', 'Heath reclamation \u00b7 woodland, heath remnants and avenues', 'list 36 \u00b7 no. 42'],
 'loc': '\U0001f4cd Around Noordwolde and Boijl \u00b7 Reclamation landscape \u00b7 Large',
 'desc': 'The area around <b>Noordwolde</b> bears the traces of one of the largest social experiments in Dutch history. Here lay the edge of the <b>Society of Benevolence</b>, which from 1818 brought the urban poor to the Drenthe-Friesland heath to reclaim it. The resulting landscape is instantly recognisable: <b>dead-straight avenues</b>, rectangular plots and identical small farms at fixed intervals \u2014 a landscape designed on the drawing board. Noordwolde itself became known for <b>wickerwork</b>, an industry that ran on the local reed beds. Ecologically it is precisely the <b>margins</b> of this rigid system that are valuable: on the poorest plots, which never became profitable, <b>heath</b> remained, and the avenues are now old rows of trees full of cavities occupied by <b>bats and hole-nesters</b>.',
 'meta': '<b>Best season &amp; peak months:</b> <b>Apr\u2013Jun</b> (song and avenues in leaf), Aug\u2013Sep (heath remnants in flower)<br>\n    <b>Best time of day:</b> Dusk \u2014 bats then hunt along the straight avenues.',
 'why': ['Edge of the <b>Society of Benevolence</b> \u2014 reclamation by the urban poor.',
         'Landscape <b>designed on the drawing board</b>: straight avenues, equal plots.',
         '<b>Heath</b> survived on the poorest plots.',
         'Old avenue trees with cavities for <b>bats and hole-nesters</b>.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f426 <b>Hole-nesters</b> occupy the avenue-tree cavities.',
          '<span class="months">May\u2013Jul</span> \U0001f426 <b>Yellowhammer and tree pipit</b> on the heath remnants.',
          '<span class="months">Aug\u2013Sep</span> \U0001f338 <b>Heather</b> flowers on the never-profitable plots.',
          '<span class="months">Jun\u2013Aug</span> \U0001f987 <b>Bats</b> follow the avenues at dusk.'],
 'wild': ['\U0001f987 Noctule \u00b7 Serotine', '\U0001f426 Stock dove \u00b7 Starling \u00b7 Nuthatch', '\U0001f426 Yellowhammer \u00b7 Tree pipit', '\U0001f338 Heather on the residual plots', '\U0001f333 Old oak and beech avenues'],
 'trail': ['Park in <b>Noordwolde</b>; the avenue system is itself the route.',
           'Visit the <b>Wickerwork Museum</b> for the context of the local craft.',
           'Cycling is ideal \u2014 the <b>straight avenues</b> make the design logic tangible.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \U0001f3db\ufe0f Historic reclamation landscape \u00b7 \U0001f6b4 Cycle route'
}))

C.append(mk.card(1324, 'Wapserveen', {
 'tags': ['Drenthe \u00b7 Westerveld', 'Beekdal \u00b7 madelanden langs de Vledder Aa', 'list 36 \u00b7 no. 43'],
 'loc': '\U0001f4cd Het beekdal bij Wapserveen \u00b7 Beekdalgraslanden \u00b7 Groot',
 'desc': 'Het dorp <b>Wapserveen</b> ligt aan een van de langste dorpsstraten van Drenthe, en die vorm verraadt zijn ontstaan: het is een <b>veenontginningsdorp</b>, waarbij boeren zich op een rij langs de ontginningsas vestigden en elk een lange, smalle strook land naar achteren toe ontgonnen. Die <b>opstrekkende verkaveling</b> is nog perfect zichtbaar op de kaart en in het veld \u2014 evenwijdige sloten die kilometers ver het beekdal in lopen. Het dal van de <b>Vledder Aa</b> eronder bestaat uit <b>madelanden</b>: eeuwenoude hooilanden die nooit bemest werden omdat de beek ze bij hoogwater zelf voedde met slib. Waar dat regime is teruggebracht, keren de karakteristieke soorten terug \u2014 <b>gevlekte orchis, blauwe knoop en moerasviooltje</b>. Het moerasviooltje is de waardplant van de zeldzame <b>zilveren maan</b>, een vlinder die hier weer voorkomt.',
 'meta': '<b>Beste seizoen &amp; piekmaanden:</b> <b>Mei\u2013jul</b> (orchidee\u00ebn en zilveren maan), apr\u2013jun (weidevogels)<br>\n    <b>Beste tijd van de dag:</b> Ochtend voor vogels; warme middag voor de vlinders.',
 'why': ['Klassieke <b>opstrekkende verkaveling</b> vanaf de lange dorpsstraat.',
         '<b>Madelanden</b> die nooit bemest hoefden \u2014 de beek deed het werk.',
         'Terugkeer van <b>gevlekte orchis en blauwe knoop</b>.',
         'De <b>zilveren maan</b> vliegt weer op het moerasviooltje.'],
 'phen': ['<span class="months">Apr\u2013Mei</span> \U0001f33c <b>Dotterbloem</b> in de natste madelanden.',
          '<span class="months">Mei\u2013Jun</span> \U0001f33c <b>Gevlekte orchis</b> bloeit in het hooiland.',
          '<span class="months">Jun\u2013Jul</span> \U0001f98b <b>Zilveren maan</b> boven het moerasviooltje.',
          '<span class="months">Nov\u2013Mrt</span> \U0001f4a7 <b>Hoogwater</b> \u2014 de beek voedt de madelanden met slib.'],
 'wild': ['\U0001f98b Zilveren maan', '\U0001f33c Gevlekte orchis \u00b7 Blauwe knoop \u00b7 Moerasviooltje', '\U0001f426 Wulp \u00b7 Watersnip \u00b7 Grutto', '\U0001f9a0 Beekjuffers', '\U0001f98c Ree'],
 'trail': ['Parkeren in <b>Wapserveen</b>; paden vanaf de dorpsstraat het dal in.',
           'Loop een <b>strook</b> af van de weg naar de beek \u2014 dat is \u00e9\u00e9n oude boerenkavel.',
           'Combineer met <b>Vledder</b> en het <b>Nijenslekerveld</b>.'],
 'foot': '\U0001f436 Honden aan de lijn \u00b7 \U0001f4b6 Gratis \u00b7 \u26a0\ufe0f Hooiland kwetsbaar \u2014 niet betreden voor de maai \u00b7 \U0001f97e Nat in de winter'
}, {
 'tags': ['Drenthe \u00b7 Westerveld', 'Brook valley \u00b7 hay meadows along the Vledder Aa', 'list 36 \u00b7 no. 43'],
 'loc': '\U0001f4cd The brook valley at Wapserveen \u00b7 Brook-valley grasslands \u00b7 Large',
 'desc': 'The village of <b>Wapserveen</b> lies along one of the longest village streets in Drenthe, and that shape betrays its origin: it is a <b>peat reclamation village</b>, where farmers settled in a row along the reclamation axis and each cleared a long, narrow strip of land running back from it. That <b>strip parcelling</b> is still perfectly visible on the map and in the field \u2014 parallel ditches running kilometres into the brook valley. The valley of the <b>Vledder Aa</b> below consists of <b>madelanden</b>: centuries-old hay meadows that were never fertilised because the brook fed them with silt at high water. Where that regime has been restored, the characteristic species return \u2014 <b>heath spotted orchid, devil\u2019s-bit scabious and marsh violet</b>. The marsh violet is the food plant of the rare <b>silver-bordered fritillary</b>, a butterfly that occurs here again.',
 'meta': '<b>Best season &amp; peak months:</b> <b>May\u2013Jul</b> (orchids and fritillary), Apr\u2013Jun (meadow birds)<br>\n    <b>Best time of day:</b> Morning for birds; warm afternoon for the butterflies.',
 'why': ['Classic <b>strip parcelling</b> running back from the long village street.',
         '<b>Hay meadows</b> that never needed manure \u2014 the brook did the work.',
         'Return of <b>heath spotted orchid and devil\u2019s-bit scabious</b>.',
         'The <b>silver-bordered fritillary</b> flies again on the marsh violet.'],
 'phen': ['<span class="months">Apr\u2013May</span> \U0001f33c <b>Marsh marigold</b> in the wettest hay meadows.',
          '<span class="months">May\u2013Jun</span> \U0001f33c <b>Heath spotted orchid</b> flowers in the hay meadow.',
          '<span class="months">Jun\u2013Jul</span> \U0001f98b <b>Silver-bordered fritillary</b> above the marsh violet.',
          '<span class="months">Nov\u2013Mar</span> \U0001f4a7 <b>High water</b> \u2014 the brook feeds the meadows with silt.'],
 'wild': ['\U0001f98b Silver-bordered fritillary', '\U0001f33c Heath spotted orchid \u00b7 Devil\u2019s-bit scabious \u00b7 Marsh violet', '\U0001f426 Curlew \u00b7 Snipe \u00b7 Black-tailed godwit', '\U0001f9a0 Demoiselles', '\U0001f98c Roe deer'],
 'trail': ['Park in <b>Wapserveen</b>; paths from the village street into the valley.',
           'Walk one <b>strip</b> from road to brook \u2014 that is a single old holding.',
           'Combine with <b>Vledder</b> and the <b>Nijenslekerveld</b>.'],
 'foot': '\U0001f436 Dogs on lead \u00b7 \U0001f4b6 Free \u00b7 \u26a0\ufe0f Hay meadow fragile \u2014 do not enter before mowing \u00b7 \U0001f97e Wet in winter'
}))

mk.insert(C, '1322')
mk.progress(1324)
mk.check()
