
# Tổng quan về Pandas

## 1. Giới thiệu (Introduction)

  * **pandas** là một thư viện trong python hỗ trợ tốt trong việc thao tác dữ liệu. Thư viện này sử dụng một cấu trúc dữ liệu riêng là Dataframe.
  * Thông tin tổng quát trên [trang](https://pandas.pydata.org/about/index.html) của pandas.
  * Ưu điểm khi sử dụng của Pandas:
    * Có thể xử lý tập dữ liệu khác nhau về định dạng: chuỗi thời gian, bảng không đồng nhất, ma trận dữ liệu
    * Khả năng thao tác dữ liệu từ nhiều bộ nhớ và định dạng file: csv,text, excel, sql, database, hdf5
    * Liên kết dữ liệu thông minh, xử lý được trường hợp dữ liệu bị thiếu.
    * Tối ưu về hiệu năng


## 2.Cài đặt (Install):

- Cài đặt môi trường để làm việc, sau đó install thư viện pandas bằng câu lệnh:

     > $ pip install pandas

- Kiểm tra thư viện pandas trong môi trường:
     > $ conda list

![list.png](https://github.com/dtrungphong/Machine_Learning_TLU/blob/master/Learning/Document/Pandas/sup/imag/list.png)

## 3. Một số ví dụ về hàm trong pandas (Example of pandas functions):

    - Việc đầu tiên ta cần import thư viện vào dự án


```python
import pandas as pd
```

3.1. Đọc file dữ liệu
 - Tham khảo tham số của [hàm](https://bom.to/y06TnU/)
 - Lưu ý:
   - Đường dẫn file dữ liệu cần đọc
   - Về tham số
        
      * **_endcodeing_**: chỉ định encoding của file đọc vào. Mặc định là utf-8
      * **_sep_**: thay đổi dấu ngăn cách giữa các cột. Mặc định là dấu phẩy (‘,’)
      * **_header_**: chỉ định file đọc vào có header(tiêu đề của các cột) hay không. Mặc định là infer
      * **_index_col_**: chỉ định chỉ số cột nào là cột chỉ số(số thứ tự). Mặc định là None
      * **_nrows_** chỉ định số bản ghi sẽ đọc vào. Mặc định là None – đọc toàn bộ
     
     
 - Ví dụ đọc file csv:


```python
house_data_df = pd.read_csv('./sup/data/house_data.csv')
```

3.2. In ra bản dữ liệu của dataframe với n số lượng phần tử đầu tiên ta dùng hàm **.head()** ngược lại là hàm **.tail()**
 - Tham khảo tham số của hàm [head][head_] hoặc hàm [tail][tail_]
 - Ví dụ về sử dụng hàm head:
[head_]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html?highlight=pandas%20head#pandas.DataFrame.head
[tail_]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html?highlight=pandas%20tail#pandas.DataFrame.tail


```python
house_data_df.head(5)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1461</td>
      <td>20</td>
      <td>RH</td>
      <td>80.0</td>
      <td>11622</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>120</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1462</td>
      <td>20</td>
      <td>RL</td>
      <td>81.0</td>
      <td>14267</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Gar2</td>
      <td>12500</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1463</td>
      <td>60</td>
      <td>RL</td>
      <td>74.0</td>
      <td>13830</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1464</td>
      <td>60</td>
      <td>RL</td>
      <td>78.0</td>
      <td>9978</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1465</td>
      <td>120</td>
      <td>RL</td>
      <td>43.0</td>
      <td>5005</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>HLS</td>
      <td>AllPub</td>
      <td>...</td>
      <td>144</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 80 columns</p>
</div>



3.3. Lấy thông tin dữ liệu của dataframe với hàm **.info()** và xem kích thước dữ liệu với hàm **.shape**
 - Tham khảo về hàm [info][info_] hoặc hàm [shape][shape_]
 - Ví dụ về sử dụng hàm info:
[info_]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html?highlight=info#pandas.DataFrame.info
[shape_]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html?highlight=shape#pandas.DataFrame.shape


```python
house_data_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1459 entries, 0 to 1458
    Data columns (total 80 columns):
    Id               1459 non-null int64
    MSSubClass       1459 non-null int64
    MSZoning         1455 non-null object
    LotFrontage      1232 non-null float64
    LotArea          1459 non-null int64
    Street           1459 non-null object
    Alley            107 non-null object
    LotShape         1459 non-null object
    LandContour      1459 non-null object
    Utilities        1457 non-null object
    LotConfig        1459 non-null object
    LandSlope        1459 non-null object
    Neighborhood     1459 non-null object
    Condition1       1459 non-null object
    Condition2       1459 non-null object
    BldgType         1459 non-null object
    HouseStyle       1459 non-null object
    OverallQual      1459 non-null int64
    OverallCond      1459 non-null int64
    YearBuilt        1459 non-null int64
    YearRemodAdd     1459 non-null int64
    RoofStyle        1459 non-null object
    RoofMatl         1459 non-null object
    Exterior1st      1458 non-null object
    Exterior2nd      1458 non-null object
    MasVnrType       1443 non-null object
    MasVnrArea       1444 non-null float64
    ExterQual        1459 non-null object
    ExterCond        1459 non-null object
    Foundation       1459 non-null object
    BsmtQual         1415 non-null object
    BsmtCond         1414 non-null object
    BsmtExposure     1415 non-null object
    BsmtFinType1     1417 non-null object
    BsmtFinSF1       1458 non-null float64
    BsmtFinType2     1417 non-null object
    BsmtFinSF2       1458 non-null float64
    BsmtUnfSF        1458 non-null float64
    TotalBsmtSF      1458 non-null float64
    Heating          1459 non-null object
    HeatingQC        1459 non-null object
    CentralAir       1459 non-null object
    Electrical       1459 non-null object
    1stFlrSF         1459 non-null int64
    2ndFlrSF         1459 non-null int64
    LowQualFinSF     1459 non-null int64
    GrLivArea        1459 non-null int64
    BsmtFullBath     1457 non-null float64
    BsmtHalfBath     1457 non-null float64
    FullBath         1459 non-null int64
    HalfBath         1459 non-null int64
    BedroomAbvGr     1459 non-null int64
    KitchenAbvGr     1459 non-null int64
    KitchenQual      1458 non-null object
    TotRmsAbvGrd     1459 non-null int64
    Functional       1457 non-null object
    Fireplaces       1459 non-null int64
    FireplaceQu      729 non-null object
    GarageType       1383 non-null object
    GarageYrBlt      1381 non-null float64
    GarageFinish     1381 non-null object
    GarageCars       1458 non-null float64
    GarageArea       1458 non-null float64
    GarageQual       1381 non-null object
    GarageCond       1381 non-null object
    PavedDrive       1459 non-null object
    WoodDeckSF       1459 non-null int64
    OpenPorchSF      1459 non-null int64
    EnclosedPorch    1459 non-null int64
    3SsnPorch        1459 non-null int64
    ScreenPorch      1459 non-null int64
    PoolArea         1459 non-null int64
    PoolQC           3 non-null object
    Fence            290 non-null object
    MiscFeature      51 non-null object
    MiscVal          1459 non-null int64
    MoSold           1459 non-null int64
    YrSold           1459 non-null int64
    SaleType         1458 non-null object
    SaleCondition    1459 non-null object
    dtypes: float64(11), int64(26), object(43)
    memory usage: 912.0+ KB


 - Ví dụ về hàm shape:


```python
house_data_df.shape
```




    (1459, 80)



3.4. Lấy giá trị
 - Ta sẽ truyền vào thông tên các cột để lấy ra thông tin của các cột đó
 - Ví dụ về lấy ra thông tin của 5 hàng cuối với hai cột **Id** và **Street**:


```python
house_data_df[['Id','Street']].tail(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Street</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1454</th>
      <td>2915</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>2916</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>2917</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>2918</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>2919</td>
      <td>Pave</td>
    </tr>
  </tbody>
</table>
</div>



 - Lấy bản ghi có điều kiện ta sẽ tìm bản ghi phù hợp điều kiện của cột đó
 - Tham khảo hướng dẫn [tại đây][link_1]
 - Ví dụ về lấy bản ghi có điều kiện **Id** nằm trong đoạn từ 1500 đến 1510:
[link_1]: https://thispointer.com/python-pandas-select-rows-in-dataframe-by-conditions-on-multiple-columns/


```python
dt_df_fr_1500_1510 = house_data_df[(house_data_df['Id']>=1500) & (house_data_df['Id']<=1510)] 
dt_df_fr_1500_1510
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>...</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>1500</td>
      <td>160</td>
      <td>FV</td>
      <td>24.0</td>
      <td>2544</td>
      <td>Pave</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1501</td>
      <td>160</td>
      <td>FV</td>
      <td>NaN</td>
      <td>2980</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1502</td>
      <td>160</td>
      <td>FV</td>
      <td>NaN</td>
      <td>2403</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1503</td>
      <td>20</td>
      <td>FV</td>
      <td>57.0</td>
      <td>12853</td>
      <td>Pave</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>New</td>
      <td>Partial</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1504</td>
      <td>60</td>
      <td>FV</td>
      <td>68.0</td>
      <td>7379</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1505</td>
      <td>20</td>
      <td>FV</td>
      <td>80.0</td>
      <td>8000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1506</td>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>10456</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1507</td>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>10791</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>47</th>
      <td>1508</td>
      <td>50</td>
      <td>RL</td>
      <td>NaN</td>
      <td>18837</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1509</td>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>49</th>
      <td>1510</td>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
  </tbody>
</table>
<p>11 rows × 80 columns</p>
</div>



3.5. Thay đổi dữ liệu
 - Thêm cột mới có giá
   - Tham khảo [tại đây][link_1]
   - Ví dụ thêm cột mới có giá trị rỗng
[link_1]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html


```python
dt_df_fr_1500_1510 =  dt_df_fr_1500_1510[['Id','LotShape','Street']]
dt_df_fr_1500_1510
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>LotShape</th>
      <th>Street</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>1500</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1501</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1502</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1503</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1504</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1505</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1506</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1507</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>47</th>
      <td>1508</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1509</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>49</th>
      <td>1510</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
  </tbody>
</table>
</div>




```python
dt_df_fr_1500_1510['n_column'] = None
dt_df_fr_1500_1510
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>LotShape</th>
      <th>Street</th>
      <th>n_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>1500</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1501</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1502</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1503</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1504</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1505</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1506</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1507</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>47</th>
      <td>1508</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1509</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>49</th>
      <td>1510</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



 - Sửa giá trị tại cột
     - Ví dụ sửa giá trị tại cột **n_column** từ **Id** 1500 đến 1505


```python
dt_df_fr_1500_1505 = dt_df_fr_1500_1510[(dt_df_fr_1500_1510['Id']<=1505)]
dt_df_fr_1500_1505['n_column']= dt_df_fr_1500_1505['LotShape']=='Reg'
dt_df_fr_1500_1505
```

    /home/supercomputer-ailab/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>LotShape</th>
      <th>Street</th>
      <th>n_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>1500</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>True</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1501</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>True</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1502</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>False</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1503</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>False</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1504</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>False</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1505</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



 - Sắp xếp dữ liệu:
   - Tham khảo [tại đây][link_1]
   - Ví dụ về sắp xếp: 
[link_1]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html?highlight=sort_value


```python
sort_dt_df_fr_1500_1505 = dt_df_fr_1500_1505.sort_values('LotShape',ascending=True)
sort_dt_df_fr_1500_1505
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>LotShape</th>
      <th>Street</th>
      <th>n_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>41</th>
      <td>1502</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>False</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1503</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>False</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1504</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>False</td>
    </tr>
    <tr>
      <th>39</th>
      <td>1500</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>True</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1501</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>True</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1505</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



 - Nối hai dataframe với nhau:
   - Tham khảo [tại đây][link_1]
   - Ví dụ:
[link_1]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.append.html?highlight=append#pandas.DataFrame.append


```python
dt_df_fr_1480_1485 = house_data_df[(house_data_df['Id']>=1480) & (house_data_df['Id']<=1485)] 
dt_df_fr_1480_1485 = dt_df_fr_1480_1485[['Id','LotShape','Street']]
dt_df_fr_1480_1485
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>LotShape</th>
      <th>Street</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19</th>
      <td>1480</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1481</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1482</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1483</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1484</td>
      <td>Reg</td>
      <td>Pave</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1485</td>
      <td>IR1</td>
      <td>Pave</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_dt_df_ap = dt_df_fr_1480_1485.append(dt_df_fr_1500_1510, sort=False)
new_dt_df_ap
```




<div>
<style scoped>
 
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    
    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>LotShape</th>
      <th>Street</th>
      <th>n_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19</th>
      <td>1480</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1481</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1482</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1483</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1484</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1485</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39</th>
      <td>1500</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1501</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1502</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1503</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1504</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1505</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1506</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1507</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>47</th>
      <td>1508</td>
      <td>IR1</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1509</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
    <tr>
      <th>49</th>
      <td>1510</td>
      <td>Reg</td>
      <td>Pave</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



3.6. Lưu xuống file csv mới

 - Tham khảo [tại đây][link]
 - Ví dụ:
[link]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv


```python
new_dt_df_ap.to_csv('./sup/data/data_new')
```

![data_.png](https://github.com/dtrungphong/Machine_Learning_TLU/blob/master/Learning/Document/Pandas/sup/imag/data_.png)

## 4. Nguồn tham khảo (Reference source):

1. Hướng dẫn về sử dụng pandas tiếng Việt [link1][1_] | [link2][2_].
2. [Trang Chủ][3_] pandas.
3. Các bạn có thể yêu cầu chỉnh sửa hoặc đóng góp thêm cho bài làm hoàn thiện hơn qua: dtphong010199@gmail.com
[3_]: https://pandas.pydata.org/
[1_]: https://labs.septeni-technology.jp/category/pandas/
[2_]: https://nguyenvanhieu.vn/thu-vien-pandas-python/
