console.log('Kek :/')


function loadLoginForm() {
    fetch('/user/login/modal') // Запрос к новому маршруту
        .then(response => response.text())
        .then(html => {
            document.getElementById('loginModalBody').innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка загрузки формы:', error);
            document.getElementById('loginModalBody').innerHTML = '<p class="text-danger">Не удалось загрузить форму авторизации.</p>';
        });
}

// Дополнительный код для обработки флэш-сообщений после входа (опционально, но полезно)
document.addEventListener('DOMContentLoaded', (event) => {
    // Если есть флэш-сообщения (например, после неудачного входа/регистрации),
    // вы можете автоматически открыть модальное окно, если это необходимо.
    // Это сложнее реализовать через AJAX, пока оставим так.
});