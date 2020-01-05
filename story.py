##导入需要用到的库
from folium import folium
from ipywidgets import Tab
import cufflinks as cf
from pyecharts.charts import Tab, Line
import plotly as py
import plotly.graph_objs as go
from flask import  request
from cufflinks import display
import folium
from flask import Flask, render_template
from jinja2 import Markup
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd
from folium import plugins

##数据准备
# 经纬度设置
from pygments.formatters import img
latitude = 37.77
longitude = -93
# 将“美国大规模射击”全部读入，读取“美国大规模射击”数据集；完整数据应为398条。已提前清理缺失数据
cdata1 = pd.read_csv('Mass.csv', encoding='ISO-8859-1', sep=',' )
data = cdata1
cdata1 = pd.read_csv('Mass.csv', encoding = "ISO-8859-1", parse_dates=["Date"])


dff = pd.read_csv('own.csv')
dd= dff[['Country','Average']]
dd1=dd.sort_values('Average',ascending=False)
dd2=dd1.head(21)
killer=data.x
d1=pd.value_counts(killer)

# 读取“枪支暴力”数据集
df = pd.read_csv('guns.csv', encoding='ISO-8859-1', sep=',' )
df.head()
dd= dff[['Country','Average']]
dd1=dd.sort_values('Average',ascending=False)
dd2=dd1.head(21)
dd3 =list(dd2.values)
df.isnull().sum()

# 准备工作
# pandas 大法读内容, 用dropna()丢缺失值, 用unique()取唯一值, 不重覆
dfs = pd.read_csv('Mass_nd.csv', encoding='ISO-8859-1', sep=',')
regions_available_loaded = list(dfs.code.dropna().unique())

# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

data2 = cdata1.Race


# 统计
gender=cdata1.Gender
gender2=gender.value_counts()

# 取出、清洗求和后的数据
gender3 =list(gender2.values)




#时间格式的转换
df_year=df.groupby(['date'])['n_killed','n_injured'].agg('sum')
states_df = df['state'].value_counts()
statesdf = pd.DataFrame()
statesdf['state'] = states_df.index
statesdf['counts'] = states_df.values
regions_availables = ["the_description", "Number_of_guns", "shooting",
                       "Injured_person", "Las_Vegas_shootings",
                      "Number_of_shootings", "Suspects", "frequent_words",
                       "Who_was_attacked",
                      "the_top_20_states",
                      "where"]
regions_availables_=[i for i in regions_availables]

app = Flask(__name__)

##描述故事：显示基本信息

@app.route('/')
def base_cover():
    return render_template('page_cover.html')
@app.route('/page_cover.html')
def base_cover_():
    return render_template('page_cover.html')


@app.route('/page_00_the_description.html')
def page_00_the_description():
    return render_template("page_00_the_description.html")


##通过a标签来到这个界面
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

@app.route('/page_02_shooting.html')
def shot():
    return render_template("page_02_shooting.html")

# 准备工作
# pandas 大法读内容, 用dropna()丢缺失值, 用unique()取唯一值, 不重覆
df = pd.read_csv('Mass_nd.csv', encoding='ISO-8859-1', sep=',')
regions_available_loaded = list(df.code.dropna().unique())

# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/page_03_details.html', methods=['GET'])
def hu_run_2019():
    data_str = df.to_html()  # 使用pandas 数据框之方法.to_html() !! 取代原 "Hello"
    # pandas真是数据科学家的好朋友!

    regions_available = regions_available_loaded  # 下拉选单有内容
    return render_template('page_03_details.html',
                           the_res=data_str,  # 表
                           the_select_region=regions_available)


