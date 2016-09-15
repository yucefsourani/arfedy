#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  talwin.py
#  
#  Copyright 2015 youssef <yousse.m.souranif@gmail.com>
#
#  www.arfedora.blogspot.com
#
#  www.arfedora.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import print_function
import os
from random import choice
import subprocess
version="1.0"

RESET="\033[0m"

def welcome():
	subprocess.call("clear")
	welcom="""
*******************************************************************
*[[[[[[[[[[[[[[[[[[[[[[[[          ~~~~~~~~~~~~~~~~~~~~~~~~~      *
*[[[[[[[[[[[[[[[[[[[[[[[[          ~~~~~~~~~~~~~~~~~~~~~~~~~      *
*{{{{{{{{{{{,{{{{{{{{{{{{          [{{{{{{{{{{{{{{{{{{{{{{{{      *
*{{{{{{{{{{,,,{{{{{{{{{{{          [[{{{{{{{{{{{{{{{{{{{{{{{      *
*{{{{{{{{{,,,,,{{{{{{{{{{          [[[{{{{{{{{{{{{{{{{{{{{{{      *
*{{{{{{{{,,,,,,,{{{{{{{{{          [[{{{{{{{{{{{{{{{{{{{{{{{      *
*{{{{{{{{{{,,,{{{{{{{{{{{          [{{{{{{{{{{{{{{{{{{{{{{{{      *
*[[[[[[[[[[[[[[[[[[[[[[[[          ,,,,,,,,,,,,,,,,,,,,,,,,,      *
*[[[[[[[[[[[[[[[[[[[[[[[[          ,,,,,,,,,,,,,,,,,,,,,,,,,      *
*                                                                 *
*Welcome to talwin Copyright 2015 version 1.0                     *
*youssef sourani <youssef.m.sourani@gmail.com>                    *
* www.arfedora.blogspot.com                                       *
*This is python script to Coloring char and word in linux terminal*
*i used : python ; fedora 21 ; geany ;google translate :P         *
*Quote from termcolor python library                              *
*Quote from The_Linux_Command_Line-arabic-14.07 book              *
*The author Mr william e. shotts jr .                             *
*Translated by Mr Abed el latif mouhamad adib aymash .            *
*python    link:https://www.python.org/                           *
*termcolor link:https://pypi.python.org/pypi/termcolor            *
*geany     link:http://www.geany.org/                             *
*fedora 21 link:http://spins.fedoraproject.org/                   *
*favorite  link:http://www.linuxac.org/forum/forum.php            *
*******************************************************************\n\n"""
	for i in welcom:
		if i=="*":
			talwin(i,"blue",end='')
		elif i=="["  :
			talwin(i,"red",bg="red",end='')
		elif i=="~"  :
			talwin(i,"black",bg="black",end='')
		elif i=="{"  :
			talwin(i,"white",bg="white",end='')
		elif i==",":
			talwin(i,"green",bg="green",end='')
		else :
			talwin(i,"yellow",end='')

COLORS={
		"black"        :"\033[30m",
		"red"          :"\033[31m",
		"green"        :"\033[32m",
		"yellow"       :"\033[33m",
		"blue"         :"\033[34m",
		"magenta"      :"\033[35m",
		"cyan"         :"\033[36m",
		"light_gray"   :"\033[37m",
		"dark_gray"    :"\033[90m",
		"light_red"    :"\033[91m",
		"light_green"  :"\033[92m",
		"light_yellow" :"\033[93m",
		"light_blue"   :"\033[94m",
		"light_magenta":"\033[95m",
		"light_cyan"   :"\033[96m",
		"white"        :"\033[97m"
		}
		
		
		
BG_COLORS={
		"black"        :"\033[40m" ,
		"red"          :"\033[41m" ,
		"green"        :"\033[42m" ,
		"yellow"       :"\033[43m" ,
		"blue"         :"\033[44m" ,
		"magenta"      :"\033[45m" ,
		"cyan"         :"\033[46m" ,
		"light_gray"   :"\033[47m" ,
		"dark_gray"    :"\033[100m",
		"light_red"    :"\033[101m",
		"light_green"  :"\033[102m",
		"light_yellow" :"\033[103m",
		"light_blue"   :"\033[104m",
		"light_magenta":"\033[105m",
		"light_cyan"   :"\033[106m",
		"white"        :"\033[107m"
		
		}


def talwin_core(text, color=None , bg=None ,**kwargs ):
	if os.getenv('ANSI_COLORS_DISABLED') is None:
		talwin_text = "%s%s"
		if color is not None:
			text = talwin_text % (COLORS[color],text) 
		if bg is not None:
			text= talwin_text % (BG_COLORS[bg],text)
		text+=RESET
	return text
	


def random_color_harf(text,exception_color=None,**kwargs): 
	result=""
	if exception_color==None:
		for char in text:
			result+="%s%s%s"%(choice(COLORS.values()),char,RESET)
	else:
		colors=COLORS.values()
		split_exception_color=exception_color.split()
		for color in split_exception_color:
			colors.remove(COLORS[color])
		for char in text:
			result+="%s%s%s"%(choice(colors),char,RESET)
	return result

