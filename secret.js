let intrusionDetected = false; 

document.addEventListener("contextmenu", function(event) {
    if (intrusionDetected) {
        event.preventDefault();
    } else {
        event.preventDefault();
        showFakeAlert();
    }
});

document.addEventListener("keydown", function(event) {
    if (intrusionDetected) {
        event.preventDefault();
    } else {
        if (event.ctrlKey && (event.key === "u" || event.key === "i")) {
            event.preventDefault();
            showFakeAlert();
        }
        if (event.keyCode === 123) { // F12
            event.preventDefault();
            showFakeAlert();
        }
    }
});

function showFakeAlert() {
    intrusionDetected = true;
    alert("🛑 ALERTE SYSTÈME : Intrusion détectée !");
    setTimeout(() => {
        intrusionDetected = false; 
    }, 5000);
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