@app.route('/map_details', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)  ## 检查用户输入, 在后台
    dfs = df.query("code=='{}'".format(the_region))  ## 使用df.query()方法. 按用户交互输入the_region过滤
    data_str = dfs.to_html()  # 数据产出dfs, 完成互动过滤

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

    with open("map_details.html", encoding="utf8", mode="r") as f:  # 把"map_details.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    regions_available = regions_available_loaded  # 下拉选单有内容
    return render_template('page_03_details.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           )

@app.route('/page_04_Injured_person.html')
def render():
    # plt.figure(figsize=(8, 6))
    # plt.scatter(np.sort(cdata1['Date']), np.sort(cdata1['total'].values))
    # plt.xlabel('Date', fontsize=12)
    # plt.ylabel('total', fontsize=12)
    # # 记得关闭，不然画出来的图是重复的
    return render_template('page_04_Injured_person.html')

@app.route('/page_05_Las_Vegas_shootings.html')
def Las_Vegas():
    people = cdata1.sort_values(by="total", ascending=False)
    data_str = people.to_html()
    return render_template('page_05_Las_Vegas_shootings.html',
                           the_res=data_str)

@app.route('/page_06_Number_of_shootings.html')
def render2():
    return render_template('page_06_Number_of_shootings.html')

@app.route('/page_07_Suspects.html')
def suspect():
    return  render_template('page_07_Suspects.html',suspects=total())
def total():
    def bar_datazoom_slider_a() -> Bar:
        c = (
            Bar()
                .add_xaxis(["Male", "Unknown", "Female", "Male/Female ", "M"])
                .add_yaxis("人数", [272, 21, 5, 4, 1])
                .set_global_opts(
                title_opts=opts.TitleOpts(title="枪手的性别分布"),
            )
        )
        return c

    def bar_datazoom_slider_b() -> Bar:
        c = (
            Bar()
                .add_xaxis(['White American or European American', 'Black American or African American  ', 'Unknown  ',
                            'Some other race', 'white',
                            'Asian American  ', 'Asian  ',
                            'Native American or Alaska Native',
                            'black',
                            'White', 'Latino', 'Two or more races', 'Asian American/Some other race ',
                            'White American or European American/Some other Race',
                            'Black American or African American/Unknown'])
                .add_yaxis("人数", [122, 76, 42, 20, 12, 11, 5, 3, 3, 2, 2, 2, 1, 1, 1])
                .set_global_opts(
                title_opts=opts.TitleOpts(title="枪手种族"),
            )
        )
        return c

    def bar_datazoom_slider_c() -> Bar:
        c = (
            Bar()
                .add_xaxis(['Unknown', 'Yes', 'No',
                            'Unclear'])
                .add_yaxis("人数", [111, 99, 90, 3])
                .set_global_opts(
                title_opts=opts.TitleOpts(title="枪手的精神状态"),
            )
        )
        return c

    tab = Tab()
    tab.add(bar_datazoom_slider_a(), "枪手的性别分布")
    tab.add(bar_datazoom_slider_b(), "枪手的种族")
    tab.add(bar_datazoom_slider_c(), "枪手的精神状态")
    return Markup(tab.render_embed())

@app.route('/page_08_frequent_words.html')
def word():
    #画图过程
    # stopwords = set(STOPWORDS)
    # wordcloud = WordCloud(background_color='white', stopwords=stopwords, max_words=100,
    #                       max_font_size=40).generate(str(cdata1['Summary']))
    # plt.figure(figsize=(10, 7))
    # plt.imshow(wordcloud)
    # plt.axis('off')
    # plt.show()
    return render_template('page_08_frequent_words.html')

@app.route('/page_09_Gun_violence.html')
def own_1():
    return render_template('page_09_Gun_violence.html',
                           own_1=own_2())
def own_2():
    # 读入数据
    dff = pd.read_csv('own.csv')

    # 提取country和average firearms per 100 people
    # 降序
    dd = dff[['Country', 'Average']]
    dd1 = dd.sort_values('Average', ascending=False)
    dd2 = dd1.head(21)

    # 写成字典
    dd3 = list(dd2.values)

    def pie_scroll_legend() -> Pie:
        c = (
            Pie()
                .add(
                "",
                dd3,

                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="枪支拥有率前二十的国家", subtitle="平均每100人拥有枪支"),
                legend_opts=opts.LegendOpts(
                    type_="scroll", pos_left="80%", orient="vertical"
                ),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return c

    own = pie_scroll_legend()
    return Markup(own.render_embed())

@app.route('/page_10_Who_was_attacked.html')
def who():
    return render_template('page_10_Who_was_attacked.html')
    # po.plot(fig, filename='templates/try.html')  ##把它转化为html文档

@app.route('/page_11_the_top_20_states.html')
def state():
    return render_template('page_11_the_top_20_states.html')

@app.route('/page_12_where.html')
def where():
    return render_template('page_12_where.html')




@app.route("/page_13_total_thing.html")
def previous():
    return render_template("page_13_total_thing.html",the_select_one=regions_availables_)


@app.route('/select',methods=["POST"])
def select():
    the_region_selected = request.form["the_region_selected"]
    if the_region_selected == "the_description":
        return render_template('page_00_the_description.html')
    elif the_region_selected == "Number_of_guns":
        return render_template('page_01_Number_of_guns.html',
                               bar=overlap_line_scatter())
    elif the_region_selected == "shooting":
        return render_template("page_02_shooting.html")
    elif the_region_selected == "Injured_person":
        return render_template("page_04_Injured_person.html")
    elif the_region_selected == "Las_Vegas_shootings":
        people = cdata1.sort_values(by="total", ascending=False)
        data_str = people.to_html()
        return render_template("page_05_Las_Vegas_shootings.html",
                               the_res=data_str
                               )
    elif the_region_selected =="Number_of_shootings":
        return render_template("page_06_Number_of_shootings.html")
    elif the_region_selected== "Suspects":
        return render_template("page_07_Suspects.html",
                               suspects=total()
                               )
    elif the_region_selected=="frequent_words":
        return render_template("page_08_frequent_words.html",
                               )
    elif the_region_selected =="Who_was_attacked":
        return render_template("page_10_Who_was_attacked.html",
                               )
    elif the_region_selected == "the_top_20_states":
        return render_template("page_11_the_top_20_states.html")
    elif the_region_selected == "where":
        return render_template("page_12_where.html")

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

@app.route("/map_02_details.html")
def map_02_details():
    # let's start again with a clean copy of the map of United State
    san_map = folium.Map(location=[latitude, longitude], zoom_start=4)
    # instantiate a mark cluster object for the incidents in the dataframe
    incidents = plugins.MarkerCluster().add_to(san_map)
    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(data.latitude, data.longitude, cdata1.Title):
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(incidents)
    # add incidents to map
    incident_map2 = san_map.add_child(incidents)
    display(incident_map2)
    incident_map2.save('templates/map_02_details.html')
    return render_template("map_02_details.html")


if __name__ == '__main__':
    app.run()
