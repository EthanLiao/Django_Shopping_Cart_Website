# --coding:UTF-8 --
from shop.models import Navbar,Category,Product
from os import listdir
from os.path import isfile,join,abspath,dirname,basename
import os
import csv
import codecs
from django.core.files.images import ImageFile
from django.core.files import File
non_url_safe = ['"', '#', '$', '%', '&', '+',
                ',', '/', ':', ';', '=', '?',
                '@', '[', '\\', ']', '^', '`',
                '{', '|', '}', '~', "'",' ']

mypath = "/home/ethan/Desktop/django-shop-tutorial _modifcation_2/media/植物照片"

'''
Create Csv file for uploading data
'''

def getPrevDir(path):
    return basename(dirname(path))

def getNavName(path):
    characters = path.split("/")
    return characters[-3]

def writeCsvFiles(path=mypath):
    file_dict_list = []
    with open('list.csv','w') as writeFile:
        fieldnames = ['navbar','category','name','directory','kilometers','price','stock','available']
        writer= csv.DictWriter(writeFile,fieldnames=fieldnames)
        for dirPath,dirNames,fileNames in os.walk(path):
            for f in fileNames:
                file_dict = {}
                file_dict['navbar'] = getNavName(join(dirPath,f))
                file_dict['category'] = getPrevDir(join(dirPath,f))
                file_dict['name'] = f.replace('.jpg','')
                file_dict['directory'] = join(dirPath,f)
                file_dict['kilometers'] = 0
                file_dict['price'] = 0
                file_dict['stock'] = 0
                file_dict['available'] = 0
                file_dict_list.append(file_dict)
        writer.writeheader()
        for f in file_dict_list:
            writer.writerow(f)
    writeFile.close()

'''
Uploading data
'''
def UpLoadDataFromCsv(path=mypath):
    writeCsvFiles(path)
    with open('list.csv','rb') as csvfile:
        rows = csv.DictReader(x.replace('','') for x in csvfile)
        for row in rows:
            try :
                Navbar.objects.get(name=row['navbar'])
                try :
                    category=Category.objects.get(name=row['category'])
                    try :
                        Product.objects.get(name=row['name'])
                        continue
                    except Product.DoesNotExist:
                        product = Product(category=category,name=row['name'],kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                        name = row['name']
                        dir = row['directory']
                        product.image = ImageFile(open(dir, 'rb'))
                        product.save()
                        #product.image.save(File(open(dir,'rb')))
                        #product.image.save(name,File(open(dir,'r')))
                        #image = ImageFile(open("".join(row['directory']),"r"))
                        #product = Product(category=category,name=row['name'],image=image,kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                        #product = Product(category=category,name=row['name'],kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                        #product.image = ImageFile(open("".join(row['directory']),"r"))
                        #product.image = "products/".join(row['directory'])
                        #product.save()
                except Category.DoesNotExist:
                    category=Category(navbar=nav,name=row['category'])
                    category.save()
                    product = Product(category=category,name=row['name'],kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                    name = row['name']
                    dir = row['directory']
                    product.image.save(name,File(open(dir,'rb')))
                    #product.image.save(row['name'].join('.jpg'),File(open(row['directory'],'r')))
                    #product = Product(category=category,name=row['name'],kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                    #product.image = ImageFile(open("".join(row['directory']),"r"))
                    #product.image = "products/".join(row['directory'])
                    #product.save()
            except Navbar.DoesNotExist:
                nav=Navbar(name=row['navbar'])
                nav.save()
                #createProduct(nav,row['category'])
                category=Category(navbar=nav,name=row['category'])
                category.save()
                name = row['name']
                dir = row['directory']
                product = Product(category=category,name=row['name'],kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                product.image.save(name,File(open(dir,'rb')))
                #product.image.save(row['name'].join('.jpg'),File(open(row['directory'],'r')))
                #product = Product(category=category,name=row['name'],kilometers=row['kilometers'],price=row['price'],stock=['stock'],available=row['available'])
                #product.image = ImageFile(open("".join(row['directory']),"r"))
                #product.image = "products/".join(row['directory'])
                #product.save()
    csvfile.close()


'''
Reference Fuction
'''
def slugify(originString):
    non_safe = [c for c in originString if c in non_url_safe] #catch the unsafe chateristic word in the string
    if non_safe:
        for c in non_safe:
            originString = originString.replace(c,'-') # eliminate the unsafe chateristic word in the string
    return originString

def createNav(add_name):
    name  = add_name
    slug = slugify(add_name)
    new_nav = Navbar(name=name,slug=slug)
    new_nav.save()