def random_bg_harf(text,exception_bg=None,**kwargs): 
	result=""
	if exception_bg==None:
		for char in text:
			result+="%s%s%s"%(choice(BG_COLORS.values()),char,RESET)
	else:
		colors=BG_COLORS.values()
		split_exception_bg=exception_bg.split()
		for color in split_exception_bg:
			colors.remove(BG_COLORS[color])
		for char in text:
			if char !=" ":
				result+="%s%s%s"%(choice(colors),char,RESET)
			else:
				result+=" "
	return result


	
	
def random_color_kalima(text,exception_color=None,**kwargs):
	stext=text.split()
	result=""
	if exception_color==None:
		for kalima in stext:
			result+="%s%s%s "%(choice(COLORS.values()),kalima,RESET)

	else:
		colors=COLORS.values()
		split_exception_color=exception_color.split()
		for color in split_exception_color:
			colors.remove(COLORS[color])
		for kalima in stext:
			result+="%s%s%s "%(choice(colors),kalima,RESET)
				
	return result

def random_bg_kalima(text,exception_bg=None,**kwargs):
	stext=text.split()
	result=""
	if exception_bg==None:
		for kalima in stext:
			result+="%s%s%s "%(choice(BG_COLORS.values()),kalima,RESET)

	else:
		colors=BG_COLORS.values()
		split_exception_bg=exception_bg.split()
		for color in split_exception_bg:
			colors.remove(BG_COLORS[color])
		for kalima in stext:
			result+="%s%s%s "%(choice(colors),kalima,RESET)
				
	return result	


def color_harf(text,char=None,color=None,**kwargs):
	count=""
	result=""
	for i in text:
		if i!=" ":
			for j in char :
				if j==i:
					result+="%s%s%s"%(COLORS[color],j,RESET)
					count=j
		if i==count:
			continue
		result+=i
	return result
def bg_harf(text,char=None,bg=None):
	count=""
	result=""
	for i in text:
		if i!=" ":
			for j in char :
				if j==i:
					result+="%s%s%s"%(BG_COLORS[bg],j,RESET)
					count=j
		if i==count:
			continue
		result+=i
	return result
	
def color_bg_harf(text,char_to_color=None,color=None,char_to_bg=None,bg=None,**kwargs):
	count1=""
	count2=""
	result=""
	listchar_to_color=list(char_to_color)
	listchar_to_bg=list(char_to_bg)
	for i in text :
		for c in listchar_to_color:
			if c==i and c!=" ":
				if c not in listchar_to_bg:
					result+="%s%s%s"%(COLORS[color],c,RESET)
					count1=c
				else:
					for b in listchar_to_bg:
						if b==c:
							result+="%s%s%s%s"%(COLORS[color],BG_COLORS[bg],c,RESET)
							count1=c
		for b in listchar_to_bg:
			if b==i and b!=" " and b not in listchar_to_color:
				result+="%s%s%s"%(BG_COLORS[bg],b,RESET)
				count2=b
		if i==count1 or i==count2:
			continue
		result+=i
	return result
	
def color_kalima(text,kalima=None,color=None,**kwargs):
	stext=text.split()
	result=""
	count=""
	skalima=kalima.split()
	for i in stext:
		if i in skalima:
			result+="%s%s%s "%(COLORS[color],i,RESET)
			count=i
		if i==count:
			continue
		result+="%s "%i
	return result	

def bg_kalima(text,kalima=None,color=None,**kwargs):
	stext=text.split()
	result=""
	count=""
	skalima=kalima.split()
	for i in stext:
		if i in skalima:
			result+="%s%s%s "%(BG_COLORS[color],i,RESET)
			count=i
		if i==count:
			continue
		result+="%s "%i
	return result
	




def talwin(text, color=None, bg=None,**kwargs):
	print((talwin_core(text, color, bg)),**kwargs)
	
	

def talwin_random_harf(text,exception_color=None ,**kwargs):
	print((random_color_harf(text,exception_color)),**kwargs)
	
def talwin_random_bg_harf(text,exception_color=None ,**kwargs):
	print((random_bg_harf(text,exception_color)),**kwargs)

def talwin_random_kalima(text,exception_color=None ,**kwargs):
	print((random_color_kalima(text,exception_color)),**kwargs)

def talwin_random_bg_kalima(text,exception_color=None ,**kwargs):
	print((random_bg_kalima(text,exception_color)),**kwargs)
	
	
	
	
	
	
def talwin_harf(text,char=None,color=None,**kwargs):
	print((color_harf(text,char,color)),**kwargs)
			
def talwin_bg_harf(text,char=None,bg=None,**kwargs):
	print((bg_harf(text,char,bg)),**kwargs)	

def talwin_bg_color_harf(text,char_to_color=None,color=None,char_to_bg=None,bg=None,**kwargs):
	print((color_bg_harf(text,char_to_color,color,char_to_bg,bg)),**kwargs)	
	
	
	
	
	

def talwin_kalima(text,kalima=None,color=None,**kwargs):
	print((color_kalima(text,kalima,color)),**kwargs)

def talwin_bg_kalima(text,kalima=None,bg=None,**kwargs):
	print((bg_kalima(text,kalima,bg)),**kwargs)		
	
