# worker.py
from jobs import q, update_job_status


  @q.worker
  def execute_job(jid):
      """
      Retrieve a job id from the task queue and execute the job.
      Monitors the job to completion and updates the database accordingly.
      """
      update_job_status(jid, "in progress")
      time.sleep(15)
      update_job_status(jid, "complete")
      # fill in ...
      # the basic steps are:
      # 1) get job id from message and update job status to indicate that the job has started
      # 2) start the analysis job and monitor it to completion.
      # 3) update the job status to indicate that the job has finished.
