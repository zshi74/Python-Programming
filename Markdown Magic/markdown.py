#Name: Zicheng Shi
#Partner: Fei Wang

#function1: Add paragraph tag
def paragraph(line):
    """ Add paragraph tag in each line """
    return "<p>"+line[:-1]+"</p>\n" #we need to use slicing and escape to finish the first function

#function2: Convert header
def header(line):
    """ We consider the header is the title, then according to "#"
        to detect whether it is header or not

    """
    if line[0] == '#' and line[1]== '#': #if there are two ##
        return "<h2>"+line[3:] + "</h2>"
    elif line[0]=='#': #if there is only one #
        return "<h1>"+line[2:]+"</h1>"

#function3: Convert emphasized text
def em(line):
    """ In Markdown, emphasized texts are wrapped with '*' characters.
        In HTML, you will have to convert these to <em> tags.

    """
    char=0
    new_line=line
    for number in range(len(line)): #use for loop to go through every single element
        if line[number] == "*":
          char = char+1
          if char %2 != 0: # if it is the first "*"
              new_line = new_line.replace("*","<em>",1)
          elif char % 2 == 0: # if it is second "*"
              new_line = new_line.replace("*","</em>",1)
    return new_line #return the value

#function4: Convert hyperlink
def link(line):
    ''' convert [text](link) to <a href> tags in HTML.'''
    while '[' in line and '](' in line and ')'in line: #make it starts to loop
        bracket2_paren1 = line.find('](' ) # find '](' together
        bracket1 = line.rfind("[",0,bracket2_paren1) # accroding to the position of '](', go backward
        paren2 = line.find(")",bracket2_paren1) # go forward
        line = line[:bracket1]+'<a href="'+ line[bracket2_paren1+2:paren2]+'">'+line[bracket1+1:bracket2_paren1]+"</a>"+line[paren2+1:] #use slicing to get expected result
    return line

def convert(input_file, output_file):
    """ try to convert the markdown to HTML """
    p10_md = open(input_file, 'r') #try to open the file
    p10_html = open(output_file,'w') # try to write in this file
    for line in p10_md: #try to go through every line
        if line[0] == "#" and line[1] == '#': # if the first character and the second are "#", which means it would be header, we just let python know
            line = header(line)
        elif line[0] == '#':
            line = header(line)
        elif line not in ['\n', '\r\n']: #if the line is not empty, just go through previous function
            line = paragraph(line)
            line = em(line)
            line = link(line)
        p10_html.write(line) # write this function
    p10_md.close() # close markdown
    p10_html.close() # close HTML
