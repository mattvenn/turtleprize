"""
#bugs

conditions where this won't work:

* import line is indented
* done () 
* where loop never ends

"""
import os
import argparse
import re
import pickle

def export():
    prog_lines = []
    #store the original program (minus the top comments)
    orig_lines = []
    tmp_file = 'tmp'
    eps_file = 'tmp.eps'
    png_file = args.file.replace('.py','.png')
    png_file = png_file.replace(' ','')
    details = {}

    try:
        os.remove(tmp_file)
        os.remove(eps_file)
    except OSError as e:
        pass

    export_line = 'getscreen().getcanvas().postscript(file="%s")\n' % eps_file
    speed_line = 'speed(0)\n'

    #open and read the file
    with open(args.file) as f:
        for line in f:
            m = re.search('name:\s*(.*)',line,re.I)
            if m:
                details['name'] = m.group(1).strip()
                continue
            m = re.search('school:\s*(.*)',line,re.I)
            if m:
                details['school'] = m.group(1).strip()
                continue
            m = re.search('email:\s*(.*)',line,re.I)
            if m:
                details['email'] = m.group(1).strip()
                continue
            orig_lines.append(line)
            #replace done() with the export_line
            if 'done()' in line:
                prog_lines.append(export_line)
            else:
                prog_lines.append(line)
            if 'from turtle import' in line:
                prog_lines.append(speed_line)

    #write the new tmp file
    with open(tmp_file,'w') as f:
        f.writelines(prog_lines)

    #store the tmp file for post
    details['text'] = ''.join(orig_lines)
    #run the tmp file (in a thread to avoid blocking if program never ends?
    os.system("python %s" % tmp_file)

    #convert the image
    try:
        os.system("convert -density 200 -resize 800 %s '%s'" % (eps_file, png_file))
        print("exported to " + png_file)
        details['png_file'] = png_file
    except IOError:
        print("problem converting image")
    return details

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
    """
    load a python turtle competition entry
    replace done() with an eps export
    convert the eps to png with the same name as the python file
    """)
    parser.add_argument('--verbose',
        action='store_const', const=True, dest='verbose', default=False,
        help="verbose")
    parser.add_argument('--file', action='store', dest='file', help="single file to open", required=True)

    args = parser.parse_args()
    details = export()
    keys = ['name','school','email','png_file']
    #check we've got what we need
    for check in keys:
        if not details.has_key(check):
            print("missing " + check)
            exit(1)
    print details
    pickle.dump( details, open( "save.p", "wb" ) )
