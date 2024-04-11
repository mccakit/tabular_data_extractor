from data_conversion import pdf_to_csv,extract_year
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os
import numpy as np


#uncomment when new file is added
# pdf_to_csv()

directory = "./Turkey Car Sales Table Data"
manufacturer = ["RENAULT","TOYOTA"]
def find_sales_data(manufacturer):
    sales_list = []
    for filename in os.listdir(directory):
        df = pd.read_csv(f"{directory}/{filename}")
        for index, value in df["MARKA"].items():
            if value == manufacturer:
                fixed_sales = int(str(df.loc[index,"SATIŞ"]).replace(".",""))
                sales_list.append({"year":extract_year(filename),"sales":fixed_sales})
    return sales_list


fig, axs = plt.subplots(2, 1,figsize=(16,10))
plt.subplots_adjust(hspace=0.5)

renault_df=pd.DataFrame(find_sales_data("RENAULT"))

axs[0].plot(renault_df["year"], renault_df["sales"], color="black")
axs[0].set_xlabel("Yıl")
axs[0].set_ylabel("Satışlar")
axs[0].set_title("Renault")
axs[0].axvline(x="2006", color='r', linestyle='--',label="Yurt İçi Fabrika Açılması")
axs[0].legend(loc='lower right')
axs[0].set_ylim(0)


toyota_df=pd.DataFrame(find_sales_data("TOYOTA"))

axs[1].plot(toyota_df["year"], toyota_df["sales"], color="black")
axs[1].set_xlabel("Yıl")
axs[1].set_ylabel("Satışlar")
axs[1].set_title("Toyota")
axs[1].axvline(x="2006", color='b', linestyle='--',label ="Yurt Dışı Fabrika Açılması")
axs[1].legend(loc='lower right')
axs[1].set_ylim(0)


plt.suptitle("Yurtiçinde ve Yurtdışında Açılan Araba Fabrikalarının Ülke İçi Perakende Satışlara Etkisinin İncelenmesi")
plt.show()