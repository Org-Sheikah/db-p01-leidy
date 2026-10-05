# Contenido HTML y CSS integrado dentro de Python
HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora de Suma</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; width: 300px; }
        h2 { color: #333; margin-bottom: 20px; }
        input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; font-size: 16px; }
        button { background-color: #007bff; color: white; border: none; padding: 10px 15px; width: 100%; border-radius: 5px; font-size: 16px; cursor: pointer; margin-top: 10px; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; font-size: 18px; font-weight: bold; color: #28a745; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Calculadora Web</h2>
        <input type="number" id="num1" placeholder="Primer número">
        <input type="number" id="num2" placeholder="Segundo número">
        <button onclick="sumar()">Sumar</button>
        <div class="result" id="resultado"></div>
    </div>

    <script>
        function sumar() {
            let n1 = parseFloat(document.getElementById('num1').value) || 0;
            let n2 = parseFloat(document.getElementById('num2').value) || 0;
            let suma = n1 + n2;
            document.getElementById('resultado').innerText = "Resultado: " + suma;
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    # Cuando Python se ejecuta, escribe el archivo index.html para la web
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print("¡Página web generada con éxito desde Python!")