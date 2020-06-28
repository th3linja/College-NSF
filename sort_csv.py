import csv
import os

states = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
          'Minnesota', 'Mississippi', 'Missouri', 'Montana',
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
          'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina',
          'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

file = 'U.S. NSF Community Colleges.csv'
columns = ['College', 'AwardNumber', 'Title', 'NSFOrganization', 'Program(s)', 'StartDate',
           'LastAmendmentDate',	'PrincipalInvestigator', 'State', 'Organization', 'AwardInstrument',
           'ProgramManager', 'EndDate',	'AwardedAmountToDate', 'Co-PIName(s)', 'PIEmailAddress',
           'OrganizationStreet', 'OrganizationCity',	'OrganizationState', 'OrganizationZip',
           'OrganizationPhone',	'NSFDirectorate', 'ProgramElementCode(s)', 'ProgramReferenceCode(s)',
           'ARRAAmount', 'Abstract']

with open(file, 'w') as csv_file:
    csv_writer = csv.writer(csv_file, lineterminator='\n')
    csv_dwriter = csv.DictWriter(csv_file, columns, lineterminator='\n')
    csv_dwriter.writeheader()
    for state in states:
        print(state)
        state_path = r'E:\College NSF\\' + state
        with open(state_path + '\\' + state + '.txt', 'r') as state_colleges:
            colleges = state_colleges.readlines()
            for college in colleges:
                college = college.rstrip()
                college_file = r'E:\College NSF\\' + state + '\\' + college + '.csv'
                if os.path.exists(college_file):
                    with open(college_file) as c_file:
                        next(c_file)
                        c_reader = csv.reader(c_file)
                        for row in c_reader:
                            csv_writer.writerow([college] + row)

