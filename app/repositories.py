from .models import Job

class JobRepository:
    def create(self, data):
        job = Job(**data)
        job.save()
        return job

    def get_all(self):
        return Job.objects.all()

    def get_by_id(self, job_id):
        return Job.objects(id=job_id).first()

    def update(self, job_id, data):
        job = self.get_by_id(job_id)
        if job:
            job.update(**data)
            return self.get_by_id(job_id)
        return None

    def delete(self, job_id):
        job = self.get_by_id(job_id)
        if job:
            job.delete()
            return True
        return False
