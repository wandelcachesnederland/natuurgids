# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Van de Lonnekerberg tot de Kagerplassen (1635–1654)</h3>
        <p class="post-meta">List 36 · Twente: Lonneker, Enschede, Hengelo en Losser — en Zuid-Holland: Leiden en de Kagerplassen</p>
        <p>Twintig gebieden voeren van de stuwwal van Enschede naar het veenland van Zuid-Holland. We sluiten Noordoost-Twente af op de <b>Lonnekerberg</b> — met zestig meter het hoogste punt rond Enschede, met zijn heldere bronnen en het graf van textielfabrikant Blijdenstein — en dalen af langs de <b>Landgoederen van Textiel</b>: het sterrenbos van <b>De Wildernis</b>, het acht eeuwen oude <b>Hof Espelo</b> en de parken van <b>\u2019t Bouwhuis</b>, <b>De Vieker</b> en <b>De Hooge Boekel</b>, waar Pieter Wattez een T-vormige zwem- en roeivijver ontwierp.</p>
        <p>Twekkelo draagt zijn landgoederen nog altijd met trots: buitenplaats <b>Het Stroot</b> met het glasheldere <b>Zwarte Ven</b>, en tussen Losser en Enschede liggen verborgen plekken als het <b>Galgenven</b> — alleen vanaf de Oude Losserseweg te zien — en <b>Lindermaten</b>, waar Natuurmonumenten een middeleeuwse <b>landweer</b> weer zichtbaar maakt. De erfnamen sluiten de reeks: <b>Penninkskotten</b>, een oude kamp in de woeste gronden, en <b>De Krabbe</b> bij Beuningen, waar cabaretier Herman Finkers een boerderij afbrak en met het oude materiaal een nieuw huis bouwde.</p>
        <p>De sprong naar het westen is een sprong naar water en buitenplaatsen. Bij Katwijk begint het met de <b>Pan van Persijn</b>, een jachtgebied van de Heren van Persijn met nog zichtbare resten van de Atlantikwall, en in Leiden wandelen we door <b>De Leidse Hout</b>, het volkspark dat in de crisistijd van 1931 door werklozen werd aangelegd. Warmond biedt een trio buitenplaatsen — <b>Oud Poelgeest</b> van Herman Boerhaave, het ensemble <b>Oostergeest</b> en het sprookjesbos van <b>Huys te Warmont</b> — en daarna strekken de <b>Kagerplassen</b> zich uit: middeleeuwse veenplassen, boezemwater van Rijnland en het oudste watersportgebied van Nederland.</p>
      </div>
      <div class="c-en">
        <h3>From the Lonnekerberg to the Kagerplassen (1635–1654)</h3>
        <p class="post-meta">List 36 · Twente: Lonneker, Enschede, Hengelo and Losser — and South Holland: Leiden and the Kagerplassen</p>
        <p>Twenty sites lead from the Enschede ice-pushed ridge to the peat country of South Holland. We close north-east Twente on the <b>Lonnekerberg</b> — at sixty metres the highest point around Enschede, with its clear springs and the grave of textile manufacturer Blijdenstein — and descend along the <b>Landgoederen van Textiel</b>: the star wood of <b>De Wildernis</b>, the eight-hundred-year-old <b>Hof Espelo</b>, and the parks of <b>\u2019t Bouwhuis</b>, <b>De Vieker</b> and <b>De Hooge Boekel</b>, where Pieter Wattez designed a T-shaped swimming and rowing pond.</p>
        <p>Twekkelo still carries its estates with pride: the country seat <b>Het Stroot</b> with the crystal-clear <b>Zwarte Ven</b>, and between Losser and Enschede lie hidden places such as the <b>Galgenven</b> — visible only from the Oude Losserseweg — and <b>Lindermaten</b>, where Natuurmonumenten is making a medieval <b>landweer</b> visible again. The farm names close the series: <b>Penninkskotten</b>, an old kamp in the wild grounds, and <b>De Krabbe</b> near Beuningen, where the comedian Herman Finkers dismantled a farmhouse and built a new house from the old materials.</p>
        <p>The leap to the west is a leap to water and country seats. Near Katwijk it begins with the <b>Pan van Persijn</b>, a hunting ground of the Heren van Persijn with still-visible remains of the Atlantikwall, and in Leiden we walk through <b>De Leidse Hout</b>, the people\u2019s park laid out by the unemployed during the crisis years from 1931. Warmond offers a trio of country seats — <b>Oud Poelgeest</b> of Herman Boerhaave, the <b>Oostergeest</b> ensemble and the fairytale wood of <b>Huys te Warmont</b> — and then the <b>Kagerplassen</b> stretch out: medieval peat lakes, boezem water of Rijnland and the oldest water-sports area in the Netherlands.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
