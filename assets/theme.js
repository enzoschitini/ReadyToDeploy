/* ============================================================
   Seletor de tema (claro / escuro / sistema) — compartilhado.

   Carregue no <head>, ANTES do <style> da página e SEM defer:
     <script src="assets/theme.js"></script>

   A primeira parte roda de imediato e aplica a classe no <html>
   antes da primeira pintura (sem flash). A segunda parte espera o
   DOM e injeta o botão dentro do header, ao lado do "Entrar".
   ============================================================ */
(function () {
  'use strict';

  var STORAGE_KEY = 'primo-theme';
  var root = document.documentElement;
  var mql = window.matchMedia ? window.matchMedia('(prefers-color-scheme: light)') : null;

  function readMode() {
    var saved;
    try { saved = localStorage.getItem(STORAGE_KEY); } catch (e) {}
    return (saved === 'light' || saved === 'dark' || saved === 'system') ? saved : 'dark';
  }

  function resolve(mode) {
    if (mode === 'system') return (mql && mql.matches) ? 'light' : 'dark';
    return mode === 'light' ? 'light' : 'dark';
  }

  function apply(mode) {
    var resolved = resolve(mode);
    root.classList.remove('dark', 'light');
    root.classList.add(resolved);
    root.setAttribute('data-theme-mode', mode);

    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', resolved === 'light' ? '#ffffff' : '#000000');
    var scheme = document.querySelector('meta[name="color-scheme"]');
    if (scheme) scheme.setAttribute('content', resolved);
  }

  /* --- 1. aplica antes da primeira pintura --- */
  apply(readMode());

  /* --- 2. monta o seletor quando o DOM estiver pronto --- */
  var ICONS = {
    sun: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>',
    moon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>',
    monitor: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
    check: '<svg class="check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg>'
  };

  var LABELS = { light: 'Claro', dark: 'Escuro', system: 'Sistema' };

  function build() {
    var inner = document.querySelector('.header-inner');
    if (!inner || inner.querySelector('.theme-switch')) return;

    var actions = inner.querySelector('.header-actions');
    var menuBtn = inner.querySelector('.menu-btn');

    var wrap = document.createElement('div');
    wrap.className = 'theme-switch';
    wrap.innerHTML =
      '<button type="button" class="theme-btn" id="theme-btn" aria-haspopup="true" aria-expanded="false" aria-controls="theme-menu">' +
        '<span class="icon-sun" aria-hidden="true">' + ICONS.sun + '</span>' +
        '<span class="icon-moon" aria-hidden="true">' + ICONS.moon + '</span>' +
      '</button>' +
      '<div class="theme-menu" id="theme-menu" role="menu" aria-label="Tema da página">' +
        '<button type="button" role="menuitemradio" aria-checked="false" data-theme="light">' + ICONS.sun + '<span>Claro</span>' + ICONS.check + '</button>' +
        '<button type="button" role="menuitemradio" aria-checked="false" data-theme="dark">' + ICONS.moon + '<span>Escuro</span>' + ICONS.check + '</button>' +
        '<button type="button" role="menuitemradio" aria-checked="false" data-theme="system">' + ICONS.monitor + '<span>Sistema</span>' + ICONS.check + '</button>' +
      '</div>';

    /* agrupa seletor + "Entrar" + menu mobile à direita do header */
    var right = inner.querySelector('.header-right');
    if (!right) {
      right = document.createElement('div');
      right.className = 'header-right';
      inner.insertBefore(right, actions || menuBtn);
      if (actions) right.appendChild(actions);
      if (menuBtn) right.appendChild(menuBtn);
    }
    right.insertBefore(wrap, right.firstChild);

    var btn = wrap.querySelector('.theme-btn');
    var menu = wrap.querySelector('.theme-menu');
    var options = Array.prototype.slice.call(menu.querySelectorAll('[data-theme]'));

    function sync() {
      var mode = root.getAttribute('data-theme-mode') || 'dark';
      var label = LABELS[mode] || LABELS.dark;
      btn.setAttribute('aria-label', 'Selecionar tema (atual: ' + label + ')');
      btn.setAttribute('title', 'Tema: ' + label);
      options.forEach(function (opt) {
        opt.setAttribute('aria-checked', opt.getAttribute('data-theme') === mode ? 'true' : 'false');
      });
    }

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
        var mode = opt.getAttribute('data-theme');
        try { localStorage.setItem(STORAGE_KEY, mode); } catch (e) {}
        apply(mode);
        sync();
        close();
        btn.focus();
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

    if (mql && mql.addEventListener) {
      mql.addEventListener('change', function () {
        if ((root.getAttribute('data-theme-mode') || 'dark') === 'system') apply('system');
      });
    }

    /* outra aba mudou o tema */
    window.addEventListener('storage', function (e) {
      if (e.key === STORAGE_KEY) { apply(readMode()); sync(); }
    });

    sync();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
