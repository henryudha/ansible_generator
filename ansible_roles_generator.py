#!/usr/bin/env python

###  RTFM : python ansible_roles_generator.py -help  ###
# henryudha@gmail.com 3

import os
import os.path
import sys
from argparse import ArgumentParser

# -  directory Skeleton please visit http://docs.ansible.com/ansible/playbooks_best_practices.html

class AnsibleGenerator:
	
	rootPath = ""
	roleName = ""
	roleSubDirs = ['files', 'handlers', 'meta','templates','tasks','vars','defaults']	
	
	## constructor
	def __init__(self, name, path):
		self.rootPath = path
		self.roleName = name

	## function to create default skeleton
	def execute(self):
		self.createRolesSubdirectory()
		self.createSiteFile()
		self.createGroupVars()
		self.createHostVars()
	
	## function to create role subdirectory 
	## format: roles/<role name>/<subdir>
	def createRolesSubdirectory(self):
		for rolesubdir in self.roleSubDirs:
			completeFilesPath = self.rootPath + "/roles/"  + self.roleName + "/" + rolesubdir
			if not os.path.exists(completeFilesPath):
				os.makedirs(completeFilesPath)
		
	## function to create site.yml 
	## format: site.yml
	def createSiteFile(self):
		filename = self.rootPath + "/site.yml"
		if not os.path.exists(filename):	
			fhandle = open(filename, 'a')
			fhandle.close()

	## function to create stage files contains all the the testing hosts
	def createStageFile(self):
		filename = self.rootPath + "/stage"
		if not os.path.exists(filename):
			fhandle = open(filename, 'a')
			fhandle.close()

	## function to create Production files contains all the production hosts
	def createProductionFile(self):
		filename = self.rootPath + "/production"
		if not os.path.exists(filename):
			fhandle = open(filename, 'a')
			fhandle.close()

	## function to create group_vars directory
	def createGroupVars(self):
		directoryname =  self.rootPath + "/group_vars/"
		if not os.path.exists(directoryname):
				os.makedirs(directoryname)

	## function to create host_vars directoy
	def createHostVars(self):
		directoryname =  self.rootPath + "/host_vars/"
		if not os.path.exists(directoryname):
				os.makedirs(directoryname)

#parser Ansible Generator
parser = ArgumentParser()
parser.add_argument("-D" , dest="directoryname")
parser.add_argument("-A", dest="ansiblerolesname")
args = parser.parse_args()

arg1 = args.directoryname
arg2 = args.ansiblerolesname

genAnsible = AnsibleGenerator(arg2, arg1)
genAnsible.execute()
