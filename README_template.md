# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioAI

## CardioSync

## 👨‍🎓 Integrantes:
- Alex da Silva Lima (RM559784)
- Johnatan Sousa Macedo Loriano (RM559546)
- Bruno Henrique Nielsen Conter (RM560518)
- Fabio Santos Cardoso (RM560479)

## 👩‍🏫 Professores:
### Tutor(a)
- Lucas Gomes Moreira
### Coordenador(a)
- André Godoi

## 📜 Descrição

Este repositório é dedicado ao projeto acadêmico CardioIA, desenvolvido para o curso de Inteligência Artificial da FIAP. O objetivo final do projeto é criar uma plataforma digital inteligente que simule um ecossistema de cardiologia moderna, integrando dados clínicos, modelos de Machine Learning, Visão Computacional, IoT e agentes inteligentes para auxiliar na triagem, diagnóstico, monitoramento e previsões médicas.

Este repositório foi criado com uma estrutura modular, pensando na evolução do projeto ao longo das próximas 7 fases do curso. A cada nova fase, o código-fonte e a documentação serão atualizados e expandidos.

---

### **Fase 1: Batimentos de Dados**

Nesta primeira fase, o grupo atuou como **Cientista de Dados Hospitalar**. O foco principal foi a coleta, organização e preparação de três tipos de dados fundamentais que servirão de base para o desenvolvimento dos módulos de IA.

