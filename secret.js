// Bloquer le clic droit
document.addEventListener("contextmenu", function(event) {
    event.preventDefault();
    showFakeAlert();
});

// Bloquer les raccourcis vers la console (F12, Ctrl+Shift+I, Ctrl+U)
document.addEventListener("keydown", function(event) {
    if (event.ctrlKey && (event.key === "u" || event.key === "U" || event.key === "i" || event.key === "I" || event.key === "c" || event.key === "C")) {
        event.preventDefault();
        showFakeAlert();
    }
    if (event.keyCode === 123) { // F12
        event.preventDefault();
        showFakeAlert();
    }
});

// Fausse alerte système
function showFakeAlert() {
    setTimeout(function() {
        alert("🛑 Système détecté : Activité suspecte !\n\nVotre accès sera bloqué si vous continuez à tenter d'inspecter le code.");
    }, 500);
}

// Obfuscation du code
eval(function(p,a,c,k,e,d){
    e=function(c){
        return c.toString(36);
    };
    if(!''.replace(/^/,String)){
        while(c--){
            d[c.toString(a)]=k[c]||c.toString(a);
        }
        k=[function(e){
            return d[e];
        }];
        e=function(){
            return '\\w+';
        };
        c=1;
    };
    while(c--){
        if(k[c]){
            p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);
        }
    }
    return p;
}('document.getElementById("secretButton").addEventListener("click",function(){window.location.href="secret.html"});',36,36,'|_|document|secretButton|addEventListener|click|function|window|location|href|secret|html'.split('|'),0,{}));