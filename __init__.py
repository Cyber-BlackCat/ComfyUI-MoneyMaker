from .function.LightorDark import lightdarkjudgment
from .yuan.Yuan import ImageJudgment, imageMinusMask, blackandwhite, PSTransfer, LoadarandomImagefromdir


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique,一行不需要逗号，多行需要逗号
# 冒号后为函数名即'值' key is in the left of ":", and the value is the function name in the right of the ":".
NODE_CLASS_MAPPINGS = {
    # "Yuan": Yuan_node,
    "Black and white": blackandwhite,
    "Light or Dark": lightdarkjudgment,
    "PhotoShop Transfer": PSTransfer,
    "Image Judgment": ImageJudgment,
    "ImageMinusMask": imageMinusMask,
    "Load Random Images": LoadarandomImagefromdir,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Yuan": "Yuan fake Node",
    "Black and white": "Black & White Converter",
    "Light or Dark": "Light or Dark",
    "PhotoShop Transfer": "PS Transfer",
    "Image Judgment": "Image Judgment",
    "ImageMinusMask": "Image Minus Mask",
    "Load Random Images": "Load Random Images",
    # key is same as the CLASS MAPPINGS, and the value is displayed to the user which is in right of the ":".
    # 冒号后是节点上显示的名字，即此字典中的‘值’,多行对应多个节点，由jian
}

