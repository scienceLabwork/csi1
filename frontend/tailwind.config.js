/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    './templates/**/*.{html,js}',
    './static/**/*.js',
    './node_modules/tw-elements/dist/js/**/*.js',
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'palcream':'#F9D3AA',
        'palpink':'#EE84D4'
      }
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("tw-elements/dist/plugin"),
    require('@tailwindcss/forms'),
    require('preline/plugin'),
    require("daisyui")
  ],
};