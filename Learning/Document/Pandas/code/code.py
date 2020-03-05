
import pandas as pd


# 3.1. Đọc file dữ liệu

house_data_df = pd.read_csv('./sup/data/house_data.csv')


# 3.2. In ra bản dữ liệu của dataframe với n số lượng phần tử đầu tiên ta dùng hàm **.head()** ngược lại là hàm **.tail()**


house_data_df.head(5)


# 3.3. Lấy thông tin dữ liệu của dataframe với hàm **.info()** và xem kích thước dữ liệu với hàm **.shape**

house_data_df.info()


#  - Ví dụ về hàm shape:


house_data_df.shape


# 3.4. Lấy giá trị

# In[16]:


house_data_df[['Id','Street']].tail(5)




dt_df_fr_1500_1510 = house_data_df[(house_data_df['Id']>=1500) & (house_data_df['Id']<=1510)] 
dt_df_fr_1500_1510


# 3.5. Thay đổi dữ liệu
#  - Thêm cột mới có giá



dt_df_fr_1500_1510 =  dt_df_fr_1500_1510[['Id','LotShape','Street']]
dt_df_fr_1500_1510


dt_df_fr_1500_1510['n_column'] = None
dt_df_fr_1500_1510


#  - Sửa giá trị tại cột

dt_df_fr_1500_1505 = dt_df_fr_1500_1510[(dt_df_fr_1500_1510['Id']<=1505)]
dt_df_fr_1500_1505['n_column']= dt_df_fr_1500_1505['LotShape']=='Reg'
dt_df_fr_1500_1505


#  - Sắp xếp dữ liệu:

sort_dt_df_fr_1500_1505 = dt_df_fr_1500_1505.sort_values('LotShape',ascending=True)
sort_dt_df_fr_1500_1505


#  - Nối hai dataframe với nhau:

dt_df_fr_1480_1485 = house_data_df[(house_data_df['Id']>=1480) & (house_data_df['Id']<=1485)] 
dt_df_fr_1480_1485 = dt_df_fr_1480_1485[['Id','LotShape','Street']]
dt_df_fr_1480_1485


new_dt_df_ap = dt_df_fr_1480_1485.append(dt_df_fr_1500_1510, sort=False)
new_dt_df_ap


# 3.6. Lưu xuống file csv mới


new_dt_df_ap.to_csv('./sup/data/data_new')

