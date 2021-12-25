import csv
from django.core.management import BaseCommand
from interview.models import Candidate

# run command to import candidates:
# python manage.py import_candidates --path /path/to/your/file.csv

class Command(BaseCommand):
    help = '从一个CSV文件的内容中读取候选人列表，导入到数据库中'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file-path', type=str, help='CSV 文件路径')
        parser.add_argument('-H', '--has-header', action='store_true', help='CSV 包含 header 行')

    def handle(self, *args, **kwargs):
        start_line = 1 if kwargs['has_header'] else 0
        file_path = kwargs['file_path']
        line_no = 0
        with open(file_path) as fp:
            reader = csv.reader(fp)
            for row in reader:
                if line_no >= start_line:
                    candidate = Candidate.objects.create(
                        username=row[0],
                        city=row[1],
                        phone=row[2],
                        bachelor_school=row[3],
                        major=row[4],
                        degree=row[5],
                        test_score_of_general_ability=float(row[6]),
                        paper_score=float(row[7])
                    )

                    print(candidate)
                line_no += 1
        print(f"Imported {line_no - start_line} rows.")
