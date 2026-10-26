(() => {
  'use strict';
  const filterButtons = document.querySelectorAll('[data-filter]');
  const papers = [...document.querySelectorAll('.paper-card')];
  const count = document.getElementById('pub-count');
  const categoryMatch = (paper, filter) => filter === 'all' || paper.dataset.category.split(' ').includes(filter);
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      filterButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle('active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      let visible = 0;
      papers.forEach(paper => {
        const show = categoryMatch(paper, filter);
        paper.hidden = !show;
        if (show) visible += 1;
      });
      if (count) count.textContent = String(visible);
    });
  });
  const toggle = document.querySelector('.mobile-toggle');
  const menu = document.querySelector('.mobile-nav');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      menu.classList.toggle('open', !expanded);
    });
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', 'false');
      menu.classList.remove('open');
    }));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('open');
      }
    });
  }
  const progress = document.getElementById('progress');
  let raf = false;
  const updateProgress = () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = (total > 0 ? Math.max(0, Math.min(100, window.scrollY / total * 100)) : 0) + '%';
    raf = false;
  };
  window.addEventListener('scroll', () => {
    if (!raf) { raf = true; window.requestAnimationFrame(updateProgress); }
  }, { passive: true });
  updateProgress();
  const navLinks = document.querySelectorAll('.site-nav .nav-link');
  const sectionNodes = document.querySelectorAll('main section[id]');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      const inView = entries.filter(e => e.isIntersecting).sort((a,b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (inView) navLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === '#' + inView.target.id));
    }, { rootMargin:'-22% 0px -55% 0px', threshold:[0,.1,.5] });
    sectionNodes.forEach(section => observer.observe(section));
  }
  const toast = document.getElementById('toast');
  let toastTimeout;
  document.querySelectorAll('[data-copy]').forEach(button => {
    button.addEventListener('click', async () => {
      const value = button.getAttribute('data-copy');
      try {
        if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(value);
        else {
          const temporary = document.createElement('textarea');
          temporary.value = value; temporary.style.position='fixed'; temporary.style.opacity='0';
          document.body.appendChild(temporary); temporary.select();
          if (!document.execCommand('copy')) throw new Error('Copy failed');
          temporary.remove();
        }
        if (toast) {
          toast.textContent = button.dataset.message || 'Copied';
          toast.classList.add('visible');
          window.clearTimeout(toastTimeout);
          toastTimeout = window.setTimeout(() => toast.classList.remove('visible'), 2000);
        }
      } catch (_) { window.location.href = 'mailto:' + value; }
    });
  });
})();
