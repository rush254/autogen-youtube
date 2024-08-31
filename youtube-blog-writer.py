from autogenstudio import WorkflowManager
# load workflow from exported json workflow file.
workflow_manager = WorkflowManager(workflow="workflow_Youtube_Blog_Workflow.json")

# run the workflow on a task
task_query = "Write a blog post for https://www.youtube.com/watch?v=Rfws9ZMmkJk and save the result as a markdown" 
workflow_manager.run(message=task_query)
