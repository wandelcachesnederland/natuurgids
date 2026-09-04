# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Van de Japanse bosjes tot de forten van de Waterlinie (1675\u20131694)</h3>
        <p class="post-meta">List 36 · Utrecht: Amersfoort, Soest, Soesterberg, De Bilt, Zeist en Bunnik — met een uitstap naar de Gelderse Vallei</p>
        <p>Twintig gebieden scharen zich rond de Utrechtse Heuvelrug en de Gelderse Vallei. Het begint westelijk van Amersfoort, waar <b>Birkhoven en Bokkeduinen</b> volksmond \u2019Japanse bosjes\u2019 werd — Jan Cock Blomhoff, de laatste opperhoofd van Deshima, liet er in 1824 zijn landhuis bouwen. Even verderop strekt landgoed <b>De Paltz</b> zich uit, vernoemd naar Duitse vluchtelingen uit de Palts, en herinneren <b>Soesterberg</b>, <b>De Vlasakkers</b> en het <b>Oude Kamp</b> aan een militaire geschiedenis van vliegkamp, oefenterrein en het zomerkamp van Willem I uit 1818.</p>
        <p>De Amersfoortse bossen tonen hun reliëf: het glooiende <b>Klein Zwitserland</b> op de Amersfoortse Berg, landgoed <b>Nimmerdor</b> dat jonkheer Everard Meyster \u2019nimmer dor\u2019 liet aanleggen, en het <b>Lockhorsterbos</b> — in 1927 de allereerste aankoop van Het Utrechts Landschap. Op landgoed Den Treek-Henschoten liggen de stuifkliffen en Ringheuvels van de <b>Bossen achter Rusthof</b>. In de Gelderse Vallei volgen het natte landgoed <b>Erica-Noord</b> met zijn vleesetende zonnedauw en de diepe kwelwaterplas <b>Grote Veenderplas</b>.</p>
        <p>Rond De Bilt liggen de buitenplaatsen aaneengeregen als een lustwarande: <b>Houdringe, Beerschoten en Heyntjeskamp</b>, het stuifzand van <b>Panbos en Tannenberg</b> met zijn ransuilen, het groene villadorp <b>Bosch en Duin</b>, <b>Dijnselburg en Vollenhove</b>, en de landgoederen <b>Sandwyck</b> en <b>Oostbroek</b> — het oudste landgoed van De Bilt, met een kloostergeschiedenis die teruggaat tot 1122. Tussen De Bilt en Bunnik ligt <b>Niënhof</b> op de overgang naar het Kromme Rijngebied.</p>
        <p>De reeks eindigt bij het water en het staal van de Nieuwe Hollandse Waterlinie: het grootste fort van de linie, <b>Fort bij Rijnauwen</b>, een waar paddenstoelenparadijs met zeven soorten vleermuizen, en <b>Fort bij Vechten</b>, gebouwd op de Romeinse legerplaats Fectio en thans het onderkomen van het Waterliniemuseum.</p>
      </div>
      <div class="c-en">
        <h3>From the Japanese groves to the Waterline forts (1675\u20131694)</h3>
        <p class="post-meta">List 36 · Utrecht: Amersfoort, Soest, Soesterberg, De Bilt, Zeist and Bunnik — with an excursion into the Gelderse Vallei</p>
        <p>Twenty sites gather around the Utrechtse Heuvelrug and the Gelderse Vallei. It begins west of Amersfoort, where <b>Birkhoven en Bokkeduinen</b> became popularly known as the \u2019Japanese groves\u2019 — Jan Cock Blomhoff, the last opperhoofd of Deshima, had his mansion built there in 1824. Nearby stretches the <b>De Paltz</b> estate, named after German refugees from the Palatinate, while <b>Soesterberg</b>, <b>De Vlasakkers</b> and the <b>Oude Kamp</b> recall a military past of airfield, training ground and the summer camp of King William I of 1818.</p>
        <p>The Amersfoort woods show their relief: the rolling <b>Klein Zwitserland</b> on the Amersfoortse Berg, the <b>Nimmerdor</b> estate that esquire Everard Meyster made \u2019never dry\u2019, and the <b>Lockhorsterbos</b> — in 1927 the very first purchase of Het Utrechts Landschap. On the Den Treek-Henschoten estate lie the drift-sand cliffs and Ringheuvels of the <b>Bossen achter Rusthof</b>. In the Gelderse Vallei follow the wet <b>Erica-Noord</b> estate with its carnivorous sundew and the deep seepage lake <b>Grote Veenderplas</b>.</p>
        <p>Around De Bilt the country seats string together like a pleasure belt: <b>Houdringe, Beerschoten en Heyntjeskamp</b>, the drift sand of <b>Panbos en Tannenberg</b> with its long-eared owls, the green villa village <b>Bosch en Duin</b>, <b>Dijnselburg en Vollenhove</b>, and the estates <b>Sandwyck</b> and <b>Oostbroek</b> — the oldest estate of De Bilt, with a monastic history going back to 1122. Between De Bilt and Bunnik lies <b>Niënhof</b> on the transition to the Kromme Rijn area.</p>
        <p>The series ends at the water and the steel of the Nieuwe Hollandse Waterlinie: the largest fort of the line, <b>Fort bij Rijnauwen</b>, a true mushroom paradise with seven species of bat, and <b>Fort bij Vechten</b>, built on the Roman camp Fectio and now home to the Waterliniemuseum.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
