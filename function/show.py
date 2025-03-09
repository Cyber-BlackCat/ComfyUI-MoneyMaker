# from nodes import PreviewImage, SaveImage, NODE_CLASS_MAPPINGS as ALL_NODE_CLASS_MAPPINGS
# import comfy.utils
# import folder_paths
import numpy as np
import json
# import pprint
import torch

from .utility import AlwaysEqualProxy


all_type = AlwaysEqualProxy("*")

class SomethingShow:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}, 
                "optional": {"something": (all_type, {}), },
                "hidden": {"unique_id": "UNIQUE_ID", 
                           "extra_pnginfo": "EXTRA_PNGINFO",
                           }}

    RETURN_TYPES = (all_type,)
    RETURN_NAMES = ('output',)
    INPUT_IS_LIST = True

    OUTPUT_NODE = True
    IS_OUTPUT = True
    FUNCTION = "someinput"
    CATEGORY = "MoneyMaker😺/show"

    def someinput(self, unique_id=None, extra_pnginfo=None, **kwargs):
        
        values = []

        if "something" in kwargs:
            for val in kwargs['something']:
                try:
                    if type(val) is str:
                        values.append(val)
                    elif type(val) is list:
                        values = val
                    elif hasattr(val, 'shape'):
                        # Extract shape if val is a tensor
                        values.append(str(list(val.shape)))
                    else:
                        val = json.dumps(val)
                        values.append(str(val))
                except Exception as e:
                    print(f"Exception occurred while processing 'something': {e}")
                    values.append(str(val))
                    pass                      

        if not extra_pnginfo:
            print("Error: extra_pnginfo is empty")
        elif (not isinstance(extra_pnginfo[0], dict) or "workflow" not in extra_pnginfo[0]):
            print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
        else:
            workflow = extra_pnginfo[0]["workflow"]
            # print(f"Workflow: {workflow}")
            node = next((x for x in workflow["nodes"] if str(x["id"]) == unique_id[0]), None)
            if node:
                # print(f"Node found: {node}")
                node["widgets_values"] = [values]
            else:
                print("Node not found")

        if isinstance(values, list) and len(values) == 1:
            # values = ",".join([str(x) for x in values]) #转为字符串
            print(f"values: {values}")
            return { "ui": {"text": values}, "result": (values[0],), }
        else:
            # values = ",".join([str(x) for x in values]) #转为字符串
            print(f"values: {values}")
            return { "ui": {"text": values}, "result": (values,), }
        # {"images": [image_tensor]}

class TensorShow:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"tensor": (all_type,)}, 
                "optional": {},
                "hidden": {"unique_id": "UNIQUE_ID", 
                            "extra_pnginfo": "EXTRA_PNGINFO",
                           }}

    RETURN_TYPES = (all_type,)
    RETURN_NAMES = ('tensor',)

    OUTPUT_NODE = True
    IS_OUTPUT = True
    FUNCTION = "showtensor"
    CATEGORY = "MoneyMaker😺/show"

    def showtensor(self, tensor, unique_id=None, extra_pnginfo=None, **kwargs):
        shapes = []
        
        def tensorShape(tensor):
            if isinstance(tensor, dict):
                for key in tensor:
                    tensorShape(tensor[key])
            elif isinstance(tensor, list):
                for i in range(len(tensor)):
                    tensorShape(tensor[i])
            elif hasattr(tensor, 'shape'):
                shapes.append(list(tensor.shape))

        
        print(f"Tensor values: {tensor}")  # 修正打印语句
        # check tensor attribute&data type
        if hasattr(tensor, 'shape') or isinstance(tensor, (list, dict)):
            tensorShape(tensor)

            # # 格式化
            # 将张量转换为列表
            # tensor_str = str(tensor)
            tensor_lsstr = [str(tensor)]
            # # shapes已经是一个列表了
            combined_list=["Tensor shape:"]+shapes+["\n"]+tensor_lsstr
            # combined_text = shapes+tensor_str
            # combined_text = pprint.pformat(combined_text)
            # print(f'Tensor shape: {shapes}\n\nTensor: {tensor_str}')
            print(f'Tensor shape: {shapes}')
            return { "ui": {"text": combined_list}}
        else:
            error_msg = f"Not a tensor or not have a shape attribute. Original input is: {tensor}"
            print(error_msg)
            return { "ui": {"text": [error_msg]}}