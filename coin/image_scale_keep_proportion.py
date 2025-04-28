from comfy.utils import common_upscale

class ImageResizeKeepProportion:
    upscale_methods = ["nearest-exact", "bilinear", "area", "bicubic", "lanczos"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "max_width": ("INT", { 
                    "default": 1024, 
                    "min": 1, 
                    "max": 8192,  # 按需调整最大值
                    "step": 1 
                }),
                "max_height": ("INT", { 
                    "default": 1024, 
                    "min": 1, 
                    "max": 8192,
                    "step": 1 
                }),
                "method": (cls.upscale_methods, {"default": "nearest-exact"}),
            }
        }

    RETURN_TYPES = ("IMAGE","INT", "INT",)
    RETURN_NAMES = ("image","Width","Height")
    FUNCTION = "resize"
    CATEGORY = "MoneyMaker😺/image"

    def resize(self, image, max_width, max_height, method):
        """
        对图像进行等比例缩放，使其宽度和高度不超过指定的最大值。
        
        :param image: 输入图像，形状为(B, H, W, C)
        :param max_width: 最大宽度
        :param max_height: 最大高度
        :param method: 缩放方法，可选值为nearest-exact、bilinear、area、bicubic、lanczos
        :return: 缩放后的图像
        """
        # 获取图像的形状
        batch_size, height, width, channels = image.shape
        
        # 如果图像宽度和高度均小于等于最大值，则无需缩放
        if width <= max_width and height <= max_height:
            return (image,)
        
        # 计算等比例缩放因子
        width_ratio = max_width / width
        height_ratio = max_height / height
        scale_factor = min(width_ratio, height_ratio)
        
        # 计算新宽度和高度
        new_width = round(width * scale_factor)
        new_height = round(height * scale_factor)
        
        # 执行缩放操作
        # 将图像的通道维度移动到第1维，以适配common_upscale函数的输入要求
        image = image.movedim(-1, 1)
        resized_image = common_upscale(
            image, 
            new_width, 
            new_height, 
            method, 
            "disabled"  # 禁用裁剪
        )
        # 将通道维度移回原位置
        resized_image = resized_image.movedim(1, -1)
        
        return (resized_image,resized_image.shape[2], resized_image.shape[1],)
