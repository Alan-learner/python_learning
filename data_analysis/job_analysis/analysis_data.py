import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager

from common_func.io_relate import get_timed_file_path
from data_analysis.job_analysis.import_data import PROJECT_PATH

from data_analysis.job_analysis.clean_data import clean_data

job = clean_data()
output_path = r"D:\Files\Output\jpg_files"
# 查看电脑自带的字体
fm = FontManager()
font_list = [font.name for font in fm.ttflist]
# 设置字体
plt.rcParams['font.family'] = 'STKaiti'
plt.rcParams['font.size'] = 40
plt.figure(figsize=(20, 15))


def save_bar_fig(data=None, title=None, file_name=None):
    # cities = job['city'].value_counts()  # 统计各城市工作数量，返回series[(北京，100)，(成都，60)],已排序
    plt.figure(figsize=(20, 15))
    plt.barh(y=data.index[::-1],  # 纵坐标的名称
             width=data.values[::-1],  # 对应名称的数值
             color='#3c7f99')  # light_blue

    plt.box(False)  # 不显示边框
    plt.title(label=title,
              fontsize=32, weight='bold', color='white',
              backgroundcolor='#c5b783', pad=30)

    plt.tick_params(labelsize=16)
    plt.grid(axis='x', linewidth=0.5, color='#3c7f99')
    fig_path = get_timed_file_path(output_path, file_name)
    plt.savefig(fig_path)


def get_city_field_fig():
    city_data = job['city'].value_counts()
    save_bar_fig(data=city_data,
                 title='           各城市数据分析岗位的需求量           ',
                 file_name="job_demand_of_cities.jpg")
    industry_data = job['industryField'].value_counts()
    save_bar_fig(data=industry_data,
                 title='           细分领域数据分析岗位的需求量（取前十           ',
                 file_name="job_demand_of_industries.jpg")


def main():
    get_city_field_fig()


if __name__ == '__main__':
    main()
