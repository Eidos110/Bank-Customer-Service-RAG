from flask import Flask, request, jsonify, render_template
from app.rag_system import BankingRAGSystem
from app.utils import format_response
import os


app = Flask(__name__,
            template_folder='../frontend/templates',
            static_folder='../frontend/static')


# Initialize the RAG system
rag_system = BankingRAGSystem()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/query', methods=['POST'])
def query():
    """API endpoint for querying the RAG system."""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()

        if not question:
            return jsonify({'error': 'Question is required.'}), 400
        
        # Get response from the RAG system
        response = rag_system.query(question)
        formatted_response = format_response(response)

        return jsonify(formatted_response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/system_info', methods=['GET'])
def system_info():
    """API endpoint to system information"""
    try:
        info = rag_system.get_system_info()
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "Banking RAG System"})


if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    )
