from makeWebsite import *
import unittest
import re

class Test_makeWebsite(unittest.TestCase):

    def test_detectingName(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingName()
        
        self.assertEqual(txtResume.name.rstrip(), 'Yan Wu')

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingName()
        
        self.assertEqual(txtResume.name.rstrip(), 'Zhengchao ni')
        
    def test_detectingEmail(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingEmail()
        
        self.assertEqual(txtResume.email.rstrip(), 'wuyan33@seas.upenn.edu')
        
        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingEmail()
        
        self.assertEqual(txtResume.email.rstrip(), 'nizc0616@seas.upenn.edu\nnizhengchao@hotmail.com')
        
    def test_detectingCourses(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingCourses()

        self.assertEqual(txtResume.courses,['CIT590', ' ESE-504', 'Introduction to Optmization Theory', ' Computer Network'])

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingCourses()
        self.assertEqual(txtResume.courses,['ESE500', ' ESE-504', 'Digtial Signal Processing'])
        
    def test_detectingDegrees(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingDegrees()
        self.assertEqual(txtResume.degrees, ['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Electrical Engineering\n', 'Peking University, Beijing, China  -  Bachelor of Science in Electrical Engineering \n', 'New Oriental Cooking University, Beijing,China  -  Doctor of Bake in Cooking Science\n'])

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingDegrees()
        self.assertEqual(txtResume.degrees, ['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in ESE\n'])

    def test_detectingProjects(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingProjects()
        
        self.assertEqual(txtResume.projects, ["Software Engineer, Seattle, USA - Designed game called 'the witcher 3', leader of the UI design team. \n", 'Remote Sensing Image Processing -  Analyzed images captured by satellites and designed algorithms to detect contents of roads and buidings.\n'])
        
        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(input_file, content)
        txtResume.detectingProjects()
        
        self.assertEqual(txtResume.projects, ['Analysis and Problem Solving - Researched and developed a survey instrument, subsequently used to obtain information\n', 'from customers regarding their satisfaction with products purchased.\n', '\n']) 
        
    def test_surround_block(self):
        self.assertEqual(surround_block('head', 'Resume'), '<head>\nResume</head>\n')
        self.assertEqual(surround_block('html', 'education'), '<html>\neducation</html>\n')
        

unittest.main()
    
