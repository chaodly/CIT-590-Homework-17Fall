'''
    Name: Zhengchao Ni
    Student ID: 73173892
    Co-worker: Yan Wu
    Student ID: 42973136

    In this program, we use CamelCase for Name of Classes and Functions,
    and we use underscores('_') for variables or parameters,
    so we can discriminate these two kinds.
'''



import re

class TxtResumeReader():

  def __init__(self, content):
    self.content = content  #contents read from the .txt file
    self.name = ''          #initialize name
    self.email = ''         #initialize email
    self.projects = []      #initialize projects as an empty list
    self.courses = []       #initialize courses as an empty list
    self.degrees = []       #initialize degrees as an empty list
    
  def detectingName(self):
    '''
        Simply detects the first line, if the first letter of the first line
        is a capital letter, then store it as the name
    '''
    if ord(self.content[0].lstrip()[0]) < 65 or ord(self.content[0].lstrip()[0]) > 90:
      raise NameError ('The first line has to be just the name with proper capitalization!')
    self.name = self.content[0]
    
  def detectingEmail(self):
    '''
        find lines contain information about emails and see if they meet the standard.
    '''
    for line_index in range(len(self.content)):
      string = self.content[line_index].rstrip()   #set another string so we can operate easier
      if '@' in string:
        if string.endswith('.com') or string.endswith('.edu'):
          string = re.sub(r'.*@','',string)
          string = string.rstrip('.com')
          string = string.rstrip('.edu')
          #these three lines delete characters before '@'(include) and the '.edu' of '.com'
          #if some thing left and the first character of it is a lower letter
          #then we decide it as legal email
          if string != '':
            if (ord(string[0]) >= 97 and ord(string[0]) <= 122) :
              self.email += self.content[line_index]
    
    
  def detectingCourses(self):
    '''
        find a line or lines contain 'Courses', extract useful information
        and delete irrelevant ones, such as symbols come before the actual
        courses.
    '''
    for line_index in self.content:
      if 'Courses' in line_index:
        string = line_index                #set a new string so we can operate better
        string = string.lstrip('Courses')  #delete white spaces on the left side
        index = 0                          #initialize a index number, helps delete irrelevant symbols
        for i in range(len(string)):
          if (ord(string[i]) >= 65 and ord(string[i]) <= 90) \
             or (ord(string[i]) >= 97 and ord(string[i]) <= 122):
            index = i      #after we found all the irrelevant symbols, record the position into index
            break
        string = string.lstrip(string[:index])  #delete those symbols
        self.courses = string.strip().split(',') #split different courses into a list
        break


  def detectingDegrees(self):
    '''
        To comfirm degrees information, we need to locate lines that contains
        'University' first, then look up for the three different degrees,
        only lines contains these two aspects can be decided as legal degree informationl.
    '''
    for line_index in range(len(self.content)): 
      if 'University' in self.content[line_index]:
        if ('Bachelor' in self.content[line_index]) or ('Master' in self.content[line_index]) \
           or ('Doctor' in self.content[line_index]):
          self.degrees += [self.content[line_index]]    #might be more than one degree
    
  def detectingProjects(self):
    '''
        Not only detects about projects, but also detects the last line of the project,
        which is '----------'
    '''
    for line_index in range(len(self.content)): 
      for i in range(len(self.content[line_index])):
        if self.content[line_index][i:i + 8] == 'Projects':  #to see if the line contains 'Projects'
          line_index += 1
          while self.content[line_index][i:i + 10] != '----------':
            #record every line after 'Projects' but before the stop sign
            self.projects.append(self.content[line_index])
            line_index += 1

