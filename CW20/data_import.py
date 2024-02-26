import pandas as pd

import HW19


#client_s = pd.read_excel("./data_import.xlsx", skiprows=1, sheet_name="List_client")
df_clients = pd.DataFrame({"name": ["Antony", "Tomy", "Anna"],
 "age": [25, 32, 22],
 "money": [10000, 100000, 5000],
 "my_home": ["Yes", "No", "No"]})
df_clients.to_excel(r"D:\NewHardSkills\Pycharm\HW\CW20\data_import.xlsx")
print(df_clients)
