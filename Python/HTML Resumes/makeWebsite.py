import re

class Resume():

  def __init__(self):
    
    self.name = None 
    self.email = None 
    self.projects = []  
    self.courses = []  
    self.degrees = [] 


class TxtResumeReader():

  def __init__(self, input_file, content):
    self.content = content
    self.Resume = Resume()
   
  def detectingName(self):
    Resume.name = ''
    if ord(self.content[0][0]) < 65 or ord(self.content[0][0]) > 90:
      raise NameError ('The first line has to be just the name with proper capitalization!')
    Resume.name = self.content[0]
    self.name = Resume.name
    
  def detectingEmail(self):
    Resume.email = '' 
    for line_index in range(len(self.content)):
      string = self.content[line_index].rstrip()
      if '@' in string:
        if string.endswith('.com') or string.endswith('.edu'):
          string = re.sub(r'.*@','',string)
          string = string.rstrip('.com')
          string = string.rstrip('.edu')
          if string != '':
            if (ord(string[0]) >= 97 and ord(string[0]) <= 122) :
              Resume.email += self.content[line_index]
    self.email = Resume.email
    
    
  def detectingCourses(self):
    for line_index in self.content:
      if 'Courses' in line_index:
        string = line_index
        string = string.lstrip('Courses')
        index = 0
        for i in range(len(string)):
          if (ord(string[i]) >= 65 and ord(string[i]) <= 90) \
             or (ord(string[i]) >= 97 and ord(string[i]) <= 122):
            index = i
            break
        string = string.lstrip(string[:index])
        Resume.courses = string.strip().split(',')
        break
    self.courses = Resume.courses

  def detectingDegrees(self):
    Resume.degrees =[]
    for line_index in range(len(self.content)): 
      if 'University' in self.content[line_index]:
        if ('Bachelor' in self.content[line_index]) or ('Master' in self.content[line_index]) \
           or ('Doctor' in self.content[line_index]):
          Resume.degrees += [self.content[line_index]]
    self.degrees = Resume.degrees
    
  def detectingProjects(self):
    Resume.projects = []
    for line_index in range(len(self.content)): 
      for i in range(len(self.content[line_index])):
        if self.content[line_index][i:i + 8] == 'Projects':
          line_index += 1
          while self.content[line_index][i:i + 10] != '----------':
            Resume.projects.append(self.content[line_index])
            line_index += 1
    self.projects = Resume.projects

class TxtResumeWriter():

  def __init__(self, output_file):
    
    self.output_file = output_file

  def writeFirstLine(self,output_file):
    self.output_file = output_file
    f=open(self.output_file,'r+')
    string = ''
    while '<body>' not in string:
      string = f.readline()
    f.seek(0,1)
    f.writelines('<div id="page-wrap">\n')
    f.close()

  def writeBasicInformation(self, output_file, name, email):
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.name = name
    self.email = email
    block1 = surround_block('h1',self.name)
    block2 = surround_block('p',self.email)
    block = surround_block('div',block1+block2)
    string = ''
    while '<div id="page-wrap">' not in string:
      string = f.readline()
    f.seek(0,1)
    f.writelines(block)
    f.close()

  def writeAboutDegrees(self, output_file, degrees):
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.degrees = degrees
    string,block = '',''
    block1 = surround_block('h2','Education\n')
    for i in range(len(self.degrees)):
      block += surround_block('li',self.degrees[i])
    block = surround_block('ul',block)
    block = surround_block('div',block1+block)
    while '</div>' not in string:
      string = f.readline()
    f.seek(0,1)
    f.writelines(block)
    f.close()
    
    
  def writeAboutProjects(self, output_file, projects):
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.projects = projects
    string, block = '', ''
    header_num = 0
    block1 = surround_block('h2','Projects\n')
    for i in range(len(self.projects)):
      block += surround_block('li', surround_block('p',self.projects[i]))
    block = surround_block('ul', block)
    block = surround_block('div',block1+block)
    while ('</div>' not in string) or (header_num !=2):
      string = f.readline()
      if '</div>' in string:
        header_num += 1
    f.seek(0,1)
    f.writelines(block)
    f.close()
    
    
  def writeAboutCourses(self, output_file, courses):
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.courses = courses
    string, block = '', ''
    header_num = 0
    block1 = surround_block('h3','Courses\n')
    for i in self.courses:
      block += i+','
    block = block.rstrip(',')
    block = surround_block('span',block.lstrip()+'\n')
    block = surround_block('div', block1 + block)
    while ('</div>' not in string) or (header_num !=3):
      string = f.readline()
      if '</div>' in string:
        header_num += 1
    f.seek(0,1)
    f.writelines(block)
    f.close()
    
    
  def writeCloseTags(self, output_file):
    self.output_file = output_file
    f=open(self.output_file,'r+')
    string = ''
    header_num = 0
    lines = '</div>\n</body>\n</html>'
    while ('</div>' not in string) or (header_num !=4):
      string = f.readline()
      if '</div>' in string:
        header_num += 1
    f.seek(0,1)
    f.writelines(lines)
    f.close()
    
def surround_block(tag, text):
    block = '<' + tag + '>\n' + text + '</' + tag + '>\n'
    return block
  
def main():
    input_file = 'resumeForTest.txt'
    with open(input_file) as stream: 
      content = stream.readlines()
    txtResume = TxtResumeReader(input_file, content)
    txtResume.detectingName()
    txtResume.detectingEmail()
    txtResume.detectingCourses()
    txtResume.detectingDegrees()
    txtResume.detectingProjects()

    output_file = 'resume.html'
    txtWriter = TxtResumeWriter(output_file)
    txtWriter.writeFirstLine(output_file)
    txtWriter.writeBasicInformation(output_file, txtResume.name, txtResume.email)
    txtWriter.writeAboutDegrees(output_file, txtResume.degrees)
    txtWriter.writeAboutProjects(output_file, txtResume.projects)
    txtWriter.writeAboutCourses(output_file, txtResume.courses)
    txtWriter.writeCloseTags(output_file)

if __name__ == '__main__':
    main()
    

