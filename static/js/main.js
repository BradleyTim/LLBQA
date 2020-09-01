const year = document.querySelector('#year');
const menuBurger = document.querySelector('#menu-burger');
const captcha = document.querySelector('#id_captcha_1');

// add dynamic year to the footer
year.textContent = new Date().getFullYear();

// add hamburger menu to navbar
menuBurger.innerHTML = `
  <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1">
    <line x1="3" y1="12" x2="21" y2="12"></line>
    <line x1="3" y1="6" x2="21" y2="6"></line>
    <line x1="3" y1="18" x2="21" y2="18"></line>
  </svg>
`;

captcha.classList.add('form-control', 'mt-2');

// REGISTER THE SERVICEWORKER FOR PWA CAPABILITIES
// window.addEventListener("load", () => {
//   if ("serviceWorker" in navigator) {
//     navigator.serviceWorker
//       .register("sw.js")
//       .then(registration => {
//         console.log(
//           "{serviceWorker} registered"
//         );
//       })
//       .catch(err => {
//         console.log("There was an error ----------->");
//         console.log(err);
//       });
//   }
// });
