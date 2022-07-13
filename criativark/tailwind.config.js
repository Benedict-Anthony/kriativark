/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./posts/templates/posts/*.html", "./posts/templates/posts/includes/*.html", "./users/templates/users/*.html"],
  theme: {
    screens: {
      sm: "480px",
      md: "768px",
      lg:"1100px"
    },
    extend: {
      colors: { 
        VeryLightRed: "hsl(13, 100%, 72%)",
        LightRed: "hsl(353, 100%, 62%)",
        VeryDarkGrayBlue: "hsl(237, 17%, 21%)",
        VeryDarkDesaturatedBlue:"hsl(237, 23%, 32%)"
      }
    },
  },
  plugins: [],
}





