# -*- coding:utf-8 -*-
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar

# bar = Bar()
# bar.add_xaxis(Faker.choose())
# bar.add_yaxis('商家',Faker.values())
# bar.render()

bar = Bar(
    init_opts=opts.InitOpts(
        theme=ThemeType.VINTAGE,
        width="1280px",
        height="720px"))
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Bar-基本示例",
        subtitle="我是副标题"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)),
    yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)))
bar.add_xaxis(Faker.choose)
bar.add_yaxis("商家",Faker.values())
bar.render()

bar = Bar(
    init_opts=opts.InitOpts(
        theme=ThemeType.WALDEN,
        width="1280px",
        height="720px"))
bar.add_xaxis(Faker.choose())
# bar.add_yaxis("商家A",Faker.values())
# bar.add_yaxis("商家B",Faker.values())
bar.add_yaxis("商家A",Faker.values(),stack='stack1')
bar.add_yaxis("商家B",Faker.values(),stack='stack1')
bar.add_yaxis("商家C",Faker.values(),stack='stack2')
bar.add_yaxis("商家D",Faker.values(),stack='stack2')
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Bar-基本示例",
        subtitle="我是副标题"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max",name="最大值"),
            opts.MarkPointItem(type_="min",name="最小值"),
        ]
    ),
    markline_opts=opts.MarkLineOpts(
        data=[
            opts.MarkLineItem(type_="average",name="平均值"),
        ]
    ),
)
bar.render()