basic_fieldsets = [ 
    ('基础信息', {
        'description': '面试人员基本信息',
        'fields': (
            "userid",
            ("username",  "city", "phone"),
            ("gender", "born_address"),
            ("apply_position", "email"),
            "candidate_remark",
        )
    }),
    ('学校与学历信息', {
        'fields': (
            "bachelor_school",
            "master_school",
            "doctor_school",
            "major",
            "degree",
        )
    }),
    ('综合能力测评成绩，笔试测评成绩', {
        'fields': (
            "test_score_of_general_ability",
            "paper_score",
        )
    })
]

_first_interviewer_fieldsets = [
    ('第一轮面试记录', {
        'fields': (
            "first_score",
            "first_learning_ability",
            "first_professional_competency",
            "first_advantage",
            "first_disadvantage",
            "first_result",
            "first_recommend_position",
            "first_interviewer_user",
            "first_remark",
        )
    }),
]

_second_interviewer_fieldsets = [
    ('第二轮面试记录', {
        'classes': ('extrapretty',),
        'fields': (
            "second_score",
            "second_learning_ability",
            "second_professional_competency",
            "second_pursue_of_excellence",
            "second_communication_ability",
            "second_pressure_score",
            "second_advantage",
            "second_disadvantage",
            "second_result",
            "second_recommend_position",
            "second_interviewer_user",
            "second_remark",
        )
    })
]

_hr_interviewer_fieldsets = [
    ('HR终面', {
        'classes': ('collapse', 'extrapretty'),
        'fields': (
            "hr_score",
            "hr_responsibility",
            "hr_communication_ability",
            "hr_logic_ability",
            "hr_potential",
            "hr_stability",
            "hr_advantage",
            "hr_disadvantage",
            "hr_result",
            "hr_interviewer_user",
            "hr_remark",
        )
    })
]

first_interviewer_fieldsets = basic_fieldsets + _first_interviewer_fieldsets
second_interviewer_fieldsets = first_interviewer_fieldsets + _second_interviewer_fieldsets
hr_interviewer_fieldsets = second_interviewer_fieldsets + _hr_interviewer_fieldsets