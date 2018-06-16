import requests, time

s = requests.session()

mainFile = open("all_sites.txt",'r')
allSites = mainFile.readlines()
mainFile.close()

print('\n################################')
print('##  Shopify Endpoint Checker  ##')
print('##      Written By @tfich     ##')
print('################################\n')

if len(allSites) != 0:
    sleepTime = input('Sleep Time between Requests (1-2 is fine): ')
else:
    print('\nPlease load at least 1 site into all_sites.txt\n')
    quit()

print('\n{} Sites Loaded Up\n'.format(len(allSites)))

for links in allSites:
    link1 = links.replace('\n','')
    if link1.endswith('/'):
        link = link1 + 'products.json'
    else:
        link = link1 + '/products.json'
    try:
        request = s.get(link)
        outfile = open("json_sites.txt","a+")
        outfile.write(link1 + '\n')
        print('[Checked] - {} - /products.json'.format(link1))
    except Exception:
        outfile = open("xml_sites.txt","a+")
        outfile.write(link1 + '\n')
        print('[Checked] - {} - /sitemap_products_1.xml'.format(link1))
        continue
    time.sleep(sleepTime)

jsonNum = len(open('json_sites.txt','r').readlines())
xmlNum = len(open('xml_sites.txt','r').readlines())

print('\n---Completed---')
print('Number of /product.json sites: {}'.format(jsonNum))
print('Number of /sitemap_products_1.xml sites: {}'.format(xmlNum))
print('---------------\n')
