import json
from .utility import AlwaysEqualProxy

any_type = AlwaysEqualProxy("*")
class ShowSomething:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}, "optional": {"anything": ("any_type", {}), },
                "hidden": {"unique_id": "UNIQUE_ID", "extra_pnginfo": "EXTRA_PNGINFO",
                           }}

    RETURN_TYPES = ("any_type",)
    RETURN_NAMES = ('output',)
    INPUT_IS_LIST = True
    OUTPUT_NODE = True
    FUNCTION = "log_input"
    CATEGORY = "MoneyMaker😺/show"

    def log_input(self, unique_id=None, extra_pnginfo=None, **kwargs):

        values = []
        if "anything" in kwargs:
            for val in kwargs['anything']:
                try:
                    if isinstance(val, str):
                        values.append(val)
                    elif isinstance(val, list):
                        values.extend(val)
                    else:
                        val = json.dumps(val)
                        values.append(str(val))
                except Exception as e:
                    values.append(f"Error processing value: {str(e)}")

        if not extra_pnginfo:
            print("Error: extra_pnginfo is empty")
        elif (not isinstance(extra_pnginfo[0], dict) or "workflow" not in extra_pnginfo[0]):
            print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
        else:
            workflow = extra_pnginfo[0]["workflow"]
            node = next((x for x in workflow["nodes"] if str(x["id"]) == unique_id[0]), None)
            if node:
                node["widgets_values"] = [values]

        return {"ui": {"text": values}, "result": tuple(values)}

class ShowTensorShapeLayout:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"tensor": ("any_type",)}, "optional": {},
                "hidden": {"unique_id": "UNIQUE_ID", "extra_pnginfo": "EXTRA_PNGINFO"
                           }}

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    INPUT_IS_LIST = True
    OUTPUT_NODE = True
    FUNCTION = "log_input"
    CATEGORY = "MoneyMaker😺/show"

    def log_input(self, tensor, unique_id=None, extra_pnginfo=None):
        shapes = []
        layouts = []

        def tensor_shape(tensor):
            if isinstance(tensor, dict):
                for k in tensor.values():
                    tensor_shape(k)
            elif isinstance(tensor, list):
                for item in tensor:
                    tensor_shape(item)
            elif hasattr(tensor, 'shape'):
                shape = list(tensor.shape)
                shapes.append(shape)
                layout = self.detect_layout(shape)
                layouts.append(layout)

        def detect_layout(shape):
            # Common dimension orders: NCHW (Batch, Channels, Height, Width) and NHWC (Batch, Height, Width, Channel)
            if len(shape) == 4:
                if shape.index(max(shape)) == 1:
                    return "NCHW"
                elif shape.index(max(shape)) == 3:
                    return "NHWC"
            return "Unknown Tensor Layout"

        tensor_shape(tensor)

        result = [{"shape": shape, "layout": layout} for shape, layout in zip(shapes, layouts)]
        return {"ui": {"text": result}}