class TxtResumeWriter():

  def __init__(self, output_file):
    self.output_file = output_file
    #only need one parameter for the object this time

  def writeFirstLine(self,output_file):
    '''
        we want to write this line right after '<body>'
    '''
    self.output_file = output_file
    f=open(self.output_file,'r+')   #'r+' is for open a file with both write and read
    string = ''  #set a string to put f.readline() in 
    while '<body>' not in string:
      string = f.readline()
    #above three lines are for detecting the position of '<body>'
    f.seek(0,1)    #means set the footage right after where f.readline() were at
    f.writelines('<div id="page-wrap">\n') #so we can write right after the '<body>' line
    f.close()

  def writeBasicInformation(self, output_file, name, email):
    '''
        this function will use surround_block() to construct
        html block codes, and then write the block into the file
    '''
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.name = name    #extract name
    self.email = email  #and email
    block1 = surround_block('h1',self.name)
    block2 = surround_block('p',self.email)
    block = surround_block('div',block1+block2)  #construct an html block code
    string = ''
    while '<div id="page-wrap">' not in string:
      string = f.readline()     #find the position of where we want to put the content
    f.seek(0,1)
    f.writelines(block)
    f.close()                 #same as the above function

  def writeAboutDegrees(self, output_file, degrees):
    '''
        this function is pretty much the same as writeBasicInformation()
    '''
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.degrees = degrees
    string,block = '',''    #initialize string and block to put values in
    block1 = surround_block('h2','Education\n')  
    for i in range(len(self.degrees)):
      block += surround_block('li',self.degrees[i])
    block = surround_block('ul',block)
    block = surround_block('div',block1+block)    #consctruct html block code
    while '</div>' not in string:
      string = f.readline()     #find the position of the first '</div>'
    f.seek(0,1)
    f.writelines(block)         #then write the block in
    f.close()
    
    
  def writeAboutProjects(self, output_file, projects):
    '''
        this function is slightly different from the above one,
        we need an additional header_num value to count the number
        of '</div>',because we need to make sure we want to write
        new contents after the last '</div>'
    '''
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.projects = projects
    string, block = '', ''      #initialize string and block to put values in
    header_num = 0
    block1 = surround_block('h2','Projects\n')
    for i in range(len(self.projects)):
      block += surround_block('li', surround_block('p',self.projects[i]))
    block = surround_block('ul', block)
    block = surround_block('div',block1+block)         #construct html block codes
    while ('</div>' not in string) or (header_num !=2):   # to see whether we find the second '</div>'
      string = f.readline()
      if '</div>' in string:
        header_num += 1          #find one, add 'one'
    f.seek(0,1)
    f.writelines(block)          #write next to the second '</div>' line   
    f.close()
    
    
  def writeAboutCourses(self, output_file, courses):
    '''
        pretty much the same as writeAboutProjects
    '''
    self.output_file = output_file
    f=open(self.output_file,'r+')
    self.courses = courses
    string, block = '', ''     #initialize string and block to put usefu value in
    header_num = 0
    block1 = surround_block('h3','Courses\n')
    for i in self.courses:
      block += i+','
    block = block.rstrip(',')
    block = surround_block('span',block.lstrip()+'\n')
    block = surround_block('div', block1 + block)        #construct html block codes
    while ('</div>' not in string) or (header_num !=3):  #this time, search for the third '</div>'
      string = f.readline()
      if '</div>' in string:
        header_num += 1
    f.seek(0,1)
    f.writelines(block)
    f.close()
    
    
  def writeCloseTags(self, output_file):
    '''
        normally we can just write the contents at the end of the file,
        but we need to make sure a perfect resume is all finished, with
        name, email, degrees, projects and courses information inside, then
        we can safely write close tags
    '''
    self.output_file = output_file
    f=open(self.output_file,'r+')
    string = ''   #initialize string to put value in
    header_num = 0
    lines = '</div>\n</body>\n</html>'   #these are the close tags
    while ('</div>' not in string) or (header_num !=4):   #to see if we have the fourth '</div>'
      string = f.readline()
      if '</div>' in string:
        header_num += 1
    f.seek(0,1)
    f.writelines(lines)
    f.close()
    
def surround_block(tag, text):
    '''
        don't need to add '<' and '>' into the parameter
    '''
    block = '<' + tag + '>\n' + text + '</' + tag + '>\n'
    return block
  
def main():
    input_file = 'C:\\Users\\nizhe\\Desktop\\2017Fall\\CIT-590\\HW\\HW5\\HW5_73173892\\resume.txt'
    with open(input_file) as stream: 
      content = stream.readlines()
    txtResume = TxtResumeReader(content)
    txtResume.detectingName()
    txtResume.detectingEmail()
    txtResume.detectingCourses()
    txtResume.detectingDegrees()
    txtResume.detectingProjects()
    #above are reading and detecting
    #below are writing 
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
    

