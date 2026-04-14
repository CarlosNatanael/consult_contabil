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

# DADOS DOS SERVIÇOS
DADOS_SERVICOS = {
    "abertura-de-empresas": {
        "titulo": "Abertura de Empresas",
        "icone": "bi-building",
        "intro": "Tirar um negócio do papel exige mais que burocracia; exige estratégia. Cuidamos de todo o processo legal para que a sua empresa nasça 100% regularizada.",
        "detalhes": "Analisamos detalhadamente o seu modelo de negócio para definir o melhor enquadramento jurídico (LTDA, SLU, etc.) e o regime tributário mais vantajoso (Simples Nacional, Lucro Presumido). Garantimos a emissão de NIF/CNPJ, alvarás e licenças de forma ágil, evitando dores de cabeça futuras com o fisco.",
        "beneficios": [
            "Escolha do CNAE correto para pagar menos impostos",
            "Elaboração de Contrato Social blindado",
            "Processo ágil sem burocracia para o cliente"
        ],
        "publico": "Novos empreendedores e profissionais liberais que querem formalizar a sua atuação.",
        "diferencial": "Planeamento tributário inicial gratuito na abertura da empresa."
    },
    "regularizacao-de-mei": {
        "titulo": "Regularização de MEI",
        "icone": "bi-card-checklist",
        "intro": "O MEI parece simples, mas pendências no DAS e no DASN podem gerar multas pesadas e a perda de benefícios previdenciários.",
        "detalhes": "Fazemos um levantamento completo da situação do seu CNPJ. Caso existam declarações atrasadas ou guias não pagas, estruturamos um plano de parcelamento e regularizamos o seu perfil junto da Autoridade Tributária. Também prestamos assessoria para o desenquadramento, caso o seu negócio tenha crescido além do limite do MEI.",
        "beneficios": [
            "Recuperação do direito ao auxílio-doença e aposentadoria",
            "Manutenção do CNPJ ativo e regular",
            "Parcelamento de dívidas ativas"
        ],
        "publico": "Microempreendedores com atrasos ou que precisam de desenquadrar por excesso de faturação.",
        "diferencial": "Análise preventiva para evitar o desenquadramento surpresa pela Receita."
    },
    "declaracao-irpf": {
        "titulo": "Declaração IRPF MEI",
        "icone": "bi-file-earmark-bar-graph",
        "intro": "O maior erro do microempreendedor é não saber separar o lucro isento do tributável na sua pessoa física.",
        "detalhes": "Realizamos o cálculo exato da sua parcela de isenção baseada na sua atividade (8%, 16% ou 32%). Elaboramos a sua Declaração de Imposto de Renda de forma estratégica para garantir que não paga imposto sobre valores que já foram tributados na empresa, evitando que caia na malha fina por erros de preenchimento.",
        "beneficios": [
            "Cálculo exato da parcela isenta e tributável",
            "Proteção total contra a malha fina",
            "Aproveitamento máximo das deduções legais"
        ],
        "publico": "Proprietários de MEI e pequenos empresários que precisam de justificar o seu património.",
        "diferencial": "Cruzamento de dados prévio idêntico ao realizado pelos sistemas da Receita Federal."
    },
    "plano-de-carreira": {
        "titulo": "Plano de Carreira",
        "icone": "bi-graph-up-arrow",
        "intro": "Reter os melhores talentos é essencial para o crescimento sustentável. Organizamos a casa para que a sua empresa cresça em segurança.",
        "detalhes": "Estruturamos planos de carreira claros e objetivos para a sua equipa. Definimos critérios técnicos para a progressão de nível, faixas salariais baseadas no mercado atual e pacotes de benefícios. Isto aumenta consideravelmente a motivação dos colaboradores e traz enorme segurança jurídica contra eventuais litígios laborais.",
        "beneficios": [
            "Aumento na retenção de talentos chave",
            "Segurança jurídica em promoções e rescisões",
            "Transparência e equidade na equipa"
        ],
        "publico": "Empresas em fase de expansão que precisam de profissionalizar a gestão de Recursos Humanos.",
        "diferencial": "Alinhamento das métricas de RH com as metas financeiras da empresa."
    },
    "descricao-de-cargos": {
        "titulo": "Descrição de Cargos",
        "icone": "bi-people",
        "intro": "Mapeamos e documentamos detalhadamente as responsabilidades, requisitos e competências de cada função dentro da sua empresa.",
        "detalhes": "Uma descrição bem feita organiza a rotina, facilita imensamente os processos de recrutamento e integração de novos funcionários, e é a peça fundamental para garantir a equidade interna. Asseguramos o cumprimento rigoroso da legislação do trabalho, evitando acúmulo de funções indevido.",
        "beneficios": [
            "Agilidade nos processos de contratação",
            "Prevenção contra processos por desvio de função",
            "Clareza de responsabilidades para cada colaborador"
        ],
        "publico": "Empresas com equipas desestruturadas ou em rápido crescimento de pessoal.",
        "diferencial": "Mapeamento feito in loco com entrevistas às lideranças do seu negócio."
    },
    "consultoria-fiscal": {
        "titulo": "Consultoria Fiscal",
        "icone": "bi-calculator",
        "intro": "Uma análise profunda da operação da sua empresa para identificar oportunidades ocultas de poupança financeira.",
        "detalhes": "Através da Elisão Fiscal (forma legal de reduzir impostos), revemos toda a sua tributação atual. Auditamos as suas operações à procura de créditos tributários não aproveitados e desenvolvemos um planeamento estratégico anual focado em aumentar a sua margem de lucro de forma totalmente legal e 100% segura.",
        "beneficios": [
            "Redução legal e imediata da carga fiscal",
            "Recuperação de impostos pagos a mais no passado",
            "Prevenção de multas por inconformidades fiscais"
        ],
        "publico": "Pequenas e médias empresas que pretendem otimizar a sua margem de lucro operacional.",
        "diferencial": "Foco exclusivo em soluções legais (Elisão Fiscal) sem expor a empresa a riscos."
    }
}

@app.route('/servicos/<url_slug>')
def detalhe_servico(url_slug):
    servico = DADOS_SERVICOS.get(url_slug)
    
    if servico:
        return render_template('servico_detalhe.html', servico=servico)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
