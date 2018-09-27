from makeWebsite import *
import unittest
import re

class Test_makeWebsite(unittest.TestCase):

    def setUp(self):
        f=open('resume.html','w')
        lines = '<html>\n<head>\n<title>Resume</title>\n</head>\n<body>\n</body>\n</html>'
        f.writelines(lines)
        f.close()
        f=open('resumeForTest.html','w')
        f.writelines(lines)
        f.close()
        #these lines are for initialize 'resume.html' and 'resumeForTest.html'
        #after initialization, these files will be just like when I created them
        #doing this can be easier for testing
    
    def test_detectingName(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        self.assertEqual(txtResume.name.rstrip(), 'Yan Wu')
        # test whether the name is right in 'resume.html'

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        self.assertEqual(txtResume.name.rstrip(), 'Zhengchao ni')
        # test whether the name is right in the object
        
    def test_detectingEmail(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingEmail()
        self.assertEqual(txtResume.email.rstrip(), 'wuyan33@seas.upenn.edu')
        #first test, with 'resume.txt'
        
        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingEmail()
        self.assertEqual(txtResume.email.rstrip(), 'nizc0616@seas.upenn.edu\nnizhengchao@hotmail.com')
        #second test, with 'resumeForTest.txt'
        
    def test_detectingCourses(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingCourses()
        self.assertEqual(txtResume.courses,['CIT590', ' ESE-504', ' Introduction to Optmization Theory', ' Computer Network'])
        #first test, correctness of courses in in the object

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingCourses()
        self.assertEqual(txtResume.courses,['ESE500', ' ESE-504', 'Digtial Signal Processing'])
        #second test
        
    def test_detectingDegrees(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingDegrees()
        self.assertEqual(txtResume.degrees, ['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Electrical Engineering\n', \
                                             'Peking University, Beijing, China  -  Bachelor of Science in Electrical Engineering \n', \
                                             'New Oriental Cooking University, Beijing,China  -  Doctor of Bake in Cooking Science\n'])
        #first test

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingDegrees()
        self.assertEqual(txtResume.degrees, ['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in ESE\n'])
        #second test

    def test_detectingProjects(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingProjects() 
        self.assertEqual(txtResume.projects, ["Software Engineer, Seattle, USA - Designed game called 'the witcher 3', leader of the UI design team. \n",\
                                              'Remote Sensing Image Processing -  Analyzed images captured by satellites and designed algorithms to detect contents of roads and buidings.\n'])
        #first
        
        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingProjects()
        self.assertEqual(txtResume.projects, ['Analysis and Problem Solving - Researched and developed a survey instrument, subsequently used to obtain information\n',\
                                              'from customers regarding their satisfaction with products purchased.\n', '\n'])
        #second

    def test_writeFirstLine(self):
        '''
            since this test is for the first line, it doesn't require any data,
            so we don't need to create txtResume object
        '''
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-1], '<div id="page-wrap">\n')
        f.close()  #cannot be forgotten to close, otherwise might cause serious problems
        

    def test_writeBasicInformation(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-3], txtResume.email)
        self.assertEqual(lines[-6], txtResume.name)
        self.assertEqual(lines[-1], '</div>\n')
        f.close()
        #first three tests to test correctness, including contents and header

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        output_file = 'resumeForTest.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-4]+lines[-3], txtResume.email)
        self.assertEqual(lines[-7], txtResume.name)
        self.assertEqual(lines[-1], '</div>\n')
        f.close()
        #second three tests to test correctness, including contents and header

    def test_writeAboutDegrees(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        txtResume.detectingDegrees()
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-10], txtResume.degrees[0])
        self.assertEqual(lines[-4], txtResume.degrees[2])
        self.assertEqual(lines[-2], '</ul>\n')
        f.close()
        #first three tests to test correctness, including contents and header

        input_file = 'resumeForTest.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        txtResume.detectingDegrees()
        output_file = 'resumeForTest.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-4], txtResume.degrees[0])
        self.assertEqual(lines[-3], '</li>\n')
        f.close()
        #second three tests to test correctness, including contents and header


    def test_writeAboutProjects(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        txtResume.detectingDegrees()
        txtResume.detectingProjects()
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
        txtWriter.writeAboutProjects(output_file, txtResume.projects)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-10], txtResume.projects[0])
        self.assertEqual(lines[-5], txtResume.projects[1])
        self.assertEqual(lines[-4], '</p>\n')
        f.close()
        #first three tests to test correctness, including contents and header

        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        txtResume.detectingDegrees()
        txtResume.detectingProjects()
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
        txtWriter.writeAboutProjects(output_file, txtResume.projects)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-10], txtResume.projects[0])
        self.assertEqual(lines[-5], txtResume.projects[1])
        self.assertEqual(lines[-2], '</ul>\n')
        f.close()
        #second three tests to test correctness, including contents and header

    def test_writeAboutCourses(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        txtResume.detectingDegrees()
        txtResume.detectingProjects()
        txtResume.detectingCourses()
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
        txtWriter.writeAboutProjects(output_file, txtResume.projects)
        txtWriter.writeAboutCourses(output_file,txtResume.courses)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-6].rstrip(), 'Courses')
        self.assertTrue(lines[-3].startswith('CIT590'))
        self.assertEqual(lines[-2], '</span>\n')
        f.close()
        #three tests to test correctness, including contents and header

    def test_writeCloseTags(self):
        input_file = 'resume.txt'
        with open(input_file) as stream:
            content = stream.readlines()
        txtResume = TxtResumeReader(content)
        txtResume.detectingName()
        txtResume.detectingEmail()
        txtResume.detectingDegrees()
        txtResume.detectingProjects()
        txtResume.detectingCourses()
        output_file = 'resume.html'
        txtWriter = TxtResumeWriter(output_file)
        txtWriter.writeFirstLine(output_file)
        txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
        txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
        txtWriter.writeAboutProjects(output_file, txtResume.projects)
        txtWriter.writeAboutCourses(output_file,txtResume.courses)
        txtWriter.writeCloseTags(output_file)
        f = open(output_file,'r')
        lines = f.readlines()
        self.assertEqual(lines[-3].rstrip(), '</div>')
        self.assertTrue(lines[-2].rstrip(), '</body>')
        self.assertEqual(lines[-1].rstrip(), '</html>')
        f.close()
        # test for three headers

    def test_surround_block(self):
        self.assertEqual(surround_block('head', 'Resume'), '<head>\nResume</head>\n')
        self.assertEqual(surround_block('html', 'education'), '<html>\neducation</html>\n')
        #test for the correctness of surround_block()
    
unittest.main()
    
