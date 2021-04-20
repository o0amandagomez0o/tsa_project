![aacbanner](https://i.pinimg.com/originals/46/9e/b1/469eb1c73edd0fdec983b8318816bfd1.png)

___

<a id='navigation'></a>

[[Project Summary](#project-summary)]
[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Tested Hypotheses](#tested-hypotheses)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Repo Replication](#repo-replication)]

___
<a name="project-summary"></a><h1><img src="https://i.pinimg.com/originals/0e/10/14/0e1014ec7b1a284b4cdd31269a407622.png"/></h1>

I looked into the possible drivers of adoptability using Austin Animal Center's data accumulated from the past seven years. With a detailed eye, I prepped and explored my data in Jupyter Lab using Pandas, Seaborn and Mathplotlib. I then used Scikit-learn to create a logistic regression model used to predict the adoptability of a pet.


<a name="project-planning"></a><h1><img src="https://i.pinimg.com/originals/9f/b7/6d/9fb76d0350228675d02435d4f5aa1197.png"/></h1>
### Goal: 
The goal for this project is to create a model that will accurately forecast the weather for Auckland for the next year.



    
### Project Planning Initial Thoughts:
**First iteration:**
I'd like my first iteration to 



    
    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src="https://i.pinimg.com/originals/3a/1e/6d/3a1e6d338b1b0bd1850f2eb067f983b4.png"/></h1>

## Exploration Key Findings:
### Univariate






[Jump to Navigation](#navigation)

<a name="tested-hypotheses"></a><h1><img src="https://i.pinimg.com/originals/35/3f/e6/353fe67133773dc3639f95987d57c386.png"/></h1>


> #### Hypothesis₁
>
> H₀ = Age and adoption rates are INDEPENDENT.
>
> H𝛼 = There is a relationship between pet age and if they get adopted.
> - **We reject the null hypothesis: Age and adoption rates are INDEPENDENT.**
<br>
>    <strong>Therefore: There is a relationship between pet age and if they get adopted.</strong>

<details>
  <summary>Click to see full list. </summary>
    
> #### Hypothesis₂
>
> H₀ = Breed and adoption rates are INDEPENDENT.
>
> H𝛼 = There is a relationship between breed and if they get adopted.
> - **We reject the null hypothesis: Breed and adoption rates are INDEPENDENT.**<br>
    **Therefore: There is a relationship between breed and if they get adopted.**
       
    
</details>


    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src="https://i.pinimg.com/originals/3f/d3/66/3fd3660db4a243c2e43640a28a44d4c2.png"/></h1>

- More features *may* not drive model accuracy as much as anticipated.
- Logistic Regression is again a good model for predicting classification.
- Neutered status is the most important driver for adoption.



[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src="https://i.pinimg.com/originals/3f/84/53/3f8453f4d3e1ff56d3934dd6ebe1d410.png"/></h1>

| column_name     | description                                                           | key                          | dtype  |
|-----------------|-----------------------------------------------------------------------|------------------------------|--------|
| `animal_id`     | Unique id assigned to all animals upon intake at Austin Animal Center |                              | object |
| `date`          | Outcome Date                                                          |                              | object |
| `breed`         | Animal breed                                                          |                              | object |
| `color`         | Animal color of coat                                                  |                              | object |
| `dob`           | Animal's date of birth                                                |                              | object |
| `outcome_age`   | Animal's final age at AAC                                             |                              | int64  |
| `elderly`       | Indicates if animal is 6+ years of age                                |                              | int64  |
| `full_grown`    | Indicates if animal is between 2-5 years of age                       |                              | int64  |
| `youngins`      | Indicates if animal is 1 year or younger                              |                              | int64  |
| `neutered_male` | Indicates if animal is a neutered male                                | 1 = yes, 0 = no              | int64  |
| `intact_male`   | Indicates if animal is a male with sexual organ intact                | 1 = yes, 0 = no              | int64  |
| `neutered`      | Indicates if animal is spayed/neutered                                | 1 = yes, 0 = no              | int64  |
| `is_male`       | Indicates if animal is male                                           | 1 = male, 0 = female         | int64  |
| `is_Dog`        | Indicates if animal is a dog                                          | 1 = dog, 0 = cat             | uint8  |
| `is_pitbull`    | Indicates if animal is of pitbull/American stafford breed             | 1 = yes, 0 = no              | int64  |
| `is_black`      | Indicates if animal's coat is black                                   | 1 = yes, 0 = no              | int64  |
| `adopted`       | Indicates if animal's outcome was adoption                            | 1 = adopted, 0 = not adopted | int64  |


<details>
  <summary>Click to see full list. </summary>

| column_name                      | description                        | key              | dtype |
|----------------------------------|------------------------------------|------------------|-------|
| `American Pit Bull Terrier Mix` | Indicates if animal is this breed. | 1 = yes, 0 = no  | int64 |
| `American Shorthair Mix`        | Indicates if animal is this breed. | 1 = yes, 0 = no  | int64 |


        
</details>

[Jump to Navigation](#navigation)

<a name="repo-replication"></a><h1><img src="https://i.pinimg.com/originals/d5/24/a6/d524a6bb62a9d6734c7cf899a11c7310.png"/></h1>

In order to get started reproducing this project, you'll need to setup a proper environment.

1. Begin by downloading the Austin Animal Center's data [here](https://www.kaggle.com/jackdaoud/animal-shelter-analytics).
![aacbanner](https://i.pinimg.com/originals/96/6b/38/966b3864e78fa6ed1e728383a499a7d8.png)    

2. Recover your downloaded zip file and unzip.

**Prep your repo.**

3. Create a new repo to house this project, and clone it into your terminal by copying the SSH link:
    ![prep your repo](https://i.pinimg.com/originals/d0/32/f0/d032f04aaafa14bcb65c675cc7ae828f.png)
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








































