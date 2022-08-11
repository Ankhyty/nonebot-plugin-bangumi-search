# bangumi-search

_:tada::tada::tada:助力你成为二次元婆罗门！:tada::tada::tada:_

## 简介

本插件可以帮你搜索 [bangumi](https://bgm.tv/)上的条目，并且根据你选择的搜索结果给你发送该条目的侧边简介栏和收藏盒。

## 特色功能

bangumi-search是一款以漫研为目的开发的插件。

- 使用[playwright](https://github.com/microsoft/playwright)作为无头浏览器，支持异步，效率更高。
- 使用re库对网页内容进行正则搜索，全面爬取条目链接。
- 方便懒得去打开bangumi网站的人查询番剧的监督、制作公司、放送时间等。

## 安装

- 推荐使用脚手架安装

```
pip install nonebot-plugin-bangumi-search
```

-然后在bot.py文件中添加

```
nonebot.load_plugin('nonebot-plugin-bangumi-search')
```

## 功能展示

- 使用 `/bgm` 指令触发机器人。
- 发送搜索内容和搜索类型，机器人会返回搜索结果。
- 再发送想浏览的搜索结果的数字顺序，机器人会返回该条目的侧边简介栏和收藏盒等信息。

![demo](/demo.jpg)

## 一些问题

- 虽然做了debug措施，但是搜索结果为空的时候还是可能会继续进行流程。
- bangumi网页的访问不稳定，虽然在代码中做了debug措施 `await page.reload()` ，但还是有概率经常访问不到。
- 没有可以手动或者自动终止流程的命令。
- 图片太长，容易刷屏。
- 不能对搜索结果进行翻页。

## 特别感谢

因为本人是第一次上手写nonebot插件，以及涉及OOP、playwright、异步等等内容的项目，因此找了不少大佬们做好的插件，从中学到了很多。

- [NoneBot2](https://github.com/nonebot/nonebot2)：本插件实装的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：稳定完善的 CQHTTP 实现。
- [HarukaBot](https://github.com/SK-415/HarukaBot)：网页截图的灵感来源。
- [miragetank](https://github.com/RafuiiChan/nonebot_plugin_miragetank)：学习了关于bot事件响应器的部分。

## 支持

大家喜欢的话可以给这个项目点个star

有bug、意见和建议都欢迎提交 [Issues](https://github.com/Ankhyty/nonebot-plugin-bangumi-search/issues) 

## 许可证
本项目使用 [MIT](https://choosealicense.com/licenses/mit/) 作为开源许可证。
