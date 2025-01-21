import pandas as pd
import requests 

def extract():
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,region,currencies")
    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data)
        return df
    
def transform(df):
    name_common = [x for x in df.columns if x.endswith(".common")]
    currencies = [x for x in df.columns if x.startswith("currencies.") and x.endswith(".symbol")] 
    # other method of listing
    # for currency in df.columns:
    #     if currency.startswith("currencies."):
    #         currencies.append(currency)
    # print(currencies)
    df["common_native_name"] = df[name_common].apply(lambda x: ", ".join(x.dropna()), axis = 1) 
    df["currencies"] = df[currencies].apply(lambda x: ",".join(x.dropna()), axis = 1)
    df = df[["name.common", "name.official", "name.nativeName.eng.common","common_native_name","region","currencies"]]
    print(df[["name.nativeName.eng.common","common_native_name", "region", "currencies"]].head(10))
# df.to_csv("countrytest.csv", index = False)
# df = pd.read_csv("countrytest.csv")
# print(df["name.common"].head())

if __name__ == "__main__":
    data = extract()
    transform(data)
    
    