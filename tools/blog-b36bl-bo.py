# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Stuwwallen, grafheuvels en de Dinkel (1595–1614)</h3>
        <p class="post-meta">List 36 · Noordoost-Twente: Ootmarsum, Tubbergen en Denekamp</p>
        <p>Twintig gebieden in Noordoost-Twente draaien om één geologische grondlijn: de <b>stuwwallen</b> die het Scandinavische landijs in het Saalien opstuwde, van de <b>Kuiperberg</b> bij Ootmarsum tot de rug naar Uelsen in Duitsland. Op die droge, hoge ruggen ontstonden de eerste woonplekken van Twente — en precies daar liggen dan ook de <b>grafheuvels</b> van de <b>Vasserheide</b> en het <b>Haarlergrafveld</b>, heidevelden waar het beheer de prehistorische heuvels bewust vrijhoudt van opslag.</p>
        <p>Waar de stuwwal water kwijt wil, ontstaat aan de voet een heel ander landschap. Uit de flanken sijpelt <b>kwel</b> die de <b>Bergvennen</b>, de <b>Hazelbekke</b> en het Natura 2000-complex <b>Achter de Voort, Agelerbroek &amp; Voltherbroek</b> voedt — elzenbroeken vol boomkikker en kamsalamander. Bij Denekamp vormt de <b>Dinkel</b> de levensader: langs het <b>Lutterzand</b> kon ze haar meanderloop behouden, en op landgoed <b>Singraven</b> (1381) drijft ze een watermolen met drie raderen uit 1448.</p>
        <p>En dan de menselijke gelaagdheid. De <b>Hunenborg</b> is een ringwalburg uit omstreeks 1050, waarschijnlijk gebouwd in opdracht van de bisschop van Utrecht; <b>Herinckhave</b> werd in 1532 “gevrijd” en <b>Erve Scholten Linde</b> draagt het jaartal 1638 in zijn niendeur. Tegenover al die monumenten staat <b>Gammelke</b> — een marke zonder kerk, café of kern, al bewoond vóór het begin van de jaartelling.</p>
      </div>
      <div class="c-en">
        <h3>Ice-pushed ridges, burial mounds and the Dinkel (1595–1614)</h3>
        <p class="post-meta">List 36 · North-east Twente: Ootmarsum, Tubbergen and Denekamp</p>
        <p>Twenty sites in North-east Twente turn on one geological line: the <b>ice-pushed ridges</b> shoved up by Scandinavian land ice in the Saalian, from the <b>Kuiperberg</b> near Ootmarsum to the ridge running to Uelsen in Germany. On those dry, high ridges the first settlements of Twente arose — and precisely there lie the <b>burial mounds</b> of the <b>Vasserheide</b> and the <b>Haarlergrafveld</b>, heathlands where management deliberately keeps the prehistoric mounds free of saplings.</p>
        <p>Where the ridge sheds its water, a different landscape forms at its foot. From the flanks seeps <b>groundwater</b> feeding the <b>Bergvennen</b>, the <b>Hazelbekke</b> and the Natura 2000 complex of <b>Achter de Voort, Agelerbroek &amp; Voltherbroek</b> — alder carrs full of tree frog and great crested newt. Near Denekamp the <b>Dinkel</b> is the lifeline: along the <b>Lutterzand</b> it kept its meandering course, and at the <b>Singraven</b> estate (1381) it drives a three-wheeled water mill of 1448.</p>
        <p>Then the human layering. The <b>Hunenborg</b> is a ring fort of around 1050, probably built on the orders of the bishop of Utrecht; <b>Herinckhave</b> was “freed” in 1532 and <b>Erve Scholten Linde</b> carries the year 1638 in its kitchen door. Against all those monuments stands <b>Gammelke</b> — a marke with no church, pub or centre, inhabited since before the start of the common era.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
