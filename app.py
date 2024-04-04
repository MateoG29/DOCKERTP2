# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

app = Flask(__name__)

deployments = {
    'service1': {'version': '1.0.0', 'status': 'ok'},
    'service2': {'version': '1.2.1', 'status': 'ok'},
    'service3': {'version': '0.9.8', 'status': 'maintenance'}
}

@app.route("/")
def home():
    return "Bonjour!"

@app.route("/status")
def status():
    return jsonify(deployments)

@app.route("/status/<service>")
def service_status(service):
    service_info = deployments.get(service, None)
    if service_info:
        return jsonify(service_info)
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route("/deploy", methods=["POST"])
def deploy():
    service_name = request.json.get('service_name')
    version = request.json.get('version')
    status = request.json.get('status', 'ok')
    
    if service_name and version:
        deployments[service_name] = {'version': version, 'status': status}
        return jsonify({"message": f"Service {service_name} deployed successfully."})
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
