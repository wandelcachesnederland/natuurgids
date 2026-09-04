# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mk

post = '''<div class="post">
      <div class="c-nl">
        <h3>Havezaten, buitenplaatsen en het broekland van de Schipbeek (1575–1594)</h3>
        <p class="post-meta">List 36 · Veluweflank, Salland en de IJsselvallei</p>
        <p>Twintig gebieden rond Twello, Olst, Raalte en Bathmen draaien om één onderliggende gelaagdheid: de <b>oeverwal</b> van de IJssel en de <b>dekzandruggen</b> daarachter. Op die droge, vruchtbare strook ontstond vanaf de achttiende eeuw de “gouden rand van Twello” — een lint van buitenplaatsen als <b>Bruggenbosch</b>, <b>Het Hunderen</b> en <b>Wezeveld</b>, waar rijk geworden Deventer en Zutphense families parken, lanen en stinzenflora achterlieten.</p>
        <p>Aan de Overijsselse kant vertelt de havezate hetzelfde verhaal in adellijk formaat. <b>Hoenlo</b> wordt al in 1233 genoemd en is met Boxbergen en De Haere een van de drie Olster havezaten die de negentiende-eeuwse sloop overleefden; <b>Dorth</b> (vermeld in 1311) is sinds 1986 van Natuurmonumenten. Rond Raalte en Heino liggen <b>’t Reelaer</b> (1608) en <b>De Vlaminkhorst</b>, en bij Olst <b>Zorgvliet</b> — gebouwd om “zorgen te laten vlieden”.</p>
        <p>Ten zuidoosten van Deventer draait alles om water. De <b>Schipbeek</b>, ooit de Marckelsche Becke, werd bevaarbaar gemaakt voor turf en goederen; de <b>Oude Schipbeek</b> is zo’n afgesneden, stil geworden meander. Het <b>Bathmense Broek</b> en de <b>Gooiermars</b> van De Bannink zijn jonge, natte weidevogelgebieden. En op <b>Oostermaet</b> — 550 hectare bos, jachthuizen en een eendenkooi — liggen zelfs kraters van V1-raketten verscholen tussen de bomen.</p>
      </div>
      <div class="c-en">
        <h3>Havezates, country seats and the brookland of the Schipbeek (1575–1594)</h3>
        <p class="post-meta">List 36 · Veluwe flank, Salland and the IJssel valley</p>
        <p>Twenty sites around Twello, Olst, Raalte and Bathmen turn on one underlying layering: the <b>levee</b> of the IJssel and the <b>cover-sand ridges</b> behind it. On that dry, fertile strip the “golden edge of Twello” arose from the eighteenth century — a ribbon of country seats such as <b>Bruggenbosch</b>, <b>Het Hunderen</b> and <b>Wezeveld</b>, where newly wealthy Deventer and Zutphen families left behind parks, avenues and stinzen flora.</p>
        <p>On the Overijssel side the havezate tells the same story in aristocratic scale. <b>Hoenlo</b> is mentioned as early as 1233 and, with Boxbergen and De Haere, is one of the three Olst havezates to survive the nineteenth-century demolitions; <b>Dorth</b> (mentioned in 1311) has belonged to Natuurmonumenten since 1986. Around Raalte and Heino lie <b>’t Reelaer</b> (1608) and <b>De Vlaminkhorst</b>, and near Olst <b>Zorgvliet</b> — built to “let worries fly”.</p>
        <p>South-east of Deventer everything turns on water. The <b>Schipbeek</b>, once the Marckelsche Becke, was made navigable for turf and goods; the <b>Oude Schipbeek</b> is one such cut-off, now silent meander. The <b>Bathmense Broek</b> and De Bannink’s <b>Gooiermars</b> are young, wet meadow-bird areas. And on <b>Oostermaet</b> — 550 hectares of woodland, shooting lodges and a duck decoy — craters from V1 rockets lie hidden among the trees.</p>
      </div>
    </div>'''

mk.blog(post)
print('blog toegevoegd')
