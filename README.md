# python_final_project
### 一、相关链接
- [github_url](https://github.com/yebail-ss/python_final_project)
- [pythonanywhere_url](http://forgunsmatter.pythonanywhere.com/)
#### 二、链接个数
- **共二十个url**
- [详情](https://github.com/yebail-ss/python_final_project/tree/master/templates)
- 其中封面的url有两个，分别是"/"和"/page_cover.html"

#### 三、基本交互功能html5控件使用丰富性
- [li标签与a标签结合写导航栏](http://forgunsmatter.pythonanywhere.com/page_03_details.html)
- [下拉框切换到对应的地图和表格](http://forgunsmatter.pythonanywhere.com/page_03_details.html)
- [利用下拉框跳转到想要的页面](http://forgunsmatter.pythonanywhere.com/page_13_total_thing.html)
#### 四、github文档格式
- 包含基本的templates，static，story.py以及三个csv数据文档
- 由于传输数据需要将map_details.html与py文件放于同一层级
#### 五、html档描述
- 文档里都写有导航栏（div,ul,li组件与a标签组合实现此功能）和翻页按钮（button组件与a标签组合实现此功能）
```
<div class="top">
        <ul>
            <li id="ml-0" class="menu-li">
                <a href="page_cover.html" data-menu-top="0"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">MASS KILLINGS</></font></a>
            </li>
            <li><a href="page_01_Number_of_guns.html"><b>枪支数量</b></a></li>
            <li><a href="page_02_shooting.html"><b>案件地点</b></a></li>
            <li><a href="page_04_Injured_person.html"><b>频率</b></a></li>
            <li><a href="page_07_Suspects.html"><b>枪手</b></a></li>
            <li><a href="page_10_Who_was_attacked.html"><b>易受攻击地点</b></a></li>
            <li><a href="page_08_frequent_words.html"><b>易受攻击人群</b></a></li>
            <li><a href="page_13_total_thing.html"><b>总结</b></a></li>
        </ul>
</div>

```
- html利用jinja2语法写有{{}}进行图表和数据传输
```
        {{ the_res|safe }}
```
- 通过img与jinja2语法结合传递图片
```
 <img src="{{ url_for("static", filename="img/attack.png") }}">
```
#### 六、Python档描述
- 导入了需要用到的模块(import)
- 对数据进行导入和处理
```
df = pd.read_csv('Mass_nd.csv', encoding='ISO-8859-1', sep=',' )
```
- 利用@app.route写路径,通过return render_template进行html传输
```
@app.route('/')
def base_cover():
    return render_template('page_cover.html')
```
- 数据筛选，可视化函数与form提交表单功能结合实现下拉框地图与表格切换
```
regions_available_loaded = list(df.code.dropna().unique())
```
- 利用request和条件判断结合实现页面切换效果
```
the_region_selected = request.form["the_region_selected"]
    if the_region_selected == "the_description":
        return render_template('page_00_the_description.html')
    elif the_region_selected == "Number_of_guns":
        return render_template('page_01_Number_of_guns.html')
    elif the_region_selected == "shooting":
        return render_template("page_02_shooting.html")
    elif the_region_selected == "Injured_person":
        return render_template("page_04_Injured_person.html")
    elif the_region_selected == "Las_Vegas_shootings":
        cdata1 = pd.read_csv('Mass.csv', encoding='ISO-8859-1', sep=',')
        people = cdata1.sort_values(by="total", ascending=False)
        data_str = people.to_html()
        return render_template("page_05_Las_Vegas_shootings.html",
                               the_res=data_str
                               )
    elif the_region_selected =="Number_of_shootings":
        return render_template("page_06_Number_of_shootings.html")
    elif the_region_selected== "Suspects":
        return render_template("page_07_Suspects.html")
    elif the_region_selected=="frequent_words":
        return render_template("page_08_frequent_words.html" )
    elif the_region_selected =="Who_was_attacked":
        return render_template("page_10_Who_was_attacked.html" )
    elif the_region_selected == "the_top_20_states":
        return render_template("page_11_the_top_20_states.html")
    elif the_region_selected == "where":
        return render_template("page_12_where.html")


```
#### 七、web app描述
- [导航栏切换](http://forgunsmatter.pythonanywhere.com/page_00_the_description.html)
- [下拉框切换到对应的地图和表格](http://forgunsmatter.pythonanywhere.com/page_03_details.html)
- [可以点击地图下切换到大地图](http://forgunsmatter.pythonanywhere.com/page_02_shooting.html)
- [利用下拉框跳转到想要的页面](http://forgunsmatter.pythonanywhere.com/page_13_total_thing.html)
#### 八、包含得分点
- 具有较复杂的结构嵌套（函数内含数列解包）
```
@app.route("/map_01_details.html")
def map_01_details():
    incidents = folium.map.FeatureGroup()
    # 将每个枪击案件添加到事件特性组
    for lat, lng, in zip(cdata1.latitude, data.longitude):
        incidents.add_child(
            folium.CircleMarker(
                [lat, lng],
                radius=7,  # define how big you want the circle markers to be
                color='yellow',
                fill=True,
                fill_color='red',
                fill_opacity=0.4
            )
        )
    # Add incidents to map
    san_map = folium.Map(location=[latitude, longitude], zoom_start=4)
    incidents_map = san_map.add_child(incidents)
    display(incidents_map)
    incidents_map.save('templates/map_01_details.html')
    return render_template("map_01_details.html")


```
- 具有推导式（列表推导）
```
regions_availables = ["the_description", "Number_of_guns", "shooting",
                       "Injured_person", "Las_Vegas_shootings",
                      "Number_of_shootings", "Suspects", "frequent_words",
                       "Who_was_attacked",
                      "the_top_20_states",
                      "where"]
regions_availables_=[i for i in regions_availables]
```
- 具有适当的条件判断 
```
the_region_selected = request.form["the_region_selected"]
    if the_region_selected == "the_description":
        return render_template('page_00_the_description.html')
    elif the_region_selected == "Number_of_guns":
        return render_template('page_01_Number_of_guns.html')
    elif the_region_selected == "shooting":
        return render_template("page_02_shooting.html")
    elif the_region_selected == "Injured_person":
        return render_template("page_04_Injured_person.html")
    elif the_region_selected == "Las_Vegas_shootings":
        cdata1 = pd.read_csv('Mass.csv', encoding='ISO-8859-1', sep=',')
        people = cdata1.sort_values(by="total", ascending=False)
        data_str = people.to_html()
        return render_template("page_05_Las_Vegas_shootings.html",
                               the_res=data_str
                               )
    elif the_region_selected =="Number_of_shootings":
        return render_template("page_06_Number_of_shootings.html")
    elif the_region_selected== "Suspects":
        return render_template("page_07_Suspects.html")
    elif the_region_selected=="frequent_words":
        return render_template("page_08_frequent_words.html" )
    elif the_region_selected =="Who_was_attacked":
        return render_template("page_10_Who_was_attacked.html" )
    elif the_region_selected == "the_top_20_states":
        return render_template("page_11_the_top_20_states.html")
    elif the_region_selected == "where":
        return render_template("page_12_where.html")


```
- 对函数进行封装，同时结合jinja2语法进行可视化图表传递
```
     {{bar|safe}}
```
```
@app.route('/page_01_Number_of_guns.html')
def bar():
    return render_template('page_01_Number_of_guns.html', bar=overlap_line_scatter())
def overlap_line_scatter() -> Bar:
    x =  ["1996", "2000", "2009"]
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("美国人口", ['243000000','259000000','310000000'])
        .set_global_opts(title_opts=opts.TitleOpts(title="美国私人拥枪的数据对比"))
    )
    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis("美国拥枪人数", ['263000000','282000000','307000000'])
    )
    bar.overlap(line)
    return Markup(bar.render_embed())

```
- 符合jinja2标准
```
 <img src="{{ url_for("static", filename="img/attack.png") }}">
 ```
 ```
    {{ the_res|safe }}

 ```
 ```
  <img src="{{ url_for("static", filename="img/injured.jpg") }}">
 ```
- 含有数据交互
```
@app.route('/map_details', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    dfs = df.query("code=='{}'".format(the_region))
    data_str = dfs.to_html()
    fig = go.Figure(data=go.Choropleth(
        locations=dfs['code'],  # Spatial coordinates
        z=dfs['total'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Millions USD",
    ))
    fig.update_layout(
        title_text='美国大型枪击事件',
        geo_scope='usa',  # limite map scope to USA
    )
    fig.show()
    py.offline.plot(fig, filename="map_details.html", auto_open=False)
    with open("map_details.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    regions_available = regions_available_loaded
    return render_template('page_03_1_details_.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           )
```

