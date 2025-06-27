import torch
import torch.nn.functional as torchfn

class MaskToGray:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "gray_intensity": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 1.0, "step": 0.01}),
                "invert": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "convert_to_gray"

    CATEGORY = "MoneyMaker😺"

    def convert_to_gray(self, mask, gray_intensity, invert):
        # 确保mask在0-1范围内
        mask = torch.clamp(mask, 0.0, 1.0)
        
        # 如果需要反转
        if invert:
            mask = 1.0 - mask
        
        # 将纯黑mask转换为灰色mask
        # gray_intensity控制灰色程度：
        # 0.0 = 保持原mask（纯黑）
        # 0.5 = 中等灰色
        # 1.0 = 完全白色
        gray_mask = mask * gray_intensity
        
        # 确保结果在0-1范围内
        gray_mask = torch.clamp(gray_mask, 0.0, 1.0)
        
        return (gray_mask,) 