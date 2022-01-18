# -*- coding:utf-8 -*-
from pyecharts.faker import Faker
from pyecharts import options as opts
#from pyecharts.globals import ThemeType
from pyecharts.charts import Bar3D
import random


data=[(i,j,random.randint(0,12))for i in range(24) for j in range(6)]
bar3d = Bar3D()
bar3d.add(
    "",
    data,
    xaxis3d_opts=opts.Axis3DOpts(Faker.clock,type_="category"),
    yaxis3d_opts=opts.Axis3DOpts(Faker.week_en,type_="category"),
    zaxis3d_opts=opts.Axis3DOpts(type_="value"),
)
bar3d.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=20),
    title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
)
bar3d.render()