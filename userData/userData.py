# -*- coding: utf-8 -*-

cookieDatas = [{ #网页版B站账户登录后的cookie填写在此，支持多账户；用于B站直播签到，投币分享视频，模拟观看视频来获取经验
    "SESSDATA": "",
    "bili_jct": "",
    "DedeUserID": "",
    }]#登录一次有效期为90天,注意过期后及时更新

app_access_keys = [""] #在这里填入B站客户端access_keys，支持多账户；用于客户端直播获取时间宝箱领取银瓜子和漫画签到
#注：B站客户端与B站漫画客户端的access_keys是通用的,可以相互登录,登录一次有效期为30天,注意过期后及时更新

SCKEY = "" #感谢server酱提供的推送微信消息服务，详情见http://sc.ftqq.com/，用于微信消息推送