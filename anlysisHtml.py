#!/usr/bin/env python3
#coding=utf-8
from html.parser import HTMLParser
class HeadingParser(HTMLParser):
	inHeading = False
	def handle_starttag(self, tag, attrs):
		if tag=="h1":
			self.inHeading=True
			print(attrs)
			print(len(attrs))
			print(attrs[0])
			print(attrs[0][0])
			print("Found a Heading 1")
	def handle_data(self, data):
		if self.inHeading:
			print(data)
			
	def handle_endtag(self, tag):
		if tag=="h1":
			self.inHeading = False
	
hParser = HeadingParser()
file = open("html.html","r")
html = file.read()
file.close
hParser.feed(html)
