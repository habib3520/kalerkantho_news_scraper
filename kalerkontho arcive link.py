import bs4
import requests
import csv


url = "https://www.kalerkantho.com/print-edition/2022/09/20"

data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')

#print(soup.prettify())

# for para in soup.find_all('a'):
#     print(para.text)
#a= soup.find_all("div",{"class":"col-xs-12 col-sm-6 col-md-6 n_row"})

divs = soup.find("div",{"class":"col-sm-8 cat_home"})



#divs = soup.find("div",{"class":"col-xs-12 col-md-8 print_edition_left"})

#print(divs)

# for i in divs.find_all("a"):
#     j=i.get('href')
#     if j[0:2] == "./":
#         print("https://www.kalerkantho.com" + j[1:len(j)])



with open('habib.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    #writer.writerow(['news link'])  # output header row as first line
    for i in divs.find_all("a"):
        j = i.get('href')
        # print(j[1:len(j)])
        # writer.writerow(j[1:len(j)])
        print(j[0:len(j)])
        writer.writerow([j[0:len(j)]])

# def write_csv(list_to_be_inserted):
#     with open('s_test.csv', mode='w', newline='',encoding='utf-8') as unit_url_list:
#         unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#         # for i in divs.find_all("a"):
#         #     j = i.get('href')
#         #     # print(j[1:len(j)])
#         #     # writer.writerow(j[1:len(j)])
#         #     print(j[0:len(j)])
#         #     unit_url_writer.writerow([j[0:len(j)]])
#
#         for url in list_to_be_inserted:
#             print(url)
#             if url!="#recent-view":
#                unit_url_writer.writerow(url)
#
#     unit_url_list.close()
#
#     pass


# total = 0
# for sum in j:
#     total  += sum
#
#     print(total)

    #print(j)

# for links in divs:
#     links.find("a")
#     link = links.get('href')
#     if link[0:2] == "./" and link != "#":
#         print("https://www.kalerkantho.com" + link[1:len(link)])

# for links in soup.find("a"):
#     link = links.get('href')
#     if link[0:2]== "./" and link!="#":
#         print("https://www.kalerkantho.com"+ link[1:len(link)])