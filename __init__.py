from .function.LightorDark import lightdarkjudgment
from .yuan.Yuan import ImageJudgment, imageMinusMask, blackandwhite, PSTransfer, LoadarandomImagefromdir


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    # "Yuan": Yuan_node,
    "Black and white": blackandwhite,
    "PhotoShop Transfer": PSTransfer,
    "Image Judgment": ImageJudgment,
    "ImageMinusMask": imageMinusMask,
    "Load Random Images": LoadarandomImagefromdir,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "Yuan": "Yuan fake Node",
    "YuanBW": "Yuan Black and White Converter",
    "Light or Dark": "Light or Dark",
    "Yuan Transfer": "Yuan Transfer",
    "Image Judgment": "ImageJudgment",
    "ImageMinusMask": "Image Minus Mask"
    # 冒号后是节点上显示的名字,多行对应多个节点
    # After the colon is the name displayed on the node. Multiple lines correspond to multiple nodes
}

