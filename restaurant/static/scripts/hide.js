const el = document.getElementById('form1');

const btn = document.getElementById('hide');

btn.addEventListener('click', function handleClick() {
  if (el.style.display === 'none') {
    el.style.display = 'block';

    btn.textContent = 'add branch';
  } else {
    el.style.display = 'none';

    btn.textContent = 'close';
  }
});
