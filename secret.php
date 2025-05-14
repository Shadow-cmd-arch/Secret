<?php
session_start();
if (!isset($_SESSION['acces_secret']) || $_SESSION['acces_secret'] !== true) {
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🛑 Accès Ultra-Confidentiel 🛑</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            background-color: black;
            color: green;
            text-align: center;
        }

        .hack-effect {
            font-size: 22px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 50px;
        }

        .buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }

        .buttons button {
            background-color: green;
            color: black;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>✅ Accès Autorisé ✅</h1>

    <p class="hack-effect" id="textEffect"></p>

    <!-- Boutons de téléchargement -->
    <div class="buttons">
        <button onclick="location.href='1.jpg'" download>Télécharger Image 1</button>
        <button onclick="location.href='2.jpg'" download>Télécharger Image 2</button>
        <button onclick="location.href='3.jpg'" download>Télécharger Image 3</button>
        <button onclick="location.href='4.jpg'" download>Télécharger Image 4</button>
        <button onclick="location.href='5.jpg'" download>Télécharger Image 5</button>
    </div>

    <script>
        function revealText(text) {
            let textContainer = document.getElementById("textEffect");
            let index = 0;
            
            function type() {
                if (index < text.length) {
                    textContainer.textContent += text.charAt(index);
                    index++;
                    setTimeout(type, 100);
                }
            }

            type();
        }

        revealText("Déchiffrement des données en cours...");
    </script>

</body>
</html>