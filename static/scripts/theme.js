const themePreference = localStorage.getItem( "theme" );
const prefersDark = window.matchMedia( "(prefers-color-scheme: dark)" ).matches;
let isDark = themePreference ? themePreference === "dark" : prefersDark;
const themeToggle = document.getElementById( "theme-toggle" );
const darkSpan = document.getElementById( "dark-span" );
const lightSpan = document.getElementById( "light-span" );

function updateTheme() {
  document.documentElement.classList.toggle( "dark", isDark );
  themeToggle.setAttribute( "aria-pressed", String( isDark ) );
  darkSpan.style.display = isDark ? 'none' : 'inline-block';
  lightSpan.style.display = isDark ? 'inline-block' : 'none';
}

function toggleTheme() {
  isDark = !isDark;
  localStorage.setItem( "theme", isDark ? "dark" : "light" );
  updateTheme();
}

if ( themeToggle && darkSpan && lightSpan ) {
  updateTheme();
}