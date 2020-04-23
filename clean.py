import os
from shutil import copyfile
import pandas as pd

common_list=[]
xml_common_list=[]

image_directory=os.listdir("/home/chandy/rumex_new/RumexClassification/annotation/")

# print(image_directory)

try:
	for i in range(len(image_directory)):
		xml_name=image_directory[i]
		name= image_directory[i]
		name= name[:-4]

		name = name+'.jpg'
		# print(name)
		common_list.append(name)
		xml_common_list.append(xml_name)

		copyfile('/home/chandy/rumex_new/RumexClassification/images/'+name, '/home/chandy/rumex_new/RumexClassification/images_new/'+name)
		# name= name[:-4]
		# name = name+'.xml'
		# os.remove('/home/chandy/RumexClassification/annota/'+name)





except:
	print(name)
	pass


# d={'common_name':common_list}
# d_xml={'common_name':xml_common_list}
# df=pd.DataFrame(data=d)
# df_xml=pd.DataFrame(data=d_xml)
# df.to_csv('common_list.csv')
# df_xml.to_csv("xml_common_list.csv")

# try:

# except:
# 	pass

