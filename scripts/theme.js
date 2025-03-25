function toggleDarkMode() {
    const html = document.documentElement;
    const isDark = html.classList.contains('dark');
    localStorage.setItem('theme', isDark ? 'light' : 'dark');
    html.classList.toggle('dark');
  }
  
  // Initialize theme
  document.addEventListener('DOMContentLoaded', () => {
    const storedTheme = localStorage.getItem('theme') || 
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      
    if (storedTheme === 'dark') {
      document.documentElement.classList.add('dark');
    }
  });
  