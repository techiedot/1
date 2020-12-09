# coding=utf-8


import os
import subprocess
class GenerateReport(object):
    '''
    Class generate test report example. Python 2.xxx
    '''





    def __init__(self, file_name = None):
        '''
        Latex tempalte broken in parts so we can fill all required fields before running lualatex command
        '''
        self.__package  = None
        self.__title = None
        self.__content = None
        self.__file_name = file_name
        self.open(file_name)
        

    def open(self, name=None):

        if name is not None:
            self.__file = open(name, 'w')

    '''
    Latex Preamble section. 
    '''

    def preambles(self, state = None):
        self.__package = str() if state is not None else None
        if state is not None:
            self.__package +=   '\n' +\
                                "\usepackage[english]{babel}" +\
                                '\n' +\
                                "\usepackage{amsmath,amsfonts,amsthm}" + \
                                '\n' + \
                                "\usepackage[utf8]{inputenc}" + \
                                '\n' + \
                                "\usepackage{float}" + \
                                '\n' + \
                                "\usepackage{lipsum}" + \
                                '\n' + \
                                "\usepackage{blindtext}" + \
                                '\n' + \
                                "\usepackage{graphicx}" + \
                                '\n' + \
                                "\usepackage{caption}" + \
                                '\n' + \
                                "\usepackage{subcaption}" + \
                                '\n' + \
                                "\usepackage[sc]{mathpazo}" + \
                                '\n' + \
                                "\usepackage[T1]{fontenc}" + \
                                '\n' +\
                                "\usepackage{longtable}" +\
                                '\n' + \
                                "\linespread{1.05}" + \
                                '\n' + \
                                "\usepackage{microtype}"+ \
                                '\n' + \
                                "\usepackage[hmarginratio=1:1,top=32mm,columnsep=20pt]{geometry}" + \
                                '\n' + \
                                "\usepackage{multicol}" + \
                                '\n' + \
                                "\usepackage{booktabs}" + \
                                '\n' + \
                                "\usepackage{float}" + \
                                '\n' + \
                                "\usepackage{hyperref}" + \
                                '\n' + \
                                "\usepackage{lettrine}"+ \
                                '\n' + \
                                "\usepackage{paralist}" + \
                                '\n' + \
                                "\usepackage{abstract}" + \
                                '\n' + \
                                "\\renewcommand{\\abstractnamefont}{\\normalfont\\bfseries}" + \
                                '\n' + \
                                "\\renewcommand{\\abstracttextfont}{\\normalfont\\small\\itshape}" + \
                                '\n' + \
                                "\usepackage{titlesec}" + \
                                '\n' + \
                                "\\renewcommand\\thesection{\\Roman{section}}" + \
                                '\n' + \
                                "\\renewcommand\\thesubsection{\\Roman{subsection}}"+ \
                                '\n' + \
                                "\\titleformat{\section}[block]{\large\scshape\centering}{}{1em}{}" + \
                                '\n' + \
                                "\\titleformat{\\subsection}[block]{\\large}{\\thesubsection.}{1em}{}" + \
                                '\n' + \
                                "\\newcommand{\\horrule}[1]{\\rule{\\linewidth}{#1}}" + \
                                '\n' + \
                                "\usepackage{fancyhdr}" + \
                                '\n' + \
                                "\pagestyle{fancy}" + \
                                '\n' + \
                                "\\fancyhead{}" + \
                                '\n' + \
                                "\\fancyfoot{}" + \
                                '\n' + \
                                "\\fancyhead[C]{Software testing is not a silver bullet}" + \
                                '\n' + \
                                "\\fancyfoot[RO,LE]{\\thepage}"
    '''
    Latex title section. 
    '''

    def title(self, state = None):
        self.__title = str() if state is not None else None
        if state is not None:
            self.__package += '\n' + \
                             "\\title{\\vspace{-15mm}\\fontsize{24pt}{10pt}\\selectfont\\textbf{Test Report for: High-Security Linux FPGA Embedded Computer}}" + \
                             '\n' + \
                             "\\author{" + \
                             '\n' + \
                             "\\large" + \
                             '\n' + \
                             "{\\textsc{Single Board Computer act as webserver and REST API(client)}}\\\[2mm]" + \
                             '\n' + \
                             "{\\textsc{200Mhz ARM9 with MMU and 32 MB SDRAM}}\\\[2mm]" + \
                             '\n' + \
                             "{\\textsc{Altera 2C8 Cyclone II FPGA}}\\\[2mm]" + \
                             '\n' + \
                             "\\normalsize Reference Computer science by Allen B. Tucker\\\[1mm]" + \
                             '\n' + \
                             "\\visit  www.techeidot.com \\\\" + \
                             '\n' + \
                             "\\normalsize Fast boot to Linux prompt-shell in 1.69 seconds \\\\" + \
                             '\n' + \
                             "\\vspace{-5mm}" + \
                             '\n' + \
                             "}" + \
                             '\n' + \
                             "\\date{}" + \
                             '\n'
                                
    '''
    Latex content section. 
    '''
    def content(self, state = None):
        self.__content = str() if state is not None else None
        if state is not None:
            self.__package += '\n' + \
                             "\\begin{document}" + \
                             '\n' + \
                             "\maketitle" + \
                             '\n' + \
                             "\\thispagestyle{fancy}" + \
                             '\n' + \
                             "\\section{Software Testing principle and methods}" + \
                             '\n' + \
                             "\\begin{itemize}" + \
                             '\n' + \
                             "\item When a program is implemented to provide a concrete representation of an algorithm, the developers of this program are naturally concerned with the correctness and performance of the implementation.Software engineers must ensure that their software systems achieve an appropriate level of quality. Software verification is the process of ensuring that a program meets its intended specification " + \
                             '\n' + \
                             "\item The IEEE standard defines a failure as the external, incorrect behavior of a program [IEEE, 1996].Traditionally, the anomalous behavior of a program is observed when incorrect output is produced or a runtime failure occurs" + \
                             '\n' + \
                             "\item  The competent programmer hypothesis assumes that competent programmers create programs that compile and very nearly meet their specification" + \
                             '\n' + \
                             "\item  A software system is considered to be robust if it can handle inappropriate inputs in a graceful fashion. Robustness testing is a type of software testing that attempts to ensure that a software system performs in an acceptable fashion when it is provided with anomalous input or placed in an inappropriate execution environment. Robustness testing is directly related to the process of hardware and software fault injection" +  \
                             '\n' + \
                             "\item  Regression test prioritization approaches assist with regression testing in a fashion that is distinctly different from test selection methods. Test case prioritization techniques allow testers to order the execution of a regression test suite in an attempt to increase the probability that the suite might detect a fault at early testing stages" + \
                             '\n' + \
                             "\item Separation of concerns allows us to deal with different aspects of a problem to dominate its complexity, so that we can concentrate on each aspect individually. Separation of concerns is a commonsense practice that we try to follow in our everyday lives to overcome the difficulties we encounter. The principle shouldalso be applied to software development, to master its inherent complexity." +\
                             '\n' + \
                             "\item  Even simple software applications have complicated and ever-changing operating environments that increase the number of interfaces and the interface interactions that must be tested. Device drivers, op-erating systems, and databases are all aspects of a software system’s environment that are often ignored during testing " + \
                             '\n' + \
                             "\item Over the past 50 years, computer systems have increased rapidly in terms of both size and complexity. As a result, it is both naive and dangerous to expect a development team to undertake a project without stating clearly and precisely what is required of the system. This is done as part of the requirements specification phase of the software life cycle, the aim of which is to describe what the system is to do, rather than how it will do it " + \
                             '\n' + \
                             "\item  Anticipation of change is perhaps the one principle that distinguishes software the most from other types of industrial productions. In fact, software undergoes changes constantly, and anticipation of change is a principle that we can use to achieve evolvability" + \
                             '\n' + \
                             "\end{itemize}" + \
                             '\n' + \
                             '\n' + \
                             '\n' + \
                             "\subsection{Description of the device}" + \
                             '\n' + \
                             "The small embedded computer is a multipurpose board designed specifically for customers needing extreme design security, flexibility, and reliability in applications such as gaming machines, building security equipment, or critical network infrastructure services such as network gateways or firewalls. A 8256 LUT Cyclone II FPGA is included on the board. The Embedded FPGA Linux system is reconfigurable on-the-fly by the 200MHz ARM9 CPU running Debian Linux when an additional real-time soft-coprocessor(s), DSP, or specific additional peripheral logic is needed" + \
                             '\n' + \
                             '\n' + \
                             "\subsection{Software test results }" + \
                             '\n' + \
                             '\n' + \
                             "\\begin{table}[!h]" + \
                             '\n' + \
                             "\\label{T:equipos}" + \
                             '\n' + \
                             "\\begin{center}" + \
                             '\n' + \
                             "\\begin{tabular}{| c | c | c | c | c |}" + \
                             '\n' + \
                             "\\hline" + \
                             '\n' + \
                             "\\textbf{Test} & \multicolumn{4}{ c |}{\\textbf{Modules}}  \\\\" + \
                             '\n' + \
                             "\\cline{2-5}" + \
                             '\n' + \
                             "& \\textbf{Device drivers} & \\textbf{Applications} & \\textbf{Libraries} & \\textbf{System} \\\\" + \
                             '\n' + \
                             "\hline" + \
                             '\n' + \
                             "Structurally-Based Criterion &  &  &  &  \\\\ \hline" + \
                             '\n' + \
                             "Control Flow-Based Criterion &  &   &   & \\\\ \hline" + \
                             '\n' + \
                             "Fault-Based Criterion &   &  &  & \\\\ \hline" + \
                             '\n' + \
                             "Error-Based Criterion &  &  &  & \\\\ \hline" + \
                             '\n' + \
                             "Database-Driven Testing &  &   &  & \\\\ \hline" + \
                             '\n' + \
                             "Testing Graphical User Interface &  &  &  & \\\\ \hline" + \
                             '\n' + \
                             "Specification testing  &  &   &   & \\\\ \hline" + \
                             '\n' + \
                             "Network-specific testing &  &   &   & \\\\ \hline" + \
                             '\n' + \
                             "Security testing &  &   &   & \\\\ \hline" + \
                             '\n' + \
                             "\end{tabular}" + \
                             '\n' + \
                             "\end{center}" + \
                             '\n' + \
                             "\end{table}" + \
                             '\n' + \
                             "\section{Analyse}" +\
                             '\n' + \
							 "\\begin{enumerate}" +\
							 '\n' + \
							 "\item Testing is an important technique for the improvement and measurement of a software system’s quality. Any approach to testing software faces essential and accidental difficulties and, as noted by Edsger Dijkstra [1968], the construction of the needed test programs is a “major intellectual effort.” While software testing is not a “silver bullet” that can guarantee the production of high-quality applications, theoretical and empirical investigations have shown that the rigorous, consistent, and intelligent application of testing techniques can improve software quality. Software testing normally involves the stages of test case selection, test case generation, test execution, test adequacy evaluation, and regression testing. Each of these stages in our model of the software testing process plays an important role in the production of programs that meet their intended specification. The body of theoretical and practical knowledge about software testing continues to grow as research expands the applicability of existing techniques and pro- poses new testing techniques for an everwidening range of programming languages and application domains" +\
							 '\n' + \
							 "\end{enumerate}" +\
                             "\end{document}" + \
                             '\n'
    

                                 
    '''
    Latex beginning of document section. 
    '''
    def top(self, state=None):
                if state is None:
                    self.__document = "\documentclass[paper=letter,fontsize=12pt]{article}"


    '''
    Generating latex document and write to the file. 
    '''
    def generate_report(self):
                self.__document = str()
                if not len(self.__document):
                    self.top()
                if self.__package is not None:
                   self.__document += self.__package
                if self.__title is not None:
                       self.__document += self.__title
                if self.__content is not None:
                       self.__document += self.__content

                self.__file.write(self.__document)
                
                cmd = ("lualatex --interaction=nonstopmode %s" % (self.__file_name))
                os.system(cmd)
'''
Change file and directory name here 
'''
r=GenerateReport(file_name="/home/../../report.tex")
r.preambles("generate")
r.title("generate")
r.content("generate")
r.generate_report()
