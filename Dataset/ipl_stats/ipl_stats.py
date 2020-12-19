import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

def team_name(team_no):
    if(team_no == '1'):
        return 'CSK'
    if(team_no == '2'):
        return 'DEC'
    if(team_no == '3'):
        return 'DC'
    if(team_no == '4'):
        return 'KXIP'
    if(team_no == '5'):
        return 'KKR'
    if(team_no == '6'):
        return 'MI'
    if(team_no == '7'):
        return 'PWI'
    if(team_no == '8'):
        return 'RR'
    if(team_no == '9'):
        return 'RCB'
    if(team_no == '10'):
        return 'KTK'
    if(team_no == '62'):
        return 'SRH'
    if(team_no == '434'):
        return 'RPS'
    if(team_no == '433'):
        return 'GL'
        
arr_year = ['08','09']
for i in range(10,20):
    arr_year.append(str(i))

for year in arr_year:
    print(year)
    url = "https://www.iplt20.com/stats/20"+year+"/player-points"
    r = requests.get(url)

    csv_file = open('ipl-stats-'+year+'_try.csv','w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['pos','name','team_no','team_name','pts','mat','wkts','dots','4s','6s','catches','stumpings'])

    soup = BeautifulSoup(r.content,'html5lib')

    i = 1
    for player in soup.find_all('tr', class_ = 'js-row'):
        name = player.find('a', class_='top-players__player-link')
        if(name == None):
            name = player.find('div', class_='top-players__player-name')
        name = name.text
        points = player.find('td', class_='top-players__pts').text
        mat = player.find('td', class_='top-players__m').text
        wkts = player.find('td', class_='top-players__w').text
        dots = player.find('td', class_='top-players__d').text
        fours = player.find('td', class_='top-players__4s').text
        sixes = player.find('td', class_='top-players__6s').text
        catches = player.find('td', class_='top-players__c').text
        stumps = player.find('td', class_='top-players__s').text
        team_no = player.get('data-team-id')
        team = team_name(team_no)

        # print(i, name, points, mat, wkts, dots, fours, sixes, catches, sixes)
        csv_writer.writerow([i, name, team_no, team, points, mat, wkts, dots, fours, sixes, catches, sixes])
        i+=1

    csv_file.close()


    csv_file = open('ipl-stats-'+year+'.csv','w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['pos','name','team_no','team_name','pts','mat','wkts','dots','4s','6s','catches','stumpings'])

    data = pd.read_csv('ipl-stats-'+year+'_try.csv')
    # data = pd.DataFrame(data)

    data = data.to_dict()

    key = 'name'
    for i in range(len(data[key])):
        data[key][i] = str(data[key][i])
        data[key][i] = data[key][i].replace('\n',' ')
        data[key][i] = data[key][i].replace('                            ','')
        data[key][i] = data[key][i].replace('      ','')

    data = pd.DataFrame(data)

    for i in range(len(data[key])):
        temp = data[key][i]
        temp = temp[1:]
        # print(temp)
        csv_writer.writerow([data['pos'][i], temp, data['team_no'][i],data['team_name'][i],data['pts'][i],data['mat'][i],data['wkts'][i],data['dots'][i],data['4s'][i],data['6s'][i],data['catches'][i],data['stumpings'][i]])

    csv_file.close()
    os.remove('ipl-stats-'+year+'_try.csv')
