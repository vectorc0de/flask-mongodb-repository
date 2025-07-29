
from flask import Blueprint, request, jsonify
from .repositories import JobRepository

bp = Blueprint('jobs', __name__, url_prefix='/jobs')
job_repository = JobRepository()

@bp.route('/', methods=['POST'])
def create_job():
    data = request.get_json()
    job = job_repository.create(data)
    return jsonify(job.to_mongo().to_dict()), 201

@bp.route('/', methods=['GET'])
def get_jobs():
    jobs = job_repository.get_all()
    return jsonify([job.to_mongo().to_dict() for job in jobs])

@bp.route('/<job_id>', methods=['GET'])
def get_job(job_id):
    job = job_repository.get_by_id(job_id)
    if job:
        return jsonify(job.to_mongo().to_dict())
    return jsonify({'error': 'Job not found'}), 404

@bp.route('/<job_id>', methods=['PUT'])
def update_job(job_id):
    data = request.get_json()
    job = job_repository.update(job_id, data)
    if job:
        return jsonify(job.to_mongo().to_dict())
    return jsonify({'error': 'Job not found'}), 404

@bp.route('/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    if job_repository.delete(job_id):
        return jsonify({'message': 'Job deleted'})
    return jsonify({'error': 'Job not found'}), 404
