#coding: utf-8
from base import WxBaseService

class WxMaterialService(WxBaseService):

    #上传素材的地址
    UPLOAD_MATERIAL_URL = "https://api.weixin.qq.com/cgi-bin/material/add_material?type={0}"

    def __init__(self, appid):
        super(WxMaterialService, self).__init__(appid)

    def upload_image(self, filepath):
        """
        上传图片素材
        :param filepath:
        :return: media_id:  String
        """
        url = self.UPLOAD_MATERIAL_URL.format('image')

        file = {}
        file['media'] = open(filepath, 'rb')

        result = self.post(url, file=file)
        return result.get('media_id') if result else None


if __name__ == '__main__':
    material_service = WxMaterialService('wxbd77bc158b32c535')
    print material_service.upload_image('cat.jpg')

