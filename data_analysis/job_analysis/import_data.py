import pandas as pd

class ProcessFileData(object):
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def get_data_by_list(self, lis):
        return self.data[lis]

    def drop_duplicates(self, data):
        return data.drop_duplicates()


def get_job_data():
    procee = ProcessFileData(r"./job.csv")
    column_list = ["positionName", "companyShortName", "city", "companySize", "education", "financeStage",
                   "industryField", "salary", "workYear", "companyLabelList", "job_detail"]
    job = procee.data[column_list]
    # print(job.shape, job['city'].unique())  # 按列查看信息并去重
    job = procee.drop_duplicates(job)
    # print(job.head())
    return job


if __name__ == '__main__':
    get_job_data()
