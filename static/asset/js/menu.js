const buttonElement = document.querySelector('.js-menu-button');
const headerElement = document.querySelector('.js-header');

buttonElement.addEventListener('click', () => {
  headerElement.classList.toggle('js-menu-closed');
});
