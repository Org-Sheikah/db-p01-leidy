import http.server
import socketserver
import urllib.parse

PORT = 8000

# HTML y CSS integrados dentro de Python
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora de Suma</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 300px;
        }
        h2 {
            color: #333;
            margin-bottom: 20px;
        }
        input[type="number"] {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 15px;
            width: 100%;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            color: #28a745;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Calculadora Web</h2>
        <form method="POST">
            <input type="number" name="num1" placeholder="Primer número" step="any" required value="{num1}">
            <input type="number" name="num2" placeholder="Segundo número" step="any" required value="{num2}">
            <input type="submit" value="Sumar">
        </form>
        <div class="result">
            {resultado_html}
        </div>
    </div>
</body>
</html>
"""

class SumaWebHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.enviar_pagina("", "", "")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        try:
            num1_val = float(params.get('num1', [0])[0])
            num2_val = float(params.get('num2', [0])[0])
            suma = num1_val + num2_val
            resultado_str = f"Resultado: {num1_val} + {num2_val} = {suma}"
            self.enviar_pagina(str(num1_val), str(num2_val), resultado_str)
        except ValueError:
            self.enviar_pagina("", "", "Por favor ingresa números válidos.")

    def enviar_pagina(self, n1, n2, res):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        pagina_llenada = HTML_TEMPLATE.format(num1=n1, num2=n2, resultado_html=res)
        self.wfile.write(pagina_llenada.encode('utf-8'))

if __name__ == "__main__":
    print(f"Servidor web iniciado en http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), SumaWebHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")