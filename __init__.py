from .function.LightorDark import lightdarkjudgment
from .function.mask_morphology import MaskPreprocessMorphology
from .function.mask_to_gray import MaskToGray
from .function.show import SomethingShow, TensorShow
from .coin.MMk import ImageJudgment, imageMinusMask, blackandwhite, PSTransfer, LoadarandomImagefromdir, Number_Decimal
from .coin.image_scale_keep_proportion import ImageResizeKeepProportion


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique

NODE_CLASS_MAPPINGS = {
    # "a fake Nod": MMk_node,
    "Black and white": blackandwhite,
    "Light or Dark": lightdarkjudgment,
    "PhotoShop Transfer": PSTransfer,
    "Image Judgment": ImageJudgment,
    "ImageMinusMask": imageMinusMask,
    "Load Random Images": LoadarandomImagefromdir,
    "Mask Preprocess Morphology": MaskPreprocessMorphology,
    "Mask To Gray": MaskToGray,
    "Number": Number_Decimal,
    "SomethingShow": SomethingShow,
    "TensorShow": TensorShow,
    "Image Resize MM": ImageResizeKeepProportion,

    # key is in the left of ":", and the value is the function name in the right of the ":".键左，冒号后为函数名即'值' 
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # "MMk": "a fake Node",
    "Black and white": "Black & White Converter",
    "Light or Dark": "Light or Dark",
    "PhotoShop Transfer": "PS Transfer",
    "Image Judgment": "Image Judgment",
    "ImageMinusMask": "Image Minus Mask",
    "Load Random Images": "Load Random Images",
    "Mask Preprocess Morphology": "Mask Preprocess Morphology",
    "Mask To Gray": "Mask To Gray",
    "Number": "Number",
    "SomethingShow": "Something Show",
    "TensorShow": "Tensor Show",
    "Image Resize MM": "Image Resize (keep proportion)",

    # key is same as the CLASS MAPPINGS, and the value is displayed to the user which is in right of the ":".
    # 冒号后是节点上显示的名字，即此字典中的'值',多行对应多个节点。
}

# ========== 版本和前端配置 ==========
__version__ = "1.1.0"  # 遵循语义化版本规范
WEB_DIRECTORY = "./moneymakerweb"  # 直接指向 web 目录

# ========== 兼容性处理 ==========
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]