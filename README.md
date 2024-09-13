# 界面

标签和按钮放置在一个垂直布局内，设置对齐方式为水平居中对齐。水平策略都设置为fixed，防止水平拉伸。

第一个标签设置为粗体，字体大小18。

![image](assets/image-20240912005658-tl3d4ix.png)


最下方的方框用QWidget实现，为QWidget配置QSS，确保边框为虚线形式。

后面发现想要实现拖放文件需要用一个类继承QWidget，并且要覆盖对应的拖拽方法。仅仅使用designer貌似做不到这点。

![image](assets/image-20240912005818-wl6flao.png)


# 业务逻辑

按钮点击事件绑定文件选择对话框，使用`ElementTree`解析`xml`，按顺序递归遍历节点树每一个节点。

![image](assets/image-20240912005552-tc0kb2o.png)

每一个`ITEM`节点代表一个书签条目，再获取对应条目的页号，将这两者拼接为一个字符串，得到的字符串保存在列表`self.res`中。

![image](assets/image-20240912005611-sz4q7t1.png)

最后遍历`self.res`，将结果写入`原文件名+_new.xml`的文件中。

![image](assets/image-20240912005501-39f7yyg.png)
