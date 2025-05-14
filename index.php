<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $password = $_POST["password"];

    if ($password === "hacker123") { // <-- Change ce mot de passe !
        $_SESSION['acces_secret'] = true;
        header("Location: secret.php");
        exit();
    } else {
        echo "<script>alert('❌ Mot de passe incorrect !');</script>";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔒 Accès Ultra-Sensible 🔒</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            background-color: black;
            color: green;
            text-align: center;
        }

        input {
            background-color: black;
            color: green;
            border: 1px solid green;
            padding: 5px;
            font-size: 16px;
            margin-top: 10px;
        }

        button.validate {
            background-color: green;
            color: black;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <h1>⚠️ Accès Restreint ⚠️</h1>
    <p>Entrez le mot de passe pour accéder aux documents :</p>

    <form method="post">
        <input type="password" name="password">
        <button class="validate" type="submit">Valider</button>
    </form>

</body>
</html>