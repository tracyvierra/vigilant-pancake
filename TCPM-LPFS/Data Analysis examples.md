```python
data = {'Name':['John','Tim','Rob'],
       'Age':[34,23,42],
        'Salary':[42000,32000,62000]
       }
```


```python
from pandas import DataFrame
frame = DataFrame(data)
```


```python
frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame = DataFrame(data, columns=['Name','Salary','Age'])
```


```python
new_frame
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
      <th>Name</th>
      <th>Salary</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>42000</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>32000</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>62000</td>
      <td>42</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame = DataFrame(data, columns=['Name','Salary','Age','Profile'])
```


```python
new_frame
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
      <th>Name</th>
      <th>Salary</th>
      <th>Age</th>
      <th>Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>42000</td>
      <td>34</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>32000</td>
      <td>23</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>62000</td>
      <td>42</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame['Salary']
```




    0    42000
    1    32000
    2    62000
    Name: Salary, dtype: int64




```python
new_frame.iloc[1]
```




    Name         Tim
    Salary     32000
    Age           23
    Profile      NaN
    Name: 1, dtype: object




```python
new_frame['Profile']='Doctor'
new_frame
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
      <th>Name</th>
      <th>Salary</th>
      <th>Age</th>
      <th>Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>42000</td>
      <td>34</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>32000</td>
      <td>23</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>62000</td>
      <td>42</td>
      <td>Doctor</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame = DataFrame(data, columns=['Name','Age','Salary','Profile'])
new_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame['Profile']='Doctor'
new_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Profile</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
      <td>Doctor</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame['Education']='Masters Degree'
new_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Profile</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
      <td>Doctor</td>
      <td>Masters Degree</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
      <td>Doctor</td>
      <td>Masters Degree</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
      <td>Doctor</td>
      <td>Masters Degree</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame['Education']='Ph.D'
new_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Profile</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
      <td>Doctor</td>
      <td>Ph.D</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
      <td>Doctor</td>
      <td>Ph.D</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
      <td>Doctor</td>
      <td>Ph.D</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame.iloc[1]
```




    Name            Tim
    Age              23
    Salary        32000
    Profile      Doctor
    Education      Ph.D
    Name: 1, dtype: object




```python
new_frame = new_frame.T
```


```python
new_frame
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Name</th>
      <td>John</td>
      <td>Tim</td>
      <td>Rob</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>34</td>
      <td>23</td>
      <td>42</td>
    </tr>
    <tr>
      <th>Salary</th>
      <td>42000</td>
      <td>32000</td>
      <td>62000</td>
    </tr>
    <tr>
      <th>Profile</th>
      <td>Doctor</td>
      <td>Doctor</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>Education</th>
      <td>Ph.D</td>
      <td>Ph.D</td>
      <td>Ph.D</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_frame = new_frame.T
```


```python
new_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Profile</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
      <td>Doctor</td>
      <td>Ph.D</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
      <td>Doctor</td>
      <td>Ph.D</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
      <td>Doctor</td>
      <td>Ph.D</td>
    </tr>
  </tbody>
</table>
</div>




```python
from pandas import Series
obj = Series([100,200,300,400,500], index=['d','a','b','e','c'])
obj
```




    d    100
    a    200
    b    300
    e    400
    c    500
    dtype: int64




```python
obj = obj.reindex(['a','b','c','d','e'])
obj
```




    a    200
    b    300
    c    500
    d    100
    e    400
    dtype: int64




```python
data = {'Name':['John','Tim','Rob'],
       'Age':[34,23,42],
        'Salary':[42000,32000,62000]
       }
frame = DataFrame(data)
frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
  </tbody>
</table>
</div>




```python
test_frame = frame.reindex([0,2,1])
test_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
  </tbody>
</table>
</div>




```python
fields = ['Age','Name','Salary']
hold_frame = test_frame.reindex(columns=fields)
hold_frame

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
      <th>Age</th>
      <th>Name</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>John</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>42</td>
      <td>Rob</td>
      <td>62000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>Tim</td>
      <td>32000</td>
    </tr>
  </tbody>
</table>
</div>




```python
fields = ['Name','Age','Salary']
hold_frame = hold_frame.reindex(columns=fields)
hold_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
  </tbody>
</table>
</div>




```python
hold = frame.reindex([0,1,2])
hold
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
  </tbody>
