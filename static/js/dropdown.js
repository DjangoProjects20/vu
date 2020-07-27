const dropdownToggleElements = document.querySelectorAll('.js-dropdown-toggle');
const addDropdownClickListener = (element) => {
  const dropdownContentElement = element.nextSibling;

  dropdownContentElement.classList.add('js-dropdown-content');
  element.addEventListener('click', (e) => {
    e.preventDefault();
    element.classList.toggle('js-dropdown-open');
  });
};

dropdownToggleElements.forEach(addDropdownClickListener);
