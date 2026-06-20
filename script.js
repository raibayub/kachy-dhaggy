 
    // Theme Toggle Logic
    const themeToggle = document.getElementById('theme-toggle');
    const iconMoon = document.getElementById('theme-icon-moon');
    const iconSun = document.getElementById('theme-icon-sun');

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      iconMoon.style.display = 'none';
      iconSun.style.display = 'block';
    } else {
      iconMoon.style.display = 'block';
      iconSun.style.display = 'none';
    }

    themeToggle.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        iconMoon.style.display = 'block';
        iconSun.style.display = 'none';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        iconMoon.style.display = 'none';
        iconSun.style.display = 'block';
      }
      themeToggle.style.transform = 'scale(0.9)';
      setTimeout(() => themeToggle.style.transform = 'scale(1)', 150);
    });

    // Sticky navbar state
    const nav = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    });

    // Scroll-reveal via IntersectionObserver
    const revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
    revealEls.forEach(el => io.observe(el));

    // Mobile nav toggle (simple show/hide)
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-menu');
    const cta = document.querySelector('.nav-cta');
    toggle.addEventListener('click', () => {
      const open = menu.style.display === 'flex';
      menu.style.display = open ? 'none' : 'flex';
      cta.style.display = open ? 'none' : 'inline-block';
      if (!open) {
        menu.style.cssText = 'display:flex;flex-direction:column;position:fixed;top:68px;left:0;right:0;background:var(--nav-scrolled);padding:32px;gap:24px;border-bottom:1px solid var(--glass-border);';
        cta.style.cssText = 'display:inline-block;position:fixed;top:300px;left:6vw;right:6vw;text-align:center;';
      }
    });

    // Number counter animation
    const statNumbers = document.querySelectorAll('.stat-number');
    const statsObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const element = entry.target;
          const target = parseInt(element.getAttribute('data-target'));
          const duration = 2000; // Animation duration in ms
          let startTime = null;

          function animation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            let progress = timeElapsed / duration;
            if (progress > 1) progress = 1;

            // easeOutExpo for a nice decelerating effect
            const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);

            element.innerText = Math.floor(easeProgress * target);

            if (progress < 1) {
              requestAnimationFrame(animation);
            } else {
              element.innerText = target;
            }
          }

          requestAnimationFrame(animation);
          statsObserver.unobserve(element);
        }
      });
    }, { threshold: 0.1 });

    statNumbers.forEach(num => statsObserver.observe(num));
  