</table>
</div>




```python
hold_frame = hold_frame.reindex([0,1,2])
hold_frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = hold_frame.drop([2])
frame2
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame
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
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
      <td>42000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
      <td>32000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
      <td>62000</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame4 = frame.drop('Salary', axis=1)
frame4

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
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tim</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rob</td>
      <td>42</td>
    </tr>
  </tbody>
</table>
</div>




```python
from pandas import Series
series1 = Series([1,2,3,4,5])
series2 = Series([100,200,300,400,500,600])
series1 + series2

```




    0    101.0
    1    202.0
    2    303.0
    3    404.0
    4    505.0
    5      NaN
    dtype: float64




```python
from pandas import Series
series1 = Series([1,2,3,4,5,6])
series2 = Series([100,200,300,400,500,600])
series1 + series2

```




    0    101
    1    202
    2    303
    3    404
    4    505
    5    606
    dtype: int64




```python
from pandas import DataFrame
data1 = {'Speed':[100,103,105], 'Temp':[34,23,42],}
frame1 = DataFrame(data1)
frame1
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
      <th>Speed</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>103</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>105</td>
      <td>42</td>
    </tr>
  </tbody>
</table>
</div>




```python
data2 = {'Speed':[101,109,106], 'Temp':[34,23,42], 'Humidity':[45,23,58]}
frame2 = DataFrame(data2)
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1 + frame2
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
      <th>Humidity</th>
      <th>Speed</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>201</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>212</td>
      <td>46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>211</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
series2 = Series([100,200,300], index=['Speed','Temperature','Humidity'])
series2
```




    Speed          100
    Temperature    200
    Humidity       300
    dtype: int64




```python
frame2 - series2
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
      <th>Humidity</th>
      <th>Speed</th>
      <th>Temp</th>
      <th>Temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-255.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-277.0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-242.0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2
series2
```




    Speed          100
    Temperature    200
    Humidity       300
    dtype: int64




```python
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
series3 = Series([100,200], index=['Speed','Temp'])
series3
```




    Speed    100
    Temp     200
    dtype: int64




```python
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 - series3
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
      <th>Humidity</th>
      <th>Speed</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>1.0</td>
      <td>-166.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>9.0</td>
      <td>-177.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>6.0</td>
      <td>-158.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 + series3
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
      <th>Humidity</th>
      <th>Speed</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>201.0</td>
      <td>234.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>209.0</td>
      <td>223.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>206.0</td>
      <td>242.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser = Series([3,7,1,4,7,2], index=[2,7,3,5,9,1])
ser
```




    2    3
    7    7
    3    1
    5    4
    9    7
    1    2
    dtype: int64




```python
ser.sort_index()
```




    1    2
    2    3
    3    1
    5    4
    7    7
    9    7
    dtype: int64




