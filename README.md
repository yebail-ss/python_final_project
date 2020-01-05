# python_final_project
### python期末项目
- [github_url](https://github.com/yebail-ss/python_final_project)

- [pythonanywhere_url_1较完整故事描述](http://forgunsmatter.pythonanywhere.com/)

- [pythonanywhere_url_2]专门做的枪手介绍描述(http://forgunsmatter2.pythonanywhere.com/)

#### 链接个数以及说明

- ##### 共十三个url
- [故事封面](http://forgunsmatter.pythonanywhere.com/page_cover.html)
- [故事描述](http://forgunsmatter.pythonanywhere.com/page_00_the_description.html)
- [私有枪支数量](http://forgunsmatter.pythonanywhere.com/page_01_Number_of_guns.html)
- [可视化枪支事件](http://forgunsmatter.pythonanywhere.com/page_02_shooting.html)
- [受伤害的人的数量](http://forgunsmatter.pythonanywhere.com/page_04_Injured_person.html)
- [拉斯维加斯枪击事件](http://forgunsmatter.pythonanywhere.com/page_05_Las_Vegas_shootings.html)
- [每年发生的大型枪击事件数量](http://forgunsmatter.pythonanywhere.com/page_06_Number_of_shootings.html)
- [枪手信息](http://forgunsmatter2.pythonanywhere.com/)
- [枪支暴力事件描述](http://forgunsmatter.pythonanywhere.com/page_09_Gun_violence.html)
- [易受攻击人群](http://forgunsmatter.pythonanywhere.com/page_08_frequent_words.html)
- [易受攻击的州和城市](http://forgunsmatter.pythonanywhere.com/page_10_Who_was_attacked.html)
- [案件多发生的具体地点](http://forgunsmatter.pythonanywhere.com/page_12_where.html)
- [总结](http://forgunsmatter.pythonanywhere.com/page_13_total_thing.html)








#### 基本交互功能html5控件使用丰富性
- 使用select实现下拉框，li标签与a标签结合写导航栏，利用input控件的submit属性与form结合实现提交表单的功能

#### github文档格式
（包含基本的templates，static，story.py以及三个csv数据文档）
#### html档描述
- 主要写了十五个html文档，分别传输不同的故事
- 文档里都写有导航栏（li组件与a标签组合实现此功能）和翻页按钮（button组件与a标签组合实现此功能）

#### Python档描述
- 导入了需要用到的模块
- 对数据进行处理
- 写了不同的路径
- py文件中为第一个页面设立路径为"/"
   通过"return render_template"将封装好的"over_line_sactter"函数的数据和"page_01_Number_of_guns.html页面到"/"
- py文件为第二个页面设定路径为"/page_02_shooting.html"
   用过"return render_template"传输了"/page_02_shooting.html"函数
- py文件为第三个页面设定路径为"/page_03_details.html"，通过"return render_template"传输了
  "page_03_details.html",为传输做准备特地处理的数据"data_str"和"region_available"
- py文件为第四个页面设定路径为"/map_details"，需要通过第三个页面提交表单才可以触发跳转，通过return render_template传输"page_03_details.html",为数据传输准备的"plot_all","data_str""regions_available"
- py文件第五个页面设定路径为"/page_04_Injured_person.html",需要通过return render_template 传输"page_04_Injured_person.html"
- py文件第六个页面设定路径为'/page_05_Las_Vegas_shootings.html'.通过return render_template 传输了page_05_Las_Vegas_shootings.html页面以及经过pandas处理的列表详情
- [杀手具体信息](http://forgunsmatter2.pythonanywhere.com/)  return render_template去传输html页面，html页面的图片是通过jinjia2语法加html语法结合放置的图片
- [词云图](http://forgunsmatter.pythonanywhere.com/page_08_frequent_words.html)  通过return render_template去传输html页面，html页面的图片是通过jinjia2语法加html语法结合放置的图片
- page_10_Who_was_attacked.html和/page_11_the_top_states.html和'/page_12_where.html'都是通过return render_template传递数据，
- '/select' 写了post方法，结合python判断加select的html控件实现跳转
- "/map_01_details.html"中用了事件组，面向对象编程， 并且通过 save方式将可视化函数的代码导出为html
-  /map_02_details.html save方式将可视化函数的代码导出为html，并通过return render_templatate导出html
#### 数据交互
- 具有较复杂的结构嵌套（函数内含数列解包）
- 具有推导式（列表推导）
- 具有适当的条件判断（[总结](http://forgunsmatter.pythonanywhere.com/page_13_total_thing.html)页面的右上角跳转判断是用条件判断写的
- python与html交互良好
- 封装较多函数，函数和模块根据功能或者相关事情有意义命名
- 功能具有可扩展性和丰富性（可以跳转页面，可以实现下拉框提交跳转，大多图表内部具有交互插件）
- python与html交互良好
- 符合jinja2标准
- 已上传pythonanywhere部署
#### 加分项
- 面向对象编程，函数内使用了列解包，将每个枪击案件添加到事件特性组




