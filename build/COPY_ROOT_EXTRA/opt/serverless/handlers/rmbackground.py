from handlers.basehandler import BaseHandler
import random
import time


"""
Handler classes are generally bound to a specific workflow file.
To modify values we have to be confident in the json structure.

One exception - RawWorkflow will send payload['workflow_json'] to the ComfyUI API after
downloading any URL's to the input directory and replacing the URL with a local path.
"""

class Image2Image(BaseHandler):
    
    WORKFLOW_JSON = "/opt/serverless/workflows/RemoveBG.json"
    
    def __init__(self, payload):
        super().__init__(payload, self.WORKFLOW_JSON)
        self.apply_modifiers()
        

    def apply_modifiers(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        """
        Input node
        """
        self.prompt["prompt"]["15"]["inputs"]["image"] = self.get_value(
            "input_image","")
        """

"""
Example Request Body:

{
    "input": {
        "handler": "Image2Image",
        "aws_access_key_id": "your-s3-access-key",
        "aws_secret_access_key": "your-s3-secret-access-key",
        "aws_endpoint_url": "https://my-endpoint.backblaze.com",
        "aws_bucket_name": "your-bucket",
        "webhook_url": "your-webhook-url",
        "webhook_extra_params": {},
        "ckpt_name": "v1-5-pruned-emaonly.ckpt",
        "include_text": "photograph of a victorian woman, arms outstretched with angel wings. cloudy sky, meadow grass",
        "exclude_text": "watermark, text",
        "denoise": 0.87,
        "input_image": "https://raw.githubusercontent.com/comfyanonymous/ComfyUI/master/input/example.png"
    }
}

"""
           
