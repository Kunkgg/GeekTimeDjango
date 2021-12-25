import csv
import random
import faker
from faker.providers import BaseProvider


class CandidateProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(faker.Faker('zh-CN'))

    def username(self) -> str:
        return self.generator.name()

    def phone(self) -> str:
        return self.generator.phone_number()

    def bachelor_school(self) -> str:
        school_suffixes = ['大学', '学院']
        return self.generator.word() + self.generator.random_element(school_suffixes)

    def major(self) -> str:
        return self.generator.job() + '专业'

    def degree(self) -> str:
        degree_type = ('本科', '硕士', '博士')
        return self.generator.random_element(degree_type)
        
    def test_score_of_general_ability(self):
        return self.randomize_nb_elements(number=60, min=40, max=90)

    def paper_score(self):
        return self.randomize_nb_elements(number=60, min=40, max=90)


def write_csv(fn, rows, header=None):
    with open(fn, mode='w', newline='') as fp:
        writer = csv.writer(fp)
        if header:
            writer.writerow(header)
        fp.writelines(rows)


def read_csv(fn, has_header=False):
    rows = []
    line_no = 0
    with open(fn, mode='r', newline='') as fp:
        reader = csv.reader(fp)
        for row in reader:
            if line_no == 0:
                header = row
            else:
                rows.append(row)
            line_no += 1
    return {
            'header': header,
            'rows': rows,
            }
        

def fake_candidates(fn):
    header = (
        'username',
        'city',
        'phone',
        'bachelor_school',
        'major',
        'degree',
        'test_score_of_general_ability',
        'paper_score',
    )

    data_columns = (
        '{{username}}',
        '{{city}}',
        '{{phone}}',
        '{{bachelor_school}}',
        '{{major}}',
        '{{degree}}',
        '{{test_score_of_general_ability}}',
        '{{paper_score}}',
    )
    faker_cn = faker.Faker('zh-CN')
    faker_cn.add_provider(CandidateProvider)
    # faker.Faker.seed(0)
    rows = faker_cn.csv(data_columns=data_columns)
    write_csv(fn, rows, header)


if __name__ == '__main__':
    fn = 'fake_candidates.csv'
    fake_candidates(fn)
    print(read_csv(fn, has_header=True))

