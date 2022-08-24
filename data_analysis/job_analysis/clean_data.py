from data_analysis.job_analysis.import_data import get_job_data

job_data = get_job_data()


def get_focused_info(data, column_name, key_word):
    # column_name中含有“key_word”关键字
    cond = data[column_name].str.contains(key_word)
    data = data[cond]
    # print(data.head())
    return data


def convert_salary_info(data):
    # 处理过程
    # 1、将salary中的字符串均小写化（因为存在8k-16k和8K-16K）
    # 2、运用正则表达式提取出薪资区间
    # 3、将提取出来的数字转化为int型
    # 4、取区间的平均值
    data.loc[:, "salary"] = data.loc[:, "salary"].str.lower() \
        .str.extract(r'(\d+)[k]-(\d+)k') \
        .applymap(lambda x: int(x)) \
        .mean(axis=1)
    # print(data.head())
    print(data.salary)


def is_key_in_column(data, column_name):
    # 判断某列是否包含下方关键字，并将信息插入到最后列
    data.loc[:, column_name] = data.loc[:, column_name].str.lower().fillna("")  # 将字符串小写化，并将缺失值赋值为空字符串

    data["Python"] = data[column_name].map(lambda x: 1 if ('python' in x) else 0)
    data["SQL"] = data[column_name].map(lambda x: 1 if ('sql' in x) or ('hive' in x) else 0)
    data["Tableau"] = data[column_name].map(lambda x: 1 if 'tableau' in x else 0)
    data["Excel"] = data[column_name].map(lambda x: 1 if 'excel' in x else 0)
    data['SPSS/SAS'] = data[column_name].map(lambda x: 1 if ('spss' in x) or ('sas' in x) else 0)
    # print(data.head())


def clean_industry(industry):
    industry = industry.split(",")  # 拆分
    if industry[0] == "移动互联网" and len(industry) > 1:
        return industry[1]
    else:
        return industry[0]


def convert_column_info(data, func):
    data.loc[:, "industryField"] = data.industryField.map(func)
    print(data.head())


def clean_data(data=job_data):
    cleaned_data = get_focused_info(data, column_name="positionName", key_word="数据分析")
    convert_salary_info(cleaned_data)
    is_key_in_column(cleaned_data, column_name="job_detail")
    convert_column_info(cleaned_data, func=clean_industry)
    return cleaned_data


if __name__ == '__main__':
    clean_data()
