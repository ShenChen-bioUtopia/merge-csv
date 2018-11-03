
import os
import csv

os.chdir(os.getcwd()+"\\test")
names = os.listdir()

#获得所有的accession号
all_accession=[]
a=-1
for i in names:
    a+=1
    with open(i,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader,"over")
        next(reader,"over")
        locals()["accession_"+str(a)] = [row[2] for row in reader]
        for accession in locals()["accession_"+str(a)]:
            if accession in all_accession:
                pass
            if accession not in all_accession:
                all_accession.append(accession)
#写入文件
with open("all_des.csv","w",newline='') as a:
    writer = csv.writer(a)
    for val in all_accession:
        writer.writerow([val])
    
    
#将PI号和表型value提取到一个字典中
for m in names:
    locals()[str(m)] = [m]
    with open(m,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader,"over")
        next(reader,"over")
        descriptor_value =  [row[4] for row in reader][1:]
        #print(descriptor_value)
    with open(m,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader,"over")
        next(reader,"over")
        descriptor_accession =  [row[2] for row in reader][1:]
        #print(descriptor_accession)
        descriptor = dict(zip(descriptor_accession,descriptor_value))
        #print(descriptor)

#找每个PI值对应的value
        for k in all_accession:
            if k in descriptor_accession:
                locals()[str(m)].append(descriptor[k])
            if k not in descriptor_accession:
                locals()[str(m)].append("NA")
        #print(locals()[str(m)])

#写入文件(在csv后面写入一列）
    with open("all_des.csv",'r+',newline='') as a:
        rows= csv.reader(a)
        writer = csv.writer(a)
        n = 0
        for row in rows:
            row.append(locals()[str(m)][n])
            #print(row)
            n += 1
            
            writer.writerow(row)