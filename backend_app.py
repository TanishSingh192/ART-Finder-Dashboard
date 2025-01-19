from flask import Flask, request, jsonify
from flask_cors import CORS
from langflow import load_flow_from_json
impo

app = Flask(__Json p.y _)
CORS(app)

# Load the Langflow JSON
with open('langflow_config.json', 'r') as f:
    langflow_json = json.load(f)

# Initialize the Langflow
flow = load_flow_from_json(langflow_json)

@app.route('/api/research', methods=['POST'])
def conduct_research():
    topic = request.json['topic']
    
    # Use Langflow to process the topic
    result = flow({"topic": topic})
    
    # Parse the Langflow output
    pain_points = result.get('pain_points', [])
    competitor_data = result.get('competitor_analysis', {})
    insights = result.get('insights', [])

    return jsonify({
        'pain_points': pain_points,
        'competitor_data': competitor_data,
        'insights': insights
    })

if __name__ == '__main__':
    app.run(debug=True)

