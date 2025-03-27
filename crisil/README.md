#Credit Rating Calculation
###Requirements
- Python 3.x

*******************
Setup
1.Clone theis repository.
2.Navigate to the project directory crisil .
3.(Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4.run the code
    python -m unittest test_credit.py
*********************
#I have provided 3 test cases in unittest
#it will pass two test case and one failed  

1.performance optimization
a:->Caching: If certain calculations are repeated  cache the results to avoid redundant computations. Libraries like functools.lru_cache can be useful for this.
b:->Use proper data structuere to store data for quick access and manupulation
c:->parallel processing: Use multiprocessing and concurrent feature for large dataset to speed up processing time.
d:-> use numpy panda slibrary for manipulation


2. Error Handlinga:
a: check valid input as specified 
b: use try and except block
c: use logging to find log of function