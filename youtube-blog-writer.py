from autogenstudio import WorkflowManager
# load workflow from exported json workflow file.
workflow_manager = WorkflowManager(workflow="workflow_Youtube_Blog_Workflow.json")

# run the workflow on a task
task_query = "Generate a blog post for https://www.youtube.com/watch?v=Rfws9ZMmkJk"
workflow_manager.run(message=task_query)
