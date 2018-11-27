import re
#word_patterns
word_patterns = [('\*\*(.)*\*\*','\*\*','<strong>','</strong>'),('\`\`(.)*\`\`','\`\`','<code>','</code>'),('_(.)*_','_','<em>','</em>')]
line_patterns = [('^###','<h3>','</h3>'),('^##','<h2>','</h2>'),('^#','<h1>','</h1>'),('^---$','<\ hr>','')]
(ul_pattern,usub_s,usub_e)=('^[*] ','<li>','</li>')
(ol_pattern,osub_s,osub_e)=('^[0-9]+.','<li>','</li>')
##prende in argomento il nome del file
def replace_word(word):
    for (pattern,start_pattern,first_replacement,end_replacement) in word_patterns:
        if re.search(pattern,word):
            word = re.sub(start_pattern,end_replacement,re.sub(start_pattern,first_replacement,word,1),1)
    return word

def replace_lines(line):
    for (pattern,first_repl,last_repl) in line_patterns:
        if re.search(pattern,line):
            return re.sub(pattern,first_repl,line)+last_repl
    if not(re.search(ul_pattern,line)) and not(re.search(ol_pattern,line)) and not (re.match('^$',line)):
        return '<p> '+line+' </ p>'
    return line
def replace_lists(lines):
    result=[]
    ol=False
    ul=False
    for line in lines:
        if not(re.search(ul_pattern,line)) and ul==True:
            ul=False
            result=result+["</ ul>"]
        if not(re.search(ol_pattern,line)) and ol==True:
            ol=False
            result=result+["</ ol>"]
        if re.search(ul_pattern,line) and ul==False:
            result=result+["<ul>"]+['\t'+re.sub(ul_pattern,usub_s,line)+usub_e]
            ul=True
        else:
            if re.search(ul_pattern,line) and ul==True:
                result=result+['\t'+re.sub(ul_pattern,usub_s,line)+usub_e]

        if re.search(ol_pattern,line) and ol==False:
            result=result+["<ol>"]+['\t'+re.sub(ol_pattern,osub_s,line)+osub_e]
            ol=True
        else:
            if re.search(ol_pattern,line) and ol==True:
                result=result+['\t'+re.sub(ol_pattern,osub_s,line)+osub_e]

        if not(re.search(ul_pattern,line)) and not(re.search(ol_pattern,line)) and ul==False and ol==False:
            result=result+[line]
    return result

def format_lines(lines):
    return replace_lists([replace_lines(replace_word(word)) for word in lines.split('\n')])


def translate(fileName):
    with open(fileName) as fileOpened:
        text = fileOpened.read()
        return '<html> \n'+'\n'.join(format_lines(text))+'\n</html>'
