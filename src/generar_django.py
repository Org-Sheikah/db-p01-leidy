import os
import sys
import django
from django.conf import settings
from django.template import Template, Context

# Configuración mínima de Django en ejecución directa
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
        }],
        SECRET_KEY='clave-secreta-para-generacion',
    )
    django.setup()

# Plantilla HTML con sintaxis de Django (CSS + HTML + JS de la suma)
django_template_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Django</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
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
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 12px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        #resultado {
            margin-top: 15px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>{{ titulo }}</h2>
        <input type="number" id="n1" placeholder="Número 1">
        <input type="number" id="n2" placeholder="Número 2">
        <button onclick="sumar()">Calcular Suma</button>
        <div id="resultado"></div>
    </div>

    <script>
        function sumar() {
            let a = parseFloat(document.getElementById('n1').value);
            let b = parseFloat(document.getElementById('n2').value);
            let res = document.getElementById('resultado');
            if (isNaN(a) || isNaN(b)) {
                res.innerHTML = "Por favor ingresa números válidos";
            } else {
                res.innerHTML = "Resultado: " + (a + b);
            }
        }
    </script>
</body>
</html>
"""

# Renderizado con el motor de plantillas de Django
template = Template(django_template_code)
context = Context({'titulo': 'Calculadora generada con Django'})
output_html = template.render(context)

# Guardar en el archivo HTML principal
with open("index.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print("¡index.html generado exitosamente usando el motor de Django!")