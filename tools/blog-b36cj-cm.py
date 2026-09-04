# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Van de Valleikanaal naar de zuidflank van de Heuvelrug (1715\u20131734)</h3>
        <p class="post-meta">List 36 · Utrecht: Maarn, Maarsbergen, Woudenberg, Scherpenzeel, Renswoude, Cothen, Langbroek, Doorn en Leersum</p>
        <p>Twintig gebieden trekken deze keer van de Gelderse Vallei omhoog naar de zuidflank van de Utrechtse Heuvelrug. Rond Maarn en Maarsbergen begint het met landgoed <b>Huis te Maarn</b>, de droge <b>\u2019t Stort</b> en buitenplaats <b>Anderstein</b> aan de spoorlijn. Dan zakken we af naar het Valleikanaal: het <b>Broekerbos</b> tussen Woudenberg en Scherpenzeel, het landgoed <b>Scherpenzeel-Berkhorst</b>, de heideontginning <b>Breeschoten</b> met de Breeschoterplas, en landgoed <b>Lambalgen en Het Hek</b> met zijn monumentale toegangshekken.</p>
        <p>Dwars door de vallei loopt de <b>Grebbelinie</b>, de achttiende-eeuwse waterlinie die in de meidagen van 1940 als Valleistelling opnieuw in stelling werd gebracht; langs de groene dijken liggen forten als de Buursteeg en Daatselaar. Bij Renswoude sluit het <b>Kasteelbos Renswoude</b> aan, met zijn 700 meter lange Grand Canal en 150 jaar oude loofbomen. Dan volgt het kastelenlint langs de Langbroekerwetering: ridderhofstad <b>Hardenbroek</b>, buitenplaats <b>Leeuwenburgh</b> met zijn zichtassen, en <b>Moersbergen</b> met het neogotische slot van d\u2019Ablaing. Aan de Kromme Rijn ligt het omgrachte <b>De Grote Maat</b>.</p>
        <p>De reeks eindigt op de Heuvelrug bij Doorn en Leersum: de <b>Kaapse Bossen</b> met uitkijktoren De Kaap, het smeltwaterdal <b>Darthuizen en Darthuizerberg</b>, buitenplaats <b>Voreneng</b>, ridderhofstad <b>Broekhuizen</b>, de heide en het hakhout van <b>Breeveen en Dartheide</b>, de <b>Lombokbossen</b> die na de valwind van 2021 herstellen, en het <b>Leersumse Veld en Plassen</b> \u2014 het stilste plekje van Nederland.</p>
      </div>
      <div class="c-en">
        <h3>From the Valleikanaal up to the southern flank of the ridge (1715\u20131734)</h3>
        <p class="post-meta">List 36 · Utrecht: Maarn, Maarsbergen, Woudenberg, Scherpenzeel, Renswoude, Cothen, Langbroek, Doorn and Leersum</p>
        <p>Twenty sites this time climb from the Gelderse Vallei up to the southern flank of the Utrechtse Heuvelrug. Around Maarn and Maarsbergen it begins with the <b>Huis te Maarn</b> estate, the dry <b>\u2019t Stort</b> and the <b>Anderstein</b> country seat on the railway line. Then we descend to the Valleikanaal: the <b>Broekerbos</b> between Woudenberg and Scherpenzeel, the <b>Scherpenzeel-Berkhorst</b> estate, the heath reclamation <b>Breeschoten</b> with the Breeschoterplas, and the <b>Lambalgen en Het Hek</b> estate with its monumental entrance gates.</p>
        <p>Straight through the valley runs the <b>Grebbelinie</b>, the eighteenth-century water line brought back into position as the Valleistelling during the May days of 1940; along the green dikes lie forts such as Buursteeg and Daatselaar. At Renswoude the <b>Kasteelbos Renswoude</b> links up, with its 700-metre Grand Canal and 150-year-old broadleaf trees. Then follows the castle belt along the Langbroekerwetering: the knightly manor <b>Hardenbroek</b>, the <b>Leeuwenburgh</b> country seat with its sightlines, and <b>Moersbergen</b> with the neo-gothic castle of d\u2019Ablaing. On the Kromme Rijn lies the moated <b>De Grote Maat</b>.</p>
        <p>The series ends on the ridge at Doorn and Leersum: the <b>Kaapse Bossen</b> with the De Kaap lookout tower, the meltwater valley <b>Darthuizen en Darthuizerberg</b>, the <b>Voreneng</b> country seat, the knightly manor <b>Broekhuizen</b>, the heath and coppice of <b>Breeveen en Dartheide</b>, the <b>Lombokbossen</b> recovering after the 2021 downburst, and the <b>Leersumse Veld en Plassen</b> \u2014 the quietest spot of the Netherlands.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
