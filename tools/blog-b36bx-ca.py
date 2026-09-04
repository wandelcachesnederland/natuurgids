# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Van de Blauwe Molen tot de Soesterduinen (1655–1674)</h3>
        <p class="post-meta">List 36 · Zuid-Holland: Kaag en Braassem, Leiden, Wassenaar, het Groene Hart — en Utrecht: de Lopikerwaard en Soest</p>
        <p>Twintig gebieden trekken een boog door het veenland van Zuid-Holland en de zandgronden van Utrecht. Het begint klein en blauw: de <b>Blauwe Molen</b> in Rijpwetering, een achthoekige poldermolen met een zeldzame overtoom, en het natuurlijke <b>Braassemermeer</b> dat na de ontginningen in omvang verdubbelde. In Zoeterwoude ligt de <b>Geerpolder</b>, die pas in 1865 — als laatste polder van Zuid-Holland — met stoom werd drooggemalen.</p>
        <p>De Wassenaarse strandwallen brengen buitenplaatsen: <b>Rust en Vreugd</b>, waar reder Van Ommeren liefdadigheid bedreef, en de koninklijke <b>De Horsten</b> van prins Frederik, Wilhelmina en nu koning Willem-Alexander. Daartussen liggen de middeleeuwse <b>Duivenvoordse Polder</b> en de tragische buitenplaats <b>Rosenburgh</b>, waar het Marot-paleis van de jonge Jacob Jan na zijn dood in 1730 volledig werd gesloopt. Bij Leidschendam groeide uit oude weilanden de jonge <b>Leidschendammerhout</b> met Schotse hooglanders en vogelplas Starrevaart.</p>
        <p>Het Groene Hart voert langs de kades en dijken: <b>Westeinde</b> bij Stompwijk, het weidevogelreservaat <b>De Wilck</b> met zijn kleine zwanen, de <b>Rijndijk</b> met het oude jaagpad van de trekschuit, de <b>Kruiskade</b> met het spookverlaat en de <b>Spijkerboorsekade en Coppierenkade</b> tussen Alphen en de Boskoopse kwekerijen. Bij Delft ligt recreatiebos <b>De Haaglanden</b>, bij Gouda groeide op een puinstort het bloemrijke <b>Noorderhout</b>, en daarna strekken de dertien <b>Reeuwijkse Plassen</b> zich uit. Het <b>Steinse Groen</b> verbindt ze met de Krimpenerwaard.</p>
        <p>De sprong naar Utrecht is een sprong naar zand en geschiedenis: de cope-ontginning van <b>Benschop</b> in de Lopikerwaard, het stuifzand van de <b>Soesterduinen</b> en het oude buurtschap <b>De Birkt</b>, waar boeren barrièreduinen met eiken opwierpen tegen het oprukkende zand.</p>
      </div>
      <div class="c-en">
        <h3>From the Blauwe Molen to the Soesterduinen (1655–1674)</h3>
        <p class="post-meta">List 36 · South Holland: Kaag en Braassem, Leiden, Wassenaar, the Groene Hart — and Utrecht: the Lopikerwaard and Soest</p>
        <p>Twenty sites trace an arc through the peat country of South Holland and the sandy soils of Utrecht. It begins small and blue: the <b>Blauwe Molen</b> in Rijpwetering, an octagonal polder mill with a rare overtoom, and the natural <b>Braassemermeer</b>, which doubled in size after the reclamations. In Zoeterwoude lies the <b>Geerpolder</b>, drained by steam only in 1865 — as the last polder of South Holland.</p>
        <p>The Wassenaar beach ridges bring country seats: <b>Rust en Vreugd</b>, where shipowner Van Ommeren practised charity, and the royal <b>De Horsten</b> of Prince Frederik, Wilhelmina and now King Willem-Alexander. Between them lie the medieval <b>Duivenvoordse Polder</b> and the tragic estate of <b>Rosenburgh</b>, where the Marot palace of the young Jacob Jan was completely demolished after his death in 1730. Near Leidschendam the young <b>Leidschendammerhout</b> grew out of old meadows, with Highland cattle and bird lake Starrevaart.</p>
        <p>The Groene Hart runs along banks and dikes: <b>Westeinde</b> near Stompwijk, the meadow bird reserve <b>De Wilck</b> with its Bewick\u2019s swans, the <b>Rijndijk</b> with the old towpath of the trekschuit, the <b>Kruiskade</b> with its \u2019ghost lock\u2019, and the <b>Spijkerboorsekade en Coppierenkade</b> between Alphen and the Boskoop nurseries. Near Delft lies recreation woodland <b>De Haaglanden</b>, near Gouda the flower-rich <b>Noorderhout</b> grew on a rubble dump, and then the thirteen <b>Reeuwijkse Plassen</b> stretch out. <b>Het Steinse Groen</b> links them to the Krimpenerwaard.</p>
        <p>The leap to Utrecht is a leap to sand and history: the cope reclamation of <b>Benschop</b> in the Lopikerwaard, the drift sand of the <b>Soesterduinen</b>, and the old hamlet <b>De Birkt</b>, where farmers raised barrier dunes of oak against the advancing sand.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
