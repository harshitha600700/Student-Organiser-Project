// Pomodoro Timer and Theme Selector
let minutes = 25, seconds = 0, timer, running = false;

function updateDisplay() {
    const text = document.getElementById("timer-text");
    text.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function startTimer() {
    if (running) return;
    running = true;
    timer = setInterval(() => {
        if (seconds === 0) {
            if (minutes === 0) {
                clearInterval(timer);
                running = false;
                alert("Pomodoro finished!");
                return;
            }
            minutes--;
            seconds = 59;
        } else {
            seconds--;
        }
        updateDisplay();
    }, 1000);
}

function pauseTimer() {
    clearInterval(timer);
    running = false;
}

function resetTimer() {
    clearInterval(timer);
    minutes = 25;
    seconds = 0;
    running = false;
    updateDisplay();
}

window.onload = function () {
    updateDisplay();

    const selector = document.getElementById("themeSelector");
    const savedTheme = localStorage.getItem("selectedTheme");

    if (savedTheme) {
        document.getElementById("themeStylesheet").href = `/static/${savedTheme}.css`;
        selector.value = savedTheme;
    }

    selector.addEventListener("change", () => {
        const theme = selector.value;
        document.getElementById("themeStylesheet").href = `/static/${theme}.css`;
        localStorage.setItem("selectedTheme", theme);  // 🔐 save theme to browser
    });
};