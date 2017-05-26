import pandas
google_data = pandas.read_csv("data/GOOGL.csv")
row_num = 0
# for index, row in google_data.iterrows():
#     row_num+=1

data_size = google_data["Date"].count()

for i in range(data_size):
    