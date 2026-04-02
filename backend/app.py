import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for, flash

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'frontend', 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'K?JLOMK/+rK?JLOMK/+rpMpMK?JLOMK/+rpM'

@app.route('/')
def home():
    return render_template('fns-assessoria.html')

@app.route('/enviar_contato', methods=['POST'])
def enviar_contato():
    nome = request.form.get('nome')
    email_cliente = request.form.get('email')
    telefone = request.form.get('telefone')
    mensagem = request.form.get('mensagem')

    email_remetente = "contabilfns904@gmail.com"
    senha_remetente = "aylomqtmyxdqrhuh"
    email_destinatario = "contabilidade.fns@gmail.com"

    corpo_html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>Você recebeu uma nova mensagem de contato pelo site:</h2>
        
        <p style="font-size: 16px;">
          <strong>Nome:</strong> {nome}<br>
          <strong>E-mail:</strong> <a href="mailto:{email_cliente}">{email_cliente}</a><br>
          <strong>WhatsApp/Telefone:</strong> {telefone}<br>
          <strong>Mensagem:</strong><br>
          {mensagem}
        </p>
        
        <br>
        
        <p style="font-size: 14px;">
          <strong>Atenção: Este e-mail foi enviado automaticamente por um bot.</strong><br>
          <strong>Por favor, não responda a esta mensagem.</strong>
        </p>
      </body>
    </html>
    """

    msg = MIMEText(corpo_html, 'html')
    msg['Subject'] = f"Novo Contato pelo Site: {nome}"
    msg['From'] = email_remetente
    msg['To'] = email_destinatario

    msg = MIMEText(corpo_html, 'html')
    msg['Subject'] = f"Novo Contato pelo Site: {nome}"
    msg['From'] = email_remetente
    msg['To'] = email_destinatario

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_remetente, senha_remetente)
        server.sendmail(email_remetente, email_destinatario, msg.as_string())
        server.quit()

        flash("Mensagem enviada com sucesso! Retornaremos em breve.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        flash("Ocorreu um erro no Servidor. Tente enviar diretamente para nosso e-mail ou WhatsApp.")

    return redirect(url_for('home', _anchor='contato'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
