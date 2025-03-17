import requests
import pandas as pd
import matplotlib.pyplot as plt 
from sqlalchemy import create_engine
from config import DB_USERNAME, DB_PASSWORD, DB_NAME

print(DB_USERNAME, DB_PASSWORD, DB_NAME)




def language_field(data):
    lang = []
    for key, value in data.items():
            lang.append(value)
    return lang
            
    
def currency_field(data):
    for key, value in data.items():
        for k, v in value.items():
            return key   
    
def extract_field(data, field):
    for key, value in data.items(): # {"eng": {"official":"Malta of Ireland,"common": "malta"}} => eng, {"official":"Malta of Ireland,"common": "malta"}
        for k, v in value.items(): # {"official":"Malta of Ireland,"common": "malta"} =>official, malta ofire, common, malta
            if k == field: 
                return v 

#  Request service to get data from REST API
response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,unMember,region,subregion,continents,area,population,languages,startOfWeek,currencies,independent,idd")
if response.status_code == 200:
    data = response.json()
        
    extracted_data = []
    
    for country in data: 
        country_name = (country['name']['common'])
        official_country_name = country['name']['official']
        common_nativename = extract_field(country['name']['nativeName'], 'common')
        currency_code = currency_field(country['currencies'])
        currency_name = extract_field(country['currencies'], 'name')
        currency_symbol = extract_field(country['currencies'], 'symbol')
        capital = ' '.join(country['capital'])
        united_nation_member = country['unMember']
        region = country['region']
        sub_region = country['subregion']
        Continents = ' '.join(country['continents'])
        independence = country.get('independent')
        area = country['area']
        population = country['population']
        start_of_week = country['startOfWeek']
        languages =','.join(language_field(country['languages']))
        #bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
        country_code = country['idd']['root'] + ' '.join(country['idd']['suffixes'])
        #country_idd = ' '.join(country['idd']['suffixes'])
        extracted_data.append({'countryname':country_name,
                              'official country name': official_country_name,
                              'startofWeek': start_of_week,
                              'independence': independence,
                              'capital': capital,
                              'common native name': common_nativename,
                              'united nation member': united_nation_member,
                              'region': region,
                              'sub region': sub_region,
                              'continents': Continents,
                              'area': area,
                              'currencycode': currency_code,
                              'currencyname': currency_name,
                              'currencysymbol': currency_symbol,
                              'population': population,
                              'languages': languages,
                              'countrycode': country_code,
                              
                                                         
                              })
        df1 = pd.DataFrame(extracted_data)
print(df1)


# cmissingvalue = pd.isnull(df1["sub region"])
# print(cmissingvalue)
#Data visualization
df1['frenchspeaking_countries'] = df1['languages'].apply(lambda x: 'French' in x)
df1['englishspeaking_countries'] = df1['languages'].apply(lambda x: 'English' in x)
df1['speaks_morethan_1_lang'] = df1['languages'].apply(lambda x: 'morethan_1_lang' if isinstance(x, str) and len(x.split(',')) > 1 else '1_language')
df2 = df1[['frenchspeaking_countries', 'englishspeaking_countries', 'speaks_morethan_1_lang']]
    

   
true_count = df1['frenchspeaking_countries'].sum()  # Counts the number of True values for French speaking countries
true1_count = df1['englishspeaking_countries'].sum()  # Counts the number of True values for English speaking countries
trueE_count = df1[df1['languages'].str.contains('English')].value_counts()  # Counts the number of True values for English speaking countries
lang_count = df1['speaks_morethan_1_lang'].value_counts()
#lang1_count = df1[df1['speaks_morethan_1_lang']==('morethan_1_lang')].value_counts
#country_lang_count = lang1_count()[languages].apply (lambda x: len(x.split(',')))
df1['language_count'] = df1['languages'].apply(lambda x: len(x.split(',')))
filtered_df = df1[df1['language_count'] > 1]

# print(true_count)
# print(true1_count)
#false_count = (~df1['languages']).sum()  # Counts the number of False values (optional)
#ml = df1[df1['speaks_morethan_1_lang'].str.contains('morethan_1_lang')] #filters for more than one lang
#country_count = ml['countryname'] #.value_counts()  #counts country with more than one lang
top_5_countries_with_lowest_area =df1.sort_values(['area'], ascending= True) #sort df1 by area in ascending order
top_5_countries_with_largest_area =df1.sort_values(['area'], ascending= False) #sort df1 by area in descending order
#largest_population_Africa = df1[df1['continents'].str.contains('Africa')].sort_values('population' , ascending=True)
largest_population_Africa = df1[df1['continents']==('Africa')].sort_values('population' , ascending=False)
lowest_population_Africa = df1[df1['continents']==('Africa')].sort_values('population' , ascending=True)
#african_population =df1[df1['continents'].str.contains('Africa')] #another option to code largest Afr. population 
#largest_africa_population =african_population.sort_values('population', ascending=True) #using 2 lines of code