```python
data2 = {'Speed':[101,109,106], 'Temp':[34,23,42], 'Humidity':[45,23,58]}
frame2 = DataFrame(data2)
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = frame2.reindex([2,1,0])
frame2

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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_index()

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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.reindex(columns=['Speed', 'Humidity','Temp'])
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
      <th>Speed</th>
      <th>Humidity</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>58</td>
      <td>42</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>45</td>
      <td>34</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_index(axis=1)
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
      <th>Humidity</th>
      <th>Speed</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>58</td>
      <td>106</td>
      <td>42</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>109</td>
      <td>23</td>
    </tr>
    <tr>
      <th>0</th>
      <td>45</td>
      <td>101</td>
      <td>34</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_index(axis=0)
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = frame2.reindex([0,1,2])
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_index(axis=1,ascending=False)
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
      <th>Temp</th>
      <th>Speed</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>101</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>109</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>42</td>
      <td>106</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_values()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_15664/613722072.py in <module>
    ----> 1 frame2.sort_values()
    

    d:\anaconda3\lib\site-packages\pandas\util\_decorators.py in wrapper(*args, **kwargs)
        309                     stacklevel=stacklevel,
        310                 )
    --> 311             return func(*args, **kwargs)
        312 
        313         return wrapper
    

    TypeError: sort_values() missing 1 required positional argument: 'by'



```python
series4 = Series([100,200,300], index=['Speed','Temp','Humidty'])
series4
```




    Speed      100
    Temp       200
    Humidty    300
    dtype: int64




```python
series4.sort_values()
```




    Speed      100
    Temp       200
    Humidty    300
    dtype: int64




```python
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_values(by='Humidity')
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_values(by='Temp')
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sort_values(by='Speed')
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
series5 = Series([100,200,300],index=['a','b','b'])
series5
```




    a    100
    b    200
    b    300
    dtype: int64




```python
series5.index.is_unique
```




    False




```python
series5 = Series([100,200,300],index=['a','b','c'])
series5
```




    a    100
    b    200
    c    300
    dtype: int64




```python
series5.index.is_unique
```




    True




```python
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.sum()
```




    Speed       316
    Temp         99
    Humidity    126
    dtype: int64




```python
frame2.sum(axis=1)
```




    0    180
    1    155
    2    206
    dtype: int64




```python
frame2.idxmax()
```




    Speed       1
    Temp        2
    Humidity    2
    dtype: int64




```python
frame2.idxmin()
```




    Speed       0
    Temp        1
    Humidity    1
    dtype: int64




```python
import numpy as np
ser = Series([1,2,3,4,np.nan],index=['a','b','c','d','e'])
ser
```




    a    1.0
    b    2.0
    c    3.0
    d    4.0
    e    NaN
    dtype: float64




```python
ser.dropna()
```




    a    1.0
    b    2.0
    c    3.0
    d    4.0
    dtype: float64




```python
ser
```




    a    1.0
    b    2.0
    c    3.0
    d    4.0
    e    NaN
    dtype: float64




```python
ser = ser.dropna()
ser
```




    a    1.0
    b    2.0
    c    3.0
    d    4.0
    dtype: float64




```python
frame2
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>34</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106</td>
      <td>42</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>




