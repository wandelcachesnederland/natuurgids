# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Van Lutterzand tot Lonnekerberg (1615–1634)</h3>
        <p class="post-meta">List 36 · Noordoost-Twente: Oldenzaal, Losser, De Lutte en Enschede</p>
        <p>Twintig gebieden volgen de stuwwal van Enschede-Oldenzaal naar het zuiden, van de <b>Hakenberg</b> en de <b>Tankenberg</b> — op landgoed Egheria, het hoogste punt van Overijssel — tot de <b>Lonnekerberg</b> bij Enschede, waar buitenplaats <b>Val Sugana</b> haar Italiaanse naam aan de Valsugana in Trentino dankt. Het is een landschap dat door de Twentse textiel voortdurend gevormd werd: het arboretum <b>Poort Bulten</b> (Springer, 1912), het productiebos <b>Haagse Bos</b> van de familie Blijdenstein, en de afgegraven zandplassen van <b>Het Hulsbeek</b>, waarmee woonwijk De Thij werd gebouwd.</p>
        <p>De oude marke De Lutte is in vier <b>heurnes</b> verdeeld — Rooderheurne, Molterheurne, Elfterheurne en Hengelheurne — en op <b>Molterheurne</b> zaait Natuurmonumenten nog elk jaar winterrogge op de oude es. Even noordelijk liggen de twee werelden van <b>Boerskotten</b>: een landgoed dat door de A1 in tweeën wordt gesneden en met een ecoduct — inclusief aanpassing voor de kamsalamander — weer verbonden is.</p>
        <p>De rijkste bossen van deze reeks zijn de natste. Het <b>Smoddebos</b> herbergt eiken-haagbeukenbos, een bostype dat je eigenlijk alleen in Zuid-Limburg verwacht, en het <b>Hoge Venterink</b> bezit een natuurlijke populatie van meer dan dertig bergiepen — uniek in Nederland. En dan is er <b>meester Bernink</b>, de onderwijzer die met Natura Docet het oudste regionale natuurmuseum van Nederland stichtte en naar wie het Berninkholt is vernoemd.</p>
      </div>
      <div class="c-en">
        <h3>From the Lutterzand to the Lonnekerberg (1615–1634)</h3>
        <p class="post-meta">List 36 · North-east Twente: Oldenzaal, Losser, De Lutte and Enschede</p>
        <p>Twenty sites follow the Enschede-Oldenzaal ice-pushed ridge southwards, from the <b>Hakenberg</b> and the <b>Tankenberg</b> — on the Egheria estate, the highest point of Overijssel — to the <b>Lonnekerberg</b> near Enschede, where the country seat <b>Val Sugana</b> owes its Italian name to the Valsugana in Trentino. It is a landscape continually shaped by Twente textiles: the <b>Poort Bulten</b> arboretum (Springer, 1912), the <b>Haagse Bos</b> production forest of the Blijdenstein family, and the sand-extraction lakes of <b>Het Hulsbeek</b>, with which the De Thij estate was built.</p>
        <p>The old marke of De Lutte is divided into four <b>heurnes</b> — Rooderheurne, Molterheurne, Elfterheurne and Hengelheurne — and on <b>Molterheurne</b> Natuurmonumenten still sows winter rye on the old es each year. A little further north lie the two worlds of <b>Boerskotten</b>: an estate cut in two by the A1 and reconnected by a wildlife overpass, complete with an adaptation for the great crested newt.</p>
        <p>The richest woods of this series are the wettest. The <b>Smoddebos</b> holds oak-hornbeam woodland, a type you would otherwise expect only in South Limburg, and the <b>Hoge Venterink</b> possesses a natural population of more than thirty wych elms — unique in the Netherlands. And then there is <b>meester Bernink</b>, the schoolteacher who founded Natura Docet, the oldest regional nature museum in the Netherlands, after whom the Berninkholt is named.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
