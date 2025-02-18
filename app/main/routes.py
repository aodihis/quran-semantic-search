from flask import current_app, jsonify, request, render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/query', methods=['POST'])
def query_documents():
    data = request.get_json()
    query_texts = data.get('query_texts', [])
    n_results = data.get('n_results', 5)

    try:
        results = current_app.vector.query_documents(
            query_texts=query_texts,
            n_results=n_results
        )
        return jsonify({'status': 'success', 'results': results})
    except Exception as e:
        current_app.logger.error(f"Error querying documents: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500