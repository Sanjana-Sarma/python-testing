import PyPDF2
import aspose.words as aw
import os
myfile=open("C:/Users/angel/OneDrive/Desktop/python trial/testing1/trial5.pdf","rb")
opfile=open("example.txt","w")
pdffileobj=PyPDF2.PdfFileReader(myfile)
numofpages=pdffileobj.numPages
for num in range(numofpages):
	page1=pdffileobj.getPage(num)
	text=page1.extractText()
	opfile.write(text)
opfile.close()
myfile.close()
newfile=open("example.txt","r")
lines=newfile.readlines()
c=len(lines)
print("No. of lines : {}".format(c))
val=0
for i in range(c):
	if val<c:
		pass
	else:
		break
	for j in range(i+1):
		file=open("ex"+str(i)+".txt","a")
		file.writelines(lines[val])
		val+=1
	file.close()
	if os.path.getsize("C:/Users/angel/OneDrive/Desktop/python trial/testing1/ex"+str(i)+".txt")==0:
		break
	imagefile=aw.Document("C:/Users/angel/OneDrive/Desktop/python trial/testing1/ex"+str(i)+".txt")
	count=imagefile.page_count
	for page in range(0,count):
		extpg=imagefile.extract_pages(page,1)
		extpg.save(f"image"+str(i)+".jpeg")
	os.remove("C:/Users/angel/OneDrive/Desktop/python trial/testing1/ex"+str(i)+".txt")
newfile.close()
		