#print(lang1_count)

# Number of French and English speaking
fig, ax = plt.subplots()
try:
    Eng_count = true1_count
    French_count =true_count
    ax.bar(['French', 'English'], [true_count, true1_count], color=['r', 'b'])
    ax.bar(['English'], [true1_count], color='b')
    ax.set_xticklabels(['French', 'English'], rotation = 90)
    ax.set_xticks([0, 1])
    ax.set_title('Number of French and English speaking')
    ax.set_xlabel('language spoken')
    ax.set_ylabel('number of countries ')
    plt.show()
except KeyError as err:
    print("error:{}".format(err))
#plt.show(['more])

# Number of English speaking
fig, ax = plt.subplots()
try:
    
    ax.bar('English',trueE_count, color='r')
    ax.set_xticklabels(['English'], rotation = 90)
    ax.set_title('English speaking')
    ax.set_xlabel('language spoken')
    ax.set_ylabel('number of countries ')
    plt.show()
except KeyError as err:
    print("error:{}".format(err))

   
    
    # Countries with more than one language
try:    
    fig, ax = plt.subplots()
    ax.bar(filtered_df['countryname'].head(30), filtered_df['language_count'].head(30), color='skyblue')
    ax.set_xticklabels(filtered_df['countryname'], rotation= 90)
    #ax.set_xticks([0, 1])
    ax.set_title(' Top 30 Countries speaking more  than one language')
    ax.set_xlabel('country')
    ax.set_ylabel('number of languages')
    fig.tight_layout()
    plt.show()
except KeyError as err:
    print(err)
       


#Lowest population by country in Africa
try:    
    fig, ax = plt.subplots()
    ax.bar(lowest_population_Africa ['countryname'].head(5), lowest_population_Africa ['population'].head(5), color='b')
    ax.set_xticklabels(lowest_population_Africa ['countryname'], rotation= 90)
    #ax.set_xticks([0, 1])
    ax.set_title('Top 5 African countries with lowest Population')
    ax.set_xlabel('country')
    ax.set_ylabel('Population')
    fig.tight_layout()
    plt.show()
except KeyError as err:
    print(err)
    
#Largest population by country in Africa
try:    
    fig, ax = plt.subplots()
    ax.bar(largest_population_Africa ['countryname'].head(5), largest_population_Africa ['population'].head(5), color='b')
    ax.set_xticklabels(largest_population_Africa ['countryname'], rotation= 90)
    #ax.set_xticks([0, 1])
    ax.set_title('Top 5 African countries with largest Population')
    ax.set_xlabel('country')
    ax.set_ylabel('Population')
    fig.tight_layout()
    plt.show()
except KeyError as err:
    print(err) 
    
    
    
#Largest Area by country
try:    
    fig, ax = plt.subplots()
    ax.bar(top_5_countries_with_largest_area['countryname'].head(5), top_5_countries_with_largest_area['area'].head(5), color='b')
    ax.set_xticklabels(top_5_countries_with_largest_area['countryname'], rotation= 90)
    #ax.set_xticks([0, 1])
    ax.set_title('Top 5 countries with Largest Area')
    ax.set_xlabel('country')
    ax.set_ylabel('Area')
    fig.tight_layout()
    plt.show()
except KeyError as err:
    print(err)
    
# Top 5 African countries with lowest Area
try:    
    fig, ax = plt.subplots()
    ax.bar(top_5_countries_with_lowest_area['countryname'].head(5), top_5_countries_with_lowest_area['area'].head(5), color='b')
    ax.set_xticklabels(top_5_countries_with_lowest_area['countryname'], rotation= 90)
    #ax.set_xticks([0, 1])
    ax.set_title('Top 5 countries with Lowest Area')
    ax.set_xlabel('country')
    ax.set_ylabel('Area')
    fig.tight_layout()
    plt.show()
except KeyError as err:
    print(err)

# Azure SQL Server connection string
connection_string = (
    'mssql+pyodbc://DB_USERNAME:DB_PASSWORD@ofgemsample.database.windows.net/DB_NAME''?driver=ODBC+Driver+18+for+SQL+Server'
)

# Create SQLAlchemy engine to connect to Azure SQL Server
engine = create_engine(connection_string)

# Load the DataFrame to SQL Server, into a table called 'countries'
df1.to_sql('countries', con=engine, if_exists='replace', index=False)

# 'if_exists' options:
# 'fail' -> Do nothing if table exists
# 'replace' -> Drop the existing table and create a new one
# 'append' -> Append data to an existing table

                    
        


  





