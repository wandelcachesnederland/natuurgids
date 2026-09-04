/**
 * Nature Reserve Guide — The Netherlands
 * Main JavaScript functionality
 *
 * Architecture: the card data lives in nature-data/reserves-*.json (split into
 * chunks listed by nature-data/index.json). This script fetches those chunks
 * and renders every <article class="card"> into <div id="cards">. The HTML
 * file itself only contains the shell (cover, hero, tabs, TOC skeleton,
 * warnings + blog) so it stays small as the reserve count grows.
 */

(function() {
  'use strict';

  var natureReserves = [];
  var BOOK_TOTAL = 2373;                       // fallback; index.json may override
  var dataReady = false;

  // --------------------------------------------------------------------------
  // Data loading
  // --------------------------------------------------------------------------

  function loadIndex() {
    return fetch('nature-data/index.json')
      .then(function(response) {
        if (!response.ok) throw new Error('index.json: ' + response.status);
        return response.json();
      });
  }

  function loadChunk(url) {
    return fetch(url).then(function(response) {
      if (!response.ok) throw new Error('Failed to load chunk: ' + url);
      return response.json();
    });
  }

  function loadData(meta) {
    var files = (meta && meta.files) || [];
    if (!files.length) return Promise.resolve([]);
    return Promise.all(files.map(function(file) {
      return loadChunk('nature-data/' + file);
    })).then(function(results) {
      var all = [];
      for (var i = 0; i < results.length; i++) {
        if (Array.isArray(results[i])) all = all.concat(results[i]);
      }
      all.sort(function(a, b) { return a.id - b.id; });
      return all;
    });
  }

  // Optional legacy section headers (<h2 class="grouphdr">) that used to sit
  // between groups of cards; kept as data so the visual structure survives.
  var sectionHeaders = [];

  function loadSections() {
    return fetch('nature-data/sections.json')
      .then(function(r) {
        if (!r.ok) throw new Error('sections.json: ' + r.status);
        return r.json();
      })
      .then(function(list) {
        sectionHeaders = Array.isArray(list) ? list : [];
        sectionHeaders.sort(function(a, b) {
          return (a.before - b.before) || 0;
        });
        // stable order within the same before-id (two headers precede nr01)
        var order = 0;
        for (var i = 0; i < sectionHeaders.length; i++) {
          sectionHeaders[i]._o = order++;
        }
        sectionHeaders.sort(function(a, b) {
          return (a.before - b.before) || (a._o - b._o);
        });
      })
      .catch(function() {
        sectionHeaders = [];   // headers are decorative; render without them
      });
  }

  function headersBefore(id) {
    var out = '';
    for (var i = 0; i < sectionHeaders.length; i++) {
      if (sectionHeaders[i].before === id) out += sectionHeaders[i].html + '\n';
    }
    return out;
  }

  // --------------------------------------------------------------------------
  // Card rendering — rebuilds the exact markup that used to live in the HTML
  // --------------------------------------------------------------------------

  function padId(id) {
    return id < 10 ? '0' + id : String(id);   // legacy anchors #nr01..#nr09
  }

  function cardHtml(rec) {
    var cls = rec.card_class || 'card';
    return '<article class="' + cls + '" id="nr' + padId(rec.id) + '">\n' +
           (rec.nl_html || '') + '\n' +
           (rec.en_html || '') + '\n</article>\n';
  }

  function renderCards() {
    var host = document.getElementById('cards');
    if (!host) return;
    var html = '';
    for (var i = 0; i < natureReserves.length; i++) {
      html += headersBefore(natureReserves[i].id);
      html += cardHtml(natureReserves[i]);
    }
    host.innerHTML = html;
  }

  function fmt(n) {
    return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  }

  function fillCounts(meta) {
    var total = natureReserves.length;
    var bookTotal = (meta && meta.book_total) || BOOK_TOTAL;
    var pct = bookTotal ? Math.round(total * 1000 / bookTotal) / 10 : 0;

    var bar = document.querySelector('.progressbar i');
    if (bar) bar.style.width = pct + '%';

    var done = document.getElementById('prog-done');
    var all = document.getElementById('prog-total');
    if (done) done.textContent = fmt(total);
    if (all) all.textContent = fmt(bookTotal);

    var tocCount = document.getElementById('toc-count');
    if (tocCount) tocCount.textContent = fmt(total);

    var coverCount = document.getElementById('cover-count');
    if (coverCount) coverCount.textContent = fmt(total);

    document.title = 'Nature Reserve Guide — The Netherlands · all ' +
                     fmt(total) + ' reserves';
  }

  function showLoadError() {
    var host = document.getElementById('cards');
    if (!host) return;
    host.innerHTML =
      '<div class="toc" style="border-left:5px solid #c0392b">' +
      '<h2>⚠️ Kaartdata kon niet worden geladen / Card data could not be loaded</h2>' +
      '<p>De kaarten worden gerenderd uit <code>nature-data/reserves-*.json</code>. ' +
      'Open deze pagina via een webserver of de live preview (fetch is niet ' +
      'beschikbaar bij het direct openen van het bestand).</p>' +
      '<p class="c-en" style="display:block">Cards are rendered from the ' +
      '<code>nature-data/reserves-*.json</code> chunks. Please open this page ' +
      'through a web server or the live preview (fetch is unavailable when ' +
      'opening the file directly).</p></div>';
  }

  // --------------------------------------------------------------------------
  // Public helpers (kept compatible)
  // --------------------------------------------------------------------------

  function getNatureReserves() { return natureReserves; }

  function getReserveById(id) {
    for (var i = 0; i < natureReserves.length; i++) {
      if (natureReserves[i].id === id) return natureReserves[i];
    }
    return null;
  }

  function getReserveByNumber(number) {
    for (var i = 0; i < natureReserves.length; i++) {
      if (natureReserves[i].number === number) return natureReserves[i];
    }
    return null;
  }

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

  window.NatureGuide = {
    loadData: function() {
      return loadIndex().then(loadData).then(function(list) {
        natureReserves = list;
        return natureReserves;
      });
    },
    getReserves: getNatureReserves,
    getById: getReserveById,
    getByNumber: getReserveByNumber,
    search: searchReserves,
    ready: function() { return dataReady; }
  };

  // --------------------------------------------------------------------------
  // Language toggle
  // --------------------------------------------------------------------------

  function applyLanguage(isEnglish) {
    document.body.classList.toggle('lang-en', !!isEnglish);
    var tabs = document.querySelectorAll('#langswitch .langtab');
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].classList.toggle('on', tabs[i].getAttribute('data-lang') ===
        (isEnglish ? 'en' : 'nl'));
    }
  }

  function initLanguageToggle() {
    document.addEventListener('click', function(e) {
      var target = e.target && e.target.closest ? e.target.closest('#langswitch .langtab') : null;
      if (!target) return;
      applyLanguage(target.getAttribute('data-lang') === 'en');
      try { localStorage.setItem('ng-lang', target.getAttribute('data-lang')); } catch (err) {}
    });

    try {
      if (localStorage.getItem('ng-lang') === 'en') applyLanguage(true);
    } catch (err) {}
  }

  // --------------------------------------------------------------------------
  // Tabs (List / Blog / Warnings)
  // --------------------------------------------------------------------------

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
      try { localStorage.setItem('ng-tab', name); } catch (err) {}
    });

    try {
      var saved = localStorage.getItem('ng-tab');
      if (saved) applyTab(saved);
    } catch (err) {}
  }

  // --------------------------------------------------------------------------
  // Warnings tab — scans the rendered cards
  // --------------------------------------------------------------------------

  function classifyWarning(text) {
    var t = text.toLowerCase();

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

    if (/ambigu|twee .*gebieden|er bestaan twee|verwarring|welke .*bedoelt|matcht met|disambiguatie|verduidelijking|niet in .*lijst|staat ten onrechte|spellingvariant|naamvariatie|verkeerde naam|juiste en offici/.test(t)) return 'naamverwarring';
    if (/verzamelkaart|collectieve kaart|geen afgebakend|geen afzonderlijk|verzamelnaam|streeknaam|veldnaam|toponiem|naamniveau|alleen als naam|naam onbekend|erf- en boerderijnaam|geen beheerd natuurgebied/.test(t)) return 'verzamel- of veldnaam';
    if (/niet betrouwbaar|kon niet|could not|niet worden gelokaliseerd|niet afzonderlijk gedocumenteerd|geen verifieerbare|bronnen zwijgen|doodlop/.test(t)) return 'niet bevestigd';
    if (/schaars|schaarse|dunne|dun gedocumenteerd|beperkt|weinig openbare documentatie|scarce|thin|geprofileerd|profiel op naamtype|verifieer/.test(t)) return 'weinig bronnen';

    return 'let op';
  }

  function firstWarningText(card) {
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
        ' kaarten dragen een \u26a0\ufe0f-melding \u2014 ' + parts.join(' \u00b7 ') + '.';
    }

    // Jumping to a card must switch back to the List tab first
    listEl.addEventListener('click', function(e) {
      var link = e.target && e.target.closest ? e.target.closest('a[data-warnjump]') : null;
      if (!link) return;
      applyTab('list');
      try { localStorage.setItem('ng-tab', 'list'); } catch (err) {}
    });
  }

  // --------------------------------------------------------------------------
  // Cover page: fullscreen book cover, click to enter the guide
  // --------------------------------------------------------------------------

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

  // --------------------------------------------------------------------------
  // Boot
  // --------------------------------------------------------------------------

  function boot() {
    initCover();
    initLanguageToggle();
    initTabSwitcher();

    loadSections()
      .then(function() { return loadIndex(); })
      .then(function(meta) {
        return loadData(meta).then(function(list) {
          natureReserves = list;
          dataReady = true;
          renderCards();
          fillCounts(meta);
          buildWarningList();
          // Re-apply the saved language/tab now that cards exist
          try {
            if (localStorage.getItem('ng-lang') === 'en') applyLanguage(true);
          } catch (err) {}
          try {
            var savedTab = localStorage.getItem('ng-tab');
            if (savedTab) applyTab(savedTab);
          } catch (err) {}
          // Deep link (#nr1735 …): jump to the card once it exists
          if (window.location.hash && /^#nr\d+$/.test(window.location.hash)) {
            var el = document.querySelector(window.location.hash);
            if (el) {
              el.scrollIntoView();
            }
          }
          console.log('Loaded ' + natureReserves.length +
                      ' nature reserves from ' +
                      ((meta && meta.files) ? meta.files.length : 0) + ' chunks');
        });
      })
      .catch(function(error) {
        console.error('Error loading nature reserves:', error);
        showLoadError();
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

})();
