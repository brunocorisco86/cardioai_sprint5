from flask import Flask, request, jsonify
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configurações do Watson Assistant
API_KEY = os.getenv('WATSON_ASSISTANT_APIKEY')
SERVICE_URL = os.getenv('WATSON_ASSISTANT_URL')
ASSISTANT_ID = os.getenv('WATSON_ASSISTANT_ID')

authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(SERVICE_URL)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    text = data.get('text', '')
    session_id = data.get('sessionId')

    try:
        if not session_id:
            session = assistant.create_session(assistant_id=ASSISTANT_ID).get_result()
            session_id = session['session_id']

        response = assistant.message(
            assistant_id=ASSISTANT_ID,
            session_id=session_id,
            input={'message_type': 'text', 'text': text}
        ).get_result()

        # Extrair texto da resposta generic do Watson V2
        output_text = "Desculpe, não entendi."
        if 'output' in response and 'generic' in response['output']:
            for item in response['output']['generic']:
                if item.get('response_type') == 'text':
                    output_text = item.get('text')
                    break

        return jsonify({
            'sessionId': session_id,
            'response': output_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
