#coding: utf-8
from base import WxBaseService

class WxMenuService(WxBaseService):

    #创建菜单的地址
    CREATE_MENU_URL = "https://api.weixin.qq.com/cgi-bin/menu/create"
    #查询菜单的地址
    QUERY_MENU_URL = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info"

    def __init__(self, appid):
        super(WxMenuService, self).__init__(appid)

    def query_menu(self):
        """
        获取所有自定义菜单
        :return:  List
        """
        result = self.get(self.QUERY_MENU_URL)
        return result.get('selfmenu_info') if result else None

    def add_menu(self, data):
        """
        添加新的菜单（还在调试中)
        :param data:
        :return:
        """
        result = self.post(self.CREATE_MENU_URL, data=data)
        return result


if __name__ == '__main__':
    menu_service = WxMenuService('wxbd77bc158b32c535')
    data =  {
        "button": [
            {
                "url": "https://group.rocketai.cn/product?pid=3804&subchn=72",
                "type": "view",
                "name": "冠状病毒保障"
            }
        ]
}
    # print menu_service.add_menu(data)
    from utils.common import change_dic_to_json_str
    print change_dic_to_json_str(menu_service.add_menu(data))
