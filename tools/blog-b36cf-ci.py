# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Langs de Stichtse Lustwarande (1695\u20131714)</h3>
        <p class="post-meta">List 36 · Utrecht: Zeist, Driebergen-Rijsenburg, Austerlitz, Doorn, Maarn en Leusden</p>
        <p>Twintig gebieden schuiven deze keer langs de zuidflank van de Utrechtse Heuvelrug, waar de <b>Stichtse Lustwarande</b> \u2014 de gordel van buitenplaatsen tussen De Bilt en Rhenen \u2014 het landschap bepaalt. Het begint bij het station van Driebergen-Zeist: landgoed <b>De Reehorst</b>, buitenplaats <b>Wulperhorst</b> met zijn grand canal en ijskelder, en de snoer van <b>buitenplaatsen langs de Driebergseweg</b> met hun slingervijvers van Zocher. Daarna strekt het eeuwenoude <b>Zeisterbos</b> zich uit, gevoed door met de hand gegraven sprengen, en de bosgordel van het <b>Zeisterwoud</b> richting Soesterberg.</p>
        <p>Bij <b>Austerlitz</b> slaat de geschiedenis van Napoleon toe: het dorp groeide uit het legerkamp van generaal De Marmont, die er in 1804 de 36 meter hoge piramide liet opwerpen. De <b>Kozakkenput en Krakeling</b> herinneren aan de kozakken van koning Willem I en aan de bakkerij voor het bezettingsleger. Dan volgt het grootste familielandgoed van Nederland, <b>Den Treek-Henschoten</b>, met de oeroude Treeker Eik, en de heide- en stuifzandgebieden <b>Heidestein, Bornia en Noordhout</b> waar Drentse heideschapen grazen. Bij Zeist ligt buitenplaats <b>De Breul</b> met zijn landschapspark en de reusachtige C\u00e4sar-bunker.</p>
        <p>Driebergen biedt het ontroerende <b>Beerschoten-Willinkshof</b>, waar bankier Willink zijn park aan de gemeente legateerde, het <b>Rijsenburgsebos</b> met de Heidetuin en Lourdesgrot, het <b>Driebergsebos</b> van het vroegere Sparrendaal, en het kleine, gesloten <b>De Kurk</b> met zijn Iberisch slakje. Rond Maarn en Doorn liggen <b>Mollenbos</b> en <b>Het Heihuis</b> met het ecoduct over de A12, de bosgraven achter de <b>Nieuwe Algemene Begraafplaats</b>, het oeroude <b>Ludenbos</b>, en de heide van <b>Hoog Moersbergen, Stameren, Bergweg en De Pol</b>. De reeks eindigt op landgoed <b>De Zonheuvel</b> rond het Maarten Maartenshuis.</p>
      </div>
      <div class="c-en">
        <h3>Along the Stichtse Lustwarande (1695\u20131714)</h3>
        <p class="post-meta">List 36 · Utrecht: Zeist, Driebergen-Rijsenburg, Austerlitz, Doorn, Maarn and Leusden</p>
        <p>Twenty sites this time slide along the southern flank of the Utrechtse Heuvelrug, where the <b>Stichtse Lustwarande</b> \u2014 the belt of country seats between De Bilt and Rhenen \u2014 shapes the landscape. It begins at Driebergen-Zeist station: the <b>De Reehorst</b> estate, the <b>Wulperhorst</b> country seat with its grand canal and ice cellar, and the string of <b>estates along the Driebergseweg</b> with their winding ponds by Zocher. Then stretches the centuries-old <b>Zeisterbos</b>, fed by hand-dug sprengen, and the woodland belt of the <b>Zeisterwoud</b> towards Soesterberg.</p>
        <p>At <b>Austerlitz</b> the history of Napoleon strikes: the village grew out of general De Marmont\u2019s army camp, where he had the 36-metre pyramid raised in 1804. The <b>Kozakkenput en Krakeling</b> recall the Cossacks of King William I and the bakery for the occupying army. Then follows the largest family estate in the Netherlands, <b>Den Treek-Henschoten</b>, with its ancient Treeker Eik, and the heath and drift-sand areas of <b>Heidestein, Bornia en Noordhout</b> where Drenthe heath sheep graze. Near Zeist lies the <b>De Breul</b> country seat with its landscape park and the gigantic C\u00e4sar bunker.</p>
        <p>Driebergen offers the moving <b>Beerschoten-Willinkshof</b>, where banker Willink bequeathed his park to the municipality, the <b>Rijsenburgsebos</b> with its heather garden and Lourdes grotto, the <b>Driebergsebos</b> of the former Sparrendaal, and the tiny, closed <b>De Kurk</b> with its Iberian snail. Around Maarn and Doorn lie <b>Mollenbos</b> and <b>Het Heihuis</b> with the ecoduct over the A12, the forest graves behind the <b>Nieuwe Algemene Begraafplaats</b>, the ancient <b>Ludenbos</b>, and the heath of <b>Hoog Moersbergen, Stameren, Bergweg en De Pol</b>. The series ends on the <b>De Zonheuvel</b> estate around the Maarten Maartenshuis.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
