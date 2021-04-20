![aacbanner](https://i.pinimg.com/originals/46/9e/b1/469eb1c73edd0fdec983b8318816bfd1.png)

___

<a id='navigation'></a>

[[Project Summary](#project-summary)]
[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Repo Replication](#repo-replication)]

___
<a name="project-summary"></a><h1><img src="https://i.pinimg.com/originals/64/e0/b1/64e0b1932483afce95657b2638afc368.png"/></h1>



Using Pandas, Seaborn and Mathplotlib in Jupyter Lab, I prepped and explored weather data gathered from Auckland, NZ over the past 120 years, to create a models that predicted the next year's monthly temperatures with minimal RMSE of 1.09.



<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/6a/85/96/6a859661d065314f3ea90624150c981d.png"/></h1>
### Goal: 
The goal for this project is to create a model that will accurately forecast the weather for Auckland for the next year.



    
### Project Planning Initial Thoughts:
**First iteration:**
I'd like my first iteration to 



    
    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/02/9c/5b/029c5be87c534ff710958758d4982fbf.png"/></h1>

## Exploration Key Findings:
### Univariate




    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/22/e9/95/22e9953988bd635bcc37ddafe2f2e573.png"/></h1>

- Looking back at the previous year will give a more focused outlook for prediction.
- 



[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/b8/4c/3a/b84c3a1bdcf9acbbf0da58556f54e864.png"/></h1>

| column_name     | description                                                           | key                          | dtype  |
|-----------------|-----------------------------------------------------------------------|------------------------------|--------|
| `dt`                  | Date of Temperature measured                                    |                              | datetime |
| `avg_temp`            | Average land temperature in celsius                             |                              | float64|
| `avg_temp_uncertainty`| 95% confidence interval around the minimum land temperature     |                              | object |
| `weekday`         | Day of the week                                                     |                              | object |
| `month`           | Numerical representation of month                                   |                              | int64  |





[Jump to Navigation](#navigation)

<a name="repo-replication"></a><h1><img src="https://i.pinimg.com/originals/d7/db/e5/d7dbe5a99b26f921f59190e6119f27ef.png"/></h1>

In order to get started reproducing this project, you'll need to setup a proper environment.

1. Begin by downloading the weather data [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).
![aacbanner](https://i.pinimg.com/originals/de/1b/51/de1b51677d5511963d8db44b964c6fbe.png)    







2. Recover your downloaded zip file and unzip.

**Prep your repo.**

3. Create a new repo to house this project, and clone it into your terminal by copying the SSH link:
    ![prep your repo](https://i.pinimg.com/originals/d0/15/c2/d015c28c08829cce7136943e7804117c.png)
> <code>git clone </code> (Cmd+V)
    

4. Create a `.gitignore` that includes any files you dont want shared on the internet and **push it**! 
    
    - (This can include your newly downloaded .csv files)
> <code>code .gitignore</code>



5. Create a `README.md` file to begin notating steps taken so far.
    
><code>code README.md</code>


6. Transfer your unzipped .csv files into your newly established folder.


7. Create a Jupyter Lab environment to continue working in.
> <code>jupyter lab</code>


8. Create Jupyter Notebook to begin the data pipeline. 

![jlablauncher](https://i.pinimg.com/originals/98/92/c5/9892c5042934750b5ba073f2d49f6184.png)
    




[Jump to Navigation](#navigation)








































