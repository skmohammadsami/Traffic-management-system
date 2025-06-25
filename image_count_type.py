
"""
stage 1:
Sample output: {'bike':19, 'car':3, 'truck':4, 'auto':0, 'bus':0}


Stage 2:

Sample Data:
sno     bike    auto    car     truck   bus     time(dependent variable)

"""
from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="SJunF9ZGtD6LD9YnNUkI"
)

result = client.run_workflow(
    workspace_name="sih-ggtws",
    workflow_id="detect-count-and-visualize-3",
    images={
        "image": "test1.jpg"
    },
    use_cache=True # cache workflow definition for 15 minutes
)


print("No of objects: " , result[0]["count_objects"])

print(result[0]["predictions"]["predictions"][0]["class"])