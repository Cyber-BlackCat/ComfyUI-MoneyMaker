from typing import Iterator, List, Tuple, Dict, Any, Union, Optional
from _decimal import Context, getcontext
from decimal import Decimal
from nodes import PreviewImage, SaveImage, NODE_CLASS_MAPPINGS as ALL_NODE_CLASS_MAPPINGS
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from PIL.PngImagePlugin import PngInfo

import numpy as np
import time
import os
import re
import csv
import json
import torch
import comfy.utils
import folder_paths

from .utility import AlwaysEqualProxy, ByPassTypeTuple, TautologyStr
# 导入comfyui默认节点中的内容
from nodes import PreviewImage, SaveImage, NODE_CLASS_MAPPINGS as ALL_NODE_CLASS_MAPPINGS

all_type = AlwaysEqualProxy("*")

class ShowSomething:
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
    RETURN_NAMES = ('sth',)
    INPUT_IS_LIST = True

    OUTPUT_NODE = True

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
            print(f"values: {values}")
            return { "ui": {"text": values}, "result": (values[0],), }
        else:
            print(f"values: {values}")
            return { "ui": {"text": values}, "result": (values,), }

class ShowTensor:
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

    FUNCTION = "showtensor"
    CATEGORY = "MoneyMaker😺/show"

    def showtensor(self, tensor, unique_id=None, extra_pnginfo=None, **kwargs):
        shapes = []

        def tensorShape(tensor):
            if isinstance(tensor, dict):
                for k in tensor:
                    tensorShape(tensor[k])
            elif isinstance(tensor, list):
                for i in range(len(tensor)):
                    tensorShape(tensor[i])
            elif hasattr(tensor, 'shape'):
                shapes.append(list(tensor.shape))

        print(f"Tensor before shape extraction: {tensor}")
        if hasattr(tensor, 'shape') or isinstance(tensor, (list, dict)):
            tensorShape(tensor)
            print(f"Extracted shapes: {shapes}")
            return { "ui": {"text": shapes}}
        else:
            print("Input is not a tensor or does not have a shape attribute.")
            return { "ui": {"text": "Input is not a tensor or does not have a shape attribute."}}
