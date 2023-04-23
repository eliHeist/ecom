//#region navigation toggles
const navToggler = document.getElementById('navbar-toggler');
const navClose = document.getElementById('nav-close-btn');
const navMenu = document.getElementById('main-nav');

const navToggle = () => {
   navMenu.classList.toggle('hidden');
}

navToggler.addEventListener('click', (e) => {
   navToggle();
});

navClose.addEventListener('click', (e) => {
   navToggle();
});
//#endregion

//#region cards 
const cardContainer = document.querySelector('#suites-row');
const suiteCards = cardContainer.children;

for (let index = 1; index < suiteCards.length; index+=2) {
   suiteCards[index].firstElementChild.firstElementChild.classList.remove('flex-sm-row');
   suiteCards[index].firstElementChild.firstElementChild.classList.add('flex-sm-row-reverse');
   
}
console.log(suiteCards[0]);
//#endregion
