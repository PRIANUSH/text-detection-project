function speakText() {
    let text = document.querySelector(".extracted-text-area p").innerText;

    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-IN"; // Indian English

    window.speechSynthesis.speak(speech);
}
function stopSpeech() {
    window.speechSynthesis.cancel();
}