```python
data2 = {'Speed':[101,np.nan,106], 'Temp':[34,np.nan,42], 'Humidity':[45,np.nan,58]}
frame3 = DataFrame(data2)
frame3
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101.0</td>
      <td>34.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106.0</td>
      <td>42.0</td>
      <td>58.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.dropna()
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101.0</td>
      <td>34.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106.0</td>
      <td>42.0</td>
      <td>58.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3 = frame3.dropna()
frame3
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101.0</td>
      <td>34.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106.0</td>
      <td>42.0</td>
      <td>58.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data2 = {'Speed':[101,np.nan,106], 'Temp':[34,np.nan,42], 'Humidity':[45,np.nan,58]}
frame3 = DataFrame(data2)
frame3
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101.0</td>
      <td>34.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106.0</td>
      <td>42.0</td>
      <td>58.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.fillna(0)
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
      <th>Speed</th>
      <th>Temp</th>
      <th>Humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101.0</td>
      <td>34.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>106.0</td>
      <td>42.0</td>
      <td>58.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas
data_frame = pandas.read_csv("test.csv")
data_frame
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
      <th>Unnamed: 0</th>
      <th>order_id</th>
      <th>product_name</th>
      <th>product_price</th>
      <th>customer_name</th>
      <th>product_category</th>
      <th>brand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>459741</td>
      <td>MacBook Air</td>
      <td>955</td>
      <td>James</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>846145</td>
      <td>Iphone 6</td>
      <td>900</td>
      <td>Tim</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>648931</td>
      <td>hp wireless mouse</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>hp</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>746512</td>
      <td>lg ips monitor</td>
      <td>200</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>lg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>546412</td>
      <td>samsung led tv</td>
      <td>500</td>
      <td>John</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>884431</td>
      <td>philips hair dryer</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>philips</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>431237</td>
      <td>samsung tab 3</td>
      <td>300</td>
      <td>James</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>701436</td>
      <td>haier air conditioner</td>
      <td>600</td>
      <td>John</td>
      <td>electronics</td>
      <td>haier</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>904716</td>
      <td>blender</td>
      <td>73</td>
      <td>Harry</td>
      <td>electronics</td>
      <td>blendtech</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>304864</td>
      <td>Dell Inspirion Laptop</td>
      <td>699</td>
      <td>Rohn</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>546168</td>
      <td>Dell Keyboard</td>
      <td>20</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_frame2 = data_frame.fillna(0)
data_frame2
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
      <th>Unnamed: 0</th>
      <th>order_id</th>
      <th>product_name</th>
      <th>product_price</th>
      <th>customer_name</th>
      <th>product_category</th>
      <th>brand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>459741</td>
      <td>MacBook Air</td>
      <td>955</td>
      <td>James</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>846145</td>
      <td>Iphone 6</td>
      <td>900</td>
      <td>Tim</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>648931</td>
      <td>hp wireless mouse</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>hp</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>746512</td>
      <td>lg ips monitor</td>
      <td>200</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>lg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>546412</td>
      <td>samsung led tv</td>
      <td>500</td>
      <td>John</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>884431</td>
      <td>philips hair dryer</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>philips</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.0</td>
      <td>431237</td>
      <td>samsung tab 3</td>
      <td>300</td>
      <td>James</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>701436</td>
      <td>haier air conditioner</td>
      <td>600</td>
      <td>John</td>
      <td>electronics</td>
      <td>haier</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.0</td>
      <td>904716</td>
      <td>blender</td>
      <td>73</td>
      <td>Harry</td>
      <td>electronics</td>
      <td>blendtech</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.0</td>
      <td>304864</td>
      <td>Dell Inspirion Laptop</td>
      <td>699</td>
      <td>Rohn</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.0</td>
      <td>546168</td>
      <td>Dell Keyboard</td>
      <td>20</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
  </tbody>
</table>
</div>




```python
from pandas import DataFrame
data_frame = DataFrame(data_frame, columns=['order_id','product_name','product_price','customer_name','product_category','brand'])
data_frame
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
      <th>order_id</th>
      <th>product_name</th>
      <th>product_price</th>
      <th>customer_name</th>
      <th>product_category</th>
      <th>brand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>459741</td>
      <td>MacBook Air</td>
      <td>955</td>
      <td>James</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>1</th>
      <td>846145</td>
      <td>Iphone 6</td>
      <td>900</td>
      <td>Tim</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>648931</td>
      <td>hp wireless mouse</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>hp</td>
    </tr>
    <tr>
      <th>3</th>
      <td>746512</td>
      <td>lg ips monitor</td>
      <td>200</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>lg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>546412</td>
      <td>samsung led tv</td>
      <td>500</td>
      <td>John</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>5</th>
      <td>884431</td>
      <td>philips hair dryer</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>philips</td>
    </tr>
    <tr>
      <th>6</th>
      <td>431237</td>
      <td>samsung tab 3</td>
      <td>300</td>
      <td>James</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>7</th>
      <td>701436</td>
      <td>haier air conditioner</td>
      <td>600</td>
      <td>John</td>
      <td>electronics</td>
      <td>haier</td>
    </tr>
    <tr>
      <th>8</th>
      <td>904716</td>
      <td>blender</td>
      <td>73</td>
      <td>Harry</td>
      <td>electronics</td>
      <td>blendtech</td>
    </tr>
    <tr>
      <th>9</th>
      <td>304864</td>
      <td>Dell Inspirion Laptop</td>
      <td>699</td>
      <td>Rohn</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>10</th>
      <td>546168</td>
      <td>Dell Keyboard</td>
      <td>20</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_frame = data_frame.drop([1])
data_frame
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
      <th>order_id</th>
      <th>product_name</th>
      <th>product_price</th>
      <th>customer_name</th>
      <th>product_category</th>
      <th>brand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>459741</td>
      <td>MacBook Air</td>
      <td>955</td>
      <td>James</td>
      <td>electronics</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>648931</td>
      <td>hp wireless mouse</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>hp</td>
    </tr>
    <tr>
      <th>3</th>
      <td>746512</td>
      <td>lg ips monitor</td>
      <td>200</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>lg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>546412</td>
      <td>samsung led tv</td>
      <td>500</td>
      <td>John</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>5</th>
      <td>884431</td>
      <td>philips hair dryer</td>
      <td>10</td>
      <td>James</td>
      <td>electronics</td>
      <td>philips</td>
    </tr>
    <tr>
      <th>6</th>
      <td>431237</td>
      <td>samsung tab 3</td>
      <td>300</td>
      <td>James</td>
      <td>electronics</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>7</th>
      <td>701436</td>
      <td>haier air conditioner</td>
      <td>600</td>
      <td>John</td>
      <td>electronics</td>
      <td>haier</td>
    </tr>
    <tr>
      <th>8</th>
      <td>904716</td>
      <td>blender</td>
      <td>73</td>
      <td>Harry</td>
      <td>electronics</td>
      <td>blendtech</td>
    </tr>
    <tr>
      <th>9</th>
      <td>304864</td>
      <td>Dell Inspirion Laptop</td>
      <td>699</td>
      <td>Rohn</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>10</th>
      <td>546168</td>
      <td>Dell Keyboard</td>
      <td>20</td>
      <td>Rob</td>
      <td>electronics</td>
      <td>dell</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_frame = data_frame.drop('product_category',axis=1)
