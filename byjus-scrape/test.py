import requests, bs4, lxml
from datetime import datetime 

startTime = datetime.now()
for i in range(6, 13):
	urlNcert = "https://byjus.com/ncert-solutions-class-" + str(i) + "-maths/"
	urlRSAgg = "https://byjus.com/cbse/rs-aggarwal-class-" + str(i) + "-solutions/"
	urlRDShr = "https://byjus.com/rd-sharma-class-" + str(i) + "-solutions/"

	resNcert = requests.get(str(urlNcert))
	soupNcert = bs4.BeautifulSoup(resNcert.text, "html.parser")
	if (5 < i < 10) or (i == 12):
		classGradeLinkContainer = soupNcert.find("div", {"id":"primary"})
		gradePTagContainer = classGradeLinkContainer.findAll("p")
		classChapterLinkContainer = gradePTagContainer[3]
		classChapterLinkATagContainer = classChapterLinkContainer.findAll("a")
		gradeChapterLinks = []
		for links in classChapterLinkATagContainer:
			gradeChapterLinks.append(links['href'])
			print(links['href'])
	else:
		classGradeLinkContainer = soupNcert.find("div", {"id":"primary"})
		gradePTagContainer = classGradeLinkContainer.findAll("p")
		classChapterLinkContainer = gradePTagContainer[2]
		classChapterLinkATagContainer = classChapterLinkContainer.findAll("a")
		gradeChapterLinks = []
		for links in classChapterLinkATagContainer:
			gradeChapterLinks.append(links['href'])
			print(links['href'])

	'''for j in range(len(gradeChapterLinks)):
		resNeo = requests.get(str(gradeChapterLinks[j]))
		soupNeo = bs4.BeautifulSoup(resNeo.text, "html.parser")'''
	if 5 < i < 11:
		resRSAgg = requests.get(str(urlRSAgg))
		soupRSAgg = bs4.BeautifulSoup(resRSAgg.text, "html.parser")

		classGradeLinkContainer = soupRSAgg.find("table")
		gradeATagContainer = classGradeLinkContainer.findAll("a")
		gradeChapterLinks = []
		for links in gradeATagContainer:
			gradeChapterLinks.append(links['href'])
			print(links['href'])

	resRDShr = requests.get(str(urlRDShr))
	soupRDShr = bs4.BeautifulSoup(resRDShr.text, "html.parser")

	classGradeLinkContainer = soupRDShr.find("table")
	gradeATagContainer = classGradeLinkContainer.findAll("a")
	gradeChapterLinks = []
	for links in gradeATagContainer:
		gradeChapterLinks.append(links['href'])
		print(links['href'])



print(str(datetime.now() - startTime))
# the corner cases you would have to think are how to get rid of question and answer p tags completely(maybe use regex). 
# download src from img tags wherever possible, look for latex characters
# at the end delete all those lines that contains more that 5or6 commas
