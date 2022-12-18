const submitBtn = document.querySelector('#btn_translate');
const hello = document.querySelector('#hello');

submitBtn.addEventListener('click', () => {
  const langCode = document.querySelector('#language_code');
  translate(langCode.value);
});

function translate (code) {
  fetch('https://stefanbohacek.com/hellosalut/?lang=' + code)
    .then(res => res.json())
    .then(data => {
      hello.innerHTML = data.hello;
    })
    .catch(err => console.err(err));
}
