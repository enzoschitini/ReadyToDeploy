/* ============================================================
   Seletor de idioma (PT-BR / IT) — compartilhado por todas as páginas.
   Ver TRADUCAO_IT.md para o mapeamento completo de arquivos.

   Carregue no <head>, DEPOIS de assets/theme.js e SEM defer:
     <script src="assets/theme.js"></script>
     <script src="assets/lang.js"></script>

   Idioma na URL (pra compartilhar link já num idioma):
     ?lang=it     ou     ?lang=pt_br
   Se presente e válido, tem prioridade sobre o localStorage e o
   grava como novo padrão. Se ausente, a página sincroniza a URL
   sozinha (replaceState, sem reload) pra refletir o idioma ativo —
   assim qualquer link copiado da barra de endereço já vem com
   ?lang= correto, mesmo sem o usuário ter clicado no seletor.

   A primeira parte roda de imediato: calcula o idioma (URL >
   localStorage > padrão), expõe `window.PRIMO_LANG` (usado pelo
   script de cada página pra montar APP_CONTENT/COURSE_CONTENT) e
   aplica <html lang> antes da primeira pintura (sem flash). A
   segunda parte espera o DOM e injeta o botão dentro do header, ao
   lado do seletor de tema.
   ============================================================ */
(function () {
  'use strict';

  var STORAGE_KEY = 'primo-lang';
  var URL_PARAM = 'lang';
  var LANGS = {
    pt_br: { label: 'Português', short: 'PT', flag: '🇧🇷', htmlLang: 'pt-BR' },
    it: { label: 'Italiano', short: 'IT', flag: '🇮🇹', htmlLang: 'it-IT' }
  };
  var DEFAULT_LANG = 'pt_br';

  function readUrlLang() {
    try {
      var v = new URLSearchParams(window.location.search).get(URL_PARAM);
      return LANGS[v] ? v : null;
    } catch (e) { return null; }
  }

  function readLang() {
    var fromUrl = readUrlLang();
    if (fromUrl) {
      try { localStorage.setItem(STORAGE_KEY, fromUrl); } catch (e) {}
      return fromUrl;
    }
    var saved;
    try { saved = localStorage.getItem(STORAGE_KEY); } catch (e) {}
    return LANGS[saved] ? saved : DEFAULT_LANG;
  }

  var LANG = readLang();

  /* --- 1. expõe o idioma escolhido e aplica antes da primeira pintura --- */
  window.PRIMO_LANG = LANG;
  document.documentElement.lang = LANGS[LANG].htmlLang;

  /* mantém a URL sincronizada com o idioma ativo, sem navegar/recarregar */
  try {
    var syncUrl = new URL(window.location.href);
    if (syncUrl.searchParams.get(URL_PARAM) !== LANG) {
      syncUrl.searchParams.set(URL_PARAM, LANG);
      window.history.replaceState(window.history.state, '', syncUrl.toString());
    }
  } catch (e) {}

  /* --- 2. monta o seletor quando o DOM estiver pronto --- */
  var CHECK_ICON = '<svg class="check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg>';

  function build() {
    var inner = document.querySelector('.header-inner');
    if (!inner || inner.querySelector('.lang-switch')) return;

    var actions = inner.querySelector('.header-actions');
    var menuBtn = inner.querySelector('.menu-btn');

    var right = inner.querySelector('.header-right');
    if (!right) {
      right = document.createElement('div');
      right.className = 'header-right';
      inner.insertBefore(right, actions || menuBtn);
      if (actions) right.appendChild(actions);
      if (menuBtn) right.appendChild(menuBtn);
    }

    var wrap = document.createElement('div');
    wrap.className = 'lang-switch';
    var current = LANGS[LANG];
    wrap.innerHTML =
      '<button type="button" class="lang-btn" id="lang-btn" aria-haspopup="true" aria-expanded="false" aria-controls="lang-menu">' +
        '<span class="flag" aria-hidden="true">' + current.flag + '</span><span>' + current.short + '</span>' +
      '</button>' +
      '<div class="lang-menu" id="lang-menu" role="menu" aria-label="Idioma da página">' +
        Object.keys(LANGS).map(function (code) {
          var l = LANGS[code];
          return '<button type="button" role="menuitemradio" aria-checked="' + (code === LANG ? 'true' : 'false') + '" data-lang="' + code + '">' +
            '<span class="flag" aria-hidden="true">' + l.flag + '</span><span>' + l.label + '</span>' +
            '<span class="check">' + CHECK_ICON + '</span>' +
          '</button>';
        }).join('') +
      '</div>';

    right.insertBefore(wrap, right.firstChild);

    var btn = wrap.querySelector('.lang-btn');
    var menu = wrap.querySelector('.lang-menu');
    var options = Array.prototype.slice.call(menu.querySelectorAll('[data-lang]'));

    function close() {
      menu.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (menu.classList.contains('open')) {
        close();
      } else {
        menu.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });

    options.forEach(function (opt) {
      opt.addEventListener('click', function () {
        var code = opt.getAttribute('data-lang');
        close();
        if (code === LANG) return;
        try { localStorage.setItem(STORAGE_KEY, code); } catch (e) {}
        var url = new URL(window.location.href);
        url.searchParams.set(URL_PARAM, code);
        window.location.href = url.toString();
      });
    });

    document.addEventListener('click', function (e) {
      if (!wrap.contains(e.target)) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        close();
        btn.focus();
      }
    });

    /* Sem listener de 'storage' aqui de propósito: cada aba fica com o
       idioma que tinha ao carregar (via URL ou localStorage). Reagir a
       mudanças de outra aba recarregando a página cria loop infinito
       quando duas abas têm ?lang= diferentes — cada reload força de
       volta o valor da própria URL no localStorage, o que dispara a
       outra aba, que faz o mesmo de volta. Se quiser aplicar um idioma
       diferente numa aba já aberta, troque pelo seletor nela mesma. */
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
