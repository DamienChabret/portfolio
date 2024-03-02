// Variables pour gérer l'animation
var visible = true;
var letterCount = 1;
var letterIncrementation = 1;
var waiting = false;
var motCommun = "Damien C";
var motAgarder = 0;
var con = document.getElementById('console');


// Fonction pour afficher du texte avec un effet de terminal
function consoleText(words, id) {
    var target = document.getElementById(id);
    var wordIndex = 0; // Variable pour suivre l'index du mot actuel
    var canSkipWord = false;

    // Intervalles pour animer le texte
    window.setInterval(function() {
        // Si le contenu de target contient déjà le mot à garder, on ne le modifie pas
        if (target.innerHTML.includes(motCommun)) {
            motAgarder = motCommun.length;
        }

        // Si le compteur de lettres est à zéro et qu'on n'attend pas
        if (letterCount === motAgarder && waiting === false) {
            if(canSkipWord)
                wordIndex+=1;
                canSkipWord = false;

            // Affichage du texte actuel
            target.innerHTML = words[wordIndex].substring(0, letterCount);
            reitialiseCompteur(1);
            canSkipWord = true;
        } 
        // Si le compteur de lettres atteint la longueur du mot et qu'on n'attend pas
        else if (letterCount === words[wordIndex].length + 1 && waiting === false) {
            if(!TargetIsLastWord(target.innerHTML,words[words.length - 1]))
                reitialiseCompteur(-1);
        } 
        // Si on n'attend pas
        else if (waiting === false) {
            // Affichage du texte actuel
            target.innerHTML = words[wordIndex].substring(0, letterCount);
            // Incrémentation du compteur de lettres
            letterCount += letterIncrementation;
        }

    }, 100);

}

function reitialiseCompteur(incrementation){
    // On attend
    waiting = true;
    // Attente d'une seconde avant de continuer
    window.setTimeout(function() {
        // Réinitialisation des compteurs et de l'attente
        letterIncrementation = incrementation;
        letterCount += letterIncrementation;
        waiting = false;
    }, 1000);
}

/**
 * Vérifie si le target vaut le dernier mot
 * @param {string} target mot donné 
 * @param {string} word mot à atteindre
 * @returns 
 */
function TargetIsLastWord(target, word){
    return target === word;
}

// Fonction exécutée lorsque la page est chargée
window.onload = () => {
    // Tableau de mots à afficher
    let words = ["Damien Cabret", "Damien Cabaret", "Damien Chabret"];
    // Appel de la fonction pour afficher le texte avec effet de terminal
    consoleText(words, 'test','black');
}