data_frame
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
      <th>order_id</th>
      <th>product_name</th>
      <th>product_price</th>
      <th>customer_name</th>
      <th>brand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>459741</td>
      <td>MacBook Air</td>
      <td>955</td>
      <td>James</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>2</th>
      <td>648931</td>
      <td>hp wireless mouse</td>
      <td>10</td>
      <td>James</td>
      <td>hp</td>
    </tr>
    <tr>
      <th>3</th>
      <td>746512</td>
      <td>lg ips monitor</td>
      <td>200</td>
      <td>Rob</td>
      <td>lg</td>
    </tr>
    <tr>
      <th>4</th>
      <td>546412</td>
      <td>samsung led tv</td>
      <td>500</td>
      <td>John</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>5</th>
      <td>884431</td>
      <td>philips hair dryer</td>
      <td>10</td>
      <td>James</td>
      <td>philips</td>
    </tr>
    <tr>
      <th>6</th>
      <td>431237</td>
      <td>samsung tab 3</td>
      <td>300</td>
      <td>James</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>7</th>
      <td>701436</td>
      <td>haier air conditioner</td>
      <td>600</td>
      <td>John</td>
      <td>haier</td>
    </tr>
    <tr>
      <th>8</th>
      <td>904716</td>
      <td>blender</td>
      <td>73</td>
      <td>Harry</td>
      <td>blendtech</td>
    </tr>
    <tr>
      <th>9</th>
      <td>304864</td>
      <td>Dell Inspirion Laptop</td>
      <td>699</td>
      <td>Rohn</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>10</th>
      <td>546168</td>
      <td>Dell Keyboard</td>
      <td>20</td>
      <td>Rob</td>
      <td>dell</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_frame.sort_values(by='product_price')

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
      <th>order_id</th>
      <th>product_name</th>
      <th>product_price</th>
      <th>customer_name</th>
      <th>brand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>648931</td>
      <td>hp wireless mouse</td>
      <td>10</td>
      <td>James</td>
      <td>hp</td>
    </tr>
    <tr>
      <th>5</th>
      <td>884431</td>
      <td>philips hair dryer</td>
      <td>10</td>
      <td>James</td>
      <td>philips</td>
    </tr>
    <tr>
      <th>10</th>
      <td>546168</td>
      <td>Dell Keyboard</td>
      <td>20</td>
      <td>Rob</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>8</th>
      <td>904716</td>
      <td>blender</td>
      <td>73</td>
      <td>Harry</td>
      <td>blendtech</td>
    </tr>
    <tr>
      <th>3</th>
      <td>746512</td>
      <td>lg ips monitor</td>
      <td>200</td>
      <td>Rob</td>
      <td>lg</td>
    </tr>
    <tr>
      <th>6</th>
      <td>431237</td>
      <td>samsung tab 3</td>
      <td>300</td>
      <td>James</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>4</th>
      <td>546412</td>
      <td>samsung led tv</td>
      <td>500</td>
      <td>John</td>
      <td>samsung</td>
    </tr>
    <tr>
      <th>7</th>
      <td>701436</td>
      <td>haier air conditioner</td>
      <td>600</td>
      <td>John</td>
      <td>haier</td>
    </tr>
    <tr>
      <th>9</th>
      <td>304864</td>
      <td>Dell Inspirion Laptop</td>
      <td>699</td>
      <td>Rohn</td>
      <td>dell</td>
    </tr>
    <tr>
      <th>0</th>
      <td>459741</td>
      <td>MacBook Air</td>
      <td>955</td>
      <td>James</td>
      <td>apple</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_frame.sum(numeric_only=True)
```




    order_id         6174448
    product_price       3367
    dtype: int64




```python

```
