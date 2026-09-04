/**
 * Nature Reserve Guide — The Netherlands
 * Main JavaScript functionality
 */

(function() {
  'use strict';

  // Nature reserve data - loaded from external JSON chunks
  var natureReserves = [];
  var dataChunks = [
    'nature-data/reserves-1-100.json',
    'nature-data/reserves-101-200.json',
    'nature-data/reserves-201-300.json',
    'nature-data/reserves-301-400.json',
    'nature-data/reserves-401-500.json',
    'nature-data/reserves-501-600.json',
    'nature-data/reserves-601-700.json',
    'nature-data/reserves-701-800.json',
    'nature-data/reserves-801-901.json',
    'nature-data/reserves-902-1001.json',
    'nature-data/reserves-1002-1031.json',
    'nature-data/reserves-1032-1131.json',
    'nature-data/reserves-1132-1231.json',
    'nature-data/reserves-1232-1331.json',
    'nature-data/reserves-1332-1431.json',
    'nature-data/reserves-1432-1531.json',
    'nature-data/reserves-1532-1631.json',
    'nature-data/reserves-1632-1731.json',
    'nature-data/reserves-1732-1831.json'
  ];

  // Load nature reserve data from JSON chunks
  function loadNatureData() {
    var totalChunks = dataChunks.length;

    // Load all chunks in parallel
    var promises = dataChunks.map(function(chunkUrl) {
      return fetch(chunkUrl)
        .then(function(response) {
          if (!response.ok) {
            throw new Error('Failed to load chunk: ' + chunkUrl);
          }
          return response.json();
        });
    });

    Promise.all(promises)
      .then(function(results) {
        // Combine all chunks into single array
        for (var i = 0; i < results.length; i++) {
          natureReserves = natureReserves.concat(results[i]);
        }
        console.log('Loaded ' + natureReserves.length + ' nature reserves from ' + totalChunks + ' chunks');
      })
      .catch(function(error) {
        console.error('Error loading nature reserves:', error);
      });
  }

  // Get all nature reserves
  function getNatureReserves() {
    return natureReserves;
  }

  // Find a reserve by ID
  function getReserveById(id) {
    for (var i = 0; i < natureReserves.length; i++) {
      if (natureReserves[i].id === id) {
        return natureReserves[i];
      }
    }
    return null;
  }

  // Find a reserve by number
  function getReserveByNumber(number) {
    for (var i = 0; i < natureReserves.length; i++) {
      if (natureReserves[i].number === number) {
        return natureReserves[i];
      }
    }
    return null;
  }

  // Search reserves by name
  function searchReserves(query, lang) {
    var results = [];
    var searchTerm = query.toLowerCase();
    
    for (var i = 0; i < natureReserves.length; i++) {
      var reserve = natureReserves[i];
      var name = reserve.name || '';
      var langData = lang === 'en' ? reserve.en : reserve.nl;
      var description = (langData && langData.description) || '';
      
      if (name.toLowerCase().indexOf(searchTerm) !== -1 || 
          description.toLowerCase().indexOf(searchTerm) !== -1) {
        results.push(reserve);
      }
    }
    
    return results;
  }

  // Expose functions globally
  window.NatureGuide = {
    loadData: loadNatureData,
    getReserves: getNatureReserves,
    getById: getReserveById,
    getByNumber: getReserveByNumber,
    search: searchReserves
  };

  // Load data on initialization
  loadNatureData();

  // Language toggle functionality
  function initLanguageToggle() {
    document.addEventListener('click', function(e) {
      var target = e.target && e.target.closest ? e.target.closest('#langswitch .langtab') : null;
      if (!target) return;

      var isEnglish = target.getAttribute('data-lang') === 'en';
      document.body.classList.toggle('lang-en', isEnglish);

      var tabs = document.querySelectorAll('#langswitch .langtab');
      for (var i = 0; i < tabs.length; i++) {
        tabs[i].classList.toggle('on', tabs[i] === target);
      }

      try {
        localStorage.setItem('ng-lang', isEnglish ? 'en' : 'nl');
      } catch (err) {
        // localStorage not available
      }
    });

    // Restore saved language preference on load
    try {
      if (localStorage.getItem('ng-lang') === 'en') {
        document.body.classList.add('lang-en');
        var englishTab = document.querySelector('#langswitch .langtab[data-lang="en"]');
        if (englishTab) {
          englishTab.classList.add('on');
          var dutchTab = document.querySelector('#langswitch .langtab[data-lang="nl"]');
          if (dutchTab) {
            dutchTab.classList.remove('on');
          }
        }
      }
    } catch (err) {
      // localStorage not available
    }
  }

  // Tab switching functionality (List / Blog / Warnings)
  var TABS = ['list', 'blog', 'warn'];

  function applyTab(name) {
    if (TABS.indexOf(name) === -1) name = 'list';
    document.body.classList.toggle('show-blog', name === 'blog');
    document.body.classList.toggle('show-warn', name === 'warn');
    var buttons = document.querySelectorAll('#tabbar .tabbtn');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].classList.toggle('on', buttons[i].getAttribute('data-tab') === name);
    }
  }

  function initTabSwitcher() {
    document.addEventListener('click', function(e) {
      var button = e.target && e.target.closest ? e.target.closest('#tabbar .tabbtn') : null;
      if (!button) return;

      var name = button.getAttribute('data-tab') || 'list';
      applyTab(name);

      try {
        localStorage.setItem('ng-tab', name);
      } catch (err) {
        // localStorage not available
      }
    });

    // Restore saved tab preference on load
    try {
      var saved = localStorage.getItem('ng-tab');
      if (saved) applyTab(saved);
    } catch (err) {
      // localStorage not available
    }
  }

  // ---- Warnings tab: collect every card carrying a warning ----------------

  function classifyWarning(text) {
    var t = text.toLowerCase();

    // Practical, on-site warnings first
    if (/getij|tide|hoogwater|overstroom|drassig/.test(t)) return 'getij & water';
    if (/militair|schietterrein|munitie|defensie/.test(t)) return 'militair terrein';
    if (/motorcross|crossbaan|drinkwaterbescherming|afvalregels|jacht/.test(t)) return 'let op ter plaatse';
    if (/verboden toegang|strikt gesloten|kijkreservaat|kijk-, geen|niet betreden/.test(t)) return 'beperkte toegang';
    if (/geen bebording|weinig bebording|geen beboord|niet bewegwijzerd|geen startpunt|geen \u00e9\u00e9n startpunt|geen enkele poort|navigeer/.test(t)) return 'geen bewegwijzering';
    if (/verspreide elementen|kleine verspreide|cluster|bescheiden gebied|klein gebied|koppel met/.test(t)) return 'verzamel- of veldnaam';
    if (/naam wisselt|gelijknamige|meerdere .*locaties|aangenomen op basis|via context gekoppeld/.test(t)) return 'naamverwarring';
    if (/geen publieke toegang|geen toegang tot|niet vrij toegankelijk|gesloten|toegang aanvragen|blijf op de (aangegeven )?(paden|wegen)|alleen .*gemarkeerde routes|broedseizoen/.test(t)) return 'beperkte toegang';
    if (/seizoensgebonden|alleen in de zomer|winter gesloten|pontjes/.test(t)) return 'seizoensgebonden';
    if (/niet openbaar|verboden|volg de aanwijzingen|werkzaamheden|afsluiten/.test(t)) return 'beperkte toegang';
    if (/corridor-kaart|kaart genoemd naar|gemapt op|de naam dekt|lijstnaam/.test(t)) return 'naamverwarring';
    if (/zonder eigen bewegwijzering|volg het wandelnetwerk/.test(t)) return 'geen bewegwijzering';
    if (/naamvolging|gehuchtniveau|dorpsniveau|buurtschapniveau/.test(t)) return 'verzamel- of veldnaam';
    if (/priv[ée]|particulier terrein|niet toegankelijk|geen toegang|respecteer|besloten|rustgebied|geen voorzieningen|geen ingang|geen paden/.test(t)) return 'beperkte toegang';

    // Naming and source issues
    if (/ambigu|twee .*gebieden|er bestaan twee|verwarring|welke .*bedoelt|matcht met|disambiguatie|verduidelijking|niet in .*lijst|staat ten onrechte|spellingvariant|naamvariatie|verkeerde naam|juiste en offici/.test(t)) return 'naamverwarring';
    if (/verzamelkaart|collectieve kaart|geen afgebakend|geen afzonderlijk|verzamelnaam|streeknaam|veldnaam|toponiem|naamniveau|alleen als naam|naam onbekend|erf- en boerderijnaam|geen beheerd natuurgebied/.test(t)) return 'verzamel- of veldnaam';
    if (/niet betrouwbaar|kon niet|could not|niet worden gelokaliseerd|niet afzonderlijk gedocumenteerd|geen verifieerbare|bronnen zwijgen|doodlop/.test(t)) return 'niet bevestigd';
    if (/schaars|schaarse|dunne|dun gedocumenteerd|beperkt|weinig openbare documentatie|scarce|thin|geprofileerd|profiel op naamtype|verifieer/.test(t)) return 'weinig bronnen';

    return 'let op';
  }

  function firstWarningText(card) {
    // Prefer an explicit note, then any element whose text starts with the sign
    var note = card.querySelector('p.note');
    if (note && note.textContent.indexOf('\u26a0') !== -1) {
      return note.textContent.slice(note.textContent.indexOf('\u26a0'));
    }

    var candidates = card.querySelectorAll('p.desc, .tag, .chip, .foot, .loc, p');
    for (var i = 0; i < candidates.length; i++) {
      var txt = (candidates[i].textContent || '').trim();
      if (txt.indexOf('\u26a0') !== -1) return txt.slice(txt.indexOf('\u26a0'));
    }
    return (card.textContent || '').trim();
  }

  function buildWarningList() {
    var listEl = document.getElementById('warnlist');
    var statsEl = document.getElementById('warnstats');
    if (!listEl) return;

    var cards = document.querySelectorAll('article.card[id^="nr"]');
    var kinds = {};
    var total = 0;
    var html = '';

    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      if ((card.textContent || '').indexOf('\u26a0') === -1) continue;

      var id = card.getAttribute('id');
      var numEl = card.querySelector('.num');
      var num = numEl ? numEl.textContent.trim() : id.replace('nr', '');
      var h2 = card.querySelector('h2');
      var name = h2 ? h2.textContent.replace(num, '').trim() : id;

      var raw = firstWarningText(card).replace(/\s+/g, ' ').trim();
      var text = raw.replace(/^[\u26a0\ufe0f\s]+/, '');
      if (text.length > 260) text = text.slice(0, 260).replace(/\s\S*$/, '') + '…';

      var kind = classifyWarning(raw);
      kinds[kind] = (kinds[kind] || 0) + 1;
      total++;

      html += '<li><span class="wnum">nr. ' + num + '</span>' +
              '<a href="#' + id + '" data-warnjump="1">' + name + '</a>' +
              '<span class="wkind">' + kind + '</span>' +
              '<span class="wtext">' + text.replace(/</g, '&lt;') + '</span></li>';
    }

    listEl.innerHTML = html;

    if (statsEl) {
      var parts = [];
      for (var k in kinds) {
        if (Object.prototype.hasOwnProperty.call(kinds, k)) {
          parts.push('<b>' + kinds[k] + '</b> ' + k);
        }
      }
      parts.sort();
      statsEl.innerHTML = '<b>' + total + '</b> van de ' + cards.length +
        ' kaarten dragen een ⚠️-melding — ' + parts.join(' · ') + '.';
    }

    // Jumping to a card must switch back to the List tab first
    listEl.addEventListener('click', function(e) {
      var link = e.target && e.target.closest ? e.target.closest('a[data-warnjump]') : null;
      if (!link) return;
      applyTab('list');
      try { localStorage.setItem('ng-tab', 'list'); } catch (err) {}
    });
  }

  // Cover page: fullscreen book cover, click to enter the guide
  function initCover() {
    var cover = document.getElementById('cover');
    var app = document.getElementById('app');
    if (!cover || !app) return;

    function open() {
      cover.classList.add('hide');
      app.classList.remove('hidden');
      document.body.classList.remove('cover-open');
    }

    function close() {
      cover.classList.remove('hide');
      app.classList.add('hidden');
      document.body.classList.add('cover-open');
      window.scrollTo(0, 0);
    }

    // Always start on the cover, also after a refresh
    try { localStorage.removeItem('ng-cover'); } catch (e) {}
    close();

    cover.addEventListener('click', open);
    cover.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
    });

    var btn = document.createElement('button');
    btn.id = 'reopen-cover';
    btn.type = 'button';
    btn.textContent = '📖 Omslag';
    btn.title = 'Terug naar de omslag';
    btn.addEventListener('click', close);
    document.body.appendChild(btn);
  }

  // Initialize all modules
  initCover();
  initLanguageToggle();
  initTabSwitcher();
  buildWarningList();

})();
