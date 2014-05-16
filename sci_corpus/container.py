import os
import json
import codecs
import sqlite3
import csv
from lxml import etree as ET
import StringIO as strio
from shutil import copy2


class ContainerDB():

    """Class container."""

    def __init__(self):
        self.__path = ''
        self.__defaultpath = '../examples/backup.db'
        self.__isModified = False
        self.createNconnectDB(flag=True)

    def createNconnectDB(self, path='', flag=False):
        """
        Create a connection to a sqlite3 database and and a table to store the
        sentences information.

        When path='' creats a connection with a in-memory database. Otherwise
        connects to a file specified by path.

        Parameters:
        -----------
        path: string

               This string contains the path.

        Returns:
        --------
        No explicity return, intead this function assign to self.__dbfile
        or self.__dbmem a sql connection.

        """

        try:
            if path != '':
                self.__dbfile = sqlite3.connect(path)
                self.__dbfile.text_factory = str
            else:
                self.__dbmem = sqlite3.connect(":memory:")
                self.__dbmem.text_factory = str

        except sqlite3.Error as err:
            print "[INFO creatNconnect] %s" % err

        else:
            if flag:
                if path != '':
                    self.__dbfile.cursor().execute('''CREATE TABLE IF NOT EXISTS
							corpus(id INTEGER PRIMARY KEY, sec TEXT, subsec TEXT,
							func TEXT, phrase TEXT, ref TEXT)''')
                    self.__dbfile.commit()
                else:
                    self.__dbmem.cursor().execute('''CREATE TABLE IF NOT EXISTS
							corpus(id INTEGER PRIMARY KEY, sec TEXT, subsec TEXT,
							func TEXT, phrase TEXT, ref TEXT)''')
                    self.__dbmem.commit()

    def importToMemory(self):
        """
        Imports a file database to a memory database.

        This function has to be called after createNconnectDB(path).


        Parameters:
        -----------
        None:


        Returns:
        --------
        No explicity return, intead this function reads from self.__dbfile
        and write to self.__dbmem.

        """
        try:
            tempfile = strio.StringIO()
            for line in self.__dbfile.iterdump():
                tempfile.write('%s\n' % line)
            self.__dbfile.close()
            tempfile.seek(0)

            self.__dbmem.cursor().execute('DROP TABLE corpus')
            self.__dbmem.cursor().executescript(tempfile.read())
            self.__dbmem.commit()

        except sqlite3.Error as err:
            print "[INFO importToMemory] %s" % err

    def importToDBFile(self):
        """
        Imports a in-memory database to a file database

        This function has to be called after createNconnectDB(path).


        Parameters:
        -----------
        None:


        Returns:
        --------
        No explicity return, intead this function reads from self.__dbmem
        and write to self.__dbfile.

        """
        try:
            tempfile = strio.StringIO()
            for line in self.__dbmem.iterdump():
                tempfile.write('%s\n' % line)
            tempfile.seek(0)

            self.__dbfile.cursor().executescript(tempfile.read())
            self.__dbfile.commit()
            self.__dbfile.close()
        except sqlite3.Error as err:
            print "[INFO importToDBFile] %s" % err

    def addDB(
            self,
            sect=['Not Classified'],
            subsect=['Not Classified'],
            funct=['Not Classified'],
            phrase=['NULL'],
            ref=['NULL']):
       """
        Add a entry on the corpus table.
        An entry is composed of: (section, subsection, function, sentence, reference)
        By default, sect=subsec=funct='Not Classified' and phrase=ref='NULL'. In doing
        so, we avoid have to pass always all the arguments.

        Parameters:
        -----------
        sect: list of strings

              Store all the sections that will be inserted

        secsect: list of strings

              Store all the subsections that will be inserted

        function: list of strings

              Store all the functions that will be inserted

        phrase: list of strings

              Store all the sentences that will be inserted

        ref: list of strings

              Store all the references that will be inserted

        Returns:
        --------
        No explicity return, intead this function adds an entry in corpus
        table of self.__dbmem connection

        """

       cursor = self.__dbmem.cursor()
       # We need to review this test
       # But now its working. Actually sect, subsect and funct can be empty
       # lists or list with empty strings.
       if (sect == []) or (sect == ['']):
           sect = ['Not Classified']
       if (subsect == []) or (subsect == ['']):
           subsect = ['Not Classified']
       if (funct == []) or (funct == ['']):
           funct = ['Not Classified']
       if phrase == ['']:
           phrase = ['NULL']
       if ref == ['']:
           ref = ['NULL']

       try:
           whatadd = [
               (a, b, c, d, e)
               for a in sect for b in subsect
               for c in funct for d in phrase for e in ref]
           cursor.executemany(
               '''INSERT INTO corpus(sec,subsec,func,phrase,ref) VALUES(?,?,?,?,?)''',
               whatadd)

       except sqlite3.Error as err:
           print "[INFO addDB] %s" % err

       else:
           self.isModified = True

    def listSections(self):

        cursor = self.__dbmem.cursor()
        
        cursor.execute('SELECT DISTINCT sec FROM corpus')
        
        return [a for (a,) in cursor.fetchall()]
        
           
    def crazyRepetition(self, sBase="", sConnect="", sItems=[]):
        """
        Combines sentences in one string to make selection easier.

        When two or more parameters are selected on section, subsectio or
        function, the program should return the sentences that lie on the
        intersection of all the itens selected. In this way, this method
        returns a string that will be used in the selection of the intersection
        of all the sentences that are in this intersection

        Parameters:
        -----------
        sBase: string

               This string will be repeated n times.

        sConnect: string

                  This string  will connect all the different sBase strings.

        sItems: list of strings

                Each string in this list will be replace the '?' signal on the
                base sentences, making new ones.

        Returns:
        --------
        sFinal: string

                This string iscomposed by all len(sItens) strings linked together
                with sConnect string.

        """

        sFinal = ''

        if(len(sItems) > 0):

            queryList = []

            for item in sItems:
                queryList.append(sBase.replace("?", "\"" + item + "\""))

            if(len(sItems) == 1):
                sFinal = queryList[0]
            else:
                for i in range(0, len(queryList) - 1):
                    sFinal += queryList[i] + " " + \
                        sConnect + " " + queryList[i + 1]

        else:
            raise AssertionError(
                "Number of itens in the sItens is incompatible!")

        return sFinal

    def listCategories(self, section=[], subsection=[], function=[]):

        cursor = self.__dbmem.cursor()

        secsubsecfunc = []
        subsecfunc = []
        functions = []
        final = []

        try:
            if section == [] and subsection == [] and function == []:
                cursor.execute(
                    '''SELECT DISTINCT sec, subsec, func FROM corpus''')
                secsubsecfunc = cursor.fetchall()

            if section != [] and subsection == [] and function == []:
                cursor.execute(
                    'SELECT DISTINCT sec, subsec, func FROM corpus WHERE sec in ({0})'.format(
                        ','.join(
                            '?' for _ in section)),
                    section)
                subsecfunc = cursor.fetchall()

            if section != [] and subsection != [] and function == []:
                secsubsecTuple = [(a, b) for a in section for b in subsection]
                for i in range(len(secsubsecTuple)):
                    cursor.execute(
                        '''SELECT DISTINCT sec, subsec, func FROM corpus WHERE sec=? AND subsec=?''',
                        secsubsecTuple[i])
                    functions.extend(cursor.fetchall())

        except sqlite3.Error as err:
            print "[INFO listCategories] %s" % err

        finally:
            final.extend(secsubsecfunc)
            final.extend(subsecfunc)
            final.extend(functions)
            return final

    def listSubSections(self,qsections=[]):
            cursor = self.__dbmem.cursor()
            query=''
            if(qsections!=[]):
                query=self.crazyRepetition('SELECT DISTINCT subsec FROM corpus WHERE sec=?',
                                           'INTERSECT', qsections)
            else:
                query='SELECT DISTINCT subsec FROM corpus'

            cursor.execute(query)
            return [a for (a,) in cursor.fetchall()]
            
    def listFunctions(self, qsections=[], qsubsections=[]):
           '''
           Coisa
           '''
           cursor = self.__dbmem.cursor()
           query='' 
           if(qsections == [] and qsubsections == []):

               query='SELECT DISTINCT func FROM corpus'   
                            
           elif(qsections != [] and qsubsections == []):

               query=self.crazyRepetition('SELECT DISTINCT func FROM corpus WHERE sec=?',
                                          'UNION', qsections) 
           elif(qsections == [] and qsubsections != []):

               query=self.crazyRepetition('SELECT DISTINCT func FROM corpus WHERE subsec=?',
                                          'INTERSECT', qsubsections)

           elif(qsections != [] and qsubsections != []):
               query1 = self.crazyRepetition('SELECT DISTINCT func FROM corpus WHERE sec=?',
                                          'INTERSECT', qsections) 
               query2 = self.crazyRepetition('SELECT DISTINCT func FROM corpus WHERE subsec=?',
                                          'INTERSECT', qsubsections)

               query = query1 +" INTERSECT "+query2
           else:
              print "Deu pau Juvenal!"

           cursor.execute(query)
           return [a for (a,) in cursor.fetchall()]
        

    def listSentences(self, section=[], subsection=[], function=[]):

        cursor = self.__dbmem.cursor()

        phrases = []

        try:
            if section == [] and subsection == [] and function == []:
                cursor.execute(
                    '''SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus''')
                phrases.extend(cursor.fetchall())

            if section != [] and subsection == [] and function == []:
                cursor.execute(
                    'SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus WHERE sec in ({0})'.format(
                        ','.join(
                            '?' for _ in section)),
                    section)
                phrases.extend(cursor.fetchall())

            if section != [] and subsection != [] and function == []:
                secsubsecTuple = [(a, b) for a in section for b in subsection]
                for i in range(len(secsubsecTuple)):
                    cursor.execute(
                        '''SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus WHERE sec=? AND subsec=?''',
                        secsubsecTuple[i])
                    phrases.extend(cursor.fetchall())

            if section != [] and subsection != [] and function != []:
                secsubsecfuncTuple = [(a, b, c)
                                      for a in section
                                      for b in subsection for c in function]
                for i in range(len(secsubsecfuncTuple)):
                    cursor.execute(
                        '''SELECT DISTINCT sec, subsec, func, phrase, ref FROM corpus WHERE sec=? AND subsec=? AND func=?''',
                        secsubsecfuncTuple[i])
                    phrases.extend(cursor.fetchall())

        except sqlite3.Error as err:
            print "[INFO listSentences] %s" % err

        finally:
            return phrases


    def listAll(self):
        """
        Dump the database.

        Parameters:
        -----------
        None

        Returns:
        --------
        Return a list of tuples with all (sections, subsections, functions,
        sentences, references) of the corpus table.

        """
        cursor = self.__dbmem.cursor()

        allInfo = []

        try:
            cursor.execute(
                'SELECT DISTINCT sec, subsec, func, phrase, ref from corpus')
            allInfo.extend(cursor.fetchall())

        except sqlite3.Error as err:
            print "[INFO listAll] %s" % err

        finally:
            return allInfo

    def update(
        self, section=[
            ('NULL', 'NULL')], subsection=[
            ('NULL', 'NULL')], function=[
                ('NULL', 'NULL')], phrase=[
                    ('NULL', 'NULL')], ref=[
                        ('NULL', 'NULL')]):
        """
        Updates an entry.

        This function substitute a value on a given entry of corpus table.
        All the arguments is a list of tuples and each tuple is of the form
        (old_value,new_value)

        Parameters:
        -----------
        section: list of tuples

                 Sections to be updated

        subsection: list of tuples

                 Subsections to be updated

        function: list of tuples

                 Functions to be updated

        phrase: list of tuples

                 Sentences to be updated

        ref: list of tuples

                 References to be updated

        Returns:
        --------
        This function hasnt a explicity return. Intead it will update an
        entry on the corpus table.

        """

        cursor = self.__dbmem.cursor()

        try:
            if section != [('NULL', 'NULL')] and subsection == [('NULL', 'NULL')] and function == [('NULL', 'NULL')] and phrase == [('NULL', 'NULL')] and ref == [('NULL', 'NULL')]:
                cursor.execute('''UPDATE corpus
                              SET sec=? WHERE sec=?''', section[0])

            if section == [('NULL', 'NULL')] and subsection != [('NULL', 'NULL')] and function == [('NULL', 'NULL')] and phrase == [('NULL', 'NULL')] and ref == [('NULL', 'NULL')]:
                cursor.execute('''UPDATE corpus
                              SET subsec=? WHERE subsec=?''', subsection[0])

            if section == [('NULL', 'NULL')] and subsection == [('NULL', 'NULL')] and function != [('NULL', 'NULL')] and phrase == [('NULL', 'NULL')] and ref == [('NULL', 'NULL')]:
                cursor.execute('''UPDATE corpus
                              SET func=? WHERE func=?''', function[0])

            if section == [('NULL', 'NULL')] and subsection == [('NULL', 'NULL')] and function == [('NULL', 'NULL')] and phrase != [('NULL', 'NULL')] and ref == [('NULL', 'NULL')]:
                cursor.execute('''UPDATE corpus
                              SET phrase=? WHERE phrase=?''', phrase[0])

            if section == [('NULL', 'NULL')] and subsection == [('NULL', 'NULL')] and function == [('NULL', 'NULL')] and phrase == [('NULL', 'NULL')] and ref != [('NULL', 'NULL')]:
                cursor.execute('''UPDATE corpus
                              SET ref=? WHERE ref=?''', ref[0])

        except sqlite3.Error as err:
            print "[INFO update] %s" % err

        else:
            self.isModified = True

    def remove(self, sect=[], subsect=[], funct=[], phrase=[]):
        """
        Removes an entry.

        This function substitute a value on a given entry of corpus table.
        If it is a section, subsection or function it will update the entry
        by 'Not Classified' and if is a sentences, by 'NULL'

        Parameters:
        -----------
        section: list of strings

                 Sections to be removed

        subsection: list of strings

                 Subsections to be removed

        function: list of strings

                 Functions to be removed

        phrase: list of strings

                 Sentences to be removed


        Returns:
        --------
        This function hasnt a explicity return. Intead it will update an
        entry on the corpus table.

        """
        cursor = self.__dbmem.cursor()

        try:
            if sect != [] and subsect == [] and funct == [] and phrase == []:
                whatup = [('Not Classified', a) for a in sect]
                self.update(section=whatup)

            if sect == [] and subsect != [] and funct == [] and phrase == []:
                whatup = [('Not Classified', a) for a in subsect]
                self.update(subsection=whatup)

            if sect == [] and subsect == [] and funct != [] and phrase == []:
                whatup = [('Not Classified', a) for a in funct]
                self.update(function=whatup)

            if sect == [] and subsect == [] and funct == [] and phrase != []:
                whatup = [('NULL', a) for a in phrase]
                self.update(phrase=whatup)

        except sqlite3.Error as err:
            print "[INFO remove] %s" % err
        else:
            self.isModified = True

    def bulk_add(self, info):
        """
        Add a lot of entry at a time.

        Parameters:
        -----------
        info: list of tuples

              This argument is formated in the following manner:
              [(section, subsection, function, sentence, reference), ...]


        Returns:
        --------
        This function hasnt a explicity return. Intead it will add entrys
        on corpus table.

        """
        cursor = self.__dbmem.cursor()

        # print info

        try:
            cursor.executemany(
                'INSERT INTO corpus(sec,subsec,func,phrase,ref) VALUES(?,?,?,?,?)',
                info)
        except sqlite3.Error as err:
            print "[INFO addbulk insert] %s" % err
        else:
            self.isModified = True

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = os.path.abspath(path)

    @property
    def defaultpath(self):
        return self.__defaultpath

    @defaultpath.setter
    def defaultpath(self, path):
        self.__defaultpath = os.path.abspath(path)

    @property
    def dbfile(self):
        self.__dbfile

    @property
    def dbmem(self):
        self.__dbmem

    @property
    def isModified(self):
        """Shows the answer for is modified question."""
        return self.__isModified

    @isModified.setter
    def isModified(self, state):
        self.__isModified = state

    def write_(self, path=''):
        """Writes file in path or in self.path if not passed."""

        self.__dbmem.commit()

        if path == '':
            path = self.path
            try:
                copy2(path, self.__defaultpath)
                os.remove(path)
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))
            else:
                self.createNconnectDB(path)
                self.importToDBFile()
        else:
            self.path = path
            try:
                os.remove(path)
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))
            finally:
                self.createNconnectDB(path)
                self.importToDBFile()

        self.isModified = False

    def read_(self, path):
        """Reads file."""

        try:
            self.createNconnectDB(path)
            self.importToMemory()
        except Exception:
            raise
        else:
            self.path = path
            self.isModified = False

    def close_(self):
        """Clear all fields."""

        try:
            self.__dbmem.close()
        except sqlite3.Error as err:
            print "[INFO close] %s" % err
        else:
            self.__path = ''
            self.__isModified = False
        finally:
            self.createNconnectDB(flag=True)

    def import_(self, path=''):
        """Import file as XML, JSON, DB."""
        # @TODO: We need to implement a signal to send a log message.
        print 'Importing from: ', path

        path = os.path.abspath(path)
        ext = os.path.splitext(path)[1]

        if (ext == '.xml') or (ext == '.XML'):
            print "Importing XML ..."

            try:
                tree = ET.parse(path)
                root = tree.getroot()

            except ET.ParseError as err:
                print "[INFO xml import] %s" % err

            else:
                info = []

                try:
                    for w in root.findall('INFOPIECE'):
                        sec = w.find('SECTION').text
                        if sec is None:
                            sec = 'Not Classified'
                        subs = w.find('SUBSECTION').text
                        if subs is None:
                            subs = 'Not Classified'
                        func = w.find('FUNCTION').text
                        if func is None:
                            func = 'Not Classified'
                        sent = w.find('PHRASE').text
                        if sent is None:
                            sent = 'Not Classified'
                        ref = w.find('REF').text
                        if ref is None:
                            ref = 'Not Classified'

                        info.append(
                            (sec.encode("utf-8"),
                             subs.encode("utf-8"),
                                func.encode("utf-8"),
                                sent.encode("utf-8"),
                                ref.encode("utf-8")))

                        # print info

                except ET.ParseError as err:
                    print "[INFO xml import] %s" % err

                else:
                    self.bulk_add(info)
                    self.isModified = True

        elif (ext == '.csv') or (ext == '.CSV'):
            print "Importing CSV ..."
            with codecs.open(path, 'rb', 'utf-8') as csv_file:
                csv_fields = csv.reader(
                    csv_file,
                    delimiter=';',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL)
                row_number = 0
                for row in csv_fields:
                    if row_number == 0:
                        column_titles = row
                    else:
                        try:
                            [sec, subs, func, sent, ref] = row
                            # Splitting many fields in the same category
                            sec = [x.encode("utf-8") for x in sec.split(',')]
                            subs = [x.encode("utf-8") for x in subs.split(',')]
                            func = [x.encode("utf-8") for x in func.split(',')]
                            self.addDB(sec,
                                       subs,
                                       func,
                                       [sent.encode("utf-8")],
                                       [ref.encode("utf-8")])
                            self.isModified = True
                        except Exception as e:
                            print "Error when importing CSV: {}".format(str(e))
                    row_number += 1

        elif (ext == '.json') or (ext == '.JSON'):
            print "Importing JSON ..."
            with codecs.open(path, 'rb', 'utf-8') as json_file:
                text = json_file.read()
                json_fields = json.loads(str(text))
                for row in json_fields:
                    try:
                        [sec, subs, func, sent, ref] = row
                        self.addDB([sec.encode('utf-8')],
                                   [subs.encode('utf-8')],
                                   [func.encode('utf-8')],
                                   [sent.encode("utf-8")],
                                   [ref.encode("utf-8")])
                        self.isModified = True
                    except Exception as e:
                        print "Error when importing JSON: {}".format(str(e))

        else:
            raise IOError(
                "Not recognized file type to import. Please, use XML, CSV or JSON.")

    def export_(self, path=''):
        """Export file as XML, JSON, DB."""
        print 'Exporting to: ', path

        path = os.path.abspath(path)
        ext = os.path.splitext(path)[1]
        try:
            info = []
            info = self.listAll()
        except sqlite3.Error as err:
            print "[INFO listall exporting] %s" % err
        else:
            if (ext == '.xml') or (ext == '.XML'):
                print "Exporting XML ..."
                try:
                    root = ET.Element('ARTINFO')
                    for (secv, subsv, funcv, sentv, refv) in info:
                        infopiece = ET.SubElement(root, 'INFOPIECE')
                        sec = ET.SubElement(infopiece, 'SECTION')
                        sec.text = secv
                        subs = ET.SubElement(infopiece, 'SUBSECTION')
                        subs.text = subsv
                        func = ET.SubElement(infopiece, 'FUNCTION')
                        func.text = funcv
                        sent = ET.SubElement(infopiece, 'PHRASE')
                        sent.text = sentv
                        ref = ET.SubElement(infopiece, 'REF')
                        ref.text = refv
                    # print ET.tostring(root, pretty_print=True,
                    # xml_declaration=True)
                    tree = ET.ElementTree(root)
                    tree.write(path, pretty_print=True, xml_declaration=True)
                except ET.ParseError as err:
                    print "[INFO xml export] %s" % err

            elif (ext == '.csv') or (ext == '.CSV'):
                print "Exporting CSV ..."

                with codecs.open(path, 'wb', 'utf-8') as csv_file:
                    csv_fields = csv.writer(
                        csv_file,
                        delimiter=';',
                        quotechar='"',
                        quoting=csv.QUOTE_ALL)
                    csv_fields.writerow(
                        ["SECTION", "SUB SECTION", "FUNCTION", "SENTENCE", "REFERENCE"])
                    for (secv, subsv, funcv, sentv, refv) in info:
                        if sentv == 'NULL':
                            sentv = ""
                        if refv == 'NULL':
                            refv = ""
                        csv_fields.writerow([secv, subsv, funcv, sentv, refv])

            elif (ext == '.json') or (ext == '.JSON'):
                print "Exporting JSON ..."
                info_without_null = []

                for (secv, subsv, funcv, sentv, refv) in info:
                    if sentv == 'NULL':
                        sentv = ""
                    if refv == 'NULL':
                        refv = ""
                    info_without_null.append([secv, subsv, funcv, sentv, refv])

                with codecs.open(path, 'wb', 'utf-8') as json_file:
                    json.dump(info, json_file, encoding='utf-8', indent=4)

            else:
                raise IOError(
                    "Not recognized file type to import. Please, use XML, CSV or JSON.")

    
