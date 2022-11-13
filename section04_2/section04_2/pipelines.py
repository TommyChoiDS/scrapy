# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv
import xlsxwriter


class Pipeline1:
    # 클래스 초기화 메소드
    def __init__(self):
        # 엑셀 처리 선언
        self.workbook = xlsxwriter.Workbook("../data/result_excel.xlsx")
        # CSV 처리 선언(a, w 옵션 변경)
        self.file_opener = open('../data/result_csv.csv', 'w')
        self.csv_writer = csv.DictWriter(self.file_opener, fieldnames=['rank_num', 'site_name', 'daily_time_site', 'daily_page_view', 'is_pass'])
        # 워크 시트
        self.worksheet = self.workbook.add_worksheet()
        # 삽입 수
        self.rowcount = 1

    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Opened.')

    def process_item(self, item, spider):
        if int(item.get('rank')) < 41:
            return item
        else:
            raise DropItem(f'Dropped Item. Rank is {item.get("rank")}')

    def close_spider(self, spider):
        # 엑셀 파일 닫기
        self.workbook.close()
        # CSV 파일 닫기
        self.file_opener.close()
        spider.logger.info('TestSpider Pipeline Closed.')