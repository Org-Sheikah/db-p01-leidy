html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Web</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .calculadora {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            width: 300px;
        }
        input {
            padding: 10px;
            margin: 10px 0;
            width: 90%;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            margin-top: 10px;
        }
        button:hover {
            background-color: #0056b3;
        }
        #resultado {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="calculadora">
        <h2>Sumar Números</h2>
        <input type="number" id="num1" placeholder="Ingresa el primer número">
        <input type="number" id="num2" placeholder="Ingresa el segundo número">
        <button onclick="calcular()">Sumar</button>
        <div id="resultado"></div>
    </div>

    <script>
        function calcular() {
            var n1 = parseFloat(document.getElementById('num1').value);
            var n2 = parseFloat(document.getElementById('num2').value);
            var res = document.getElementById('resultado');

            if(isNaN(n1) || isNaN(n2)) {
                res.innerHTML = "<span style='color:red;'>Ingresa ambos números</span>";
            } else {
                res.innerHTML = "Resultado: " + (n1 + n2);
            }
        }
    </script>
</body>
</html>
"""

# Se escribe el contenido HTML en un archivo
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("¡Archivo index.html generado con éxito!")