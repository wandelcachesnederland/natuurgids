# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Van de Blanke Waal tot de Bergvlietse Kade: slikken, forten en kaden (1995–2014)</h3>
        <p class="post-meta">List 36 · Zuid-Holland: Zwartewaal, Hellevoetsluis, Spijkenisse, Simonshaven, Goedereede, Stellendam, Zuidland, Goudswaard, Strijen, Numansdorp en Vlist</p>
        <p>Twintig gebieden trekken deze keer van de polders van Zwartewaal via de fortenlinie naar de Haringvlietslikken en de waard. Het begint bij het <b>Blanke Waal</b> — een wiel na een dijkdoorbraak met Cetti’s zanger — en het weidevogelreservaat <b>Hillenhoek</b> tussen de maisakkers. De <b>Bosobjecten Voorne</b> tonen de groene dooradering van Staatsbosbeheer, van Mallebos tot Spuigors, en <b>Fort Noorddijk</b> (1884) bewaakt met Penserdijk de Monden der Maas. Het <b>Quackgors</b> achter de Haringvlietsluizen is voormalig getijdengebied met broedeenden en reeën. Bij Hellevoetsluis volgt het <b>Graswegbos</b> met zijn burgernatuurgebied, het plasdrasse <b>Waalhoek</b> rond het Katerwaaltje uit circa 1350, en de 300 hectare grote <b>Bernisse</b> — zeven kilometer voormalige rivier met strandjes en surfmeer.</p>
        <p>Dan de veenweiden van <b>Biert</b> met het 12,4 kilometer lange Biertpad, en het <b>Mallebos</b> van Spijkenisse op het in 1164 verdronken Schiekamp. Op Goeree-Overflakkee liggen de dynamische <b>Kwade Hoek</b> met zijn vogelkijkhut, de <b>Kop van Goeree</b> met ’t Kiekgat en de Westhoofdvallei, en het vogelreservaat <b>Scheelhoek</b> met observatorium TIJ als metershoog sterns-ei. De <b>Bosobjecten Stellendam</b> blijken een eerlijke gidsnaam zonder eigen terrein — wandelaars wijken uit naar Scheelhoekbos en Zuiderdiepgorzen. De <b>Beningerslikken</b> bieden een rondwandeling van vijf kilometer met trekpontje op de trekroute.</p>
        <p>De reeks eindigt met de <b>Korendijkse Slikken</b> — bijna 500 hectare zoetwatergetij met zeearend, alleen open van juli tot november — de <b>Kreken van de Hoekse Waard</b> met Oudeland van Strijen en Bekade Gorzen, de <b>Bosobjecten Hoekse Waard</b> met Zuid-Beijerlandse Bos en IJsvogelroute, de <b>Hennepakkers</b> als leesteken van het touwverleden, en de <b>Bergvlietse Kade</b> — ruim drie kilometer oudste onverharde kade met wiebelig vlonderpad.</p>
      </div>
      <div class="c-en">
        <h3>From the Blanke Waal to the Bergvlietse Kade: mudflats, forts and embankments (1995–2014)</h3>
        <p class="post-meta">List 36 · Zuid-Holland: Zwartewaal, Hellevoetsluis, Spijkenisse, Simonshaven, Goedereede, Stellendam, Zuidland, Goudswaard, Strijen, Numansdorp and Vlist</p>
        <p>Twenty sites this time travel from the Zwartewaal polders via the fortress line to the Haringvliet mudflats and the waard. It starts at the <b>Blanke Waal</b> — a breach pool with Cetti’s warbler — and the <b>Hillenhoek</b> meadow-bird reserve among the maize fields. The <b>Voorne Forest Objects</b> show Staatsbosbeheer’s green veining, from Mallebos to Spuigors, and <b>Fort Noorddijk</b> (1884) guards the Meuse mouths together with Penserdijk. The <b>Quackgors</b> behind the Haringvliet sluices is former tidal land with breeding ducks and roe deer. Near Hellevoetsluis follow the <b>Graswegbos</b> with its citizen nature area, the splashy-wet <b>Waalhoek</b> around the Katerwaaltje of around 1350, and the 300-hectare <b>Bernisse</b> — seven kilometres of former river with beaches and surf lake.</p>
        <p>Then the peat meadows of <b>Biert</b> with the 12.4-kilometre Biertpad, and the Spijkenisse <b>Mallebos</b> on the Schiekamp drowned in 1164. On Goeree-Overflakkee lie the dynamic <b>Kwade Hoek</b> with its bird hide, the <b>Kop van Goeree</b> with ’t Kiekgat and the Westhoofdvallei, and the <b>Scheelhoek</b> bird reserve with the TIJ observatory as a metres-high tern egg. The <b>Stellendam Forest Objects</b> turn out to be an honest guide name without terrain of their own — walkers divert to Scheelhoekbos and Zuiderdiepgorzen. The <b>Beningerslikken</b> offer a five-kilometre circuit with pull ferry on the flyway.</p>
        <p>The series ends with the <b>Korendijkse Slikken</b> — almost 500 hectares of freshwater tide with white-tailed eagle, open July to November only — the <b>Hoeksche Waard Creeks</b> with Oudeland van Strijen and Bekade Gorzen, the <b>Hoeksche Waard Forest Objects</b> with Zuid-Beijerlandse Bos and Kingfisher route, the <b>Hennepakkers</b> as a legible trace of the rope past, and the <b>Bergvlietse Kade</b> — over three kilometres of oldest unpaved embankment with a wobbly boardwalk.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