*   **1. Dados Numéricos (IoT)**: O dataset numérico utilizado é o "Heart Disease UCI", um conjunto de dados clássico e amplamente utilizado, proveniente da Cleveland Clinic Foundation.
    *   **Fontes e Acesso aos Dados**:
        *   **Fonte Original (Kaggle)**: [Heart Disease UCI](https://www.kaggle.com/datasets/data855/heart-disease?resource=download)
        *   **Cópia Local**: Os dados brutos podem ser salvos no diretório `data/raw/` (ex: `data/raw/previsões de doenças cardíacas.csv`).
        *   **Cópia em Nuvem (Google Drive)**: [Link para o Google Drive](https://drive.google.com/file/d/1A8RgDcJegtEAq41ApoB67SSJTOjWMBmU/view?usp=sharing)

*   **2. Dados Textuais (NLP)**: Foram selecionados quatro artigos científicos em formato `.txt`, abordando diferentes dimensões das doenças cardiovasculares (DCV) no Brasil.
    *   **Caminho no Repositório**: Os arquivos de texto estão localizados na pasta `assets/`.

*   **3. Dados Visuais (Visão Computacional)**: O conjunto de dados visual é composto por mais de 100 imagens de Eletrocardiogramas (ECG) em formato `.png`, obtidas do repositório público "ECG-Image-Kit".
    *   **Link para as Imagens**: [https://github.com/alphanumericslab/ecg-image-kit/tree/main/sample-data/ecg-images](https://github.com/alphanumericslab/ecg-image-kit/tree/main/sample-data/ecg-images)
    *   **Imagens - Google Drive**: https://drive.google.com/drive/folders/1Q4JwGnt5m5cCo0OJoQPVVP7BS6pkjcJo?usp=drive_link

---

### **Fase 2: Início da IA avançada - Diagnóstico Automatizado**

Nesta fase, o projeto avançou para a criação de um sistema de **triagem e diagnóstico assistido por IA**, simulando como a tecnologia pode auxiliar profissionais de saúde na tomada de decisão. Foi desenvolvida uma solução de **IA Híbrida**, que combina o poder da análise semântica (IA Simbólica) com a capacidade de previsão do Machine Learning (IA Estatística).

O núcleo da solução está no notebook `notebooks/symptom_analysis_interactive.ipynb`, que orquestra duas abordagens principais:

*   **1. Análise Semântica para Diagnóstico Diferencial (Junta Médica Virtual):**
    *   **Objetivo:** Interpretar a descrição de um sintoma em linguagem natural e sugerir os diagnósticos mais prováveis.
    *   **Como funciona:** Utilizando a biblioteca `spaCy` e seu modelo de linguagem para português (`pt_core_news_md`), o sistema calcula a **similaridade semântica** entre a frase do paciente e as mais de 90 descrições de sintomas catalogadas na base de conhecimento (`assets/tabela_sintoma_diagnostico_risco.csv`).
    *   **Resultado:** O sistema apresenta as **três hipóteses diagnósticas** com maior similaridade, atuando como uma "junta médica virtual" que oferece diagnósticos diferenciais para o profissional de saúde.

*   **2. Classificação de Risco com Machine Learning:**
    *   **Objetivo:** Classificar automaticamente o nível de risco de um paciente (Alto, Médio ou Baixo) com base na descrição dos sintomas.
    *   **Como funciona:**
        1.  As frases da base de conhecimento são vetorizadas usando a técnica **TF-IDF**, que transforma o texto em uma representação numérica, dando mais importância às palavras que são relevantes para cada sintoma.
        2.  Um modelo de classificação (`DecisionTreeClassifier`) é treinado com esses vetores para aprender a associar os padrões de texto aos seus respectivos graus de risco.
    *   **Resultado:** O modelo é capaz de prever o risco de uma nova frase, fornecendo uma triagem rápida e automatizada, essencial para priorizar casos urgentes.

**Entregáveis e Artefatos Gerados:**

*   **Base de Conhecimento (`assets/tabela_sintoma_diagnostico_risco.csv`):** Um arquivo CSV robusto com 94 sintomas, mapeando descrições em primeira pessoa para o sintoma técnico, grau de risco e diagnóstico principal.
*   **Frases de Pacientes (`assets/frases_descricao_sintomas.txt`):** Um conjunto de frases que simulam relatos reais de pacientes, utilizado para testes em lote.
*   **Analisador em Lote (`src/symptom_analyzer.py`):** Um script que processa o arquivo de frases e aplica a lógica de análise de sintomas.
*   **Notebook Interativo (`notebooks/symptom_analysis_interactive.ipynb`):** A principal aplicação desta fase, onde é possível inserir uma frase e visualizar em tempo real a análise semântica e a previsão de risco do modelo de Machine Learning.
*   **Vídeo de Demonstração:** [Assista no YouTube](https://youtu.be/0_CQm8VvZyA)

---

### **Fase 3: CardioIA Conectada: IoT e Visualização de Dados**

Nesta fase, o projeto expandiu para o universo da Internet das Coisas (IoT), com o objetivo de criar um protótipo funcional de monitoramento contínuo de sinais vitais. Desviando da abordagem simulada, a equipe optou por uma **implementação com hardware real** para uma experiência mais prática e robusta.

A solução desenvolvida captura dados de sensores, os transmite para uma plataforma de processamento e os exibe em um dashboard interativo, simulando um sistema de monitoramento de saúde em tempo real.

A arquitetura foi dividida em três camadas:
*   **1. Edge (Captura de Dados):** Um microcontrolador **ESP32 C3 SuperMini** com um sensor **DHT22** coleta dados de temperatura e umidade. O código foi desenvolvido em C++ e pode ser encontrado em `docs/EntregaFase3_Cap1/sketch_dht22_Cardio.ino`.
*   **2. Comunicação (MQTT):** Os dados são transmitidos via Wi-Fi para um broker **MQTT** (Mosquitto) rodando em um **Raspberry Pi 3B**, que atua como servidor na rede local.
*   **3. Fog/Cloud (Processamento e Visualização):** O **Node-RED**, também no Raspberry Pi, assina os tópicos MQTT, recebe os dados, e os exibe em um dashboard com gráficos, medidores e alertas visuais. O fluxo também inclui uma integração para enviar notificações via Telegram.

**Entregáveis e Artefatos Gerados:**

*   **Código do Microcontrolador (`docs/EntregaFase3_Cap1/sketch_dht22_Cardio.ino`):** Sketch C++ para o ESP32 que realiza a leitura do sensor e a comunicação MQTT.
*   **Fluxo do Node-RED (`docs/EntregaFase3_Cap1/flows_node_red.json`):** Arquivo de exportação do fluxo completo, incluindo a lógica do dashboard e os alertas.
*   **Relatório Detalhado (`relatorio_fase3_cardioAi.md`):** Documento markdown com a descrição completa da arquitetura, implementação e resultados da fase.
*   **Evidências Visuais (`docs/EntregaFase3_Cap1/`):** A pasta contém fotos do hardware utilizado (`fotoProjetoHomelab.jpg`, `fotoRaspberryPi_3B.jpg`) e prints do dashboard e do fluxo no Node-RED (`PrintDashBoardNodeRed.png`, `PrintFlowNodeRed.png`).

---
### **Dados Visuais (Visão Computacional)**

*   **Descrição e Origem**: O conjunto de dados visual é composto por mais de 100 imagens de Eletrocardiogramas (ECG) em formato `.png`. As imagens foram obtidas do repositório público "ECG-Image-Kit", que fornece um kit de ferramentas para trabalhar com imagens de ECG.

*   **Link para as Imagens**: [https://github.com/alphanumericslab/ecg-image-kit/tree/main/sample-data/ecg-images](https://github.com/alphanumericslab/ecg-image-kit/tree/main/sample-data/ecg-images)
  
*   **Fonte Complementar (Google Drive)**: [Link para o Google Drive](https://drive.google.com/drive/folders/1Q4JwGnt5m5cCo0OJoQPVVP7BS6pkjcJo?usp=drive_link)

*   **Relevância e Exploração com Visão Computacional**: Imagens de ECG são fundamentais para o diagnóstico de uma vasta gama de condições cardíacas. A aplicação de algoritmos de Visão Computacional (VC) sobre esses dados permite automatizar e escalar a análise, trazendo grande valor para a área da saúde.

    *   **Detecção de Padrões e Segmentação**: Modelos de VC podem ser treinados para identificar e segmentar as diferentes ondas (P, QRS, T), segmentos (ST) e intervalos (PR, QT) em uma imagem de ECG.
        *   **Justificativa**: A análise precisa das características e durações desses padrões é a base do diagnóstico por ECG. A automação dessa tarefa permite extrair medições quantitativas de forma rápida e consistente, auxiliando na identificação de irregularidades.

    *   **Reconhecimento de Anomalias e Classificação**: Uma vez que os padrões são identificados, a IA pode ser usada para detectar anomalias e classificar os ECGs. Por exemplo, um modelo pode aprender a diferenciar um ritmo sinusal normal de arritmias comuns, como fibrilação atrial, ou a identificar sinais de isquemia e infarto do miocárdio (ex: elevação ou depressão do segmento ST).
        *   **Justificativa**: Um sistema de IA capaz de realizar essa classificação pode atuar como uma ferramenta de triagem, alertando médicos sobre exames críticos que necessitam de atenção imediata. Isso otimiza o fluxo de trabalho, reduz o tempo para o diagnóstico e pode ser crucial em emergências.

    *   **Identificação de Bordas e Características Morfológicas**: Algoritmos de identificação de bordas podem ser aplicados para analisar a morfologia das ondas (sua forma, altura e contorno), que também contém informações diagnósticas importantes.
        *   **Justificativa**: Mudanças sutis na forma das ondas, que podem ser difíceis de quantificar manualmente, podem ser detectadas por um modelo de IA, oferecendo um nível adicional de detalhe para o diagnóstico e auxiliando na detecção precoce de patologias.

Para detalhes completos sobre os próximos passos e entregáveis desta fase, consulte o documento [next_steps.md](docs/next_steps.md).

---

## 📁 Estrutura de Pastas

O projeto está organizado com uma estrutura de pastas modular para suportar as diferentes fases de desenvolvimento, desde a análise de dados até a implementação dos modelos de IA.

```
.
├── .github/         # Configurações do GitHub (ex: templates de issue).
├── assets/          # Arquivos de dados não-estruturados (textos, imagens, etc.).
├── config/          # Arquivos de configuração do projeto.
├── data/            # Datasets utilizados no projeto.
│   ├── raw/         # Dados brutos e imutáveis (ex: CSVs originais).
│   └── processed/   # Dados intermediários ou limpos após processamento.
├── docs/            # Documentação do projeto (relatórios, diagramas, etc.).
├── notebooks/       # Jupyter notebooks para análise exploratória e modelagem.
├── scripts/         # Scripts auxiliares (ex: automação, deploy, migração).
├── src/             # Código-fonte principal da aplicação e modelos de IA.
├── .gitattributes   # Define atributos por caminho do Git.
├── .gitignore       # Especifica arquivos a serem ignorados pelo Git.
└── README.md        # Este arquivo.
```

## 🔧 Como executar o código

### **Fase 3: Monitoramento com IoT**

A execução desta fase requer a montagem do hardware e a configuração dos serviços.

1.  **Hardware:**
    *   Um microcontrolador ESP32 (no projeto, um C3 SuperMini).
    *   Um sensor de temperatura e umidade DHT22.
    *   Um Raspberry Pi (no projeto, um 3B) ou outro computador para atuar como servidor.
2.  **Configuração do ESP32:**
    *   Abra o arquivo `docs/EntregaFase3_Cap1/sketch_dht22_Cardio.ino` na IDE do Arduino.
    *   Atualize as credenciais de Wi-Fi (`WIFI_SSID`, `WIFI_PASS`) e do broker MQTT (`MQTT_SERVER`, `MQTT_USER`, `MQTT_PASS`).
    *   Flashe o código no ESP32.
3.  **Configuração do Servidor (Raspberry Pi):**
    *   Instale um broker MQTT, como o Mosquitto.
    *   Instale o Node-RED.
    *   Inicie o Node-RED e importe o fluxo a partir do arquivo `docs/EntregaFase3_Cap1/flows_node_red.json`.
    *   Acesse o dashboard do Node-RED no seu navegador (geralmente em `http://<IP_DO_RASPBERRY_PI>:1880/ui`).

### **Fase 2: Análise de Sintomas com NLP**

Para executar a análise de sintomas baseada em Processamento de Linguagem Natural (NLP), foram criados um script de análise em lote e um notebook interativo.

**Pré-requisitos:**

Certifique-se de que as bibliotecas `spaCy` e seu modelo de português estão instalados:
```bash
pip install spacy pandas
python -m spacy download pt_core_news_sm
```

**1. Análise em Lote via Script**

O script `src/symptom_analyzer.py` analisa todas as frases contidas em `assets/frases_descricao_sintomas.txt` e, para cada uma, identifica o sintoma, o risco e o diagnóstico correspondente da base de conhecimento.

Para executá-lo, utilize o seguinte comando na raiz do projeto:
```bash
python src/symptom_analyzer.py
```

**2. Análise Interativa via Jupyter Notebook**

Para uma análise interativa, onde você pode inserir uma frase e obter o resultado, utilize o notebook `notebooks/symptom_analysis_interactive.ipynb`.

1.  Inicie o JupyterLab (instruções na seção anterior).
2.  Abra o arquivo `notebooks/symptom_analysis_interactive.ipynb`.
3.  Execute as células para carregar as dependências e a base de conhecimento.
4.  Na última célula, você pode alterar a frase de exemplo para testar qualquer descrição de sintoma.

### **Fase 1: Preparação de Dados**

1.  **Pré-requisitos**:
    *   Python 3.x
    *   Bibliotecas Python para análise de dados (ex: Pandas, Matplotlib, scikit-learn).
    *   Git para clonar o repositório.

2.  **Instalação e Execução**:
    ```bash
    # Clone o repositório
    git clone [https://github.com/brunocorisco86/cardioai.git](https://github.com/brunocorisco86/cardioai.git)

    # Navegue até a pasta do projeto
    cd cardioai

    # Instale as dependências (se aplicável para fases futuras)
    pip install -r requirements.txt
    ```
    Nesta fase, o foco é a organização dos dados e da documentação. O código de análise será desenvolvido nas próximas etapas e adicionado na pasta `src/`.

3.  **Jupyter Notebooks**:

    Na pasta `notebooks/`, você encontrará os seguintes notebooks:

    *   `eda.ipynb`: Realiza uma análise exploratória dos dados (EDA) do dataset de doenças cardíacas. Este notebook carrega os dados, exibe informações básicas, estatísticas descritivas e visualizações para entender a distribuição e as relações entre as variáveis.
    *   `model_building.ipynb`: Demonstra a construção de um modelo de classificação simples (Regressão Logística) para prever a presença de doenças cardíacas. O notebook inclui o pré-processamento dos dados, a divisão em conjuntos de treino and teste, o treinamento do modelo e a avaliação de sua performance.

    Para executar os notebooks, você precisará ter o Jupyter Notebook ou o JupyterLab instalado:

    ```bash
    # Instale o JupyterLab
    pip install jupyterlab

    # Inicie o JupyterLab na pasta do projeto
    jupyter-lab
    ```

## 🗃 Histórico de lançamentos

*   0.3.0 - 24/10/2025
    *   Concluída a Fase 3: CardioIA Conectada.
    *   Implementado protótipo de monitoramento IoT com hardware real (ESP32, DHT22, Raspberry Pi).
    *   Desenvolvido dashboard em Node-RED para visualização de dados em tempo real e sistema de alertas via Telegram.
    *   Adicionados todos os artefatos da fase, incluindo código do ESP32, fluxo do Node-RED e relatório detalhado.
    *   Atualizado o `README.md` com a documentação e instruções da Fase 3.
*   0.2.3 - 08/10/2025
    *   Refatorada a documentação da Fase 2 no `README.md` para detalhar a abordagem de IA Híbrida e a solução desenvolvida.
    *   Adicionado o link para o vídeo de demonstração da Fase 2.
    *   Finalizados e commitados os artefatos da Fase 2, incluindo o notebook interativo e a reorganização da pasta de documentação.
*   0.2.2 - 06/10/2025
    *   Concluído "Parte 1 - Entregável 3": Desenvolvido o script `src/symptom_analyzer.py` que utiliza NLP (spaCy) para analisar frases de sintomas, identificar o sintoma correspondente, o grau de risco e o diagnóstico associado.
    *   Criado o notebook `notebooks/symptom_analysis_interactive.ipynb` para permitir a análise interativa de frases de sintomas.
    *   Atualizado o `README.md` com a seção "Análise de Sintomas com NLP" e instruções de uso.
*   0.2.1 - 06/10/2025
    *   Início da Fase 2: Início da IA avançada - Diagnóstico Automatizado.
    *   Concluído "Parte 1 - Entregável 1": Criação do arquivo `assets/frases_descricao_sintomas.txt`.
    *   Concluído "Parte 1 - Entregável 2": Criação do arquivo `tabela_sintoma_diagnostico_risco.csv`.
    *   Atualizado `docs/next_steps.md` para refletir o progresso da Fase 2.
    *   Atualizado `README.md` com informações da Fase 2 e link para `next_steps.md`.
*   0.2.0 - 03/09/2025
    *   Adicionado diretório `notebooks` para análise de dados e modelagem.
    *   Criado notebook `eda.ipynb` para análise exploratória dos dados.
    *   Criado notebook `model_building.ipynb` para construção de um modelo de classificação.
    *   Adicionado `requirements.txt` com as dependências do projeto.
    *   Atualizado o `README.md` com as novas seções e informações.
*   0.1.0 - 14/08/2025
    *   Estrutura inicial do repositório
    *   Coleta e organização dos datasets numéricos, textuais e visuais (Fase 1)
    *   Criação do README.md detalhado

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
